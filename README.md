# Chinese Editing Skill · 中文编辑

一个按任务加载规则的中文编辑 skill，覆盖排版校对、文档审校、技术说明和界面文案。保留事实、作者语气与技术字面量，可用于支持 `SKILL.md` 的 Agent。

| 任务 | 工作范围 |
| --- | --- |
| 排版校对 | 中西文留白、标点、数字、单位和名称拼写 |
| 文档审校 | 知识库、博客、README、报告的组织、术语与证据 |
| 技术与界面文案 | 操作步骤、API 说明、按钮、状态、错误和空状态 |

默认简体中文横排弯引号；项目既有规范可以覆盖。只要求排版时不重写语气，要求审阅时只报告问题。规则不限于 Markdown，但编辑二进制文档需要宿主的相应工具。

## 安装

只需安装 `skills/chinese-editing/` 整个目录。运行 skill 本身不需要 Python、Node.js、API Key 或 MCP；仓库维护检查另用 Python。

### Pi：项目级

```sh
git clone https://github.com/senmoxiu/chinese-editing-skill.git
```

将仓库克隆到一个独立目录，在目标项目中把 `skills/chinese-editing/` 复制到 `.agents/skills/chinese-editing/`。Pi 的 Agent Skills 发现机制支持项目 `.agents/skills/`。

在 Pi 中执行 `/reload`，然后调用：

```text
/skill:chinese-editing 只校对这段中文排版，保留代码和原有语气。
```

也可不安装，通过 `pi --skill /absolute/path/to/chinese-editing-skill/skills/chinese-editing` 临时加载。以上命令与路径机制依据 [Pi 文档](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md) 和 [CLI 文档](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/cli.md)，尚未在所有版本和模型上实测。

### Codex 与其他 Agent

将同一完整目录放入目标 Agent 支持的项目技能目录，再显式请求使用 `chinese-editing`。例如 Codex 支持的会话中可输入：

```text
使用 $chinese-editing 审校这份笔记，保留第一人称和未解决的问题。
```

不同客户端的发现目录与刷新方式可能不同，以客户端文档为准。`agents/openai.yaml` 仅提供 Codex 展示信息，核心规则不依赖它。无需一次安装本仓库的评估、维护脚本或笔记。

如果已安装同名 skill，先比较后更新，避免覆盖自己的规则。项目级安装仅供该项目使用；全局安装由你自行选择。

## 使用示例

```text
只检查 README.md 的中文排版，按位置给建议，不修改文件。
```

```text
整理这篇学习笔记，让概念和例子更清楚；保留我的疑问与个人判断。
```

```text
改进这个提示。已知任务仅进入队列，完成时间未知：
“操作成功，马上完成！”
```

最后一个请求可得到“已提交，等待处理”，而不会凭空补上完成时限。

## 规则与参考

入口：[SKILL.md](skills/chinese-editing/SKILL.md)。按需参考：[排版](skills/chinese-editing/references/typography.md)、[文档](skills/chinese-editing/references/documents.md)、[技术与界面文案](skills/chinese-editing/references/technical-copy.md)。

本项目参考 aaranxu 的中文排版指南，以及 hankunpeng、hachiwar、Fenng 的相关 skill。阅读文件、固定版本链接、授权状态和差异见[来源与取舍](skills/chinese-editing/references/sources.md)。未移植上游自动修复脚本，也不把本 skill 当作国家标准或行业合规认证。

## 验证与维护

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

校验只检查 skill 元数据、相对链接、来源版本、笔记和评估数据结构。它不能证明模型输出质量。

[验收样例](evals/cases.json) 包含真实使用请求与行为评分点。按 [evals/README.md](evals/README.md) 在目标 Agent 和模型中复测，不把人工样例当作模型实测成绩。

拉取更新后重新校验并对比已安装目录；本仓库不自动更新全局配置，不创建 Git 钩子。

## 许可

本仓库自行编写的内容使用 [MIT License](LICENSE)。第三方项目保持各自许可，详见来源记录。
