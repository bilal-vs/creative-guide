"""Build the Taste Lab page (writing/taste/taste-lab.html) from writing/taste/rounds.json.

Usage: python3 tools/build_taste_lab.py
Each round names a post file whose "## Prompt X · Name" sections hold the prompts (one ```text
block each). The page stores uploads with the artifact `assets` capability and ratings in `db`:
collection `images` (doc id = asset id: round, variant, assetId, rating 1-10, tags, note,
createdAt) and doc `rounds/<id>` (favorite, note). Claude reads them back with ArtifactData
and fetches the images with Artifact read (path = asset id).
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ROUNDS = json.loads((ROOT / 'writing/taste/rounds.json').read_text())
for r in ROUNDS:
    text = (ROOT / r['post_file']).read_text()
    for v in r['variants']:
        m = re.search(r'## Prompt %s · .*?```text\n(.*?)```' % re.escape(v['key']), text, re.S)
        v['prompt'] = m.group(1).strip()

TAGS = {
    'good': ['Love the colours', 'Premium', 'Modern', 'Clear to read', 'Stops my scroll', 'On brand'],
    'bad': ['Too dull', 'Too busy', 'Too blue', 'Text hard to read', 'Looks AI', 'Old-fashioned', 'Text wrong', 'Logo wrong'],
}

HTML = r'''<title>Verdant Taste Lab</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: an engineering-report page. Sticky score bar, then one section per visual direction (letter, prompt, uploads, rating cards), then the favourite pick. */
:root{
  --page:#F5F9FD; --surface:#FFFFFF; --sunk:#E8F0F8; --ink:#050816; --muted:#42658A; --line:#C9DCEC;
  --lagoon:#00727F; --ocean:#007A9E; --royal:#2457D6; --on-accent:#FFFFFF;
  --good:#00727F; --good-bg:#E3F3F3; --bad:#B4233C; --bad-bg:#FBE9EC;
  --sans:"Inter",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  color-scheme:light;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --page:#050816; --surface:#0B1530; --sunk:#0A1030; --ink:#FFFFFF; --muted:#A6CAEC; --line:#1C2B4E;
  --lagoon:#34CCA4; --ocean:#09CACC; --royal:#A6CAEC; --on-accent:#050816;
  --good:#34CCA4; --good-bg:#0A2A2C; --bad:#FF8A9A; --bad-bg:#2A0E18; color-scheme:dark}}
:root[data-theme="dark"]{
  --page:#050816; --surface:#0B1530; --sunk:#0A1030; --ink:#FFFFFF; --muted:#A6CAEC; --line:#1C2B4E;
  --lagoon:#34CCA4; --ocean:#09CACC; --royal:#A6CAEC; --on-accent:#050816;
  --good:#34CCA4; --good-bg:#0A2A2C; --bad:#FF8A9A; --bad-bg:#2A0E18; color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--page);color:var(--ink);font:15px/1.55 var(--sans)}
.wrap{max-width:1180px;margin:0 auto;padding-inline:16px;padding-block:0 72px}
h1,h2,h3{margin:0;text-wrap:balance}
button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--ocean);outline-offset:2px}
.mono{font-family:var(--mono);font-size:12.5px;letter-spacing:.01em}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:color-mix(in srgb,var(--page) 90%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.bar-in{max-width:1180px;margin:0 auto;padding:10px 16px;display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center}
.bar b{font-variant-numeric:tabular-nums}
.minis{display:flex;gap:10px;flex-wrap:wrap}
.mini{display:flex;align-items:center;gap:6px;font-family:var(--mono);font-size:12px;color:var(--muted)}
.mini i{display:block;width:44px;height:6px;border-radius:3px;background:var(--sunk);overflow:hidden;position:relative}
.mini i::after{content:"";position:absolute;inset:0;width:var(--w,0%);background:linear-gradient(90deg,var(--royal),var(--ocean))}
.save{margin-left:auto;font-size:12px;color:var(--muted)}
.intro{display:grid;gap:14px;padding-block:36px 10px;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);align-items:start}
@media (max-width:820px){.intro{grid-template-columns:minmax(0,1fr)}}
.intro h1{font-size:clamp(30px,4.6vw,46px);font-weight:800;letter-spacing:-.025em;line-height:1.05}
.intro p{margin:0;color:var(--muted);max-width:62ch}
.steps{margin:0;padding-left:20px;display:grid;gap:4px;max-width:62ch}
.settings{border:1px solid var(--line);background:var(--surface);border-radius:10px;padding:14px;display:grid;gap:10px}
.settings img{width:120px;border:1px solid var(--line);border-radius:6px;background:var(--sunk)}
.tabs{display:flex;gap:6px;flex-wrap:wrap;padding-block:8px}
.tabs button{border:1px solid var(--line);background:var(--surface);border-radius:999px;padding:5px 12px;cursor:pointer;font-size:13px}
.tabs button[aria-selected="true"]{border-color:var(--ocean);color:var(--ocean);font-weight:600}
section.variant{border-top:1px solid var(--line);padding-block:30px 10px;display:grid;gap:14px;scroll-margin-top:70px}
.v-head{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:16px;align-items:start}
@media (max-width:640px){.v-head{grid-template-columns:auto minmax(0,1fr)}.v-score{grid-column:1/-1}}
.letter{font-size:56px;font-weight:800;line-height:.9;letter-spacing:-.04em;background:linear-gradient(160deg,var(--royal),var(--ocean));-webkit-background-clip:text;background-clip:text;color:transparent}
.v-head h2{font-size:24px;font-weight:700;letter-spacing:-.01em}
.v-head p{margin:2px 0 0;max-width:70ch}
.v-head .tests{color:var(--muted);font-size:13.5px}
.v-score{text-align:right;font-family:var(--mono);font-size:13px;color:var(--muted);white-space:nowrap}
.v-score b{display:block;font-family:var(--sans);font-size:30px;color:var(--ink);font-weight:800;line-height:1;font-variant-numeric:tabular-nums}
.actions{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.btn{border:1px solid var(--line);background:var(--surface);border-radius:8px;padding:8px 14px;min-height:40px;cursor:pointer;font-weight:600;font-size:14px}
.btn.primary{background:var(--ocean);border-color:var(--ocean);color:var(--on-accent)}
.btn input{position:absolute;width:1px;height:1px;opacity:0;pointer-events:none}
label.btn{position:relative;display:inline-flex;align-items:center}
.status{font-size:13px;color:var(--muted)}
details{width:100%}
details summary{cursor:pointer;color:var(--muted);font-size:13px}
details pre{white-space:pre-wrap;word-wrap:break-word;font:12.5px/1.55 var(--mono);background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:12px;max-height:340px;overflow:auto;margin:8px 0 0}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px}
.empty{margin:0;padding:22px;border:1px dashed var(--line);border-radius:10px;color:var(--muted);text-align:center}
.drop{outline:2px dashed var(--ocean);outline-offset:6px;border-radius:12px}
figure.shot{margin:0;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px;display:grid;gap:10px;min-width:0}
.shot-img{aspect-ratio:3/4;background:var(--sunk);border-radius:8px;overflow:hidden;display:grid;place-items:center}
.shot-img img{width:100%;height:100%;object-fit:contain;display:block}
.rate{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}
.rate button{min-height:38px;border:1px solid var(--line);background:var(--page);border-radius:7px;cursor:pointer;font-weight:700;font-variant-numeric:tabular-nums}
.rate button[aria-pressed="true"]{background:linear-gradient(135deg,var(--royal),var(--ocean));border-color:transparent;color:var(--on-accent)}
.tags{display:flex;flex-wrap:wrap;gap:6px}
.tags button{border:1px solid var(--line);background:var(--page);border-radius:999px;padding:4px 10px;font-size:12.5px;cursor:pointer;min-height:30px}
.tags button.good[aria-pressed="true"]{background:var(--good-bg);border-color:var(--good);color:var(--good);font-weight:600}
.tags button.bad[aria-pressed="true"]{background:var(--bad-bg);border-color:var(--bad);color:var(--bad);font-weight:600}
textarea{width:100%;min-height:40px;resize:vertical;font:13px/1.45 var(--sans);color:var(--ink);background:var(--page);border:1px solid var(--line);border-radius:8px;padding:8px 10px}
.shot-foot{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
.shot-foot .mono{color:var(--muted)}
.link{background:none;border:0;padding:4px 0;color:var(--muted);text-decoration:underline;cursor:pointer;font-size:13px}
.confirm{display:inline-flex;gap:8px;align-items:center;font-size:13px}
.confirm .yes{color:var(--bad);font-weight:600}
.fav{border-top:1px solid var(--line);padding-block:30px 0;display:grid;gap:12px;max-width:760px}
.fav h2{font-size:24px;font-weight:700}
.fav-pick{display:flex;gap:10px;flex-wrap:wrap}
.fav-pick button{min-width:110px;min-height:56px;border:1px solid var(--line);background:var(--surface);border-radius:10px;cursor:pointer;text-align:left;padding:8px 12px;display:grid}
.fav-pick button b{font-size:22px;font-weight:800;line-height:1}
.fav-pick button span{font-size:12.5px;color:var(--muted)}
.fav-pick button[aria-pressed="true"]{border-color:var(--ocean);box-shadow:0 0 0 2px var(--ocean)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

<div class="bar" role="region" aria-label="Progress">
  <div class="bar-in">
    <span class="mono">Round <b id="roundId"></b></span>
    <span><b id="nImages">0</b> images · <b id="nRated">0</b> rated</span>
    <div class="minis" id="minis" aria-label="Average rating per direction"></div>
    <span class="save" id="saveState" aria-live="polite">Connecting…</span>
  </div>
</div>

<div class="wrap">
  <section class="intro">
    <div style="display:grid;gap:14px;min-width:0">
      <span class="eyebrow">Verdant Soft · visual training · light first, then dark</span>
      <h1>Which look feels like Verdant?</h1>
      <p>One post, four visual directions. The text is the same in every version, so only the look changes. Your scores teach Claude your taste before we train the rest of the feed.</p>
      <ol class="steps">
        <li>Copy a prompt and paste it into Google Flow exactly as written.</li>
        <li>Upload all of its outputs under the same letter.</li>
        <li>Rate every image from 1 to 10 and tap what you feel.</li>
        <li>Pick your favourite direction at the bottom.</li>
      </ol>
    </div>
    <aside class="settings" aria-label="Flow settings">
      <span class="eyebrow">Flow settings</span>
      <span class="mono">Images · Nano Banana 2 · 3:4 · 4 outputs</span>
      <span class="mono">One ingredient: this logo file</span>
      <img id="refImg" alt="Verdant Soft logo reference to attach in Flow">
      <button type="button" class="btn primary" id="saveLogo" hidden>Save logo file</button>
      <span class="status" id="logoHelp">Tap Save logo file, or download the logo file sent in the chat.</span>
    </aside>
  </section>
  <div class="tabs" id="tabs" role="tablist" aria-label="Rounds" hidden></div>
  <main id="variants"></main>
  <section class="fav" id="fav">
    <span class="eyebrow">Last step</span>
    <h2>Your favourite direction</h2>
    <div class="fav-pick" id="favPick" role="group" aria-label="Favourite direction"></div>
    <label for="favNote" class="status">What should we keep from the others? (optional)</label>
    <textarea id="favNote" placeholder="e.g. B's colours with A's clean layout"></textarea>
  </section>
</div>

<script>
const ROUNDS = __ROUNDS__;
const TAGS = __TAGS__;
let round = ROUNDS[ROUNDS.length - 1];   // newest round first
let db = null, assets = null, downloads = null;
let images = {};            // asset id -> doc data
let roundDocs = {};         // round id -> {favorite, note}
const queues = {};          // per-doc write chains
let editing = false, dirty = false;
const pendingNotes = {};    // asset id -> unsaved note text
const noteTimers = {};

const $ = s => document.querySelector(s);
const el = (tag, attrs = {}, kids = []) => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') n.className = v; else if (k === 'text') n.textContent = v;
    else if (k.startsWith('on')) n.addEventListener(k.slice(2), v); else if (v !== null && v !== undefined) n.setAttribute(k, v);
  }
  for (const c of [].concat(kids)) if (c) n.append(c);
  return n;
};
const state = t => { $('#saveState').textContent = t; };

function write(path, op, data) {
  if (!db) return Promise.resolve();
  const run = () => (op === 'delete' ? db.doc(path).delete() : op === 'update' ? db.doc(path).update(data) : db.doc(path).set(data));
  queues[path] = (queues[path] || Promise.resolve()).then(() => { state('Saving…'); return run(); })
    .then(() => state('All changes saved'))
    .catch(e => state(e && e.code === 'unavailable' ? 'Connection hiccup. Try that again.' : "Couldn't save (" + (e && e.code || 'error') + ')'));
  return queues[path];
}

function roundImages(v) {
  return Object.entries(images).filter(([, d]) => d.round === round.id && (!v || d.variant === v))
    .sort((a, b) => String(a[1].createdAt).localeCompare(String(b[1].createdAt)));
}
function avg(v) {
  const r = roundImages(v).map(([, d]) => d.rating).filter(x => typeof x === 'number');
  return r.length ? (r.reduce((a, b) => a + b, 0) / r.length) : null;
}

async function downscale(file) {
  const bmp = await createImageBitmap(file);
  const scale = Math.min(1, 1600 / Math.max(bmp.width, bmp.height));
  const c = document.createElement('canvas');
  c.width = Math.round(bmp.width * scale); c.height = Math.round(bmp.height * scale);
  c.getContext('2d').drawImage(bmp, 0, 0, c.width, c.height);
  return await new Promise(res => c.toBlob(b => res(b), 'image/jpeg', 0.9));
}
const UPLOAD_ERRORS = {
  too_large: 'That file is over 20 MB. Export a smaller size from Flow and try again.',
  unsupported_type: 'Only PNG, JPEG, WEBP or GIF images can be uploaded.',
  quota_or_state: "This page's storage is full. Remove a few images, then try again.",
  rate_limited: 'Too many uploads at once. Wait a moment, then try again.',
};
async function upload(variant, files, statusEl) {
  if (!assets || !db) { statusEl.textContent = 'Uploading needs edit access to this page.'; return; }
  const list = [...files].filter(f => /^image\//.test(f.type) || /\.(png|jpe?g|webp|gif)$/i.test(f.name));
  for (let i = 0; i < list.length; i++) {
    statusEl.textContent = `Uploading ${i + 1} of ${list.length}…`;
    let blob = list[i];
    try { blob = await downscale(list[i]) || list[i]; } catch (_) { blob = list[i]; }
    try {
      const r = await assets.upload(blob, { type: blob.type || 'image/jpeg' });
      images[r.id] = { round: round.id, variant, assetId: r.id, rating: null, tags: [], note: '', name: list[i].name, createdAt: new Date().toISOString() };
      render();
      await write('images/' + r.id, 'set', images[r.id]);
    } catch (e) {
      statusEl.textContent = UPLOAD_ERRORS[e && e.code] || `Upload failed (${e && e.code || 'error'}). Try again.`;
      return;
    }
  }
  statusEl.textContent = list.length ? `Uploaded ${list.length}. Now rate them.` : 'No images in that selection.';
}

function shotCard(id, d, n) {
  const fig = el('figure', { class: 'shot', 'data-id': id });
  fig.append(el('div', { class: 'shot-img' }, el('img', { src: '/_blob/' + d.assetId, alt: `Direction ${d.variant}, output ${n}`, loading: 'lazy' })));
  const rate = el('div', { class: 'rate', role: 'group', 'aria-label': 'Rating from 1 to 10' });
  for (let i = 1; i <= 10; i++) rate.append(el('button', { type: 'button', id: `r-${id}-${i}`, 'aria-pressed': String(d.rating === i), 'aria-label': `Rate ${i} out of 10`, text: String(i),
    onclick: () => { const cur = images[id]; cur.rating = cur.rating === i ? null : i; render(); write('images/' + id, 'update', { rating: cur.rating }); } }));
  fig.append(rate);
  const tags = el('div', { class: 'tags', role: 'group', 'aria-label': 'What you feel' });
  for (const [kind, list] of Object.entries(TAGS)) for (const t of list)
    tags.append(el('button', { type: 'button', id: `t-${id}-${kind}-${list.indexOf(t)}`, class: kind, 'aria-pressed': String((d.tags || []).includes(t)), text: t,
      onclick: () => { const cur = images[id]; const s = new Set(cur.tags || []); s.has(t) ? s.delete(t) : s.add(t); cur.tags = [...s]; render(); write('images/' + id, 'update', { tags: cur.tags }); } }));
  fig.append(tags);
  const ta = el('textarea', { id: 'note-' + id, 'aria-label': `Note for direction ${d.variant} output ${n}`, placeholder: 'Note (optional)' });
  ta.value = pendingNotes[id] ?? (d.note || '');
  const flush = () => { if (!(id in pendingNotes)) return; clearTimeout(noteTimers[id]); const v = pendingNotes[id]; delete pendingNotes[id]; if (images[id]) images[id].note = v; write('images/' + id, 'update', { note: v }); };
  ta.addEventListener('input', () => { pendingNotes[id] = ta.value; if (images[id]) images[id].note = ta.value; clearTimeout(noteTimers[id]); noteTimers[id] = setTimeout(flush, 700); });
  ta.addEventListener('blur', flush);
  fig.append(ta);
  const confirm = el('span', { class: 'confirm', hidden: '' }, [
    el('span', { text: 'Remove this image?' }),
    el('button', { type: 'button', class: 'link yes', text: 'Yes, remove', onclick: async () => {
      try { if (assets) await assets.delete(d.assetId); } catch (_) {}
      delete images[id]; render(); write('images/' + id, 'delete'); } }),
    el('button', { type: 'button', class: 'link', text: 'Keep', onclick: () => { confirm.hidden = true; rm.hidden = false; } }),
  ]);
  const rm = el('button', { type: 'button', class: 'link', text: 'Remove', onclick: () => { rm.hidden = true; confirm.hidden = false; } });
  fig.append(el('div', { class: 'shot-foot' }, [el('span', { class: 'mono', text: `${d.variant}${n}${d.rating ? ' · ' + d.rating + '/10' : ''}` }), rm, confirm]));
  return fig;
}

function variantSection(v) {
  const sec = el('section', { class: 'variant', id: 'v-' + v.key, 'aria-labelledby': 'h-' + v.key });
  const a = avg(v.key), rated = roundImages(v.key).filter(([, d]) => typeof d.rating === 'number').length;
  sec.append(el('div', { class: 'v-head' }, [
    el('span', { class: 'letter', 'aria-hidden': 'true', text: v.key }),
    el('div', {}, [el('h2', { id: 'h-' + v.key, text: `${v.key} · ${v.name}` }), el('p', { text: v.look }), el('p', { class: 'tests', text: 'What it tests: ' + v.tests })]),
    el('div', { class: 'v-score' }, [el('b', { text: a === null ? '–' : a.toFixed(1) }), el('span', { text: rated ? `average of ${rated} rated` : 'not rated yet' })]),
  ]));
  const status = el('span', { class: 'status', 'aria-live': 'polite' });
  const copyBtn = el('button', { type: 'button', class: 'btn', text: 'Copy prompt ' + v.key });
  const pre = el('pre', { text: v.prompt });
  const det = el('details', {}, [el('summary', { text: 'Show prompt ' + v.key }), pre]);
  copyBtn.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(v.prompt); copyBtn.textContent = 'Copied'; setTimeout(() => (copyBtn.textContent = 'Copy prompt ' + v.key), 2000); }
    catch (_) { det.open = true; const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); status.textContent = 'Copy blocked here: the prompt is selected, so copy it with your keyboard or menu.'; }
  });
  const input = el('input', { type: 'file', id: 'file-' + v.key, accept: 'image/png,image/jpeg,image/webp,image/gif', multiple: '' });
  input.addEventListener('change', () => { upload(v.key, input.files, status); input.value = ''; });
  const uploadBtn = el('label', { class: 'btn primary', for: 'file-' + v.key }, ['Upload images', input]);
  if (!assets) uploadBtn.hidden = true;
  sec.append(el('div', { class: 'actions' }, [copyBtn, uploadBtn, status]), det);
  const grid = el('div', { class: 'grid', 'data-variant': v.key });
  const rows = roundImages(v.key);
  rows.forEach(([id, d], i) => grid.append(shotCard(id, d, i + 1)));
  sec.append(rows.length ? grid : el('p', { class: 'empty', text: assets
    ? `No images yet. Run prompt ${v.key} in Flow, then upload all its outputs here, or drop them on this section.`
    : 'No images yet.' }));
  sec.addEventListener('dragover', e => { if (assets) { e.preventDefault(); sec.classList.add('drop'); } });
  sec.addEventListener('dragleave', () => sec.classList.remove('drop'));
  sec.addEventListener('drop', e => { e.preventDefault(); sec.classList.remove('drop'); if (e.dataTransfer && e.dataTransfer.files.length) upload(v.key, e.dataTransfer.files, status); });
  return sec;
}

function renderBar() {
  $('#roundId').textContent = `${round.id} · ${round.theme}`;
  const all = roundImages();
  $('#nImages').textContent = all.length;
  $('#nRated').textContent = all.filter(([, d]) => typeof d.rating === 'number').length;
  $('#minis').replaceChildren(...round.variants.map(v => { const a = avg(v.key); const i = el('i'); i.style.setProperty('--w', a === null ? '0%' : (a * 10) + '%');
    return el('span', { class: 'mini', title: `Direction ${v.key} average` }, [document.createTextNode(v.key), i, document.createTextNode(a === null ? '–' : a.toFixed(1))]); }));
}

function render() {
  renderBar();
  if (editing) { dirty = true; return; }
  dirty = false;
  const focused = document.activeElement && document.activeElement.id;
  const main = $('#variants'); main.replaceChildren(...round.variants.map(variantSection));
  const rd = roundDocs[round.id] || {};
  $('#favPick').replaceChildren(...round.variants.map(v => el('button', { type: 'button', 'aria-pressed': String(rd.favorite === v.key),
    onclick: () => { const cur = roundDocs[round.id] = { ...(roundDocs[round.id] || {}) }; cur.favorite = cur.favorite === v.key ? null : v.key; render();
      write('rounds/' + round.id, 'set', { favorite: cur.favorite, note: cur.note || '', updatedAt: new Date().toISOString() }); } },
    [el('b', { text: v.key }), el('span', { text: v.name })])));
  const fn = $('#favNote'); if (document.activeElement !== fn) fn.value = rd.note || '';
  $('#refImg').src = round.ref_file;
  const tabs = $('#tabs'); tabs.hidden = ROUNDS.length < 2;
  tabs.replaceChildren(...ROUNDS.map(r => el('button', { type: 'button', role: 'tab', 'aria-selected': String(r.id === round.id), text: r.title,
    onclick: () => { round = r; render(); } })));
  if (focused && document.getElementById(focused)) document.getElementById(focused).focus();
}

document.addEventListener('focusin', e => { if (e.target.tagName === 'TEXTAREA') editing = true; });
document.addEventListener('focusout', e => { if (e.target.tagName === 'TEXTAREA') { editing = false; setTimeout(() => { if (!editing && dirty) render(); }, 0); } });

$('#saveLogo').addEventListener('click', async () => {
  const help = $('#logoHelp');
  try {
    const blob = await (await fetch(round.ref_file)).blob();
    await downloads.save({ filename: round.ref_file.replace('ref-pack-v2', 'verdant-logo-reference'), data: blob });
    help.textContent = 'Saved. Attach this file in Flow as the one ingredient.';
  } catch (e) {
    const code = e && e.code;
    if (code === 'declined') help.textContent = 'Not saved. Tap Save logo file again when you are ready.';
    else if (code === 'rate_limited') help.textContent = 'A save prompt is already open. Finish it first.';
    else { help.textContent = 'Saving is not available here. Download the logo file sent in the chat instead.'; $('#saveLogo').hidden = true; }
  }
});

let favTimer;
$('#favNote').addEventListener('input', e => { clearTimeout(favTimer); favTimer = setTimeout(() => {
  const cur = roundDocs[round.id] = { ...(roundDocs[round.id] || {}) }; cur.note = e.target.value;
  write('rounds/' + round.id, 'set', { favorite: cur.favorite || null, note: cur.note, updatedAt: new Date().toISOString() }); }, 700); });

render();
(async () => {
  try { db = window.claude ? await window.claude.use('db') : null; } catch (_) { db = null; }
  try { assets = window.claude ? await window.claude.use('assets') : null; } catch (_) { assets = null; }
  try { downloads = window.claude ? await window.claude.use('downloads') : null; } catch (_) { downloads = null; }
  $('#saveLogo').hidden = !downloads;
  if (!db) { state('Saving is off in this view. Open the page in Claude to upload and rate.'); render(); return; }
  state(assets ? 'Ready' : 'View only: uploading needs edit access');
  render();
  db.collection('images').onSnapshot(snap => {
    const next = {};
    snap.docs.forEach(d => { if (d.exists) next[d.id] = { ...d.data() }; });
    for (const [id, v] of Object.entries(pendingNotes)) if (next[id]) next[id].note = v;
    images = next; render();
  }, err => state('Live sync stopped (' + err.code + '). Reload the page.'));
  db.collection('rounds').onSnapshot(snap => {
    const next = {};
    snap.docs.forEach(d => { if (d.exists) next[d.id] = { ...d.data() }; });
    roundDocs = next; render();
  }, () => {});
})();
</script>
'''


def main():
    out = ROOT / 'writing/taste/taste-lab.html'
    data = json.dumps(ROUNDS, ensure_ascii=False).replace('</', '<\\/')
    out.write_text(HTML.replace('__ROUNDS__', data).replace('__TAGS__', json.dumps(TAGS)))
    print(f'wrote {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB), rounds: {[r["id"] for r in ROUNDS]}')


if __name__ == '__main__':
    main()
