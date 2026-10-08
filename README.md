# Chinese Editing Skill · 中文编辑

一个按任务加载规则的中文编辑 skill，覆盖排版校对、文档审校、技术说明和界面文案。保留事实、作者语气与技术字面量，可用于支持 `SKILL.md` 的 Agent。

| 任务 | 工作范围 |
| --- | --- |
| 排版校对 | 中西文留白、标点、数字、单位和名称拼写 |
| 文档审校 | 知识库、博客、README、报告的组织、术语与证据 |
| 技术与界面文案 | 操作步骤、API 说明、按钮、状态、错误和空状态 |

默认简体中文横排弯引号；项目既有规范可以覆盖。只要求排版时不重写语气，要求审阅时只报告问题。规则不限于 Markdown，但编辑二进制文档需要宿主的相应工具。

## 安装

只需安装 `skills/chinese-editing/` 整个目录。

### 使用 skills CLI

已安装 Node.js 和 npm 时，在目标项目目录运行：

```sh
npx skills add senmoxiu/chinese-editing-skill --skill chinese-editing
```

按提示选择目标 Agent。默认安装到当前项目；只有添加 `-g` 才安装到用户级目录。

如果只想查看仓库中可发现的 skill，不进行安装：

```sh
npx skills add senmoxiu/chinese-editing-skill --list
```

命令说明见 [skills CLI 文档](https://github.com/vercel-labs/skills#install-a-skill)。skills.sh 根据正常 CLI 安装的遥测自动记录并收录；关闭遥测的安装不提供该统计，`--list` 和直接克隆也不等同于安装。收录机制见 [官方 FAQ](https://www.skills.sh/docs/faq)，不保证安装后立即可搜索到。


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

校验只检查 skill 元数据、相对链接、来源版本和笔记。它不能证明模型输出质量。

拉取更新后重新校验并对比已安装目录；本仓库不自动更新全局配置，不创建 Git 钩子。

## 许可

本仓库自行编写的内容使用 [MIT License](LICENSE)。第三方项目保持各自许可，详见来源记录。
