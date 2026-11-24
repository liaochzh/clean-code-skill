# 派单模板（review 编号基线）

> 用法：替换 `{{DIFF}}`、`{{AFTER_FILES}}`、`{{SLUG}}` 后整段交给 `subagent(agent=review)`。
> **约束**：本模板与派单文本中不得出现「编号」二字——否则测的是「按指令产出」，不是「自发引用」。

---

审查以下改动。以下内联内容即完整审查范围，**无法也无需定位文件**：不要执行任何 read/ls/head/grep/git 之类命令，也不要尝试推断文件在磁盘上的位置。

审查范围：仅下面这处 diff。

```diff
{{DIFF}}
```

{{AFTER_FILES}}

要求：按 clean-code 规范审查，沿用你自己的报告格式；审查落档 slug 用 `{{SLUG}}`。
