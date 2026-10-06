"""Build the keep/kill review page for a writing round.

Usage: python3 tools/build_review.py writing/round-02-lane-packs.md writing/review/round-02.html
The packs (YAML blocks after <!-- pack: ID -->) are embedded as page content. Marks are stored in
the artifact's db capability (collection `marks`, doc id `<pack>-<part>`), so Claude can read
them back with ArtifactData.
"""
import json, re, sys, pathlib, yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_packs import words, caption_body  # noqa: E402


def load(path):
    text = pathlib.Path(path).read_text()
    packs = [yaml.safe_load(b) for b in re.findall(r'<!-- pack: \w+ -->\n```yaml\n(.*?)```', text, re.S)]
    for p in packs:
        p['li_words'] = len(words(caption_body(p['linkedin'])))
        p['ig_words'] = len(words(caption_body(p['instagram'])))
        p['linkedin'] = p['linkedin'].rstrip()
        p['instagram'] = p['instagram'].rstrip()
    return packs


TEMPLATE = r'''<title>Round 2 Copy Review</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<style>
/* Layout: sticky progress bar, then one section per lane pack; carousels as a horizontal strip of 4:5 slide cards, singles as one 4:5 card beside its captions. */
:root{
  --bg:#F5F9FD; --surface:#FFFFFF; --sunk:#E8F0F8; --ink:#050816; --muted:#42658A; --line:#C9DCEC;
  --accent:#2457D6; --accent-2:#007A9E; --hl-a:#2457D6; --hl-b:#007A9E;
  --keep:#00727F; --keep-bg:#E3F3F3; --kill:#B4233C; --kill-bg:#FBE9EC; --note-bg:#E9F7F6;
  --sans:"Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  color-scheme:light;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#050816; --surface:#0B1530; --sunk:#0A1030; --ink:#FFFFFF; --muted:#A6CAEC; --line:#1C2B4E;
  --accent:#A6CAEC; --accent-2:#09CACC; --hl-a:#A6CAEC; --hl-b:#09CACC;
  --keep:#34CCA4; --keep-bg:#0A2A2C; --kill:#FF8A9A; --kill-bg:#2A0E18; --note-bg:#08262F; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#050816; --surface:#0B1530; --sunk:#0A1030; --ink:#FFFFFF; --muted:#A6CAEC; --line:#1C2B4E;
  --accent:#A6CAEC; --accent-2:#09CACC; --hl-a:#A6CAEC; --hl-b:#09CACC;
  --keep:#34CCA4; --keep-bg:#0A2A2C; --kill:#FF8A9A; --kill-bg:#2A0E18; --note-bg:#08262F; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.55;margin:0}
.wrap{max-width:1120px;margin:0 auto;padding-inline:16px;padding-block:0 64px}
h1,h2,h3{text-wrap:balance;margin:0}
.hl{background:linear-gradient(90deg,var(--hl-a),var(--hl-b));-webkit-background-clip:text;background-clip:text;color:transparent}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.bar-in{max-width:1120px;margin:0 auto;padding:10px 16px;display:flex;flex-wrap:wrap;gap:8px 20px;align-items:center}
.bar b{font-variant-numeric:tabular-nums}
.meter{flex:1 1 160px;height:6px;border-radius:3px;background:var(--sunk);overflow:hidden;min-width:120px}
.meter i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--hl-a),var(--hl-b));transition:width .3s}
.bar label{display:flex;gap:6px;align-items:center;font-size:13px;color:var(--muted);cursor:pointer}
.save{font-size:12px;color:var(--muted)}
header.intro{padding-block:36px 8px;display:grid;gap:14px;max-width:70ch}
.eyebrow{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600}
header.intro h1{font-size:clamp(28px,4.4vw,44px);font-weight:800;letter-spacing:-.02em;line-height:1.08}
header.intro p{margin:0;color:var(--muted)}
.notice{border:1px solid var(--line);border-left:3px solid var(--accent-2);background:var(--surface);padding:12px 14px;border-radius:8px;font-size:14px}
.nav{display:flex;flex-wrap:wrap;gap:6px;padding-block:18px 6px}
.nav a{font-size:13px;text-decoration:none;color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:4px 10px;background:var(--surface);font-variant-numeric:tabular-nums}
.nav a:focus-visible,button:focus-visible,textarea:focus-visible,input:focus-visible{outline:2px solid var(--accent-2);outline-offset:2px}
section.pack{border-top:1px solid var(--line);padding-block:28px 8px;display:grid;gap:16px;scroll-margin-top:64px}
.pack-head{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:baseline}
.pack-head h2{font-size:22px;font-weight:700;letter-spacing:-.01em}
.meta{font-size:13px;color:var(--muted)}
.tally{margin-left:auto;font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:2px 9px;color:var(--muted)}
.chip.warn{border-color:var(--kill);color:var(--kill)}
.strip{display:flex;gap:14px;overflow-x:auto;padding-bottom:8px;scroll-snap-type:x mandatory}
.strip>.part{flex:0 0 min(300px,82vw);scroll-snap-align:start}
.single{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:16px;align-items:start}
@media (max-width:760px){.single{grid-template-columns:minmax(0,1fr)}}
.captions{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
@media (max-width:760px){.captions{grid-template-columns:minmax(0,1fr)}}
.part{display:grid;gap:8px;min-width:0}
.part[data-v="keep"] .frame{box-shadow:0 0 0 2px var(--keep)}
.part[data-v="kill"] .frame{box-shadow:0 0 0 2px var(--kill)}
.frame{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px;min-width:0}
.post{aspect-ratio:4/5;display:flex;flex-direction:column;gap:10px;overflow:auto}
.post .top{display:flex;justify-content:space-between;font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}
.post .pill{align-self:flex-start;font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;color:#fff;background:linear-gradient(90deg,#2457D6,#007A9E)}
.post .role{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.post h3{font-size:21px;line-height:1.15;font-weight:800;letter-spacing:-.01em}
.post h3.quote{font-size:17px;font-weight:700;line-height:1.3}
.post h3.big{font-size:64px;line-height:1}
.post p{margin:0;font-size:13.5px;color:var(--ink)}
.post .bridge{color:var(--accent-2);font-weight:600;font-size:13px}
.post .src{margin-top:auto;font-size:11px;color:var(--muted)}
.post ol{margin:0;padding-left:20px;font-size:13px;display:grid;gap:4px}
.post .foot{margin-top:auto;display:flex;justify-content:space-between;font-size:11px;color:var(--muted)}
.cap h4{margin:0 0 6px;font-size:13px;font-weight:600;display:flex;justify-content:space-between;gap:8px}
.cap h4 span{color:var(--muted);font-weight:500;font-variant-numeric:tabular-nums}
.cap pre{margin:0;white-space:pre-wrap;word-wrap:break-word;font-family:var(--sans);font-size:13.5px;line-height:1.55}
.alts{margin:0;padding-left:20px;font-size:13px;display:grid;gap:4px}
.ctrl{display:flex;gap:6px;align-items:center}
.ctrl button{font:600 13px var(--sans);border:1px solid var(--line);background:var(--surface);color:var(--ink);border-radius:8px;padding:6px 14px;cursor:pointer;min-height:36px}
.ctrl button[aria-pressed="true"].k{background:var(--keep-bg);border-color:var(--keep);color:var(--keep)}
.ctrl button[aria-pressed="true"].x{background:var(--kill-bg);border-color:var(--kill);color:var(--kill)}
.ctrl .lbl{font-size:12px;color:var(--muted);margin-right:auto;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
textarea{width:100%;min-height:38px;resize:vertical;font:13px/1.45 var(--sans);color:var(--ink);background:var(--note-bg);border:1px solid var(--line);border-radius:8px;padding:8px 10px}
.part.done-hidden{display:none}
.general{padding-block:28px 0;border-top:1px solid var(--line);display:grid;gap:10px;max-width:70ch}
.general textarea{min-height:110px}
@media (prefers-reduced-motion:reduce){.meter i{transition:none}}
</style>

<div class="bar" role="region" aria-label="Review progress">
  <div class="bar-in">
    <span><b id="marked">0</b> of <b id="total">0</b> marked</span>
    <div class="meter" aria-hidden="true"><i id="meter"></i></div>
    <span>Keep rate <b id="rate">–</b></span>
    <label for="onlyOpen"><input type="checkbox" id="onlyOpen"> Show unmarked only</label>
    <span class="save" id="saveState" aria-live="polite">Connecting…</span>
  </div>
</div>

<div class="wrap">
  <header class="intro">
    <span class="eyebrow">Verdant Soft · Writing practice · Round 2 · 2026-10-06</span>
    <h1>Nine lanes, one week of posts. <span class="hl">Keep or kill</span> each part.</h1>
    <p>Mark every slide, on-image text, caption and the hashtags with alt text. Add a note when you kill something, or when something is close. Your marks save automatically and I read them in the next session.</p>
    <p>The goal is two rounds in a row at 80% keep or better, with no truth or voice failures. Then these rules move into the style guide.</p>
    <div class="notice"><b>Practice only:</b> Pack 1 uses three news items that are still pending a source check (this environment could only open anthropic.com). They show the roundup format and can't be published until their sources are read. The cards show the words only; visuals come at the visuals stage.</div>
  </header>
  <nav class="nav" id="nav" aria-label="Packs"></nav>
  <main id="packs"></main>
  <section class="general">
    <h2 style="font-size:20px">Overall notes</h2>
    <p class="meta">Anything that applies to every lane: tone, length, what you'd never post.</p>
    <textarea id="note-general" aria-label="Overall notes" placeholder="e.g. LinkedIn captions feel long; I like the Our take lines"></textarea>
  </section>
</div>

<script>
const PACKS = __PACKS__;
const NAMES = {trends:"Trends & news", ai:"AI & LLMs", startup:"Startup & product", numbers:"Facts & numbers", concepts:"Software concepts", "how-we-work":"How we work", "build-notes":"Build Notes", proof:"Proof", "grow-with-us":"Grow with us"};
const parts = [];          // {key, pack}
let marks = {};            // key -> {verdict, note}
let db = null, local = false;

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const hl = s => esc(s).replace(/\[([^\]]+)\]/g, '<span class="hl">$1</span>');

function control(key, label) {
  parts.push({key, pack: key.split("-")[0]});
  return `<div class="ctrl"><span class="lbl">${esc(label)}</span>
    <button type="button" class="k" data-key="${key}" data-v="keep" aria-pressed="false">Keep</button>
    <button type="button" class="x" data-key="${key}" data-v="kill" aria-pressed="false">Kill</button></div>
    <textarea id="note-${key}" data-note="${key}" rows="1" aria-label="Note for ${esc(label)}" placeholder="Note (optional)"></textarea>`;
}

function slideCard(p, s, n) {
  const key = `${p.id}-s${s.n}`;
  const big = /^\[?\d+%?\]?$/.test(s.headline || "");
  const list = s.list ? `<ol>${s.list.map(i => `<li>${esc(i)}</li>`).join("")}</ol>` : "";
  return `<div class="part" data-key="${key}"><div class="frame post">
      <div class="top"><span>Verdant Soft</span><span>${String(s.n).padStart(2,"0")} / ${String(n).padStart(2,"0")}</span></div>
      ${s.pill ? `<span class="pill">${esc(s.pill)}</span>` : `<span class="role">${esc(s.role.replace("-", " "))}</span>`}
      <h3 class="${big ? "big" : ""}">${hl(s.headline)}</h3>
      ${s.body ? `<p>${esc(s.body)}</p>` : ""}${list}
      ${s.bridge ? `<p class="bridge">${esc(s.bridge)}</p>` : ""}
      ${s.extra ? `<p class="meta">${esc(s.extra)}</p>` : ""}
      ${s.source_line ? `<p class="src">${esc(s.source_line)}</p>` : ""}
    </div>${control(key, `Slide ${s.n} · ${s.role.replace("-", " ")}`)}</div>`;
}

function singleCard(p) {
  const o = p.on_image, key = `${p.id}-img`;
  const cls = p.headline_formula === "quote" ? "quote" : (/^\[?\d+%?\]?$/.test(o.headline) ? "big" : "");
  return `<div class="part" data-key="${key}"><div class="frame post">
      <div class="top"><span>Verdant Soft</span><span>4:5</span></div>
      <span class="pill">${esc(o.pill)}</span>
      <h3 class="${cls}">${hl(o.headline)}</h3>
      ${o.subline ? `<p>${esc(o.subline)}</p>` : ""}
      ${o.source_line ? `<p class="src">${esc(o.source_line)}</p>` : `<div class="foot"><span>verdant-soft.com</span></div>`}
    </div>${control(key, "On-image text")}</div>`;
}

function captions(p) {
  const cap = (k, title, text, n, range) => `<div class="part" data-key="${p.id}-${k}"><div class="frame cap">
      <h4>${title}<span>${n} words · ${range}</span></h4><pre>${esc(text)}</pre></div>${control(`${p.id}-${k}`, title)}</div>`;
  const alts = `<div class="part" data-key="${p.id}-alt"><div class="frame cap"><h4>Alt text<span>${p.alt_text.length} line${p.alt_text.length > 1 ? "s" : ""}</span></h4>
      <ol class="alts">${p.alt_text.map(a => `<li>${esc(a)}</li>`).join("")}</ol></div>${control(`${p.id}-alt`, "Hashtags & alt text")}</div>`;
  return `<div class="captions">${cap("li", "LinkedIn caption", p.linkedin, p.li_words, "120–220")}${cap("ig", "Instagram caption", p.instagram, p.ig_words, "40–100")}</div>${alts}`;
}

function render() {
  const nav = [], out = [];
  for (const p of PACKS) {
    const pending = /PENDING/.test(JSON.stringify(p));
    const chips = [`${p.format}${p.variant ? " · " + p.variant : ""}`, `headline: ${p.headline_formula}`, p.cta === "direct" ? "direct CTA" : "soft CTA", p.question ? "ends with a question" : null, p.term ? `term: ${p.term}` : null].filter(Boolean);
    nav.push(`<a href="#${p.id}">${p.id} · ${esc(p.day)} · ${esc(p.series)}</a>`);
    out.push(`<section class="pack" id="${p.id}">
      <div class="pack-head"><h2>${p.id} · ${esc(p.series)}</h2><span class="meta">${esc(p.day)} · ${esc(NAMES[p.lane] || p.lane)}</span><span class="tally" data-tally="${p.id}"></span></div>
      <div class="chips">${chips.map(c => `<span class="chip">${esc(c)}</span>`).join("")}${pending ? '<span class="chip warn">practice only: sources pending</span>' : ""}</div>
      ${p.format === "carousel"
        ? `<div class="strip" role="group" aria-label="${p.id} slides">${p.slides.map(s => slideCard(p, s, p.slides.length)).join("")}</div>${captions(p)}`
        : `<div class="single">${singleCard(p)}<div class="part-stack" style="display:grid;gap:14px;min-width:0">${captions(p)}</div></div>`}
    </section>`);
  }
  document.getElementById("nav").innerHTML = nav.join("");
  document.getElementById("packs").innerHTML = out.join("");
  document.getElementById("total").textContent = parts.length;
}

function paint() {
  const only = document.getElementById("onlyOpen").checked;
  let marked = 0, keep = 0;
  const per = {};
  for (const {key, pack} of parts) {
    const m = marks[key] || {};
    const el = document.querySelector(`.part[data-key="${key}"]`);
    el.dataset.v = m.verdict || "";
    el.querySelectorAll("button[data-v]").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.v === m.verdict)));
    const ta = document.getElementById("note-" + key);
    if (document.activeElement !== ta) ta.value = m.note || "";
    el.classList.toggle("done-hidden", only && !!m.verdict);
    per[pack] = per[pack] || {n: 0, keep: 0, marked: 0};
    per[pack].n++;
    if (m.verdict) { marked++; per[pack].marked++; }
    if (m.verdict === "keep") { keep++; per[pack].keep++; }
  }
  for (const [id, t] of Object.entries(per)) document.querySelector(`[data-tally="${id}"]`).textContent = `${t.keep} kept · ${t.marked}/${t.n} marked`;
  document.getElementById("marked").textContent = marked;
  document.getElementById("rate").textContent = marked ? Math.round(100 * keep / marked) + "%" : "–";
  document.getElementById("meter").style.width = (100 * marked / parts.length) + "%";
  const g = document.getElementById("note-general");
  if (document.activeElement !== g) g.value = (marks.general || {}).note || "";
}

function setState(t) { document.getElementById("saveState").textContent = t; }

async function save(key, patch) {
  const pack = key === "general" ? "general" : key.split("-")[0];
  const next = {...(marks[key] || {}), ...patch, pack, part: key, at: new Date().toISOString()};
  marks[key] = next;
  paint();
  if (db) {
    setState("Saving…");
    try { await db.doc("marks/" + key).set(next); setState("Saved"); }
    catch (e) {
      if (e && e.code === "unavailable") { setTimeout(() => save(key, {}), 800 + Math.random() * 800); setState("Retrying…"); }
      else setState("Couldn't save: " + (e && e.code || "error"));
    }
  } else if (local) {
    try { localStorage.setItem("round02-marks", JSON.stringify(marks)); } catch (_) {}
  }
}

document.addEventListener("click", e => {
  const b = e.target.closest("button[data-v]");
  if (!b) return;
  const key = b.dataset.key, cur = (marks[key] || {}).verdict;
  save(key, {verdict: cur === b.dataset.v ? null : b.dataset.v});
});
const timers = {};
document.addEventListener("input", e => {
  const t = e.target;
  const key = t.dataset.note || (t.id === "note-general" ? "general" : null);
  if (!key) return;
  clearTimeout(timers[key]);
  timers[key] = setTimeout(() => save(key, {note: t.value}), 700);
});
document.getElementById("onlyOpen").addEventListener("change", paint);

render();
paint();

(async () => {
  try { db = window.claude ? await window.claude.use("db") : null; } catch (_) { db = null; }
  if (!db) {
    local = true;
    try { marks = JSON.parse(localStorage.getItem("round02-marks") || "{}") || {}; } catch (_) { marks = {}; }
    paint();
    setState("Saving is off here: marks stay in this browser. Reply in chat with your notes.");
    return;
  }
  setState("Saved marks load live");
  db.collection("marks").onSnapshot(snap => {
    const next = {};
    snap.docs.forEach(d => { if (d.exists) next[d.id] = d.data(); });
    marks = next;
    paint();
    setState(snap.metadata.hasPendingWrites ? "Saving…" : "All marks saved");
  }, err => setState("Live sync stopped (" + err.code + "). Reload the page."));
})();
</script>
'''


def main(src, dst):
    packs = load(src)
    html = TEMPLATE.replace('__PACKS__', json.dumps(packs, ensure_ascii=False).replace('</', '<\\/'))
    pathlib.Path(dst).write_text(html)
    print(f'wrote {dst}: {len(packs)} packs, {len(html)//1024} KB')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
