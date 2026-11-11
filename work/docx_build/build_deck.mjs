// Board defence deck (16:9), pitch version: one message per slide, charts and isolated KPIs on screen,
// explanations in the speaker notes. Same structure and style as the frozen v1 (build_deck_v1.mjs).
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
  GOOD = '4E7A12', GREY = '5F6B7A', CARD = 'F2F5F9', RULE = 'DCE5EB', WHITE = 'FFFFFF', PINK = 'FDECEC';
const FONT = 'Arial';
const SPEAKERS = ['Alexandre Waerniers', 'Vincent Lamy', 'Yoni Mahieddine', 'Nahel Bachriri']; // ponytail: chapter order = name order; swap here
const CHAPTERS = [
  { name: 'Where we stand', color: RED, n: 2, speaker: SPEAKERS[0], items: ['Readiness and bottleneck', 'Delivery model: the dedicated trio'] },
  { name: 'What we fund', color: ORANGE, n: 4, speaker: SPEAKERS[1], items: ['Portfolio and horizon mix', 'Focus: P13 retail', 'Focus: P01 refining', 'Focus: P03 drilling'] },
  { name: 'What it returns', color: BLUE, n: 3, speaker: SPEAKERS[2], items: ['Investment envelope', 'Scenarios and cost of inaction', 'J-curve and staged release'] },
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
// Isolated KPI tile: small label, big value, one-line note.
function kpi(s, x, y, w, h, label, value, note, color = NAVY, size = 32, fill = CARD) {
  card(s, x, y, w, h, fill);
  text(s, label, { x: x + 0.1, y: y + 0.14, w: w - 0.2, h: 0.3, fontSize: 11, bold: true, color: GREY, align: 'center' });
  text(s, value, { x: x + 0.05, y: y + 0.42, w: w - 0.1, h: h - 0.85, fontSize: size, bold: true, color, align: 'center', valign: 'middle', fit: 'shrink' });
  if (note) text(s, note, { x: x + 0.1, y: y + h - 0.42, w: w - 0.2, h: 0.3, fontSize: 10.5, color: GREY, align: 'center' });
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
  s.addNotes('Introduce the team in one sentence each. We play TotalEnergies’ internal digital transformation team; the professor is the CEO. Read the question on the right: that is the only decision we ask for.');
}

// ---------- 2. Decision (answer first) ----------
{
  const s = pres.addSlide(); s.background = { color: WHITE };
  frame(s, { ch: -1 });
  head(s, 'We ask you to release $2.90m today, the first tranche of a $21.94m gated envelope', 'The decision in one page');
  const kpis = [['Decision today', '$2.90m', 'Tranche 1 (Y0)', RED], ['Five-year envelope', '$21.94m', 'ceiling, released by gates', NAVY],
    ['Expected NPV at 10%', '+$5.62m', '30 / 50 / 20 scenarios', NAVY], ['Expected IRR', '27.8%', 'vs 10% hurdle', NAVY], ['Downside NPV', '−$1.30m', 'cash still repaid by Y5', RED]];
  kpis.forEach(([l, v, n, c], i) => kpi(s, 0.5 + i * 2.5, 1.8, 2.33, 2.1, l, v, n, c, 36));
  pill(s, 'Why now', 0.5, 4.3, BLUE);
  const why = [['10,000+', 'AI models already live'], ['4', 'reporting lines per project today'], ['−$0.65m', 'NPV lost per year of delay']];
  why.forEach(([v, l], i) => {
    const x = 0.5 + i * 4.18;
    text(s, v, { x, y: 4.75, w: 1.75, h: 0.7, fontSize: 30, bold: true, color: i === 2 ? RED : BLUE, valign: 'middle' });
    text(s, l, { x: x + 1.8, y: 4.75, w: 2.2, h: 0.7, fontSize: 13, color: '1A1A1A', valign: 'middle' });
  });
  takeaway(s, 'Only $2.90m is at risk before the first gate; every later dollar needs evidence.');
  s.addNotes(`Lead with the answer.
Resolution (read it): invest $21.94m over five years (Y0–Y5) in ten AI initiatives run by dedicated branch–Digital Factory teams, to create an expected NPV of $5.62m at 10% (IRR 27.8%), with a downside NPV of −$1.30m, only $2.90m committed before the first gate, and every later release conditional on Finance-verified gates.
Why now, three facts: platforms exist (more than 10,000 live AI models, about 100 Digital Factory solutions); the bottleneck is organisational (each project is split across four reporting lines); waiting costs $0.65m of NPV per year.
Point at the red downside tile: even in the downside the programme returns its cash (+$2.27m by Y5); it only misses the 10% hurdle.`);
}

// ---------- 3. Agenda ----------
{
  const s = pres.addSlide(); s.background = { color: WHITE };
  frame(s, { ch: -1 });
  head(s, 'Four questions a sceptical Board asks, answered in order', 'Agenda');
  CHAPTERS.forEach((c, i) => {
    const x = 0.5 + i * 3.1;
    card(s, x, 1.8, 2.9, 4.1);
    text(s, String(i + 1).padStart(2, '0'), { x: x + 0.25, y: 2.1, w: 2.4, h: 1.1, fontSize: 54, bold: true, color: c.color });
    text(s, c.name, { x: x + 0.25, y: 3.35, w: 2.4, h: 1.0, fontSize: 22, bold: true });
    text(s, c.speaker, { x: x + 0.25, y: 5.3, w: 2.4, h: 0.3, fontSize: 12, bold: true, color: c.color });
  });
  takeaway(s, 'Answer first, then the evidence: diagnosis, portfolio, returns, execution.');
  s.addNotes('Ten seconds: four chapters, one speaker each. 1 Where we stand: readiness and the delivery bottleneck. 2 What we fund: portfolio and three focus cases. 3 What it returns: envelope, scenarios, J-curve. 4 How we make it stick: change and the ask. Details are in the appendix for Q&A.');
}

// ---------- Chapter I ----------
divider(0);
{
  const s = content(0, 1, 'Strong foundations: the organisation of delivery holds value back', 'Outside-in readiness assessment, scored 1–5',
    `We are at the implementing stage, approaching scale.
Facts: more than 10,000 live AI models; about 100 Digital Factory solutions since 2020, 60% with AI; AspenTech and Cognite data platforms rolling out to 2027–2028; Digital Line created in September 2025.
Strategy, data and delivery experience score 3 to 3.5; organisation and governance score lowest (2.5).
Bottleneck: one project, four reporting lines. Project lead, branch data engineer, TDF data scientist and end user do not share objectives, so iterations are slow and each lead steers few projects.
Source: public facts plus our insider’s local observation; scores are a team assessment, not an internal audit. The first 90 days test the bottleneck against actual lead times and data blockers.`);
  img(s, A('v3_readiness.png'), 0.4, 1.65, { w: 8.2, h: 4.5 });
  kpi(s, 9.0, 1.7, 3.85, 1.35, 'Live AI models', '10,000+', null, BLUE, 30);
  kpi(s, 9.0, 3.2, 3.85, 1.35, 'Digital Factory solutions', '~100', null, BLUE, 30);
  kpi(s, 9.0, 4.7, 3.85, 1.45, 'Reporting lines per project', '4', 'the bottleneck', RED, 34, PINK);
  takeaway(s, 'The constraint is how project work is organised, not technology or ownership.');
}
{
  const s = content(0, 2, 'Keep the hub; give each project a dedicated trio', 'Hub-and-spoke unchanged; objectives and gates unchanged',
    `Left, today: four people on four lines; nobody owns the project result end to end.
Right, proposed: TDF data scientist, branch data engineer and business expert work together for a large share of their time, report day to day to the branch project lead, and keep their line manager for standards and careers.
What we test: lead time to first live use, interval between progress reviews, projects steered per lead, active users and decisions recorded.
Cost: inside the project envelopes. No new organisation, no new platform.`);
  img(s, A('v3_operating_model.png'), 0.6, 1.65, { w: 12.1, h: 4.55 });
  takeaway(s, 'Shorter cycles and more projects per lead, with the same standards and gates.');
}

// ---------- Chapter II ----------
divider(1);
{
  const s = content(1, 1, 'Ten initiatives, 70/20/10 by design: H1 pays back first', 'Portfolio: $9.82m one-time investment, $21.94m over Y0–Y5',
    `Ten initiatives across branches; mix measured on one-time investment.
H1, 70.5%: reliability and cost on existing assets, fast payback (P01, P02, P04, P05, P08, P13, E01).
H2, 19.4%: cross-functional workflows where contracts allow cash capture (P03, P09).
H3, 10.2%: P12 e-SAF technology licensing, a bounded option that stops with a $0.10m closure if its gates fail.
Sourcing: buy or blend market tools with our data and experts; partner for H3; no proprietary model is built.`);
  img(s, A('selected_portfolio_map.png'), 0.4, 1.6, { w: 7.4, h: 4.6 });
  const hz = [['H1', '70.5%', 'fast payback on existing assets', BLUE], ['H2', '19.4%', 'new cross-functional workflows', TEAL], ['H3', '10.2%', 'bounded option, stops if gates fail', ORANGE]];
  hz.forEach(([h, v, d, c], i) => {
    const y = 1.7 + i * 1.5;
    card(s, 8.2, y, 4.65, 1.35);
    pill(s, h, 8.4, y + 0.2, c, 0.6);
    text(s, v, { x: 9.15, y: y + 0.08, w: 3.5, h: 0.75, fontSize: 34, bold: true, color: c, valign: 'middle' });
    text(s, d, { x: 8.4, y: y + 0.87, w: 4.3, h: 0.35, fontSize: 12, color: GREY });
  });
  takeaway(s, 'A portfolio, not a list of pilots: each horizon has a role and a stop rule.');
}

// Focus slides share one layout: the project J-curve, four KPIs and the weakest assumption.
function focus(k, f) {
  const s = content(1, k, f.title, f.sub, f.notes);
  img(s, A(f.chart), 0.4, 1.65, { w: 7.6, h: 4.5 });
  f.kpis.forEach(([l, v, n], i) => kpi(s, 8.3 + (i % 2) * 2.35, 1.7 + Math.floor(i / 2) * 1.6, 2.2, 1.45, l, v, n, NAVY, 26));
  card(s, 8.3, 4.95, 4.55, 1.2, PINK);
  pill(s, 'Weakest assumption', 8.5, 5.07, RED, 1.95);
  text(s, f.weak, { x: 8.5, y: 5.45, w: 4.2, h: 0.65, fontSize: 12.5, bold: true, color: '1A1A1A' });
  takeaway(s, f.take);
}
focus(2, {
  title: 'P13 retail: €1.0m in 100 stations pays back in 2.9 years, if markdowns prove incremental',
  sub: 'Focus 1 · French retail demand and controlled markdowns · H1 · buy labels, blend forecasting',
  chart: 'selected_p13_jcurve.png',
  kpis: [['Invest', '€1.0m', 'one-time, Y0–Y1'], ['Benefit', '€0.64m', 'a year at full scale'], ['Base NPV at 9%', '+€0.49m', 'IRR 30.0%'], ['Payback', '2.9 yrs', 'downside 3.8 yrs']],
  weak: 'Markdowns must be incremental: without them, the case falls below break-even.',
  take: 'We name the weakest assumption, measure it first and keep a cheaper fallback.',
  notes: `The case we know best through our insider. Walk the chain: money in, value, go/no-go, next step.
Money in: €1.0m one-time (€0.8m electronic labels and software as capex, €0.2m integration and training); run cost €0.06–0.12m a year. Our insider’s local observation: about €1m for 100 large stations.
Value: €0.635m a year at full scale. Waste 100 × €350k × 70% × 4% × 25% = €0.245m; markdowns 100 × 1,000 items × €2.50 = €0.250m; stock-outs 100 × €50k × 8% × 35% = €0.140m.
Go/no-go at month 12 (retail sponsor + Finance): matched-store trial vs baseline; at least 60% of decisions in the tool; prospective NPV above zero at 9%; labels must beat forecast-only.
If it works: labels in all 100 stations in Y2; wider rollout needs a separate case. If labels do not pay, keep forecast-only; if the case fails 9%, stop.
Chart: all three scenarios turn positive; downside NPV +€0.14m (IRR 14.8%).
Weakest assumption: without markdowns, benefit falls to €0.385m a year, below the €0.446m break-even. Markdown value is measured first on separate SKU cohorts.`,
});
focus(3, {
  title: 'P01 refining: $1.4m to recover 0.45% throughput; NPV stays positive at 58% of the benefit',
  sub: 'Focus 2 · Refinery predictive maintenance on two sites · H1 · vendor tools blended with site expertise',
  chart: 'selected_p01_jcurve.png',
  kpis: [['Invest', '$1.4m', 'one-time, Y0–Y1'], ['Benefit', '$1.87m', 'a year at full scale'], ['Base NPV at 9.5%', '+$1.62m', 'IRR 47.6%'], ['Payback', '2.6 yrs', 'downside 3.7 yrs']],
  weak: 'Throughput gain is assumed, not measured: NPV holds down to 58% of it.',
  take: 'A prediction score is not a return: we count only sold barrels and avoided repair invoices.',
  notes: `Classic H1: fast payback on an existing asset.
Money in: $1.4m one-time ($1.0m hardware and software as capex, $0.4m implementation and training); run cost $0.20–0.40m a year; the existing AspenTech platform is reused.
Value: $1.87m a year = 250 kb/d × 365 × 0.45% recovered × 70% sold × $6/bbl ($1.72m) + $0.15m avoided emergency repairs.
Go/no-go at month 12 (refining sponsor + Finance): safe pilot; alert → action → sold barrel verified; at least 60% of decisions in the tool; prospective NPV above zero at 9.5%.
If it works: more equipment on the two sites; other refineries only through a separate case. Pause or stop on safety or missed thresholds.
Weakest assumption: throughput, margin and sold share are assumptions, not site actuals. NPV reaches zero at $1.08m a year, 57.6% of the model, so the benefit can fall 42% first. Equinor reports $120m cumulative predictive-maintenance value since 2020: context, not proof.`,
});
focus(4, {
  title: 'P03 drilling: $1.4m that pays only if saved rig days reduce what we pay',
  sub: 'Focus 3 · Deepwater drilling advisory on two operated rigs · H2 · buy and blend, no autonomous steering',
  chart: 'selected_p03_jcurve.png',
  kpis: [['Invest', '$1.4m', 'one-time, Y0–Y1'], ['Benefit', '$2.88m', 'a year at full scale'], ['Base NPV at 11%', '+$1.86m', 'IRR 43.2%'], ['Payback', '3.1 yrs', 'downside 3.9 yrs']],
  weak: 'The rig contract must turn saved days into lower payments: tested at Gate 0.',
  take: 'Time saved is not cash saved: the contract test comes before any Y1 spend.',
  notes: `H2: a redesigned cross-functional workflow, higher value and later payback. The key risk is contractual, not technical.
Money in: $1.4m one-time ($0.8m integration and software as capex, $0.6m commissioning and training); run cost $0.30–0.50m a year; the existing Cognite deployment is reused.
Value: $2.88m a year = 2 rigs × 6 avoidable days × $0.40m a day × 60% realisation (80% economic share × 75% payment avoidability).
Go/no-go: Gate 0 checks that the contract allows rig release or lower charges, with operator and partner consent. Month 12: invoice-verified saving; prospective NPV above zero at 11%.
If it works: further operated campaigns. If the contract prevents capture, stop that scope. HSE and drilling experts keep authority; no autonomous steering.
Weakest assumption: at a 40% economic share instead of 80%, the benefit halves to $1.44m a year, below the $1.66m break-even. That is why the contract test comes before Y1 spend. BP’s published well-planning example is context only.`,
});

// ---------- Chapter III ----------
divider(2);
{
  const s = content(2, 1, 'Build in Y1, then about $2.8m a year of run cost from Y4', 'Investment envelope by cost category, $m (Y0–Y3; full table in appendix)',
    `Six categories. Y1 is the build year: integration and talent 25% each. By Y3, model operations reach 22% and governance 8%; integration falls to 12%.
Capex $5.69m only in Y0–Y1, for bought hardware and software (labels, tools); cloud, licences and support are opex.
Totals: Y0 $2.90m, Y1 $8.55m, Y2 $2.31m, Y3 $2.64m. From Y4 the run cost is $2.74–2.79m a year, for $21.94m over Y0–Y5.
Branches co-fund 40% of Y2 and 60% of Y3–Y5 run costs.`);
  const cats = [['Compute and equipment', [0.87, 1.71, 0.46, 0.48]], ['Talent and change', [0.72, 2.14, 0.58, 0.63]], ['Integration', [0.58, 2.14, 0.35, 0.32]],
    ['Model operations', [0.14, 0.68, 0.39, 0.58]], ['Data engineering', [0.43, 1.45, 0.37, 0.42]], ['Governance and legal', [0.14, 0.43, 0.16, 0.21]]];
  s.addChart(pres.charts.BAR, cats.map(([name, values]) => ({ name, labels: ['Y0', 'Y1', 'Y2', 'Y3'], values })), {
    x: 0.4, y: 1.6, w: 7.6, h: 4.6, barDir: 'col', barGrouping: 'stacked', barGapWidthPct: 60,
    chartColors: [NAVY, BLUE, TEAL, GREEN, ORANGE, GREY], showLegend: true, legendPos: 'r', legendFontSize: 10, legendFontFace: FONT, legendColor: '1A1A1A',
    catAxisLabelColor: GREY, catAxisLabelFontSize: 12, catAxisLabelFontFace: FONT, valAxisLabelColor: GREY, valAxisLabelFontSize: 10, valAxisLabelFontFace: FONT,
    valAxisMaxVal: 9, valAxisMajorUnit: 3, valGridLine: { color: RULE, size: 0.5 }, catGridLine: { style: 'none' },
  });
  kpi(s, 8.3, 1.7, 2.2, 1.45, 'Envelope Y0–Y5', '$21.94m', 'planning ceiling', NAVY, 24);
  kpi(s, 10.65, 1.7, 2.2, 1.45, 'Build year Y1', '$8.55m', 'released at Gate 0', NAVY, 24);
  kpi(s, 8.3, 3.3, 2.2, 1.45, 'Capex', '$5.69m', 'Y0–Y1 only', NAVY, 24);
  kpi(s, 10.65, 3.3, 2.2, 1.45, 'Run cost from Y4', '$2.8m/yr', '$2.74–2.79m', NAVY, 24);
  kpi(s, 8.3, 4.9, 4.55, 1.25, 'Branch co-funding of run costs', '40% → 60%', 'Y2, then Y3–Y5', GOOD, 26);
  takeaway(s, 'Run costs are budgeted from day one, and branches take over most of them.');
}
{
  const s = content(2, 2, 'Expected NPV +$5.62m at 10%; not investing costs $1.32m more', 'Three scenarios on one central cost estimate; probability-weighted 30 / 50 / 20',
    `Left: NPV by scenario. Downside: slower adoption, 80–90% of benefits, 105–110% of costs, P12 stopped (−$1.30m, IRR 5.7%). Base: planned adoption (+$7.11m, 32.6%). Upside: 115% of benefits, faster ramp (+$12.28m, 48.2%). Expected: +$5.62m, 27.8%.
Hurdle 10% = 7% WACC + 3-point AI premium; expected IRR clears it by 18 points.
The downside misses the hurdle but still returns cash: +$2.27m cumulative by Y5. We do not hide it: that is what the gates are for.
Right: doing nothing is not neutral. Refining margin, rig rates and customer churn deteriorate; avoiding part of that is worth $1.32m, so the decision value is $6.94m. A one-year delay costs $0.65m of NPV.`);
  img(s, A('selected_scenario_npv.png'), 0.4, 1.65, { w: 6.1, h: 4.5 });
  img(s, A('selected_inaction_bridge.png'), 6.75, 1.65, { w: 6.1, h: 4.5 });
  takeaway(s, 'An honest downside below the hurdle, but no scenario loses cash.');
}
{
  const s = content(2, 3, 'Costs land first; each release needs evidence', 'Base-case J-curve with funding gates, $m',
    `Trough −$9.8m at end Y1 in the base case (−$10.2m expected, −$11.5m downside). Break-even after 3.3 years (3.4 expected, about 4.6 downside).
Each tranche needs evidence:
Now, Tranche 1 $2.90m (Y0): existing-solution, rights and safety checks per case.
About day 90, Gate 0 releases $8.55m (Y1): trio staffed, baseline signed by Finance.
Month 12, Gate 1 releases $2.31m (Y2): verified benefit, adoption thresholds, spend within 10% of plan, 40% co-funding.
Month 24, Gate 2 releases Y3–Y5 run funding: benefits cover run costs, 60% co-funding.
A failed gate stops further avoidable spend.`);
  img(s, A('v3_funding_gates.png'), 0.4, 1.6, { w: 8.6, h: 4.6 });
  const gates = [['Now', '$2.90m', RED], ['~Day 90 · Gate 0', '$8.55m', BLUE], ['Month 12 · Gate 1', '$2.31m', BLUE], ['Month 24 · Gate 2', 'Run Y3–Y5', BLUE]];
  gates.forEach(([t, v, c], i) => {
    const y = 1.7 + i * 1.12;
    card(s, 9.3, y, 3.55, 1.0);
    pill(s, t, 9.45, y + 0.12, c, 1.75);
    text(s, v, { x: 9.45, y: y + 0.45, w: 3.25, h: 0.48, fontSize: 22, bold: true, color: c === RED ? RED : NAVY, valign: 'middle' });
  });
  takeaway(s, 'Maximum exposure before the first gate: $2.90m.');
}

// ---------- Chapter IV ----------
divider(3);
{
  const s = content(3, 1, 'Adoption measured step by step; four risks, four named owners', 'Change management: adoption measured as a staircase',
    `Adoption staircase, thresholds agreed now: months 0–6 usage (at least 40% of eligible users active at month 6); months 6–12 behaviour (at least 60% of decisions recorded in the tool at month 12); from month 12 value (Finance-verified incremental cash).
Failure modes, early signal and owner:
Specialist shortage or attrition: unfilled secondments, single points of failure (CHRO + Digital Factory lead).
Managers cannot release experts: protected time not met, low attendance (branch sponsors).
Governance lag: consultation or clearance missing before release (General Counsel, DPO).
Board impatience in the J-curve: budget questioned before month 12 (CEO + CFO).
Training in three tiers: all affected staff (AI literacy, data use, escalation); trio and managers (workflow, validation, oversight); executives (scenarios, portfolio risk, gates).
Communication: weekly user sessions, monthly one-page dashboard, quarterly gate reviews.`);
  const stairs = [['Months 0–6', 'Usage', '≥40%', 'users active'], ['Months 6–12', 'Behaviour', '≥60%', 'decisions in the tool'], ['Month 12+', 'Value', 'Cash', 'verified by Finance']];
  stairs.forEach(([p, t, v, d], i) => {
    const x = 0.5 + i * 2.25, h = 1.9 + i * 0.95, y = 5.6 - h;
    s.addShape(pres.shapes.RECTANGLE, { x, y, w: 2.15, h, fill: { color: [TEAL, BLUE, NAVY][i] }, line: { color: WHITE } });
    text(s, t, { x: x + 0.15, y: y + 0.15, w: 1.9, h: 0.35, fontSize: 14, bold: true, color: WHITE });
    text(s, v, { x: x + 0.15, y: y + 0.55, w: 1.9, h: 0.65, fontSize: 30, bold: true, color: WHITE, valign: 'middle' });
    text(s, d, { x: x + 0.15, y: y + 1.25, w: 1.9, h: 0.5, fontSize: 11, color: WHITE });
    text(s, p, { x, y: 5.68, w: 2.15, h: 0.28, fontSize: 11, color: GREY, align: 'center' });
  });
  const modes = [['Specialist shortage', 'CHRO + Digital Factory lead'], ['Experts not released', 'Branch sponsors'], ['Governance lag', 'General Counsel, DPO'], ['Board impatience', 'CEO + CFO']];
  modes.forEach(([t, o], i) => {
    const x = 7.6 + (i % 2) * 2.67, y = 1.7 + Math.floor(i / 2) * 2.15;
    card(s, x, y, 2.55, 1.95);
    text(s, t, { x: x + 0.18, y: y + 0.2, w: 2.2, h: 0.75, fontSize: 15, bold: true });
    text(s, 'Owner', { x: x + 0.18, y: y + 1.05, w: 2.2, h: 0.25, fontSize: 10, bold: true, color: BLUE });
    text(s, o, { x: x + 0.18, y: y + 1.3, w: 2.2, h: 0.55, fontSize: 12, color: '1A1A1A' });
  });
  takeaway(s, 'Stop rules are agreed before launch: metric, threshold, date, owner.');
}
{
  const s = pres.addSlide(); s.background = { color: NAVY };
  slideNo += 1; gauge(s, 3, 2, true);
  s.addImage({ path: LOGO, x: 12.05, y: 0.28, w: 0.82, h: 0.82 / ratio(LOGO) });
  text(s, `Fictional academic document · AI Transformation Strategies course, Albert School   |   ${slideNo}`, { x: 8.05, y: 7.02, w: 4.8, h: 0.3, fontSize: 8, color: 'B8C4D0', align: 'right' });
  text(s, 'The ask: approve Tranche 1 today', { x: 0.5, y: 0.45, w: 11, h: 0.8, fontSize: 32, bold: true, color: WHITE });
  text(s, '$21.94m five-year envelope: a planning ceiling, not a commitment to deploy every project.', { x: 0.5, y: 1.3, w: 11, h: 0.4, fontSize: 15, color: 'D6E4F2' });
  const steps = [['Today', '$2.90m', 'Tranche 1 (Y0)'], ['~Day 90 · Gate 0', '$8.55m', 'trios staffed, baselines signed'],
    ['Month 12 · Gate 1', '$2.31m', 'verified benefit and adoption'], ['Month 24 · Gate 2', 'Run Y3–Y5', 'benefits cover run costs']];
  steps.forEach(([t, v, d], i) => {
    const x = 0.5 + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.3, w: 2.9, h: 2.9, fill: { color: i === 0 ? RED : '17345C' }, line: { color: i === 0 ? RED : '17345C' }, rectRadius: 0.08 });
    text(s, t, { x: x + 0.2, y: 2.45, w: 2.5, h: 0.35, fontSize: 12, bold: true, color: i === 0 ? WHITE : TEAL });
    text(s, v, { x: x + 0.2, y: 2.95, w: 2.5, h: 0.9, fontSize: 34, bold: true, color: WHITE, valign: 'middle' });
    text(s, d, { x: x + 0.2, y: 4.1, w: 2.5, h: 0.8, fontSize: 13, color: 'D6E4F2' });
  });
  text(s, 'Decision date: 16 November 2026', { x: 0.5, y: 5.6, w: 12.33, h: 0.5, fontSize: 20, bold: true, color: WHITE, align: 'center' });
  s.addNotes(`Close on the ask: one vote today, $2.90m.
1. Approve the $21.94m five-year envelope as a planning ceiling.
2. Release Tranche 1 today, $2.90m (Y0), case by case after existing-solution, rights and safety checks.
3. Gate 0 (about day 90) releases Y1 ($8.55m) per case once its trio is staffed and Finance has signed its baseline.
4. Gate 1 (month 12) releases Y2 ($2.31m) against verified benefit, adoption thresholds, spend within 10% of plan and 40% co-funding.
5. Gate 2 (month 24) releases Y3–Y5 run funding only if annual benefits cover run costs and branches co-fund 60%.
Everything after today is released against evidence the Board will see. Then open Q&A; use the appendix.`);
}

// ---------- Appendix ----------
{
  const s = pres.addSlide(); s.background = { color: WHITE };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 4.6, h: 6.8, fill: { color: GREY }, line: { color: GREY } });
  text(s, 'A', { x: 0.6, y: 2.2, w: 3.6, h: 2.2, fontSize: 120, bold: true, color: WHITE, valign: 'middle' });
  frame(s, { appendix: true });
  text(s, 'Appendix', { x: 5.3, y: 1.6, w: 7.3, h: 1.0, fontSize: 40, bold: true, color: GREY, valign: 'middle' });
  arrows(s, ['Stop rules by risk', 'Portfolio returns by scenario', 'Investment envelope by category', 'Focus cases: how value is computed', 'Focus cases: cumulative cash', 'P12 e-SAF licensing option (H3)', 'If the budget is halved', 'Complementary cases'], 5.3, 2.8, 7, 3.4, 15);
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
  const s = appx('Portfolio returns by scenario', 'NPV at 10%, IRR and cumulative cash, $m',
    'Spread from 5.7% to 48.2% IRR: value depends on adoption, which is why release is gated. Downside: slower adoption, 80–90% of benefits, 105–110% of costs, P12 stopped. Upside: 115% of benefits, faster ramp.');
  table(s, [['Scenario', 'Prob.', 'NPV 10%', 'IRR', 'Cash Y5'],
    ['Downside', '30%', '−1.30', '5.7%', '+2.27'], ['Base', '50%', '+7.11', '32.6%', '+13.78'], ['Upside', '20%', '+12.28', '48.2%', '+20.83'],
    ['Expected', '', '+5.62', '27.8%', '+11.74']], 0.5, 1.75, 6.2, [1.7, 0.9, 1.2, 1.1, 1.3], 13);
  text(s, 'Downside: slower adoption, 80–90% of benefits, 105–110% of costs, P12 stopped. Upside: 115% of benefits, faster ramp. Hurdle 10% = 7% WACC + 3 points.',
    { x: 0.5, y: 3.95, w: 6.2, h: 0.8, fontSize: 11, color: GREY });
  img(s, A('selected_scenario_irr.png'), 6.95, 1.7, { w: 5.9, h: 4.5 });
}
{
  const s = appx('Investment envelope by category', '$m; capex only in Y0–Y1', 'Use when challenged on the cost split or the capex/opex boundary.');
  table(s, [['$m', 'Y0', 'Y1', 'Y2', 'Y3', 'Y0–Y3'],
    ['Compute and equipment', '0.87', '1.71', '0.46', '0.48', '3.52'], ['Talent and change', '0.72', '2.14', '0.58', '0.63', '4.07'],
    ['Integration', '0.58', '2.14', '0.35', '0.32', '3.38'], ['Model operations', '0.14', '0.68', '0.39', '0.58', '1.80'],
    ['Data engineering', '0.43', '1.45', '0.37', '0.42', '2.68'], ['Governance and legal', '0.14', '0.43', '0.16', '0.21', '0.95'],
    ['Total', '2.90', '8.55', '2.31', '2.64', '16.40'], ['of which capital expenditure', '2.90', '2.80', '0.00', '0.00', '5.69']],
  1.5, 1.75, 10.3, [4.0, 1.2, 1.2, 1.2, 1.2, 1.5], 14);
  text(s, 'From Y4: run cost $2.74–2.79m a year, for $21.94m over Y0–Y5. Branches co-fund 40% of Y2 and 60% of Y3–Y5 run costs.',
    { x: 1.5, y: 5.75, w: 10.3, h: 0.4, fontSize: 12, color: GREY });
}
{
  const s = appx('Focus cases: how each value is computed', 'Money in → value → go / no-go; all inputs are explicit assumptions',
    'Each line is auditable: change one input and the benefit moves proportionally. The break-even column shows how much room we have.');
  table(s, [['Case', 'Money in (one-time; run a year)', 'Value a year at full scale', 'Break-even', 'Go / no-go'],
    ['P13 retail', '€1.0m; €0.06–0.12m', 'Waste €0.245m + markdowns €0.250m + stock-outs €0.140m = €0.635m', '€0.446m', 'Month 12: matched-store trial; labels beat forecast-only'],
    ['P01 refining', '$1.4m; $0.20–0.40m', '250 kb/d × 365 × 0.45% × 70% sold × $6/bbl + $0.15m repairs = $1.87m', '$1.08m', 'Month 12: alert → action → sold barrel verified'],
    ['P03 drilling', '$1.4m; $0.30–0.50m', '2 rigs × 6 days × $0.40m × 60% realisation = $2.88m', '$1.66m', 'Gate 0: contract allows capture; month 12: invoice-verified']],
  0.5, 1.75, 12.33, [1.5, 2.2, 4.33, 1.3, 3.0], 12.5);
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
