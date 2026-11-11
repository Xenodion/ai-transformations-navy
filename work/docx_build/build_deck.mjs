// Board defence deck (16:9) in the report's art direction, inspired by TotalEnergies' public strategy decks.
// Usage (repository root): node work/docx_build/build_deck.mjs -> deliverables/slides/ai_strategy_deck.pptx
// Numbers are copied from the validated report and memo (deliverables/); change them there first.
import path from 'node:path';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import sizeOf from 'image-size';
import pptxgen from 'pptxgenjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const A = (f) => path.join(ROOT, 'work/projects/assets', f);
const LOGO = path.join(ROOT, 'sources/assets/Logo_TotalEnergies.svg.png');
const BAND = path.join(ROOT, 'work/docx_build/brand_band.png');
const OUT = process.env.DECK_OUT || path.join(ROOT, 'deliverables/slides/ai_strategy_deck.pptx');

const NAVY = '0B1F3A', BLUE = '00509E', TEAL = '00A3E0', ORANGE = 'F37021', RED = 'E30613', GREEN = '84C225',
  GOOD = '4E7A12', GREY = '5F6B7A', CARD = 'F2F5F9', RULE = 'DCE5EB', WHITE = 'FFFFFF';
const FONT = 'Arial';
const W = 13.333;
const SPEAKERS = ['Alexandre Waerniers', 'Vincent Lamy', 'Yoni Mahieddine', 'Nahel Bachriri']; // ponytail: chapter order = name order; swap here
const CHAPTERS = [
  { name: 'Where we stand', color: RED, n: 2, speaker: SPEAKERS[0], items: ['Readiness and bottleneck', 'Delivery model: the dedicated trio'] },
  { name: 'What we fund', color: ORANGE, n: 4, speaker: SPEAKERS[1], items: ['Portfolio and horizon mix', 'Focus: P13 retail', 'Focus: P01 refining', 'Focus: P03 drilling'] },
  { name: 'What it returns', color: BLUE, n: 3, speaker: SPEAKERS[2], items: ['Investment envelope', 'Scenarios, hurdle and cost of inaction', 'J-curve and staged release'] },
  { name: 'How we make it stick', color: GREEN, n: 2, speaker: SPEAKERS[3], items: ['Change, adoption and owners', 'The ask'] },
];

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE';
pres.title = 'Accelerating AI value across TotalEnergies';
pres.author = 'Albert School student team (fictional academic case)';
let slideNo = 0;

// ---------- shared furniture ----------
const ratio = (f) => { const { width, height } = sizeOf(fs.readFileSync(f)); return width / height; };
function img(s, f, x, y, { w, h }) {
  const r = ratio(f);
  if (w && h) { if (w / h > r) w = h * r; else h = w / r; }
  else if (w) h = w / r; else w = h * r;
  s.addImage({ path: f, x, y, w, h });
  return { w, h };
}
const text = (s, t, o) => s.addText(t, { fontFace: FONT, margin: 0, color: NAVY, valign: 'top', ...o });
const card = (s, x, y, w, h, fill = CARD) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: fill }, line: { color: fill }, rectRadius: 0.08 });
function pill(s, label, x, y, color = RED, w = null) {
  const width = w ?? 0.2 + label.length * 0.085;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: width, h: 0.3, fill: { color }, line: { color }, rectRadius: 0.15 });
  text(s, label, { x, y, w: width, h: 0.3, fontSize: 10.5, bold: true, color: WHITE, align: 'center', valign: 'middle' });
}
// Red-arrow list in the TotalEnergies style; items may be strings or [bold, rest].
function arrows(s, items, x, y, w, h, size = 12.5) {
  const runs = [];
  items.forEach((it, i) => {
    const [b, r] = Array.isArray(it) ? it : [null, it];
    runs.push({ text: '→  ', options: { color: RED, bold: true } });
    if (b) runs.push({ text: b, options: { bold: true } });
    runs.push({ text: r, options: { breakLine: i < items.length - 1, paraSpaceAfter: 5 } });
  });
  text(s, runs, { x, y, w, h, fontSize: size, color: '1A1A1A' });
}

function gauge(s, ch, k, dark = false) {
  const x0 = 0.5, total = 7.4, gap = 0.08, seg = (total - gap * 3) / 4, y = 7.0;
  CHAPTERS.forEach((c, i) => {
    const x = x0 + i * (seg + gap);
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: seg, h: 0.07, fill: { color: RULE }, line: { color: RULE } });
    const fill = i < ch ? 1 : i > ch ? 0 : k === 0 ? 0.06 : k / c.n;
    if (fill > 0) s.addShape(pres.shapes.RECTANGLE, { x, y, w: seg * fill, h: 0.07, fill: { color: c.color }, line: { color: c.color } });
    text(s, `${i + 1}  ${c.name}`, { x, y: y + 0.11, w: seg, h: 0.22, fontSize: 8.5, bold: i === ch, color: i === ch ? (dark ? WHITE : NAVY) : '8A96A3' });
  });
}
function frame(s, { ch = -1, k = 0, logo = true, appendix = false } = {}) {
  slideNo += 1;
  if (logo) s.addImage({ path: LOGO, x: 12.05, y: 0.28, w: 0.82, h: 0.82 / ratio(LOGO) });
  if (appendix) text(s, 'Appendix', { x: 0.5, y: 7.02, w: 3, h: 0.3, fontSize: 9, bold: true, color: GREY });
  else gauge(s, ch, k);
  text(s, `Fictional academic document · AI Transformation Strategies course, Albert School   |   ${slideNo}`,
    { x: 8.05, y: 7.02, w: 4.8, h: 0.3, fontSize: 8, color: GREY, align: 'right' });
}
function head(s, title, sub) {
  text(s, title, { x: 0.5, y: 0.32, w: 11.2, h: 0.85, fontSize: 24, bold: true, valign: 'middle', fit: 'shrink' });
  if (sub) text(s, sub, { x: 0.5, y: 1.18, w: 11.2, h: 0.32, fontSize: 13, color: BLUE });
}
const takeaway = (s, t) => text(s, t, { x: 0.5, y: 6.3, w: 12.33, h: 0.5, fontSize: 15, bold: true, align: 'center', valign: 'middle' });
function content(ch, k, title, sub, notes) {
  const s = pres.addSlide(); s.background = { color: WHITE };
  frame(s, { ch, k }); head(s, title, sub); s.addNotes(notes); return s;
}
function table(s, rows, x, y, w, colW, size = 11) {
  const border = { type: 'solid', pt: 0.5, color: RULE };
  const data = rows.map((r, i) => r.map((c) => {
    const bold = i === 0 || /^(Expected|Total)/.test(r[0]);
    return { text: String(c), options: { bold, color: i === 0 ? WHITE : '1A1A1A', fill: { color: i === 0 ? BLUE : i % 2 ? WHITE : CARD },
      align: i > 0 && /^[−+\-$€\d.,% ]+(years|y)?$/.test(String(c)) && c !== '' ? 'right' : 'left' } };
  }));
  s.addTable(data, { x, y, w, colW, fontFace: FONT, fontSize: size, border, margin: [3, 6, 3, 6], valign: 'middle' });
}
function divider(ch) {
  const c = CHAPTERS[ch];
  const s = pres.addSlide(); s.background = { color: WHITE };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 4.6, h: 6.8, fill: { color: c.color }, line: { color: c.color } });
  text(s, String(ch + 1).padStart(2, '0'), { x: 0.6, y: 2.2, w: 3.6, h: 2.2, fontSize: 120, bold: true, color: WHITE, valign: 'middle' });
  frame(s, { ch, k: 0 });
  text(s, c.name, { x: 5.3, y: 2.0, w: 7.3, h: 1.0, fontSize: 40, bold: true, color: c.color, valign: 'middle' });
  arrows(s, c.items, 5.3, 3.2, 7, 1.8, 16);
  text(s, [{ text: 'Presented by  ', options: { color: GREY } }, { text: c.speaker, options: { bold: true } }], { x: 5.3, y: 5.4, w: 7, h: 0.4, fontSize: 14 });
  s.addNotes(`Chapter ${ch + 1}: ${c.name}. Hand over to ${c.speaker}. Pass in a few seconds.`);
}

// ---------- 1. Cover ----------
{
  const s = pres.addSlide(); s.background = { color: WHITE }; slideNo += 1;
  s.addImage({ path: LOGO, x: 0.6, y: 0.5, w: 1.5, h: 1.5 / ratio(LOGO) });
  text(s, 'Fictional academic document | AI Transformation Strategies course, Albert School', { x: 0.6, y: 2.45, w: 7.6, h: 0.3, fontSize: 11, bold: true, color: RED });
  text(s, 'Accelerating AI value across TotalEnergies', { x: 0.6, y: 2.85, w: 7.4, h: 1.7, fontSize: 40, bold: true, valign: 'top' });
  text(s, 'AI transformation programme 2027–2031: investment case for Board decision', { x: 0.6, y: 4.55, w: 7.2, h: 0.7, fontSize: 16, color: BLUE });
  s.addImage({ path: BAND, x: 0.6, y: 5.35, w: 3.2, h: 0.04 });
  text(s, SPEAKERS.join('   ·   '), { x: 0.6, y: 5.6, w: 7.6, h: 0.3, fontSize: 12.5, bold: true });
  text(s, 'Digital transformation team (role-play) · 16 November 2026', { x: 0.6, y: 5.95, w: 7.6, h: 0.3, fontSize: 11, color: GREY });
  s.addShape(pres.shapes.RECTANGLE, { x: 8.75, y: 0, w: 4.583, h: 7.5, fill: { color: NAVY }, line: { color: NAVY } });
  text(s, 'The question for the Board', { x: 9.25, y: 2.3, w: 3.7, h: 0.35, fontSize: 12, bold: true, color: TEAL });
  text(s, 'Should we invest $21.94m to turn existing AI solutions into measured cash, released gate by gate?',
    { x: 9.25, y: 2.75, w: 3.7, h: 2.2, fontSize: 20, bold: true, color: WHITE });
  text(s, 'Not a TotalEnergies document. Company facts from public sources; figures and recommendations are the authors’ assumptions and calculations.',
    { x: 9.25, y: 6.35, w: 3.7, h: 0.75, fontSize: 8.5, color: 'B8C4D0' });
  s.addNotes('Introduce the team in one sentence each. We play TotalEnergies’ internal digital transformation team; the professor is the CEO.');
}

// ---------- 2. Decision (answer first) ----------
{
  const s = pres.addSlide(); s.background = { color: WHITE };
  frame(s, { ch: -1 });
  head(s, 'We ask you to release $2.90m today, the first tranche of a $21.94m gated envelope', 'The decision in one page');
  const kpis = [['Decision today', '$2.90m', 'Tranche 1 (Y0)', NAVY], ['Five-year envelope', '$21.94m', 'ceiling, released by gates', NAVY],
    ['Expected NPV at 10%', '+$5.62m', '30 / 50 / 20 scenarios', NAVY], ['Expected IRR', '27.8%', 'vs 10% hurdle', NAVY], ['Downside NPV', '−$1.30m', 'cash still repaid by Y5', RED]];
  kpis.forEach(([l, v, n, c], i) => {
    const x = 0.5 + i * 2.5;
    card(s, x, 1.75, 2.33, 1.55);
    text(s, l, { x, y: 1.9, w: 2.33, h: 0.3, fontSize: 11, bold: true, color: GREY, align: 'center' });
    text(s, v, { x, y: 2.2, w: 2.33, h: 0.65, fontSize: 30, bold: true, color: c, align: 'center', valign: 'middle' });
    text(s, n, { x, y: 2.88, w: 2.33, h: 0.3, fontSize: 10.5, color: GREY, align: 'center' });
  });
  pill(s, 'Resolution', 0.5, 3.6);
  text(s, 'Invest $21.94m over five years (Y0–Y5) in ten AI initiatives run by dedicated branch–Digital Factory teams, to create an expected NPV of $5.62m at 10%, with a downside NPV of −$1.30m, only $2.90m committed before the first gate, and every later release conditional on Finance-verified gates.',
    { x: 0.5, y: 4.0, w: 6.2, h: 2.1, fontSize: 15 });
  pill(s, 'Why now', 7.1, 3.6, BLUE);
  arrows(s, [['Platforms exist: ', 'more than 10,000 live AI models and about 100 Digital Factory solutions.'],
    ['The bottleneck is organisational: ', 'each project is split across four reporting lines.'],
    ['Waiting costs value: ', 'each year of delay costs $0.65m of NPV.']], 7.1, 4.0, 5.7, 2.1, 14);
  takeaway(s, 'Only $2.90m is at risk before the first gate; every later dollar needs evidence.');
  s.addNotes('Lead with the answer. Read the resolution, then the three reasons. Point at the red tile: even in the downside the programme returns its cash (+$2.27m by Y5); it only misses the 10% hurdle.');
}

// ---------- 3. Agenda ----------
{
  const s = pres.addSlide(); s.background = { color: WHITE };
  frame(s, { ch: -1 });
  head(s, 'Four questions a sceptical Board asks, answered in order', 'Agenda');
  CHAPTERS.forEach((c, i) => {
    const x = 0.5 + i * 3.1;
    card(s, x, 1.8, 2.9, 4.1);
    text(s, String(i + 1).padStart(2, '0'), { x: x + 0.25, y: 2.0, w: 2.4, h: 0.8, fontSize: 40, bold: true, color: c.color });
    text(s, c.name, { x: x + 0.25, y: 2.85, w: 2.4, h: 0.45, fontSize: 18, bold: true });
    arrows(s, c.items, x + 0.25, 3.45, 2.45, 1.8, 13);
    text(s, c.speaker, { x: x + 0.25, y: 5.35, w: 2.4, h: 0.3, fontSize: 11.5, bold: true, color: c.color });
  });
  takeaway(s, 'Answer first, then the evidence: diagnosis, portfolio, returns, execution.');
  s.addNotes('Ten seconds: four chapters, one speaker each. Details are in the appendix for Q&A.');
}

// ---------- Chapter I ----------
divider(0);
{
  const s = content(0, 1, 'Strong foundations: the organisation of delivery holds value back', 'Outside-in readiness assessment, scored 1–5',
    'We are at the implementing stage, approaching scale. Strategy, data and delivery experience are solid. Organisation and governance score lowest. The bottleneck comes from public facts plus our insider’s local observation; the first 90 days test it against actual lead times and data blockers.');
  img(s, A('v3_readiness.png'), 0.4, 1.65, { w: 7.7, h: 4.5 });
  card(s, 8.45, 1.7, 4.4, 4.4);
  pill(s, 'Facts', 8.7, 1.9, BLUE);
  arrows(s, ['More than 10,000 live AI models', 'About 100 Digital Factory solutions since 2020, 60% with AI', 'AspenTech and Cognite data platforms rolling out to 2027–2028', 'Digital Line created in September 2025'], 8.7, 2.35, 4.0, 2.0, 12.5);
  pill(s, 'Bottleneck', 8.7, 4.4);
  text(s, 'One project, four reporting lines: project lead, branch data engineer, TDF data scientist and end user do not share objectives.', { x: 8.7, y: 4.8, w: 4.0, h: 1.2, fontSize: 12.5, color: '1A1A1A' });
  takeaway(s, 'The constraint is how project work is organised, not technology or ownership.');
}
{
  const s = content(0, 2, 'Keep the hub; give each project a dedicated trio', 'Hub-and-spoke unchanged; objectives and gates unchanged',
    'Today four people on four lines. Proposed: TDF data scientist, branch data engineer and business expert work together for a large share of their time, report day to day to the branch project lead, and keep their line manager for standards and careers. We measure lead time, review intervals, projects per lead and adoption.');
  img(s, A('v3_operating_model.png'), 0.4, 1.65, { w: 9.3, h: 4.55 });
  card(s, 9.95, 1.7, 2.9, 4.4);
  pill(s, 'What we test', 10.15, 1.9, BLUE);
  arrows(s, ['Lead time to first live use', 'Interval between progress reviews', 'Projects steered per lead', 'Active users and decisions recorded'], 10.15, 2.35, 2.55, 2.4, 12.5);
  pill(s, 'Cost', 10.15, 4.85, GOOD);
  text(s, 'Inside project envelopes: no new organisation, no new platform.', { x: 10.15, y: 5.25, w: 2.55, h: 0.8, fontSize: 11, color: '1A1A1A' });
  takeaway(s, 'Shorter cycles and more projects per lead, with the same standards and gates.');
}

// ---------- Chapter II ----------
divider(1);
{
  const s = content(1, 1, 'Ten initiatives, 70/20/10 by design: H1 pays back first and funds the J-curve', 'Portfolio: $9.82m one-time investment, $21.94m over Y0–Y5',
    'Ten initiatives across branches. H1 at 70.5% of one-time investment: reliability and cost on long-lived assets pay back fastest. H2 at 19.4%: cross-functional workflows where contracts allow cash capture. H3 at 10.2%: P12 e-SAF licensing, a bounded option that stops if its gates fail. No proprietary model is built.');
  img(s, A('selected_portfolio_map.png'), 0.4, 1.6, { w: 6.6, h: 4.6 });
  const hz = [['H1  ·  70.5%', BLUE, 'Reliability and cost on existing assets, fast payback', 'P01 · P02 · P04 · P05 · P08 · P13 · E01'],
    ['H2  ·  19.4%', TEAL, 'Cross-functional workflows where contracts allow cash capture', 'P03 · P09'],
    ['H3  ·  10.2%', ORANGE, 'Bounded option: stops, with a $0.10m closure, if gates fail', 'P12 e-SAF technology licensing']];
  hz.forEach(([t, c, d, p], i) => {
    const y = 1.7 + i * 1.32;
    card(s, 7.3, y, 5.55, 1.18);
    pill(s, t, 7.5, y + 0.15, c, 1.6);
    text(s, d, { x: 9.25, y: y + 0.13, w: 3.45, h: 0.6, fontSize: 11.5, bold: true });
    text(s, p, { x: 7.5, y: y + 0.65, w: 5.2, h: 0.4, fontSize: 11, color: GREY });
  });
  text(s, [{ text: 'Sourcing: ', options: { bold: true } }, { text: 'buy or blend market tools with our data and experts; partner for H3; no proprietary model.' }],
    { x: 7.3, y: 5.75, w: 5.55, h: 0.45, fontSize: 11, color: '1A1A1A' });
  takeaway(s, 'A portfolio, not a list of pilots: each horizon has a role and a stop rule.');
}

// Focus slides share one layout: four-step chain, then scenarios and the weakest assumption.
function focus(k, f) {
  const s = content(1, k, f.title, f.sub, f.notes);
  const steps = [['1  Money in', f.money], ['2  Value created', f.value], ['3  Go / no-go', f.gate], ['4  If it works', f.next]];
  steps.forEach(([t, body], i) => {
    const x = 0.5 + i * 3.1;
    card(s, x, 1.65, 2.95, 2.55);
    pill(s, t, x + 0.18, 1.8, i === 2 ? RED : BLUE, 1.75);
    text(s, body, { x: x + 0.18, y: 2.22, w: 2.6, h: 1.9, fontSize: 12, color: '1A1A1A' });
    if (i < 3) text(s, '›', { x: x + 2.93, y: 2.6, w: 0.2, h: 0.5, fontSize: 22, bold: true, color: RED, align: 'center' });
  });
  text(s, `Returns by scenario, ${f.unit} at ${f.hurdle} project hurdle`, { x: 0.5, y: 4.38, w: 6, h: 0.3, fontSize: 11, bold: true, color: GREY });
  table(s, [['Scenario', 'NPV', 'IRR', 'Payback'], ...f.rows], 0.5, 4.7, 6.0, [1.8, 1.4, 1.3, 1.5], 11);
  card(s, 6.8, 4.38, 6.05, 1.75, 'FDECEC');
  pill(s, 'Weakest assumption', 7.0, 4.52, RED, 1.95);
  text(s, f.weak, { x: 7.0, y: 4.92, w: 5.7, h: 1.15, fontSize: 12.5, color: '1A1A1A' });
  takeaway(s, f.take);
}
focus(2, {
  title: 'P13 retail: €1.0m in 100 stations pays back in 2.9 years, if markdowns prove incremental',
  sub: 'Focus 1 · French retail demand and controlled markdowns · H1 · buy labels, blend forecasting',
  money: '€1.0m one-time: €0.8m electronic labels and software (capex, Y0–Y1), €0.2m integration and training.\nRun cost €0.06–0.12m a year.\nOur insider’s local observation: about €1m for 100 large stations.',
  value: '€0.635m a year at full scale:\nWaste 100 × €350k × 70% × 4% × 25% = €0.245m\nMarkdowns 100 × 1,000 items × €2.50 = €0.250m\nStock-outs 100 × €50k × 8% × 35% = €0.140m',
  gate: 'Month 12, retail sponsor + Finance:\nmatched-store trial vs baseline; ≥60% of decisions in the tool; prospective NPV > 0 at 9%; labels must beat forecast-only.',
  next: 'Roll labels out to all 100 stations in Y2.\nIf labels do not pay, keep forecast-only; if the case fails 9%, stop.\nWider rollout needs a separate case.',
  unit: '€m', hurdle: '9%',
  rows: [['Downside', '+0.14', '14.8%', '3.8 years'], ['Base', '+0.49', '30.0%', '2.9 years'], ['Upside', '+0.84', '46.0%', '2.3 years']],
  weak: 'Without the markdown stream, benefit falls to €0.385m a year, below the €0.446m break-even. Markdown value is measured first, on separate SKU cohorts; the cheaper forecast-only design is the fallback.',
  take: 'We name the weakest assumption, measure it first and keep a cheaper fallback.',
  notes: 'This is the case we know best through our insider. Walk the chain left to right: where the money goes, how each euro of value is computed, what decides go or no-go at month 12, what happens next. Then the downside: still positive at project level. Weakest point: incremental markdown value.',
});
focus(3, {
  title: 'P01 refining: $1.4m to recover 0.45% throughput; NPV stays positive at 58% of the benefit',
  sub: 'Focus 2 · Refinery predictive maintenance on two sites · H1 · vendor tools blended with site expertise',
  money: '$1.4m one-time: $1.0m hardware and software (capex, Y0–Y1), $0.4m implementation and training.\nRun cost $0.20–0.40m a year.\nExisting AspenTech platform is reused.',
  value: '$1.87m a year at full scale:\n250 kb/d × 365 × 0.45% recovered × 70% sold × $6/bbl = $1.72m\n+ $0.15m avoided emergency repairs',
  gate: 'Month 12, refining sponsor + Finance:\nsafe pilot; alert → action → sold barrel verified; ≥60% of decisions in the tool; prospective NPV > 0 at 9.5%.',
  next: 'Extend to more equipment on the two sites.\nOther refineries only through a separate case.\nPause or stop on safety or missed thresholds.',
  unit: '$m', hurdle: '9.5%',
  rows: [['Downside', '+0.43', '19.1%', '3.7 years'], ['Base', '+1.62', '47.6%', '2.6 years'], ['Upside', '+2.53', '69.1%', '2.2 years']],
  weak: 'Throughput, margin and sold share are assumptions, not site actuals. NPV reaches zero at $1.08m a year, 57.6% of the model. Equinor reports $120m cumulative predictive-maintenance value since 2020: context, not proof.',
  take: 'A prediction score is not a return: we count only sold barrels and avoided repair invoices.',
  notes: 'Classic H1: fast payback on an existing asset. Emphasise the evidence chain and that a missed or unacted alert earns nothing. Margin of safety: the benefit can fall by 42% before NPV turns negative.',
});
focus(4, {
  title: 'P03 drilling: $1.4m that pays only if saved rig days reduce what we pay',
  sub: 'Focus 3 · Deepwater drilling advisory on two operated rigs · H2 · buy and blend, no autonomous steering',
  money: '$1.4m one-time: $0.8m integration and software (capex, Y0–Y1), $0.6m commissioning and training.\nRun cost $0.30–0.50m a year.\nExisting Cognite deployment is reused.',
  value: '$2.88m a year at full scale:\n2 rigs × 6 avoidable days × $0.40m/day × 60% realisation\n(80% economic share × 75% payment avoidability)',
  gate: 'Gate 0: contract allows rig release or lower charges; operator and partner consent.\nMonth 12: invoice-verified saving; prospective NPV > 0 at 11%.',
  next: 'Extend to further operated campaigns.\nIf the contract prevents capture, stop that scope.\nHSE and drilling experts keep authority.',
  unit: '$m', hurdle: '11%',
  rows: [['Downside', '+0.42', '18.4%', '3.9 years'], ['Base', '+1.86', '43.2%', '3.1 years'], ['Upside', '+2.79', '57.4%', '2.7 years']],
  weak: 'If our economic share is 40% rather than 80%, the benefit halves to $1.44m a year, below the $1.66m break-even. That is why the contract test comes at Gate 0, before Y1 spend.',
  take: 'Time saved is not cash saved: the contract test comes before any Y1 spend.',
  notes: 'H2: a redesigned cross-functional workflow, with higher value and later payback. The key risk is contractual, not technical. BP’s published well-planning example is context only.',
});

// ---------- Chapter III ----------
divider(2);
{
  const s = content(2, 1, 'Build in Y1, then about $2.8m a year of run cost from Y4', 'Investment envelope by cost category, $m',
    'Six categories. Y1 build: integration and talent 25% each. By Y3, model operations 22% and governance 8%; integration falls to 12%. Capex $5.69m only in Y0–Y1, for bought hardware and software; cloud, licences and support are opex. Run cost $2.74–2.79m from Y4. Branches co-fund 40% of Y2 and 60% of Y3–Y5.');
  table(s, [['$m', 'Y0', 'Y1', 'Y2', 'Y3', 'Y0–Y3'],
    ['Compute and equipment', '0.87', '1.71', '0.46', '0.48', '3.52'], ['Talent and change', '0.72', '2.14', '0.58', '0.63', '4.07'],
    ['Integration', '0.58', '2.14', '0.35', '0.32', '3.38'], ['Model operations', '0.14', '0.68', '0.39', '0.58', '1.80'],
    ['Data engineering', '0.43', '1.45', '0.37', '0.42', '2.68'], ['Governance and legal', '0.14', '0.43', '0.16', '0.21', '0.95'],
    ['Total', '2.90', '8.55', '2.31', '2.64', '16.40'], ['of which capital expenditure', '2.90', '2.80', '0.00', '0.00', '5.69']],
  0.5, 1.75, 7.3, [2.8, 0.85, 0.85, 0.85, 0.85, 1.1], 13);
  const facts = [['Build to run', 'Integration and talent 25% each in Y1; model operations 22% and governance 8% by Y3.'],
    ['Capex vs opex', 'Bought labels and tools are capex ($5.69m, Y0–Y1); cloud, licences and support are opex.'],
    ['Run cost', '$2.74–2.79m a year from Y4, for $21.94m over Y0–Y5.'],
    ['Co-funding', 'Branches pay 40% of Y2 and 60% of Y3–Y5 run costs.']];
  facts.forEach(([t, d], i) => {
    const y = 1.75 + i * 1.08;
    card(s, 8.15, y, 4.7, 0.95);
    text(s, t, { x: 8.35, y: y + 0.1, w: 4.3, h: 0.3, fontSize: 12, bold: true, color: BLUE });
    text(s, d, { x: 8.35, y: y + 0.4, w: 4.3, h: 0.5, fontSize: 11.5, color: '1A1A1A' });
  });
  takeaway(s, 'Run costs are budgeted from day one, and branches take over most of them.');
}
{
  const s = content(2, 2, 'Expected NPV +$5.62m at 10%; not investing costs $1.32m more', 'Three scenarios on one central cost estimate; probability-weighted',
    'Hurdle 10% = 7% WACC + 3-point AI premium. Expected IRR 27.8% clears it by 18 points. The downside misses the hurdle (5.7%) but still returns cash: +$2.27m by Y5. Doing nothing lets refining margin, rig rates and churn deteriorate: avoiding part of that is worth $1.32m, so the decision value is $6.94m. A one-year delay costs $0.65m.');
  table(s, [['Scenario', 'Prob.', 'NPV 10%', 'IRR', 'Cash Y5'],
    ['Downside', '30%', '−1.30', '5.7%', '+2.27'], ['Base', '50%', '+7.11', '32.6%', '+13.78'], ['Upside', '20%', '+12.28', '48.2%', '+20.83'],
    ['Expected', '', '+5.62', '27.8%', '+11.74']], 0.5, 1.75, 6.2, [1.7, 0.9, 1.2, 1.1, 1.3], 12.5);
  text(s, 'Downside: slower adoption, 80–90% of benefits, 105–110% of costs, P12 stopped. Upside: 115% of benefits, faster ramp.',
    { x: 0.5, y: 3.85, w: 6.2, h: 0.5, fontSize: 10, color: GREY });
  const big = [['27.8%', 'expected IRR vs 10% hurdle\n(7% WACC + 3 pts)'], ['$6.94m', 'decision value vs doing nothing'], ['−$0.65m', 'NPV lost per year of delay']];
  big.forEach(([v, l], i) => {
    const x = 0.5 + i * 2.1;
    card(s, x, 4.45, 1.95, 1.65);
    text(s, v, { x, y: 4.58, w: 1.95, h: 0.6, fontSize: 24, bold: true, color: i === 2 ? RED : NAVY, align: 'center', valign: 'middle' });
    text(s, l, { x: x + 0.1, y: 5.22, w: 1.75, h: 0.8, fontSize: 10, color: GREY, align: 'center' });
  });
  img(s, A('selected_inaction_bridge.png'), 7.0, 1.7, { w: 5.85, h: 4.45 });
  takeaway(s, 'An honest downside below the hurdle, but no scenario loses cash.');
}
{
  const s = content(2, 3, 'Costs land first; each release needs evidence', 'Base-case J-curve with funding gates, $m',
    'Trough −$9.8m at end Y1 in the base case (−$10.2m expected, −$11.5m downside). Break-even after 3.3 years (3.4 expected, about 4.6 downside). Each tranche is released only on the gate evidence on the right. A failed gate stops further avoidable spend.');
  img(s, A('v3_funding_gates.png'), 0.4, 1.6, { w: 7.9, h: 4.6 });
  const gates = [['Now', 'Tranche 1: $2.90m (Y0)', 'Existing-solution, rights and safety checks per case'],
    ['~Day 90', 'Gate 0 releases $8.55m (Y1)', 'Trio staffed, baseline signed by Finance'],
    ['Month 12', 'Gate 1 releases $2.31m (Y2)', 'Verified benefit, adoption thresholds, spend within 10%, 40% co-funding'],
    ['Month 24', 'Gate 2 releases Y3–Y5 run', 'Benefits cover run costs, 60% co-funding']];
  gates.forEach(([t, a, d], i) => {
    const y = 1.7 + i * 1.12;
    card(s, 8.55, y, 4.3, 1.0);
    pill(s, t, 8.7, y + 0.12, i === 0 ? RED : BLUE, 1.15);
    text(s, a, { x: 9.98, y: y + 0.12, w: 2.8, h: 0.3, fontSize: 11.5, bold: true });
    text(s, d, { x: 8.7, y: y + 0.5, w: 4.05, h: 0.45, fontSize: 11, color: '1A1A1A' });
  });
  takeaway(s, 'Maximum exposure before the first gate: $2.90m.');
}

// ---------- Chapter IV ----------
divider(3);
{
  const s = content(3, 1, 'Four failure modes, four owners, early signals before month 6', 'Change management, adoption and skills',
    'Each failure mode has an early signal and a named owner. Adoption is measured as a staircase: usage, then behaviour, then value. Thresholds are agreed now: 40% of eligible users active at month 6, 60% of decisions recorded through the tool at month 12. Training in three tiers. Communication runs bottom-up: weekly user sessions, monthly one-page dashboard, quarterly gate reviews.');
  const modes = [['Specialist shortage or attrition', 'Unfilled secondments, single points of failure', 'CHRO + Digital Factory lead'],
    ['Managers cannot release experts', 'Protected time not met, low attendance', 'Branch sponsors'],
    ['Governance lag', 'Consultation or clearance missing before release', 'General Counsel, DPO'],
    ['Board impatience in the J-curve', 'Budget questioned before month 12', 'CEO + CFO']];
  modes.forEach(([t, sig, o], i) => {
    const x = 0.5 + (i % 2) * 3.55, y = 1.7 + Math.floor(i / 2) * 2.25;
    card(s, x, y, 3.4, 2.1);
    text(s, t, { x: x + 0.2, y: y + 0.15, w: 3.0, h: 0.6, fontSize: 13, bold: true });
    text(s, [{ text: 'Signal  ', options: { bold: true, color: RED } }, { text: sig }], { x: x + 0.2, y: y + 0.8, w: 3.0, h: 0.6, fontSize: 12, color: '1A1A1A' });
    text(s, [{ text: 'Owner  ', options: { bold: true, color: BLUE } }, { text: o }], { x: x + 0.2, y: y + 1.45, w: 3.0, h: 0.5, fontSize: 12, color: '1A1A1A' });
  });
  const stairs = [['Months 0–6', 'Usage', '≥40% of eligible users active'], ['Months 6–12', 'Behaviour', '≥60% of decisions recorded in the tool'], ['Month 12+', 'Value', 'Finance-verified incremental cash']];
  text(s, 'Adoption staircase', { x: 7.85, y: 1.7, w: 5, h: 0.3, fontSize: 12, bold: true, color: GREY });
  stairs.forEach(([p, t, d], i) => {
    const x = 7.85 + i * 1.68, h = 1.2 + i * 0.55, y = 4.15 - h;
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 1.6, h, fill: { color: [TEAL, BLUE, NAVY][i] }, line: { color: WHITE } });
    text(s, t, { x: x + 0.1, y: y + 0.1, w: 1.4, h: 0.3, fontSize: 12, bold: true, color: WHITE });
    text(s, d, { x: x + 0.1, y: y + 0.42, w: 1.4, h: 0.7, fontSize: 9.5, color: WHITE });
    text(s, p, { x, y: 4.2, w: 1.6, h: 0.25, fontSize: 9.5, color: GREY, align: 'center' });
  });
  card(s, 7.85, 4.6, 5.0, 1.55);
  text(s, 'Training in three tiers', { x: 8.05, y: 4.7, w: 4.6, h: 0.3, fontSize: 12, bold: true, color: BLUE });
  arrows(s, [['All affected staff: ', 'AI literacy, data use, escalation'], ['Trio and managers: ', 'workflow, validation, oversight'], ['Executives: ', 'scenarios, portfolio risk, gates']], 8.05, 5.05, 4.65, 1.05, 10.5);
  takeaway(s, 'Stop rules are agreed before launch: metric, threshold, date, owner.');
}
{
  const s = pres.addSlide(); s.background = { color: NAVY };
  slideNo += 1; gauge(s, 3, 2, true);
  s.addImage({ path: LOGO, x: 12.05, y: 0.28, w: 0.82, h: 0.82 / ratio(LOGO) });
  text(s, `Fictional academic document · AI Transformation Strategies course, Albert School   |   ${slideNo}`, { x: 8.05, y: 7.02, w: 4.8, h: 0.3, fontSize: 8, color: 'B8C4D0', align: 'right' });
  text(s, 'The ask: approve Tranche 1 today', { x: 0.5, y: 0.45, w: 11, h: 0.8, fontSize: 32, bold: true, color: WHITE });
  text(s, 'Approve the $21.94m five-year envelope as a planning ceiling, not a commitment to deploy every project.', { x: 0.5, y: 1.3, w: 11, h: 0.4, fontSize: 15, color: 'D6E4F2' });
  const steps = [['Today', '$2.90m', 'Tranche 1 (Y0), case by case after rights and safety checks'], ['~Day 90 · Gate 0', '$8.55m', 'Y1, once each trio is staffed and its baseline signed'],
    ['Month 12 · Gate 1', '$2.31m', 'Y2, on verified benefit, adoption, spend within 10%, 40% co-funding'], ['Month 24 · Gate 2', 'Run Y3–Y5', 'Only if benefits cover run costs and branches co-fund 60%']];
  steps.forEach(([t, v, d], i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.3, w: 2.9, h: 2.9, fill: { color: i === 0 ? RED : '17345C' }, line: { color: i === 0 ? RED : '17345C' }, rectRadius: 0.08 });
    text(s, t, { x: x + 0.2, y: 2.45, w: 2.5, h: 0.35, fontSize: 12, bold: true, color: i === 0 ? WHITE : TEAL });
    text(s, v, { x: x + 0.2, y: 2.9, w: 2.5, h: 0.75, fontSize: 30, bold: true, color: WHITE, valign: 'middle' });
    text(s, d, { x: x + 0.2, y: 3.8, w: 2.5, h: 1.2, fontSize: 11.5, color: 'D6E4F2' });
  });
  text(s, 'Decision date: 16 November 2026', { x: 0.5, y: 5.6, w: 12.33, h: 0.5, fontSize: 20, bold: true, color: WHITE, align: 'center' });
  s.addNotes('Close on the ask: one vote today, $2.90m. Everything after that is released against evidence the Board will see. Then open Q&A; use the appendix.');
}

// ---------- Appendix ----------
{
  const s = pres.addSlide(); s.background = { color: WHITE };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 4.6, h: 6.8, fill: { color: GREY }, line: { color: GREY } });
  text(s, 'A', { x: 0.6, y: 2.2, w: 3.6, h: 2.2, fontSize: 120, bold: true, color: WHITE, valign: 'middle' });
  frame(s, { appendix: true });
  text(s, 'Appendix', { x: 5.3, y: 2.0, w: 7.3, h: 1.0, fontSize: 40, bold: true, color: GREY, valign: 'middle' });
  arrows(s, ['Stop rules by risk', 'Portfolio returns by scenario', 'Focus cases: cumulative cash', 'P12 e-SAF licensing option (H3)', 'If the budget is halved', 'Complementary cases'], 5.3, 3.2, 7, 2.6, 15);
  s.addNotes('Backup for Q&A only.');
}
function appx(title, sub, notes) { const s = pres.addSlide(); s.background = { color: WHITE }; frame(s, { appendix: true }); head(s, title, sub); s.addNotes(notes); return s; }
{
  const s = appx('Every risk has a dated stop rule and an owner', 'Metric, threshold, date, action', 'Read the relevant row when challenged on a specific risk.');
  table(s, [['Risk', 'Stop rule (metric, threshold, date, action)', 'Owner'],
    ['Value', 'No Finance-verified incremental benefit, or negative prospective NPV at the project hurdle, at month 12 → pause, redesign or stop', 'CFO + branch sponsor'],
    ['Delivery', 'Contract does not allow capture of rig payments at Gate 0 (P03), or labels do not beat forecast-only at month 12 (P13) → stop that scope', 'Digital Factory lead + project lead'],
    ['Trust and compliance', 'Any critical safety, cyber or privacy incident, or missing employee consultation → immediate pause until the control owner approves restart', 'General Counsel, DPO, HSE'],
    ['People and adoption', 'Under 40% of eligible users active at month 6 → remediate or stop within 30 days; under 60% of decisions recorded at month 12 → no expansion', 'Branch sponsor + CHRO'],
    ['H3 option', 'No IP clearance and two qualified developers by Y2, or no paid-evaluation interest by Y3 → stop; $0.10m closure', 'OneTech + commercial lead']],
  0.5, 1.75, 12.33, [2.1, 7.4, 2.83], 13);
}
{
  const s = appx('Portfolio returns by scenario', 'NPV at 10% and IRR, $m', 'Spread from 5.7% to 48.2% IRR: value depends on adoption, which is why release is gated.');
  img(s, A('selected_scenario_npv.png'), 0.4, 1.7, { w: 6.1, h: 4.5 });
  img(s, A('selected_scenario_irr.png'), 6.75, 1.7, { w: 6.1, h: 4.5 });
}
{
  const s = appx('Focus cases: cumulative cash by scenario', 'P01, P03, P12 and P13', 'All focus cases except P12 stay positive at project level in the downside.');
  img(s, A('selected_focus_jcurves.png'), 3.4, 1.6, { w: 6.6, h: 5.3 });
}
{
  const s = appx('P12 e-SAF licensing: a bounded H3 option, with no invented payback', 'Conditional third-party technology fees; $2.85m over Y0–Y5',
    'H3 is an option: gates on IP, developer interest and paid evaluation. If any fails, avoidable spending stops with a $0.10m closure allowance.');
  img(s, A('selected_p12_jcurve.png'), 0.4, 1.7, { w: 6.3, h: 4.4 });
  card(s, 7.0, 1.75, 5.85, 4.3);
  pill(s, 'Gates', 7.2, 1.95, RED);
  arrows(s, ['Before Y0: OneTech and Legal confirm non-duplication, data and licensing rights',
    'Before Y2: two qualified third-party developers agree to discuss a defined application',
    'Before Y3: three independent runs repeat the result; freedom-to-operate check; one developer ready for a paid evaluation',
    'Any failure: stop avoidable spend; $0.10m closure'], 7.2, 2.4, 5.45, 3.5, 13);
}
{
  const s = appx('If the budget is halved: four featured cases keep a 34.8% base IRR', '$11.35m instead of $21.94m',
    'Half budget keeps P01, P03, P12, P13 but drops five complementary cases and relies on existing controls.');
  img(s, A('selected_half_budget.png'), 1.9, 1.7, { w: 9.5, h: 4.5 });
}
{
  const s = appx('Complementary cases: same method, simpler estimates', 'Base assumptions at full rollout; each needs a business-owner baseline',
    'These cases follow the same chain but with lighter evidence; they are released only after a baseline is signed.');
  table(s, [['Case', 'Horizon', 'Cost Y0–Y5, $m', 'Value formula (assumptions)'],
    ['P02 Upstream production surveillance', 'H1', '2.23', '2 hubs × 135 b/d recovered × $15/bbl contribution'],
    ['P04 Renewable fleet performance', 'H1', '2.70', '3,000 MW × 8,760 h × 30% × 0.45% × $45/MWh = $1.60m/yr'],
    ['P05 Copilot licence management', 'H1', '0.73', '10,000 licences × 12% cancellable × $30/month'],
    ['P08 Customer retention', 'H1', '2.95', '1.2m accounts × 10% churn × 9% reduction × $150 = $1.62m/yr'],
    ['P09 LNG voyage optimisation', 'H2', '1.04', '30 voyages × $1m fuel × 2% improvement'],
    ['E01 Shared value and model controls', 'H1', '0.94', 'Register, baselines, controls; no separate benefit booked']],
  0.5, 1.75, 12.33, [3.6, 1.1, 1.7, 5.93], 13);
}

fs.mkdirSync(path.dirname(OUT), { recursive: true });
await pres.writeFile({ fileName: OUT });
console.log(`Wrote ${path.relative(ROOT, OUT)} (${slideNo} slides)`);
