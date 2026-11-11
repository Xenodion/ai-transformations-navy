// Markdown -> Word for the board deliverables, in a sober TotalEnergies-inspired style.
// Usage (repository root):
//   node work/docx_build/build_docx.mjs report   -> deliverables/report/full_strategy_report.docx
//   node work/docx_build/build_docx.mjs memo     -> deliverables/memo/executive_memo.docx
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { marked } from 'marked';
import sizeOf from 'image-size';
import {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, HeadingLevel, BorderStyle, Footer, PageNumber, TableOfContents, LevelFormat,
  ExternalHyperlink, PageBreak, TabStopType, VerticalAlign,
} from 'docx';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '../..');
const MODE = process.argv[2] ?? 'report';
const CFG = {
  report: { src: 'deliverables/report/full_strategy_report.md', out: 'deliverables/report/full_strategy_report.docx',
    body: 20, table: 16, margin: 1250, cover: true },
  memo: { src: 'deliverables/memo/executive_memo.md', out: 'deliverables/memo/executive_memo.docx',
    body: 19, table: 16, margin: 850, cover: false },
}[MODE];

const BLUE = '00509E', NAVY = '0B1F3A', RED = 'E30613', GREY = '5F6B7A', ZEBRA = 'F2F5F9', RULE = 'DCE5EB';
const FONT = 'Arial';
const PAGE_W = 11906, CONTENT_W = PAGE_W - 2 * CFG.margin;
const PX_PER_DXA = 96 / 1440;
const MAX_IMG_W = Math.round(CONTENT_W * PX_PER_DXA);

const srcPath = path.join(ROOT, CFG.src);
const srcDir = path.dirname(srcPath);
const md = fs.readFileSync(srcPath, 'utf8');
const tokens = marked.lexer(md);

// ---------- inline text ----------
function runs(inl, style = {}) {
  const out = [];
  for (const t of inl ?? []) {
    const s = { font: FONT, size: style.size ?? CFG.body, color: style.color ?? '1A1A1A', bold: style.bold, italics: style.italics };
    switch (t.type) {
      case 'strong': out.push(...runs(t.tokens, { ...style, bold: true })); break;
      case 'em': out.push(...runs(t.tokens, { ...style, italics: true })); break;
      case 'codespan': out.push(new TextRun({ ...s, text: unescape(t.text) })); break;
      case 'link': {
        const inner = runs(t.tokens, style);
        if (/^https?:/.test(t.href)) out.push(new ExternalHyperlink({ link: t.href, children: runs(t.tokens, { ...style, color: BLUE }) }));
        else out.push(...inner); // repository links read as plain text in Word
        break;
      }
      case 'br': out.push(new TextRun({ ...s, break: 1 })); break;
      case 'text': case 'escape':
        if (t.tokens?.length) out.push(...runs(t.tokens, style));
        else out.push(new TextRun({ ...s, text: unescape(t.text) }));
        break;
      default: if (t.text) out.push(new TextRun({ ...s, text: unescape(t.text) }));
    }
  }
  return out;
}
const unescape = (x) => x.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
const plain = (inl) => (inl ?? []).map((t) => (t.tokens ? plain(t.tokens) : unescape(t.text ?? ''))).join('');

// ---------- blocks ----------
let figure = 0, listInstance = 0;
const SPACING = { after: MODE === 'memo' ? 70 : 120, line: MODE === 'memo' ? 252 : 276 };

// Numeric tables are images in the Markdown; in Word they become native tables from the same JSON.
const TABLES = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(ROOT, 'work/projects/report_tables.json'), 'utf8')).map((t) => [t.id, t]));
let tableNo = 0;
function nativeTable(id) {
  const t = TABLES[id];
  const line = (r) => `| ${r.map((c) => c.replace(/\|/g, '/')).join(' | ')} |`;
  const mdTable = [line(t.rows[0]), line(t.rows[0].map(() => '---')), ...t.rows.slice(1).map(line)].join('\n');
  tableNo += 1;
  return [new Paragraph({ keepNext: true, spacing: { before: 120, after: 60 },
    children: [new TextRun({ text: `Table ${tableNo}. `, bold: true, font: FONT, size: CFG.table, color: GREY }), new TextRun({ text: t.title, font: FONT, size: CFG.table, color: GREY })] }),
  ...table(marked.lexer(mdTable)[0])];
}

function image(href, alt, pct) {
  const id = path.basename(href, '.png');
  if (TABLES[id]) return nativeTable(id);
  const file = path.resolve(srcDir, href);
  const buf = fs.readFileSync(file);
  const { width, height } = sizeOf(buf);
  const w = Math.min(Math.round(MAX_IMG_W * (Number(pct) || 100) / 100), Math.round(width * 0.42));
  const h = Math.round((height / width) * w);
  figure += 1;
  return [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 40 }, keepNext: true,
      children: [new ImageRun({ type: 'png', data: buf, transformation: { width: w, height: h }, altText: { title: alt, description: alt, name: alt } })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
      children: [new TextRun({ text: `Figure ${figure}. `, bold: true, font: FONT, size: CFG.table, color: GREY }), new TextRun({ text: alt, font: FONT, size: CFG.table, color: GREY })] }),
  ];
}

const NUMERIC = /^[\s(+\-−–$€]*[\d.,]+\s*(%|m|years?|x)?\)?$/i;
function table(t) {
  const ncol = t.header.length;
  const lens = [...Array(ncol).keys()].map((c) => Math.max(plain(t.header[c].tokens).length, ...t.rows.map((r) => plain(r[c].tokens).length)));
  const weights = lens.map((l) => Math.min(60, Math.max(6, l)) ** 0.8);
  const total = weights.reduce((a, b) => a + b, 0);
  const widths = weights.map((w) => Math.floor((w / total) * CONTENT_W));
  widths[widths.length - 1] += CONTENT_W - widths.reduce((a, b) => a + b, 0);
  const border = { style: BorderStyle.SINGLE, size: 4, color: RULE };
  const numCol = [...Array(ncol).keys()].map((c) => c > 0 && t.rows.every((row) => NUMERIC.test(plain(row[c].tokens)) || !plain(row[c].tokens).trim()));
  const totalRow = t.rows.map((row) => /^(total|net cash|average)/i.test(plain(row[0].tokens)));
  const cell = (inl, c, r) => {
    const txt = plain(inl);
    const head = r < 0;
    const right = c > 0 && (head ? numCol[c] : NUMERIC.test(txt));
    if (!head && totalRow[r]) inl = [{ type: 'strong', tokens: inl }];
    return new TableCell({
      width: { size: widths[c], type: WidthType.DXA },
      verticalAlign: VerticalAlign.CENTER,
      shading: head ? { type: ShadingType.CLEAR, fill: BLUE, color: 'auto' } : r % 2 ? { type: ShadingType.CLEAR, fill: ZEBRA, color: 'auto' } : undefined,
      margins: MODE === 'memo' ? { top: 20, bottom: 20, left: 80, right: 80 } : { top: 50, bottom: 50, left: 90, right: 90 },
      borders: { top: border, bottom: border, left: border, right: border },
      children: [new Paragraph({ alignment: right ? AlignmentType.RIGHT : AlignmentType.LEFT, spacing: { after: 0, line: 240 },
        children: runs(inl, { size: CFG.table, bold: head || undefined, color: head ? 'FFFFFF' : '1A1A1A' }) })],
    });
  };
  return [
    new Table({
      width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths,
      rows: [new TableRow({ tableHeader: true, children: t.header.map((h, c) => cell(h.tokens, c, -1)) }),
        ...t.rows.map((row, r) => new TableRow({ cantSplit: true, children: row.map((x, c) => cell(x.tokens, c, r)) }))],
    }),
    new Paragraph({ spacing: { after: MODE === 'memo' ? 0 : 120, line: MODE === 'memo' ? 120 : undefined }, children: [] }),
  ];
}

function list(t, level = 0) {
  const out = [];
  const instance = t.ordered ? ++listInstance : 0;
  for (const item of t.items) {
    const inl = []; const nested = [];
    for (const sub of item.tokens) (sub.type === 'list' ? nested : inl).push(sub);
    const flat = inl.flatMap((x) => (x.tokens ? x.tokens : [x]));
    out.push(new Paragraph({ numbering: { reference: t.ordered ? 'num' : 'bullet', level, instance }, spacing: { after: 60, line: SPACING.line },
      children: runs(flat) }));
    for (const n of nested) out.push(...list(n, level + 1));
  }
  return out;
}

const HEAD = { 2: HeadingLevel.HEADING_1, 3: HeadingLevel.HEADING_2, 4: HeadingLevel.HEADING_3 };
let title = '', subtitle = [], started = !CFG.cover, kpiNext = false;
const body = [];
for (const t of tokens) {
  if (t.type === 'heading' && t.depth === 1) { title = plain(t.tokens); if (!CFG.cover) body.push(memoTitle(title)); continue; }
  if (!started) {
    if (t.type === 'heading') started = true;
    else { if (t.type === 'paragraph') subtitle.push(plain(t.tokens)); continue; }
  }
  switch (t.type) {
    case 'heading':
      body.push(new Paragraph({ heading: HEAD[t.depth] ?? HeadingLevel.HEADING_3, keepNext: true, children: runs(t.tokens, {}).length ? [new TextRun({ text: plain(t.tokens) })] : [] }));
      break;
    case 'paragraph': {
      const imgs = t.tokens.filter((x) => x.type === 'image');
      if (imgs.length && t.tokens.every((x) => x.type === 'image' || (x.type === 'text' && !x.text.trim()))) {
        for (const im of imgs) body.push(...image(im.href, im.text, im.title));
      } else body.push(new Paragraph({ spacing: SPACING, children: runs(t.tokens) }));
      break;
    }
    case 'list': body.push(...list(t)); break;
    case 'table': body.push(...(kpiNext ? kpiBand(t) : table(t))); kpiNext = false; break;
    case 'html':
      if (/pagebreak/.test(t.raw)) body.push(new Paragraph({ children: [new PageBreak()] }));
      if (/kpi/.test(t.raw)) kpiNext = true;
      break;
    case 'hr': body.push(new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 1 } }, children: [] })); break;
    default: break;
  }
}

// Headline figures: large value, label above, short note below; no grid lines.
function kpiBand(t) {
  const n = t.header.length, w = Math.floor(CONTENT_W / n);
  const none = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  const line = (text, size, color, bold) => new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0, line: 240 },
    children: [new TextRun({ text, font: FONT, size, color, bold })] });
  const cells = t.header.map((h, c) => {
    const value = plain(t.rows[0][c].tokens);
    return new TableCell({ width: { size: w, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, fill: ZEBRA, color: 'auto' },
      margins: { top: 60, bottom: 60, left: 60, right: 60 },
      borders: { top: { style: BorderStyle.SINGLE, size: 18, color: c === n - 1 ? RED : BLUE }, bottom: none, left: { style: BorderStyle.SINGLE, size: 12, color: 'FFFFFF' }, right: none },
      children: [line(plain(h.tokens), 14, GREY, true), line(value, 30, c === n - 1 ? RED : NAVY, true),
        ...(t.rows[1] ? [line(plain(t.rows[1][c].tokens), 14, GREY)] : [])] });
  });
  return [new Table({ width: { size: w * n, type: WidthType.DXA }, columnWidths: Array(n).fill(w), rows: [new TableRow({ cantSplit: true, children: cells })] }),
    new Paragraph({ spacing: { after: 0, line: 160 }, children: [] })];
}

function memoTitle(text) {
  return new Paragraph({ spacing: { after: 40 }, children: [new TextRun({ text, font: FONT, size: 30, bold: true, color: NAVY })] });
}

// ---------- cover ----------
const band = fs.readFileSync(path.join(HERE, 'brand_band.png'));
const logo = fs.readFileSync(path.join(ROOT, 'sources/assets/Logo_TotalEnergies.svg.png'));
const bandW = MAX_IMG_W;
function cover() {
  const meta = subtitle.map((s) => s.replace(/\*\*/g, '')).filter((s) => !s.startsWith('Fictional')); // the cover disclaimer says it
  return [
    new Paragraph({ spacing: { after: 600 }, children: [new ImageRun({ type: 'png', data: logo, transformation: { width: 150, height: Math.round(150 * 1012 / 1280) } })] }),
    new Paragraph({ spacing: { before: 1800, after: 200 }, children: [new TextRun({ text: ACADEMIC_TAG, font: FONT, size: 18, bold: true, color: RED })] }),
    new Paragraph({ spacing: { after: 300 }, children: [new TextRun({ text: title, font: FONT, size: 56, bold: true, color: NAVY })] }),
    new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: 'AI transformation programme 2027–2031: strategy, portfolio, investment case and delivery model', font: FONT, size: 26, color: BLUE })] }),
    new Paragraph({ spacing: { after: 2400 }, children: [new ImageRun({ type: 'png', data: band, transformation: { width: 260, height: 3 } })] }),
    ...meta.map((m) => new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: m, font: FONT, size: 19, color: GREY })] })),
    new Paragraph({ spacing: { before: 600 }, border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 6 } },
      children: [new TextRun({ text: DISCLAIMER, font: FONT, size: 16, italics: true, color: GREY })] }),
    new Paragraph({ children: [new PageBreak()] }),
    new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: 'Contents', font: FONT, size: 32, bold: true, color: NAVY })] }),
    new TableOfContents('Contents', { hyperlink: true, headingStyleRange: '1-2' }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

const running = MODE === 'memo' ? 'Executive memo' : 'Full strategy report';
const ACADEMIC_TAG = 'Fictional academic document | AI Transformation Strategies course, Albert School';
const DISCLAIMER = 'Fictional academic document written by students for the AI Transformation Strategies course at Albert School (November 2026). '
  + 'It is not a TotalEnergies document and does not reflect the views or decisions of TotalEnergies. Company facts come from public sources; '
  + 'the internal role-play, figures and recommendations are the authors’ own assumptions and calculations.';
const doc = new Document({
  creator: 'TotalEnergies digital transformation team', title, features: { updateFields: CFG.cover },
  styles: {
    default: { document: { run: { font: FONT, size: CFG.body, color: '1A1A1A' }, paragraph: { spacing: SPACING } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: FONT, size: MODE === 'memo' ? 21 : 30, bold: true, color: NAVY },
        paragraph: { spacing: { before: MODE === 'memo' ? 140 : 360, after: MODE === 'memo' ? 50 : 140 }, outlineLevel: 0,
          border: MODE === 'memo' ? undefined : { bottom: { style: BorderStyle.SINGLE, size: 6, color: BLUE, space: 4 } } } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: FONT, size: MODE === 'memo' ? 18 : 24, bold: true, color: BLUE },
        paragraph: { spacing: { before: MODE === 'memo' ? 100 : 260, after: 80 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { font: FONT, size: 20, bold: true, color: NAVY },
        paragraph: { spacing: { before: 200, after: 60 }, outlineLevel: 2 } },
    ],
  },
  numbering: { config: [
    { reference: 'bullet', levels: [0, 1].map((l) => ({ level: l, format: LevelFormat.BULLET, text: l ? '–' : '•', alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 360 * (l + 1), hanging: 240 } }, run: { color: BLUE } } })) },
    { reference: 'num', levels: [0, 1].map((l) => ({ level: l, format: LevelFormat.DECIMAL, text: `%${l + 1}.`, alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 360 * (l + 1), hanging: 300 } } } })) },
  ] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: CFG.margin, bottom: CFG.margin, left: CFG.margin, right: CFG.margin, header: 400, footer: 400 } },
      titlePage: CFG.cover },
    footers: { default: new Footer({ children: [new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } }, spacing: { after: 0 },
      children: [new TextRun({ text: `${running}  |  `, font: FONT, size: 14, bold: true, color: NAVY }),
        new TextRun({ text: 'Fictional academic document for the AI Transformation Strategies course, Albert School. Not a TotalEnergies document.', font: FONT, size: 14, color: GREY }),
        new TextRun({ font: FONT, size: 14, color: GREY, children: ['	', PageNumber.CURRENT, ' / ', PageNumber.TOTAL_PAGES] })] })] }) },
    children: [...(CFG.cover ? cover() : []), ...body],
  }],
});

const outPath = process.env.DOCX_OUT || path.join(ROOT, CFG.out); // DOCX_OUT: preview copy when Word holds the file
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, await Packer.toBuffer(doc));
console.log(`Wrote ${CFG.out} (${figure} figures)`);
