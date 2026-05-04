# 随机演化论 · Random Evolution

> 随机性如何塑造宇宙、生命与文明

一本从单一公理出发，推导出五条核心定律和一系列推论，用统一的演化逻辑解释从宇宙到文明一切系统兴衰的科普叙事著作。

**作者**：魏永江

---

## 👀 我是读者，怎么读？

- **在线版**（推荐）：`https://felixwayne0318.github.io/RandomEvolution/`（GitHub Pages 启用后生效）
- **GitHub 直接读**：从下方"全书结构"逐章点击
- **下载 PDF/EPUB**：在线版页面右上角下载按钮（构建后可用）

### 全书结构

- 📖 [卷首](./index.qmd)
- ✍️ [引言：一切系统终将崩溃？](./引言初稿.md)
- 📐 [第一部分 · 理论篇——秩序的真相](./第一部分_理论篇.md)
- 🎼 第二部分 · 应用篇——七重奏
  - [第一章 · 宇宙](./第二部分_应用篇/01_宇宙.md)
  - [第二章 · 生命](./第二部分_应用篇/02_生命.md)
  - [第三章 · 生态](./第二部分_应用篇/03_生态.md)
  - [第四章 · 社会](./第二部分_应用篇/04_社会.md)
  - [第五章 · 文明](./第二部分_应用篇/05_文明.md)
  - [第六章 · 经济](./第二部分_应用篇/06_经济.md)
  - [第七章 · 技术](./第二部分_应用篇/07_技术.md)
- ⚖️ [第三部分 · 哲学篇——秩序的代价](./第三部分_哲学篇.md)
- 🌊 [第四部分 · 未来篇——与扰动共舞](./第四部分_未来篇.md)

### 反馈

- 内容意见 / 错误纠正：在 [GitHub Issues](https://github.com/FelixWayne0318/RandomEvolution/issues) 提交，标题前缀 `[反馈]`
- 学科专家审读：欢迎 fork + PR

---

## ✍️ 我是作者/合作者，怎么写？

### 写作前必读

| 文件 | 用途 |
|:---|:---|
| [`CLAUDE.md`](./CLAUDE.md) | 写作风格、规范细则、工作流 |
| [`术语表.md`](./术语表.md) | 单一真相源——术语 / 定理 / 案例归属 |
| [`全书提纲.md`](./全书提纲.md) | 章节责任分配 + 主讲/复演归属 |
| [`字数预算.md`](./字数预算.md) | 各章字数目标 |

### 评估提示词

| 文件 | 用途 |
|:---|:---|
| [`评估提示词.md`](./评估提示词.md) | 单文档评估（仅引言） |
| [`全面评估提示词.md`](./全面评估提示词.md) | 里程碑评估（多文档 + 基础设施） |

### 章节修订日志

详见 [`docs/`](./docs/) 目录，每章一个 `CHANGELOG-{章}.md`。

### 字数追踪

```bash
python3 scripts/wordcount.py
```

输出当前各章中文字符数 + 进度条 + 与预算的对比。

### 草稿放哪里

- 过程性草稿、废弃版本、个人笔记 → `drafts/`（已在 `.gitignore` 排除）
- 写作中途临时文件 → 同样放 `drafts/`

---

## 🛠️ 我是开发者，怎么构建？

本项目使用 **[Quarto](https://quarto.org/)** 作为成书工具链，从一份 Markdown 源同时生成网页、PDF、EPUB 三种格式。

### 一次性环境准备

```bash
# 1. 安装 Quarto（任选一种）
#    macOS:
brew install --cask quarto
#    Ubuntu/Debian:
#    从 https://quarto.org/docs/get-started/ 下载 .deb 安装
#    Windows:
#    从 https://quarto.org/docs/get-started/ 下载 .msi 安装

# 2. （仅 PDF 输出需要）安装 TinyTeX
quarto install tinytex
```

### 渲染整本书

```bash
quarto render                      # 渲染所有格式（HTML + PDF + EPUB）
quarto render --to html            # 仅渲染网页版（最快，日常预览推荐）
quarto render --to pdf             # 仅渲染 PDF（适合校对）
quarto render --to epub            # 仅渲染电子书
```

输出文件位于 `_book/` 目录。

### 实时预览

```bash
quarto preview
```

启动本地服务器，文件保存即自动刷新浏览器。

### 自动出版（GitHub Actions）

每次 push 到 `main` 分支后，CI 自动渲染网页版并部署到 GitHub Pages。

**首次启用步骤**（仅需做一次）：

1. push 到 `main` 触发首次构建（自动创建 `gh-pages` 分支）
2. 仓库 `Settings → Pages → Build and deployment`，Source 设为 `Deploy from a branch`，分支选 `gh-pages` / `(root)`
3. 等 1-2 分钟，访问 `https://felixwayne0318.github.io/RandomEvolution/`

工作流文件：

- [`.github/workflows/publish.yml`](./.github/workflows/publish.yml) — 自动出版
- [`.github/workflows/link-check.yml`](./.github/workflows/link-check.yml) — Markdown 链接检查（每周一 + push 触发）

### 项目结构

```
.
├── 引言初稿.md                  # 引言（已 v0.2）
├── 第一部分_理论篇.md            # 理论篇（§1 已写，§2-§7 待）
├── 第二部分_应用篇/              # 应用篇 7 章占位
├── 第三部分_哲学篇.md            # 占位
├── 第四部分_未来篇.md            # 占位
├── index.qmd                    # 卷首
├── _quarto.yml                  # Quarto 项目配置
├── theme.scss                   # 中文排版主题
├── filters/                     # Pandoc Lua 过滤器
├── references.bib               # BibTeX 参考文献库
├── 术语表.md                     # 单一真相源（不进正文）
├── 全书提纲.md                   # 写作脚手架（不进正文）
├── 字数预算.md                   # 字数目标（不进正文）
├── 评估提示词.md                 # 单文档评估提示词
├── 全面评估提示词.md             # 里程碑评估提示词
├── scripts/wordcount.py         # 字数追踪
├── docs/                        # 章节修订日志
├── .github/                     # CI 工作流
├── CLAUDE.md                    # 项目规范
└── LICENSE                      # 许可
```

---

## 版权

- **正文** 采用 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh-Hans) 许可（署名–非商业–禁止演绎）
- **构建配置**（`_quarto.yml` / `filters/` / `theme.scss` / `scripts/` / `.github/workflows/`）以 MIT 许可发布，可自由复用

详见 [LICENSE](./LICENSE)。
