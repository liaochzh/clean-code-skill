import hashlib
import json
import re

cur = '/Users/lcr/.config/opencode/opencode.jsonc'
bak = '/Users/lcr/.config/opencode/.backups/20261027-product-system-hardening/opencode.jsonc'


def sys_line(path):
    for i, line in enumerate(open(path, encoding='utf-8'), 1):
        if line.strip().startswith('"system": "只 review 明确范围内的改动'):
            return i, line.strip()
    return None, None


for p in (cur, bak):
    n, s = sys_line(p)
    print(p.split('/')[-2] if 'backups' in p else 'current', 'line', n,
          'sha256', hashlib.sha256(s.encode()).hexdigest()[:16] if s else '-')

n1, s1 = sys_line(cur)
n2, s2 = sys_line(bak)
print('identical_text', s1 == s2)

# 顺带确认 review 段起止行与 model 行
lines = open(cur, encoding='utf-8').read().splitlines()
for i in range(n1 - 3, n1 + 1):
    print(i + 1, lines[i].strip()[:60])
