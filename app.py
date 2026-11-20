import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Exponent Mastery Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove default Streamlit padding/chrome so the interactive app fills the screen cleanly
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.75rem;
            padding-bottom: 0.5rem;
            padding-left: 1rem;
            padding-right: 1rem;
            max-width: 100%;
        }
        header[data-testid="stHeader"] {
            height: 2rem;
            background: transparent;
        }
        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_APP = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Exponent Mastery Studio</title>
<style>
  :root {
    --bg: #0f172a;
    --panel: #1e293b;
    --panel-2: #273549;
    --border: #334155;
    --text: #f8fafc;
    --muted: #94a3b8;
    --accent: #38bdf8;
    --accent-2: #818cf8;
    --success: #22c55e;
    --warning: #f59e0b;
    --danger: #ef4444;
  }
  * { box-sizing: border-box; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    line-height: 1.5;
  }
  .container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 20px;
  }
  header {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    padding-bottom: 18px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 22px;
  }
  .title-group h1 {
    margin: 0;
    font-size: 1.65rem;
    background: linear-gradient(90deg, var(--accent), var(--accent-2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .title-group p {
    margin: 4px 0 0;
    color: var(--muted);
    font-size: 0.92rem;
  }
  .stats-bar {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }
  .stat-pill {
    background: var(--panel);
    border: 1px solid var(--border);
    padding: 8px 14px;
    border-radius: 12px;
    text-align: center;
    min-width: 88px;
  }
  .stat-pill .val {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--accent);
  }
  .stat-pill .lbl {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--muted);
  }
  .tabs {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
  }
  .tab-btn {
    background: var(--panel);
    color: var(--muted);
    border: 1px solid var(--border);
    padding: 10px 18px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.15s ease;
  }
  .tab-btn.active {
    background: linear-gradient(135deg, rgba(56,189,248,0.18), rgba(129,140,248,0.18));
    color: var(--text);
    border-color: var(--accent);
  }
  .grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 20px;
  }
  @media (max-width: 850px) {
    .grid { grid-template-columns: 1fr; }
  }
  .card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 22px;
  }
  .controls {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 18px;
  }
  select, input[type="text"] {
    background: var(--bg);
    color: var(--text);
    border: 1px solid var(--border);
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 0.95rem;
  }
  select:focus, input[type="text"]:focus {
    outline: none;
    border-color: var(--accent);
  }
  .problem-box {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 28px 20px;
    text-align: center;
    margin-bottom: 18px;
  }
  .rule-badge {
    display: inline-block;
    background: rgba(129, 140, 248, 0.15);
    color: #a5b4fc;
    border: 1px solid rgba(129, 140, 248, 0.35);
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-bottom: 12px;
  }
  .math-display {
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: 0.02em;
    margin: 8px 0;
  }
  .math-display sup {
    font-size: 1.15rem;
    color: var(--accent);
  }
  .frac {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    vertical-align: middle;
    margin: 0 6px;
  }
  .frac .num {
    border-bottom: 2px solid var(--text);
    padding: 0 8px 3px;
  }
  .frac .den {
    padding: 3px 8px 0;
  }
  .answer-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .answer-row input {
    flex: 1;
    min-width: 200px;
    font-size: 1.1rem;
    font-family: 'JetBrains Mono', monospace;
  }
  .preview-box {
    margin-top: 10px;
    padding: 8px 12px;
    border-radius: 8px;
    background: rgba(15, 23, 42, 0.6);
    font-size: 0.92rem;
    color: var(--muted);
    min-height: 36px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .btn {
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
    font-size: 0.95rem;
    cursor: pointer;
    transition: transform 0.08s ease, opacity 0.15s ease;
  }
  .btn:active { transform: scale(0.98); }
  .btn-primary {
    background: linear-gradient(135deg, var(--accent), var(--accent-2));
    color: #0f172a;
  }
  .btn-secondary {
    background: var(--panel-2);
    color: var(--text);
    border: 1px solid var(--border);
  }
  .feedback {
    margin-top: 16px;
    padding: 14px 16px;
    border-radius: 12px;
    display: none;
  }
  .feedback.show { display: block; }
  .feedback.ok {
    background: rgba(34, 197, 94, 0.14);
    border: 1px solid rgba(34, 197, 94, 0.4);
    color: #86efac;
  }
  .feedback.warn {
    background: rgba(245, 158, 11, 0.14);
    border: 1px solid rgba(245, 158, 11, 0.4);
    color: #fcd34d;
  }
  .feedback.err {
    background: rgba(239, 68, 68, 0.14);
    border: 1px solid rgba(239, 68, 68, 0.4);
    color: #fca5a5;
  }
  .solution-box {
    margin-top: 12px;
    padding: 12px 14px;
    background: var(--bg);
    border-radius: 10px;
    color: var(--text);
    font-size: 0.92rem;
  }
  .mastery-item {
    margin-bottom: 12px;
  }
  .mastery-top {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    margin-bottom: 4px;
  }
  .bar-bg {
    height: 8px;
    background: var(--bg);
    border-radius: 999px;
    overflow: hidden;
  }
  .bar-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--accent), var(--success));
    width: 0%;
    transition: width 0.3s ease;
  }
  .cheat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
    gap: 16px;
  }
  .rule-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
  }
  .rule-card h3 {
    margin: 0 0 6px;
    color: var(--accent);
    font-size: 1.05rem;
  }
  .formula {
    background: var(--bg);
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 10px 0;
    text-align: center;
  }
  .explorer-box {
    margin-top: 20px;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 20px;
  }
  .slider-row {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    align-items: center;
    margin: 12px 0;
  }
</style>
</head>
<body>
<div class="container">
  <header>
    <div class="title-group">
      <h1>⚡ Exponent Mastery Studio</h1>
      <p>Interactive algebra practice with instant feedback, step-by-step hints &amp; rule explorer</p>
    </div>
    <div class="stats-bar">
      <div class="stat-pill"><div class="val" id="stat-score">0</div><div class="lbl">Solved</div></div>
      <div class="stat-pill"><div class="val" id="stat-streak">0🔥</div><div class="lbl">Streak</div></div>
      <div class="stat-pill"><div class="val" id="stat-acc">—</div><div class="lbl">Accuracy</div></div>
    </div>
  </header>

  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('practice', this)">🎯 Practice Arena</button>
    <button class="tab-btn" onclick="switchTab('cheatsheet', this)">📘 Rule Cheat Sheet &amp; Visualizer</button>
  </div>

  <!-- PRACTICE TAB -->
  <div id="tab-practice" class="grid">
    <div class="card">
      <div class="controls">
        <select id="rule-select" onchange="newProblem()">
          <option value="mixed">All Rules (Mixed)</option>
          <option value="product">Product Rule (xᵃ · xᵇ)</option>
          <option value="quotient">Quotient Rule (xᵃ / xᵇ)</option>
          <option value="power">Power of a Power ((xᵃ)ᵇ)</option>
          <option value="prod_power">Power of Product/Quotient</option>
          <option value="zero">Zero Exponent (x⁰)</option>
          <option value="negative">Negative Exponents (x⁻ᵃ)</option>
        </select>
        <select id="diff-select" onchange="newProblem()">
          <option value="easy">Easy (Single Variable)</option>
          <option value="medium" selected>Medium (Coefficients &amp; Multi-Var)</option>
          <option value="hard">Hard (Multi-Step Combos)</option>
        </select>
        <button class="btn btn-secondary" onclick="newProblem()">↻ Skip / New</button>
      </div>

      <div class="problem-box">
        <div class="rule-badge" id="prob-category">Product Rule</div>
        <div style="color: var(--muted); font-size: 0.9rem;">Simplify completely using only <strong>positive exponents</strong>:</div>
        <div class="math-display" id="prob-math">x<sup>3</sup> · x<sup>4</sup></div>
      </div>

      <div class="answer-row">
        <input type="text" id="ans-input" placeholder="Type answer, e.g. 8x^6 or 1/x^3" oninput="updatePreview()" onkeydown="if(event.key==='Enter') checkAnswer()" />
        <button class="btn btn-primary" onclick="checkAnswer()">Check Answer</button>
        <button class="btn btn-secondary" onclick="showHint()">💡 Hint</button>
      </div>

      <div class="preview-box">
        <span>Preview:</span>
        <strong id="math-preview" style="color: var(--text); font-size: 1.1rem;">—</strong>
      </div>

      <div id="hint-box" class="solution-box" style="display:none; border-left: 3px solid var(--warning);"></div>
      <div id="feedback-box" class="feedback"></div>
    </div>

    <div class="card">
      <h3 style="margin-top:0;">📊 Rule Mastery</h3>
      <p style="color:var(--muted); font-size:0.85rem; margin-top:-6px;">Solve 5 problems per rule to reach 100% mastery.</p>
      <div id="mastery-list"></div>
      <hr style="border-color: var(--border); margin: 18px 0;">
      <div style="font-size: 0.85rem; color: var(--muted);">
        <strong>Typing Tips:</strong>
        <ul style="padding-left: 18px; margin: 6px 0;">
          <li>Use <code>^</code> for exponents: <code>x^5</code></li>
          <li>Use <code>/</code> for fractions: <code>3x^2/y^4</code></li>
          <li>Always rewrite negative exponents as positive fractions!</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- CHEAT SHEET TAB -->
  <div id="tab-cheatsheet" style="display:none;">
    <div class="cheat-grid">
      <div class="rule-card">
        <h3>1. Product Rule</h3>
        <div class="formula">x<sup>a</sup> · x<sup>b</sup> = x<sup>a + b</sup></div>
        <p style="color:var(--muted); font-size:0.9rem;">When multiplying matching bases, <strong>add</strong> the exponents. Multiply coefficients normally.</p>
      </div>
      <div class="rule-card">
        <h3>2. Quotient Rule</h3>
        <div class="formula">x<sup>a</sup> / x<sup>b</sup> = x<sup>a − b</sup></div>
        <p style="color:var(--muted); font-size:0.9rem;">When dividing matching bases, <strong>subtract</strong> the denominator exponent from the numerator exponent.</p>
      </div>
      <div class="rule-card">
        <h3>3. Power of a Power</h3>
        <div class="formula">(x<sup>a</sup>)<sup>b</sup> = x<sup>a · b</sup></div>
        <p style="color:var(--muted); font-size:0.9rem;">When raising a power to another power, <strong>multiply</strong> the exponents.</p>
      </div>
      <div class="rule-card">
        <h3>4. Power of a Product / Quotient</h3>
        <div class="formula">(xy)<sup>a</sup> = x<sup>a</sup>y<sup>a</sup> &nbsp;|&nbsp; (x/y)<sup>a</sup> = x<sup>a</sup>/y<sup>a</sup></div>
        <p style="color:var(--muted); font-size:0.9rem;">Distribute the outside exponent to <strong>every</strong> factor inside (including numbers!).</p>
      </div>
      <div class="rule-card">
        <h3>5. Zero Exponent Rule</h3>
        <div class="formula">x<sup>0</sup> = 1 &nbsp; (x ≠ 0)</div>
        <p style="color:var(--muted); font-size:0.9rem;">Any non-zero base raised to the 0 power equals <strong>1</strong>. Watch out for coefficients outside parentheses like <code>5x⁰ = 5</code>.</p>
      </div>
      <div class="rule-card">
        <h3>6. Negative Exponent Rule</h3>
        <div class="formula">x<sup>−a</sup> = 1 / x<sup>a</sup></div>
        <p style="color:var(--muted); font-size:0.9rem;">A negative exponent flips the base across the fraction bar and turns positive.</p>
      </div>
    </div>

    <div class="explorer-box">
      <h3 style="margin-top:0;">🔬 Interactive Expansion Visualizer</h3>
      <p style="color:var(--muted); font-size:0.9rem;">Slide the exponents to see <em>why</em> the Product and Power rules work by expanding into repeated multiplication:</p>
      <div class="slider-row">
        <label>a = <strong id="lbl-a">2</strong> <input type="range" id="sl-a" min="1" max="5" value="2" oninput="updateExplorer()"></label>
        <label>b = <strong id="lbl-b">3</strong> <input type="range" id="sl-b" min="1" max="5" value="3" oninput="updateExplorer()"></label>
      </div>
      <div id="explorer-output" class="solution-box" style="font-size:1rem; line-height:1.8;"></div>
    </div>
  </div>
</div>

<script>
const RULES = [
  { id: 'product', name: 'Product Rule' },
  { id: 'quotient', name: 'Quotient Rule' },
  { id: 'power', name: 'Power of a Power' },
  { id: 'prod_power', name: 'Power of Product/Quotient' },
  { id: 'zero', name: 'Zero Exponent' },
  { id: 'negative', name: 'Negative Exponents' }
];

let state = {
  solved: 0,
  attempts: 0,
  streak: 0,
  mastery: { product: 0, quotient: 0, power: 0, prod_power: 0, zero: 0, negative: 0 },
  current: null,
  hintStep: 0,
  alreadyScored: false
};

function rand(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
function pick(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}
function gcd(a, b) {
  a = Math.abs(a); b = Math.abs(b);
  while (b) { [a, b] = [b, a % b]; }
  return a || 1;
}

// Canonical monomial representation: { num: number, den: number, vars: { x: exp, y: exp } }
function formatMonomialHTML(m) {
  let numParts = [];
  let denParts = [];

  if (m.num !== 1 || Object.values(m.vars).every(e => e <= 0)) {
    numParts.push(String(m.num));
  }
  if (m.den !== 1) {
    denParts.push(String(m.den));
  }

  for (const v of ['x', 'y']) {
    const e = m.vars[v] || 0;
    if (e > 0) {
      numParts.push(e === 1 ? v : `${v}<sup>${e}</sup>`);
    } else if (e < 0) {
      const ae = Math.abs(e);
      denParts.push(ae === 1 ? v : `${v}<sup>${ae}</sup>`);
    }
  }

  const numStr = numParts.length ? numParts.join('') : '1';
  if (denParts.length === 0) return numStr;
  return `<span class="frac"><span class="num">${numStr}</span><span class="den">${denParts.join('')}</span></span>`;
}

function formatMonomialPlain(m) {
  let numParts = [];
  let denParts = [];
  if (m.num !== 1 || Object.values(m.vars).every(e => e <= 0)) numParts.push(String(m.num));
  if (m.den !== 1) denParts.push(String(m.den));
  for (const v of ['x', 'y']) {
    const e = m.vars[v] || 0;
    if (e > 0) numParts.push(e === 1 ? v : `${v}^${e}`);
    else if (e < 0) denParts.push(Math.abs(e) === 1 ? v : `${v}^${Math.abs(e)}`);
  }
  const numStr = numParts.length ? numParts.join('') : '1';
  return denParts.length ? `${numStr}/${denParts.join('')}` : numStr;
}

function generateProblem(ruleId, diff) {
  if (ruleId === 'mixed') ruleId = pick(RULES).id;

  if (ruleId === 'product') {
    const a = rand(2, 6), b = rand(2, 6);
    if (diff === 'easy') {
      return {
        ruleId, category: 'Product Rule',
        html: `x<sup>${a}</sup> · x<sup>${b}</sup>`,
        ans: { num: 1, den: 1, vars: { x: a + b } },
        hints: [`Keep the base x and add the exponents: ${a} + ${b}.`, `x^(${a} + ${b}) = x^${a + b}`],
        explanation: `Using the Product Rule (xᵃ · xᵇ = xᵃ⁺ᵇ), add the exponents: ${a} + ${b} = ${a + b}, giving <strong>x<sup>${a + b}</sup></strong>.`
      };
    } else if (diff === 'medium') {
      const c1 = rand(2, 5), c2 = rand(2, 5);
      return {
        ruleId, category: 'Product Rule',
        html: `(${c1}x<sup>${a}</sup>)(${c2}x<sup>${b}</sup>)`,
        ans: { num: c1 * c2, den: 1, vars: { x: a + b } },
        hints: [`Multiply the coefficients (${c1} · ${c2}) and add the exponents (${a} + ${b}).`, `${c1 * c2}x^${a + b}`],
        explanation: `Multiply coefficients: ${c1} × ${c2} = ${c1 * c2}. Add exponents on x: ${a} + ${b} = ${a + b}. Result: <strong>${c1 * c2}x<sup>${a + b}</sup></strong>.`
      };
    } else {
      const c1 = rand(2, 4), c2 = rand(2, 5), ay = rand(2, 4), by = rand(2, 5);
      return {
        ruleId, category: 'Product Rule (Multi-Variable)',
        html: `(${c1}x<sup>${a}</sup>y<sup>${ay}</sup>)(${c2}x<sup>${b}</sup>y<sup>${by}</sup>)`,
        ans: { num: c1 * c2, den: 1, vars: { x: a + b, y: ay + by } },
        hints: [`Multiply ${c1} · ${c2}, then combine x terms and y terms separately.`, `${c1 * c2}x^${a + b}y^${ay + by}`],
        explanation: `Coefficients: ${c1}·${c2} = ${c1 * c2}. For x: ${a}+${b} = ${a + b}. For y: ${ay}+${by} = ${ay + by}. Result: <strong>${c1 * c2}x<sup>${a + b}</sup>y<sup>${ay + by}</sup></strong>.`
      };
    }
  }

  if (ruleId === 'quotient') {
    if (diff === 'easy') {
      const b = rand(2, 5), a = b + rand(2, 6);
      return {
        ruleId, category: 'Quotient Rule',
        html: `<span class="frac"><span class="num">x<sup>${a}</sup></span><span class="den">x<sup>${b}</sup></span></span>`,
        ans: { num: 1, den: 1, vars: { x: a - b } },
        hints: [`Subtract the bottom exponent from the top exponent: ${a} − ${b}.`, `x^${a - b}`],
        explanation: `Subtract exponents: ${a} − ${b} = ${a - b}, giving <strong>x<sup>${a - b}</sup></strong>.`
      };
    } else if (diff === 'medium') {
      const k = rand(2, 5), c1 = k * rand(2, 4), c2 = k;
      const b = rand(2, 4), a = b + rand(2, 5);
      return {
        ruleId, category: 'Quotient Rule',
        html: `<span class="frac"><span class="num">${c1}x<sup>${a}</sup></span><span class="den">${c2}x<sup>${b}</sup></span></span>`,
        ans: { num: c1 / c2, den: 1, vars: { x: a - b } },
        hints: [`Divide ${c1} by ${c2}, and subtract the exponents ${a} − ${b}.`, `${c1 / c2}x^${a - b}`],
        explanation: `Divide coefficients: ${c1}/${c2} = ${c1 / c2}. Subtract exponents: ${a} − ${b} = ${a - b}. Result: <strong>${c1 / c2}x<sup>${a - b}</sup></strong>.`
      };
    } else {
      const ax = rand(4, 8), bx = rand(1, 3), ay = rand(2, 4), by = ay + rand(2, 4);
      const ans = { num: 3, den: 1, vars: { x: ax - bx, y: ay - by } };
      return {
        ruleId, category: 'Quotient Rule (Multi-Variable)',
        html: `<span class="frac"><span class="num">12x<sup>${ax}</sup>y<sup>${ay}</sup></span><span class="den">4x<sup>${bx}</sup>y<sup>${by}</sup></span></span>`,
        ans,
        hints: [`12/4 = 3. Subtract exponents: x^(${ax}−${bx}) and y^(${ay}−${by}).`, `Move any negative exponent to the denominator.`],
        explanation: `12/4 = 3, x<sup>${ax - bx}</sup>, and y<sup>${ay - by}</sup>. Moving y<sup>${ay - by}</sup> to the denominator gives <strong>${formatMonomialHTML(ans)}</strong>.`
      };
    }
  }

  if (ruleId === 'power') {
    const a = rand(2, 5), b = rand(2, 4);
    if (diff === 'easy') {
      return {
        ruleId, category: 'Power of a Power',
        html: `(x<sup>${a}</sup>)<sup>${b}</sup>`,
        ans: { num: 1, den: 1, vars: { x: a * b } },
        hints: [`Multiply the exponents together: ${a} · ${b}.`, `x^${a * b}`],
        explanation: `Multiply the exponents: ${a} × ${b} = ${a * b}, giving <strong>x<sup>${a * b}</sup></strong>.`
      };
    } else {
      const c = rand(2, 4);
      return {
        ruleId, category: 'Power of a Power',
        html: `(x<sup>${a}</sup>)<sup>${b}</sup> · x<sup>${c}</sup>`,
        ans: { num: 1, den: 1, vars: { x: a * b + c } },
        hints: [`First simplify (x^${a})^${b} by multiplying exponents, then add ${c}.`, `x^${a * b} · x^${c} = x^${a * b + c}`],
        explanation: `First, (x<sup>${a}</sup>)<sup>${b}</sup> = x<sup>${a * b}</sup>. Then multiply by x<sup>${c}</sup> by adding exponents: ${a * b} + ${c} = ${a * b + c}, giving <strong>x<sup>${a * b + c}</sup></strong>.`
      };
    }
  }

  if (ruleId === 'prod_power') {
    const c = rand(2, 4), p = rand(2, 3), ax = rand(2, 4);
    if (diff === 'easy') {
      return {
        ruleId, category: 'Power of a Product',
        html: `(${c}x)<sup>${p}</sup>`,
        ans: { num: Math.pow(c, p), den: 1, vars: { x: p } },
        hints: [`Raise BOTH ${c} and x to the power of ${p}.`, `${c}^${p} = ${Math.pow(c, p)}, so ${Math.pow(c, p)}x^${p}`],
        explanation: `Distribute the exponent ${p} to both factors: ${c}<sup>${p}</sup> · x<sup>${p}</sup> = <strong>${Math.pow(c, p)}x<sup>${p}</sup></strong>.`
      };
    } else if (diff === 'medium') {
      const ay = rand(2, 3);
      return {
        ruleId, category: 'Power of a Product',
        html: `(${c}x<sup>${ax}</sup>y<sup>${ay}</sup>)<sup>${p}</sup>`,
        ans: { num: Math.pow(c, p), den: 1, vars: { x: ax * p, y: ay * p } },
        hints: [`Compute ${c}^${p}, and multiply each variable's exponent by ${p}.`, `${Math.pow(c, p)}x^${ax * p}y^${ay * p}`],
        explanation: `${c}<sup>${p}</sup> = ${Math.pow(c, p)}, x<sup>${ax}·${p}</sup> = x<sup>${ax * p}</sup>, y<sup>${ay}·${p}</sup> = y<sup>${ay * p}</sup>. Result: <strong>${Math.pow(c, p)}x<sup>${ax * p}</sup>y<sup>${ay * p}</sup></strong>.`
      };
    } else {
      const d = pick([2, 3]), ay = rand(2, 3);
      return {
        ruleId, category: 'Power of a Quotient',
        html: `<span class="frac"><span class="num">${c}x<sup>${ax}</sup></span><span class="den">${d}y<sup>${ay}</sup></span></span><sup style="font-size:1.3rem;">${p}</sup>`,
        ans: { num: Math.pow(c, p), den: Math.pow(d, p), vars: { x: ax * p, y: -ay * p } },
        hints: [`Apply the exponent ${p} to every part of the numerator and denominator.`, `${Math.pow(c, p)}x^${ax * p} / (${Math.pow(d, p)}y^${ay * p})`],
        explanation: `Raise numerator and denominator to power ${p}: ${c}<sup>${p}</sup>x<sup>${ax * p}</sup> / ${d}<sup>${p}</sup>y<sup>${ay * p}</sup> = <strong>${Math.pow(c, p)}x<sup>${ax * p}</sup>/${Math.pow(d, p)}y<sup>${ay * p}</sup></strong>.`
      };
    }
  }

  if (ruleId === 'zero') {
    const c = rand(2, 9), a = rand(2, 6);
    if (diff === 'easy') {
      return {
        ruleId, category: 'Zero Exponent Rule',
        html: `(${c}x<sup>${a}</sup>)<sup>0</sup>`,
        ans: { num: 1, den: 1, vars: {} },
        hints: [`The entire expression inside parentheses is raised to the 0 power.`, `Any non-zero base to the 0 power is 1.`],
        explanation: `Because the 0 exponent is outside the parentheses, everything inside becomes <strong>1</strong>.`
      };
    } else {
      const b = rand(2, 5);
      return {
        ruleId, category: 'Zero Exponent Rule',
        html: `${c}x<sup>0</sup>y<sup>${b}</sup>`,
        ans: { num: c, den: 1, vars: { y: b } },
        hints: [`Only x is raised to the 0 power (x⁰ = 1).`, `${c} · 1 · y^${b}`],
        explanation: `x<sup>0</sup> = 1, while ${c} and y<sup>${b}</sup> keep their powers. Result: <strong>${c}y<sup>${b}</sup></strong>.`
      };
    }
  }

  // negative exponents
  const a = rand(2, 6);
  if (diff === 'easy') {
    return {
      ruleId: 'negative', category: 'Negative Exponent Rule',
      html: `x<sup>−${a}</sup>`,
      ans: { num: 1, den: 1, vars: { x: -a } },
      hints: [`Flip x^−${a} to the denominator to make the exponent positive.`, `1/x^${a}`],
      explanation: `Using x<sup>−a</sup> = 1/x<sup>a</sup>, rewrite x<sup>−${a}</sup> as <strong>1/x<sup>${a}</sup></strong>.`
    };
  } else if (diff === 'medium') {
    const c = rand(2, 7);
    return {
      ruleId: 'negative', category: 'Negative Exponent Rule',
      html: `${c}x<sup>−${a}</sup>`,
      ans: { num: c, den: 1, vars: { x: -a } },
      hints: [`Notice ${c} has a positive exponent of 1; only x has a negative exponent.`, `Keep ${c} in the numerator and move x^${a} to the denominator.`],
      explanation: `Only x<sup>−${a}</sup> has a negative exponent, so ${c} stays on top: <strong>${c}/x<sup>${a}</sup></strong>.`
    };
  } else {
    const b = rand(2, 5), c = rand(2, 6);
    return {
      ruleId: 'negative', category: 'Negative Exponent Rule (Hard)',
      html: `<span class="frac"><span class="num">${c}x<sup>−${a}</sup></span><span class="den">y<sup>−${b}</sup></span></span>`,
      ans: { num: c, den: 1, vars: { x: -a, y: b } },
      hints: [`Move x^−${a} down to the denominator, and move y^−${b} up to the numerator.`, `${c}y^${b}/x^${a}`],
      explanation: `Flip negative exponents across the fraction bar: x<sup>−${a}</sup> moves down and y<sup>−${b}</sup> moves up, giving <strong>${c}y<sup>${b}</sup>/x<sup>${a}</sup></strong>.`
    };
  }
}

// Parse user answer into canonical monomial + detect if negative exponents remain
function parseUserMonomial(raw) {
  let s = raw.replace(/\s+/g, '').replace(/\*\*/g, '^').replace(/\*/g, '');
  if (!s) return null;

  let hasNegativeExp = /-\d+/.test(s);
  let parts = s.split('/');
  if (parts.length > 2) return null;

  function parseSide(side) {
    side = side.replace(/[()]/g, '');
    if (!side || side === '1') return { coeff: 1, vars: {} };
    let coeff = 1;
    let vars = {};
    const numMatch = side.match(/^[+-]?\d+/);
    if (numMatch) {
      coeff = parseInt(numMatch[0], 10);
      side = side.slice(numMatch[0].length);
    }
    const tokenRegex = /([xy])(?:\^([+-]?\d+))?/g;
    let m;
    let consumed = 0;
    while ((m = tokenRegex.exec(side)) !== null) {
      consumed += m[0].length;
      const v = m[1];
      const exp = m[2] !== undefined ? parseInt(m[2], 10) : 1;
      vars[v] = (vars[v] || 0) + exp;
    }
    if (consumed !== side.length) return null;
    return { coeff, vars };
  }

  const top = parseSide(parts[0]);
  const bot = parts[1] !== undefined ? parseSide(parts[1]) : { coeff: 1, vars: {} };
  if (!top || !bot || bot.coeff === 0) return null;

  const g = gcd(top.coeff, bot.coeff);
  let num = top.coeff / g;
  let den = bot.coeff / g;
  let vars = {};
  for (const v of ['x', 'y']) {
    const e = (top.vars[v] || 0) - (bot.vars[v] || 0);
    if (e !== 0) vars[v] = e;
  }
  return { num, den, vars, hasNegativeExp };
}

function monomialsEqual(a, b) {
  if (a.num !== b.num || a.den !== b.den) return false;
  for (const v of ['x', 'y']) {
    if ((a.vars[v] || 0) !== (b.vars[v] || 0)) return false;
  }
  return true;
}

function updatePreview() {
  const val = document.getElementById('ans-input').value;
  const prev = document.getElementById('math-preview');
  if (!val.trim()) {
    prev.innerHTML = '—';
    return;
  }
  const parsed = parseUserMonomial(val);
  if (!parsed) {
    prev.innerHTML = `<span style="color:var(--warning); font-size:0.9rem;">Keep typing (example format: <code>4x^3/y^2</code>)</span>`;
    return;
  }
  prev.innerHTML = formatMonomialHTML(parsed);
}

function newProblem() {
  const ruleId = document.getElementById('rule-select').value;
  const diff = document.getElementById('diff-select').value;
  state.current = generateProblem(ruleId, diff);
  state.hintStep = 0;
  state.alreadyScored = false;

  document.getElementById('prob-category').textContent = state.current.category;
  document.getElementById('prob-math').innerHTML = state.current.html;
  document.getElementById('ans-input').value = '';
  document.getElementById('math-preview').innerHTML = '—';
  document.getElementById('hint-box').style.display = 'none';
  const fb = document.getElementById('feedback-box');
  fb.className = 'feedback';
  fb.innerHTML = '';
  document.getElementById('ans-input').focus();
}

function showHint() {
  if (!state.current) return;
  const hb = document.getElementById('hint-box');
  const idx = Math.min(state.hintStep, state.current.hints.length - 1);
  hb.style.display = 'block';
  hb.innerHTML = `<strong>💡 Hint ${idx + 1}:</strong> ${state.current.hints[idx]}`;
  state.hintStep++;
}

function checkAnswer() {
  const raw = document.getElementById('ans-input').value.trim();
  const fb = document.getElementById('feedback-box');
  if (!raw) return;

  const parsed = parseUserMonomial(raw);
  if (!parsed) {
    fb.className = 'feedback warn show';
    fb.innerHTML = `⚠️ Could not read that expression. Try a format like <code>3x^4</code> or <code>1/x^2</code>.`;
    return;
  }

  if (monomialsEqual(parsed, state.current.ans)) {
    if (parsed.hasNegativeExp) {
      fb.className = 'feedback warn show';
      fb.innerHTML = `✨ Algebraically equivalent, <strong>but</strong> rewrite your answer using only <strong>positive exponents</strong> (e.g. flip negative exponents across the fraction bar).`;
      return;
    }

    if (!state.alreadyScored) {
      state.solved++;
      state.attempts++;
      state.streak++;
      state.mastery[state.current.ruleId] = Math.min(5, (state.mastery[state.current.ruleId] || 0) + 1);
      state.alreadyScored = true;
      updateStats();
    }

    fb.className = 'feedback ok show';
    fb.innerHTML = `
      <div><strong>✅ Correct! Great job.</strong></div>
      <div class="solution-box">${state.current.explanation}</div>
      <div style="margin-top:12px;"><button class="btn btn-primary" onclick="newProblem()">Next Problem →</button></div>
    `;
  } else {
    if (!state.alreadyScored) {
      state.attempts++;
      state.streak = 0;
      updateStats();
    }
    fb.className = 'feedback err show';
    fb.innerHTML = `
      <div><strong>❌ Not quite.</strong> Check the exponent rule and try again, or review the breakdown below:</div>
      <div class="solution-box">${state.current.explanation}</div>
    `;
  }
}

function updateStats() {
  document.getElementById('stat-score').textContent = state.solved;
  document.getElementById('stat-streak').textContent = `${state.streak}🔥`;
  const acc = state.attempts ? Math.round((state.solved / state.attempts) * 100) + '%' : '—';
  document.getElementById('stat-acc').textContent = acc;

  const list = document.getElementById('mastery-list');
  list.innerHTML = RULES.map(r => {
    const pct = Math.round(((state.mastery[r.id] || 0) / 5) * 100);
    return `
      <div class="mastery-item">
        <div class="mastery-top"><span>${r.name}</span><span>${pct}%</span></div>
        <div class="bar-bg"><div class="bar-fill" style="width:${pct}%"></div></div>
      </div>
    `;
  }).join('');
}

function switchTab(tab, btn) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('tab-practice').style.display = tab === 'practice' ? 'grid' : 'none';
  document.getElementById('tab-cheatsheet').style.display = tab === 'cheatsheet' ? 'block' : 'none';
}

function updateExplorer() {
  const a = parseInt(document.getElementById('sl-a').value, 10);
  const b = parseInt(document.getElementById('sl-b').value, 10);
  document.getElementById('lbl-a').textContent = a;
  document.getElementById('lbl-b').textContent = b;

  const expA = Array(a).fill('x').join(' · ');
  const expB = Array(b).fill('x').join(' · ');
  const prodTotal = Array(a + b).fill('x').join(' · ');
  const powerGroups = Array(b).fill(`(${expA})`).join(' · ');

  document.getElementById('explorer-output').innerHTML = `
    <div><strong>Product Rule:</strong> x<sup>${a}</sup> · x<sup>${b}</sup> = (${expA}) · (${expB}) = ${prodTotal} = <strong style="color:var(--accent)">x<sup>${a + b}</sup></strong></div>
    <div style="margin-top:8px;"><strong>Power of a Power:</strong> (x<sup>${a}</sup>)<sup>${b}</sup> = ${powerGroups} = <strong style="color:var(--success)">x<sup>${a * b}</sup></strong> (${b} groups of ${a})</div>
  `;
}

updateStats();
updateExplorer();
newProblem();
</script>
</body>
</html>
"""

components.html(HTML_APP, height=860, scrolling=True)
