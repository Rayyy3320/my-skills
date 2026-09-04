---
name: advisor-review
description: Opt-in dual-model collaboration mode. Load ONLY when the user explicitly asks to enable advisor/second-model collaboration (e.g. 开启顾问模式 / advisor mode). Adds a read-only second model as reviewer/consultant alongside the primary executor. Without loading this skill, the project runs its normal single-executor process — nothing in this file should be read or applied.
---

# Advisor Review Mode（顾问模式）

**本 skill 被加载 = 模式开启**，对当前会话/当前波次生效；卸载或新会话未加载 = 回到
项目原有单执行者流程。本模式不在仓库文档中留任何痕迹，不修改所有权表与常读文档。

## 模式铁律

1. **决策权唯一**：主执行者（Coordinator + 用户）拥有全部写入权与最终裁量；顾问只读、
   只建议。顾问的产出是"发现清单"，不是任务清单。
2. **顾问永不写**：不修改文件、不跑测试、不执行命令。若确需其动手，隔离在独立分支/独立
   checkout，绝不与主执行者共享工作区。
3. **按需启停**：用户明确要求时加载本 skill；波次结束或用户说关闭即停。恢复默认流程时
   不遗留任何状态。
4. **与治理体系正交**：本 skill 可配合 project-governance skill 使用（治理管结构与流程，
   本 skill 管第二模型协作），也可独立用于任何项目。顾问的发现进入主执行者既有的
   triage/波次管线（采纳排期 / 拒绝一行理由 / 存疑交用户），不改变验收与判定流程本身。

## 顾问的三个使用时机（仅在此加载后有效）

| 时机 | 触发 | 产出 |
|---|---|---|
| 波次边界评审 | 共享层（primitive/契约/数据形状）有改动的波结束时 | 分级发现清单 |
| 疑难升级 | 同一 bug 主执行者两轮未修复 | 定向诊断 + 建议路径 |
| 设计预审 | 大型机制开工前（一次性） | 风险与替代方案清单 |

## 评审请求合同（发给顾问的封闭格式）

过度防御型模型的正确用法是封闭合同。每次请求必须包含：

```text
[角色] 你是只读评审，不修改文件、不运行测试/命令、不扩大范围。
[范围] 仅评审以下文件/diff：<精确清单>；仅回答以下问题（≤3 个）：<问题列表>
[输出] 按严重度（blocker/major/minor/nit）分级的发现列表，
       每条含：位置、依据、建议。无发现则明确说"无"。
[上下文] 项目治理规则见 <常读文档路径>（若顾问生态原生读取如 AGENTS.md，则指出即可）
```

## 升级咨询包（疑难 bug 时）

最小复现步骤 + 期望 vs 实际 + 主执行者已尝试的路径与排除项 + 相关文件清单 +
一个具体问题。禁止粘贴整段历史——顾问要的是精确切片。

## 发现的 triage（主执行者执行）

逐条标注：采纳（排入当前波或下波）/ 拒绝（一行理由）/ 存疑（交用户仲裁）。
triage 结果回传用户；拒绝不解释超过一行，防止评审驱动发散。

## 可迁移性

本模式对顾问模型不做任何假定（Codex/GPT/Claude/其他均可），术语一律用
"顾问模型/主执行者"。顾问生态若原生读取项目的常读文档（如 AGENTS.md），
治理规则自动对其生效，无需重复传授。
