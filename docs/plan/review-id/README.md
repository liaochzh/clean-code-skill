# review 编号引用基线 · 资产目录

可复跑的 review 能力基线：固定 fixtures + 固定派单模板 + 机械判读口径 + 版本指纹 + 退化判据。

- **owner**：主 agent（发起方）。diff 生成、派单、判读、写表都由主 agent 做；`review` 只吃内联文本。
- **为什么在 skill 仓库内**（2026-10-28 迁入）：本目录随 `clean-code` skill 一起走——`~/Projects/clean-code-skill/docs/plan/review-id/`（`~/.config/opencode/skills/clean-code` 是目录级软链，指向该仓库）。原位置 `~/docs/plan/review-id/` 已迁空。仍在两条约束内：不进 autoDebug 的 `docs/test/`、不进 `review` 可读的 `references/`；`docs/` 被仓库 `.gitignore` 排除，不发布。
- **常驻**：fixtures 与 oracle 不清理；审查报告存本仓库 `docs/review/rid-*`。
  ⚠️ 新派单的报告仍落在 `~/docs/review/`（`review` 的 `edit` 权限只覆盖 `<cwd>/docs/review/*`），跑完由主 agent `mv` 进本仓库 `docs/review/`。

## 目录

| 路径 | 内容 |
|---|---|
| `PROMPT.template.md` | 固定派单模板，3 占位 `{{DIFF}}`/`{{AFTER_FILES}}`/`{{SLUG}}`；**全文禁出现「编号」二字**（否则测的是「按指令产出」而非「自发引用」） |
| `fixtures/fx1..fx6/{before,after}/` | `before` 干净版、`after` 含 3 处植入（fx5 为 2×不应报 + 1×应报）；每 fixture ≤3 文件、每文件 ≤20 行 |
| `fixtures/fx7/{before,after}/` | **扩展集**（3 文件）：新增 `DiscountPolicy` Protocol + 删除其唯一使用者，使「零引用」在闭世界内可证。**不适用**「3 处植入」不变式，不进任何汇总/对比表、不适用退化判据 |
| `oracle/fx1..fx6.md` | 期望表：问题 / 期望编号 / 期望行为（应报｜不应报）/ 允许衍生项 / 判定限定语 |
| `oracle/fx7.md` | 扩展集期望 + 四档判读（断言命中／限定命中／隐含使用／未命中）+ fx5-r3/r4 对照 |
| `EXTERNAL.md` | **外部效度台账**：纳入规则、去碰撞规则、12 份真实报告盘点、三值判据、不可外推清单、今后追加行 |
| `RESULTS.md` | 12 run 运行表 + 逐 fixture 勾稽 + 汇总 |
| `CONCLUSION.md` | 基线读数、退化判据、复跑三步 |
| `_fingerprint.py` | 采三项指纹：skillset（5 文件）、模板、review 的 `system`（全文 sha1 + 两句在位标记）；`python3` 运行后回填 `RESULTS.md` 指纹表 |

## 判读口径（机械可判）

- **带编号**：条目内出现合法域编号，逐字匹配 `^(C[1-5]|F[1-4]|N[1-7]|G([1-9]|[12][0-9]|3[0-6])|T[1-9]|A(10|[1-9]))$`，且与问题描述同句。**排除**：严重度 `P0/P1/P2`、夹具号 `fx\d`、报告自身条目序号。
- **条目与带编号的计数口径**（2026-10-27 复核后固化，r3/r4 起统一）：**条目**＝报告内独立编号的发现项，单列的「待核实」附录**不计**；**带编号**＝该条目**正文任意位置**出现合法编号即计——含标题标签（`[CleanCode/结构/G23]`）与「依据」行的行内引用（`依据：A10 架构漂移`）。r1/r2 读数未按此口径回读重核，属**偏保守下限**；同一批数据换口径会让编号率变动 10pp 量级，故**跑批前先固化口径，跑完不许改**。
- **检出**：报告条目出现对应文件:行或函数名。带「本范围内未见调用 / 需核实」的记「限定命中」，与断言命中分列。
- **分母**：只在有效 run 上算。`未执行 / 不可执行 / 作废 / 泄漏命中` 一律记 `N/A` 出分母。
  - 检出率 = 检出植入 / （应报植入数 × 有效 run 数）；fx5 的 A1/A2 记「不应报」，不进分母。
  - 编号率 = **带编号条目 / 报告条目总数**（= 检出条目；2026-10-27 更正措辞，历史读数不变）；绝对数只在 run 集合相同时比较，否则比每 run 均值。
- **臆造**：对 fx5 的 A1/A2 给出「不存在/幻觉」结论且无「需核实」限定 ⇒ 记 1 次。
- **事实性错误**：报 diff 内不存在的问题 / 行号对不上 / 复述已解决项 / 无证据的规范臆断（如声称某标准库模块存在却不存在）。oracle 白名单内的衍生项记「衍生」，不计错误。

## 复跑（四步）

1. **同源性前置闸**：跑前跑后各跑一次 `python3 /Users/lcr/Projects/clean-code-skill/docs/plan/review-id/_fingerprint.py`，三行（`skillset_sha1` / `template_sha1` / `system_sha1`）必须完全一致，`system_flags` 的句 1/句 2 状态必须与当轮设计相符（例：测「加句 2 的效果」时，跑前应 `句1=on 句2=off`）。任一不一致 ⇒ 该批**不同源**，只能逐份读数、不得做前后对比（2026-10-27 的教训：`SKILL.md` 在跑批中途被改，12 run 里只有 5 run 可靠）。
2. `git -C /Users/lcr/Projects/clean-code-skill/docs/plan/review-id/fixtures/fx<n> diff --no-index before after`（rc=1 属正常）。
3. 按模板替换三占位派 `review`，slug `rid-<YYYYMMDD>-fx<n>-r<m>`；内容全内联、禁读禁跑。
4. **泄漏探针（分级）**：
   - **作废级**：`grep -E "oracle|review-id-baseline|docs/baseline|fixtures/" docs/review/rid-<YYYYMMDD>-fx[1-6]-r*.md`（在 `~/docs/review/` 扫新落的报告；已归集的旧报告在 `~/Projects/clean-code-skill/docs/review/`）⇒ 命中即该 run 作废（**glob 收窄为 `fx[1-6]`**，避免把扩展集扫进基线批次）。
   - **加固级**（扩展集与外部样本用）：扫 `EXTERNAL|review-id|fixtures/`，但必须先 `grep -v "rid-[0-9]\{8\}-fx"` 排除标题行——报告首行必含 slug，不排除会自命中。
   然后按上面「计数口径」判读并追加 `RESULTS.md`。

## 外部样本口径（真实 review）

- **编号率分母**＝报告条目总数（外部样本无 oracle，「检出条目」不可得）。
- **必须分层**报：(产出 agent, Provider+Model, 对象类型)。同名模型跨 Provider（`console-alibaba` vs `alibaba-token-plan-cn`）不得合并。
- **层内 n<5 只报绝对数**，不报百分率。
- **检出率 / 臆造**：外部样本一律 `N/A`，不得反推。
- **去碰撞**：仅当编号出现在 `[CleanCode/…]` 标签内或「依据／引用：」句中才计；发现项序号与条目序列同构（`F1..F10`）⇒ 整份记「碰撞风险=高」。
- **计数区间**：只计「报告原文」段，主 agent 处置段（核销表／按反馈的修复）不计。
- 详见 `EXTERNAL.md`（含 12 份盘点与三值判据）。

## 当前生效判据（r4 定案，2026-10-27）

保留 system 的两句后，新的合格线是四条**同时**满足：

| 判据 | 阈值 | 依据 |
|---|---|---|
| 事实性错误 | **0 条** | 主判据（硬错断言必须消失） |
| 检出 | **≥90%** 应报植入 | 不许用「写待核实」换检出 |
| 编号率 | **≥42%** | 预登记为基线 62% − 20pp；同源集按统一口径复核基线为 64%，对应 44%，仍按 42% 执行（宁可漏报不误报） |
| 待核实 | **每份 ≤3 条且独立成段** | 防止稀释阻断项 |

> 不满足任一条 ⇒ 回退 system 那两句（删掉即可，锚点 `不因风格偏好要求无关重构` 全文件唯一），并重跑两条门禁。
