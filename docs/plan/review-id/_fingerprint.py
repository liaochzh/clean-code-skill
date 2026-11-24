"""采 review 编号基线的版本指纹。

skillset = clean-code 的 SKILL.md + 技能内 references/*.md + 可委派的全局扩展规则，
按文件名排序后拼接取 sha1（任一变动即视为「规则改版」）。
system = review agent 的 `system` 提示词全文 sha1（改题面等于换被测对象），
并输出两句证据范围纪律是否在位，供人眼快速判同源。
"""
import hashlib
import json
import os
import re

base = '/Users/lcr/.config/opencode/skills/clean-code/'
global_ref = '/Users/lcr/.config/opencode/references/'
config = '/Users/lcr/.config/opencode/opencode.jsonc'

files = [base + 'SKILL.md', base + 'references/solid-and-architecture.md',
         global_ref + 'project-type-detect.md',
         global_ref + 'flutter-getx-mvvm.md',
         global_ref + 'flutter-riverpod-clean.md']

h = hashlib.sha1()
for p in files:
    if not os.path.exists(p):
        print('MISSING', p)
        continue
    with open(p, 'rb') as f:
        data = f.read()
    h.update(os.path.basename(p).encode() + b'\0' + data)
    print(os.path.basename(p), hashlib.sha1(data).hexdigest()[:12])
print('skillset_sha1', h.hexdigest())

with open('/Users/lcr/Projects/clean-code-skill/docs/plan/review-id/PROMPT.template.md', 'rb') as f:
    t = f.read()
print('template_sha1', hashlib.sha1(t).hexdigest())

# review 的 system：opencode.jsonc 是 JSONC（含注释），不整体解析；
# 只在含该 agent 首句的那一行里取 JSON 字符串字面量，再按 JSON 规则反转义。
marker = '只 review 明确范围内的改动'
with open(config, encoding='utf-8') as f:
    line = next((l for l in f if marker in l), None)
if line is None:
    print('SYSTEM_MISSING', config)
else:
    m = re.search(r'"system"\s*:\s*"((?:[^"\\]|\\.)*)"', line)
    if m is None:
        print('SYSTEM_UNPARSED', config)
    else:
        sys_text = json.loads('"' + m.group(1) + '"')
        print('system_sha1', hashlib.sha1(sys_text.encode()).hexdigest())
        s1 = '证据必须落在被审范围内'
        s2 = '待核实项每份最多 3 条'
        print('system_flags', '句1=%s 句2=%s' % ('on' if s1 in sys_text else 'off',
                                               'on' if s2 in sys_text else 'off'),
              '(%d 字符)' % len(sys_text))
