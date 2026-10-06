"""Parse every <!-- id: X --> YAML block in a markdown file. Usage: python3 tools/check_yaml.py STYLE_GUIDE.md"""
import re,yaml,sys
s=open(sys.argv[1]).read()
n=0
for m in re.finditer(r'<!-- id: ([A-Za-z0-9-]+) -->\n```yaml\n(.*?)```', s, re.S):
    n+=1
    try:
        yaml.safe_load(m.group(2)); print('ok', m.group(1))
    except Exception as e:
        print('FAIL', m.group(1), e)
print(n,'blocks')
