"""Simulate 6 weeks of STYLE_GUIDE.md CONTENT-MIX-v1 and assert the mix, carousel cycle and CTA caps. Run from the repo root."""
import re,yaml,datetime as dt
s=open('STYLE_GUIDE.md').read()
m=re.search(r'<!-- id: CONTENT-MIX-v1 -->\n```yaml\n(.*?)```', s, re.S)
cfg=yaml.safe_load(m.group(1))
cal=cfg['calendar']; anchor=dt.date.fromisoformat(cal['anchor_monday'])
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
verdant=set(cfg['verdant_pillars'])
direct=set(cfg['ctas']['direct']['allowed_on'])
tot=ver=car=0; pill_dates={}
for n in range(6):
    wtype='A' if n%2==0 else 'B'; cyc=n%3+1
    wk_car=0; wk_direct=0
    row=[]
    for i,d in enumerate(days):
        date=anchor+dt.timedelta(days=7*n+i)
        spec=cal['days'][d]
        slot=spec.get('lane') or spec[wtype]
        is_car = d in cal['carousel_days'][cyc]
        fmt_rule=spec['format']
        # consistency check between per-day format text and carousel_days
        if fmt_rule=='carousel': assert is_car
        elif fmt_rule=='single': assert not is_car,(d,cyc)
        else:
            assert (f'cycle week {cyc}' in fmt_rule)==is_car,(d,cyc,fmt_rule)
        tot+=1; car+=is_car; wk_car+=is_car
        if slot in verdant: ver+=1; pill_dates.setdefault(slot,[]).append(date)
        if slot in direct: wk_direct+=1
        row.append(f"{d}:{slot}{'*' if is_car else ''}")
    assert wk_direct<=cfg['ctas']['direct']['max_per_week']
    assert wk_car==[2,2,3][n%3]
    print(f"wk{n} {wtype} c{cyc} | "+'  '.join(row))
print('verdant share',ver,'/',tot,'=',round(ver/tot,3)); print('carousels',car,'/',tot)
assert ver*7==tot*2 and car*3==tot
for p,ds in pill_dates.items():
    gaps={(b-a).days for a,b in zip(ds,ds[1:])}; print(p,'gaps',gaps); assert gaps=={14}
print('ALL OK')
