# SOLID 与 Clean Architecture（clean-code 细化）

> 何时读：涉及继承 / 接口设计、模块分层、跨层依赖、依赖注入方向、组件划分时；未读不得就分层问题下结论。
> 引用口径：报告里按「SOLID-S / O / L / I / D」「依赖规则」「四层职责」「组件原则 CCP / CRP / SDP / SAP」引用，不复述定义。
> 其余规则在 `../SKILL.md`；本文件只放细化判据，不重复正文。

## SOLID 原则

### S — Single Responsibility
**A class has one reason to change. One actor, one responsibility.**
- 每个类只服务一个"角色"（Actor）
- 检测：类同时修改状态 AND 调用网络 → 职责混乱，需拆分

### O — Open/Closed
**Open for extension, closed for modification.**
- 用多态替代条件分支
- 新增行为通过新增代码，不修改稳定代码

### L — Liskov Substitution
**Subtypes must be substitutable for their base types without breaking behavior.**
- 子类/实现类必须能完全替代父类/接口
- 不缩小返回值类型、不抛出更宽泛异常、不改变方法契约语义

### I — Interface Segregation
**Many specific interfaces beat one general-purpose interface.**
- 客户端不应依赖不用的方法
- 接口按功能拆分，不合并成"万能接口"

### D — Dependency Inversion
**Depend on abstractions, not concretions.**
- 高层模块不依赖低层模块，二者都依赖抽象
- 抽象不依赖细节，细节依赖抽象

---

## Clean Architecture

### 依赖规则
**Source code dependencies must point inward — toward higher-level policies.**

```
Frameworks & Drivers → Interface Adapters → Use Cases → Entities
(outer)                                                  (inner)
```

### 四层职责
| 层 | 职责 | 示例 |
|------|------|------|
| **Entities** | 企业业务规则，纯领域对象 | User, Order, Payment |
| **Use Cases** | 应用特定业务规则（编排实体） | CreateOrder, ProcessPayment |
| **Interface Adapters** | 转换 use case 格式与外部格式 | Controllers, Presenters, Gateways |
| **Frameworks & Drivers** | 最外层细节（DB、Web 框架、UI） | Spring, Django, React, SQL, gRPC |

### 关键规则
- 内层**不知晓**外层任何东西
- 跨边界数据用简单 DTO/值对象 — **永不**传框架特定类型
- 数据库是细节。Web 是细节。框架是细节。可替换。

### 组件原则
- **CCP** (Common Closure): 一起变的类放一起
- **CRP** (Common Reuse): 别强迫用户依赖不用的东西
- **SDP** (Stable Dependencies): 依赖方向指向稳定性
- **SAP** (Stable Abstractions): 稳定组件应是抽象的

