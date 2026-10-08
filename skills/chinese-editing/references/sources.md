# 来源与取舍

参考核查日期：2026-10-09。以下链接固定到核查时的提交，便于复查；本文件仅在维护、溯源和规则争议时读取。

本 skill 是按任务重新组织的编辑指导。未打包上游仓库、原文全文或检查脚本；示例为本项目编写。来源许可证是核查时 GitHub 仓库元数据的标记，不代表本项目获得了所有第三方材料的授权。

## 参考项目

| 项目与版本 | 阅读内容 | 采用思路 | 本项目的调整 |
| --- | --- | --- | --- |
| [aaranxu/chinese-copywriting-guidelines](https://github.com/aaranxu/chinese-copywriting-guidelines/tree/d7a12dde413a35939a5a8c71e9e9777a844e7a8b)（WTFPL） | README 排版指南 | 中西文混排、全半角、名称拼写与引号选择 | 使用弯引号作为默认，不照搬关于网站现状、法律效力或旧浏览器的断言 |
| [hankunpeng/skills](https://github.com/hankunpeng/skills/tree/e5244b736dc34cf0d62df6814397e6f2accd2f02/skills/chinese-copywriting-linter)（MIT） | SKILL.md 与 scripts/linter.py | 区分只检查和修复，提供具体位置与建议 | 不复制正则修复器，不强制转换直角引号；将载体语法保护放在修订前 |
| [hachiwar/codex-skills](https://github.com/hachiwar/codex-skills/tree/da31b67e83b53cac8a60cc417a5296e6fbbad17b/chinese-document-style)（未确认许可证） | SKILL.md 与 references/chinese-style-guide.md | 文档用途、证据约束、引用完整性、规则层级 | 只作概念比较，不复制原文或实现；正式文体限定在对应文档场景 |
| [Fenng/tech-doc-style-chinese](https://github.com/Fenng/tech-doc-style-chinese/tree/b119d01c9bb7cd132b3c62fafdff34227c4410d1)（MIT） | SKILL.md；references 下的 terminology-and-typography.md、api-status-copy.md、controlled-technical-chinese.md | 技术状态语义、错误恢复、操作前提、按内容选规则 | 保留思路并重写场景指导，不照搬词表和长篇样例，不让所有正文遵循操作手册语气 |

上游许可证及署名仍归各自作者。本仓库的 MIT 许可覆盖自行编写的文件；将来若引入上游实现或实质性原文，应先核查该版本授权并保留相应通知。未确认许可证的来源不作为可自由复制素材。

## 已处理的差异

- **引号**：aaranxu 采用弯引号，hankunpeng 强制直角引号，Fenng 默认直角引号但允许覆盖。本项目使用可覆盖的弯引号默认值，不改固定引用。
- **温度与角度**：hachiwar 示例将 `°C` 与数字相连，Fenng 区分角度与温度。本项目正文默认 `30°`、`30 °C`；遇到明确的行业／出版要求，核实并按目标要求处理。
- **空格规则的性质**：本项目将普通正文的混排留白作为编辑惯例，不宣称它是所有文种统一的强制国家标准。
- **语气**：正式报告、个人学习笔记和品牌文本分别处理；仅排版不会触发风格重写。
- **硬换行**：不强制所有 Markdown 一段一行，保留显式换行和项目惯例。
- **自动修复**：阅读 hankunpeng 脚本时发现，全角数字修复在遮罩检测后对原始整行执行替换，可能连带改变代码字面量；引号修复还使用遮罩后的捕获内容。这是本版不移植该修复器的具体依据，未在本项目执行上游脚本。

## 后续更新

更新时重新查看各来源的提交与许可证，记录影响现有规则的变化。发现冲突先确定适用语境，再修订参考说明；不自动覆盖用户项目的文风选择。若引入批量格式化器，应验证语法保护、不可解析输入、只读模式及错误退出行为后再发布。
