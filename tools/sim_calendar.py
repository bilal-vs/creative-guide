"""Simulate 8 weeks of STYLE_GUIDE.md CONTENT-MIX-v2 and assert the user's main rule (70% Verdant, 30% external; external = carousels only; Verdant = 60% singles, 40% carousels), the Thursday lane rotation and the CTA cap. Run from the repo root."""
import re,yaml,datetime as dt
s=open('STYLE_GUIDE.md').read()
m=re.search(r'<!-- id: CONTENT-MIX-v2 -->\n```yaml\n(.*?)```', s, re.S)
cfg=yaml.safe_load(m.group(1))
cal=cfg['calendar']; anchor=dt.date.fromisoformat(cal['anchor_monday'])
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
direct=set(cfg['ctas']['direct']['allowed_on'])
mix=cfg['mix']
tot=0; count={('verdant','single'):0,('verdant','carousel'):0,('external','single'):0,('external','carousel'):0}
thu_seen=[]
for n in range(8):
    wtype='A' if n%2==0 else 'B'
    wk={k:0 for k in count}; wk_direct=0; wk_pillars=[]
    row=[]
    for i,d in enumerate(days):
        spec=cal['days'][d]
        side=spec['side']; fmt=spec['format']
        if d=='Thu': slot=cal['thu_lanes'][n%4]; thu_seen.append(slot)
        else: slot=spec.get('lane') or spec.get('pillar') or spec[wtype]
        if side=='external': assert fmt=='carousel',(d,fmt)          # hard rule 1
        if fmt=='single': assert side=='verdant',(d,side)
        if side=='verdant': assert slot in cfg['verdant_pillars'],(d,slot); wk_pillars.append((slot,fmt))
        else: assert slot in cfg['lanes'],(d,slot)
        if slot in direct: wk_direct+=1
        wk[(side,fmt)]+=1; count[(side,fmt)]+=1; tot+=1
        row.append(f"{d}:{slot}{'*' if fmt=='carousel' else ''}")
    v,e=mix['verdant'],mix['external']
    assert wk[('verdant','single')]==v['singles'] and wk[('verdant','carousel')]==v['carousels'],wk
    assert wk[('external','carousel')]==e['carousels'] and wk[('external','single')]==0,wk
    assert wk_direct<=cfg['ctas']['direct']['max_per_week'],wk_direct
    # one How we work carousel and one Build Notes carousel every week
    assert sorted(p for p,f in wk_pillars if f=='carousel')==['build-notes','how-we-work'],wk_pillars
    print(f"wk{n} {wtype} | "+'  '.join(row))
ver=count[('verdant','single')]+count[('verdant','carousel')]
print('verdant',ver,'/',tot,'=',round(ver/tot,3),'| verdant singles',count[('verdant','single')],'/',ver,'=',round(count[('verdant','single')]/ver,3))
assert abs(ver/tot-mix['verdant']['share'])<0.02
assert abs(count[('verdant','single')]/ver-0.60)<0.001
assert set(thu_seen)==set(cal['thu_lanes'])
print('ALL OK')
