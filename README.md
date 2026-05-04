# 随机演化论 · Random Evolution

> 随机性如何塑造宇宙、生命与文明

一本从单一公理出发，推导出五条核心定律和一系列推论，用统一的演化逻辑解释从宇宙到文明一切系统兴衰的科普叙事著作。

## 全书结构

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

## 写作工具链

本项目使用 **[Quarto](https://quarto.org/)** 作为成书工具链，支持从一份 Markdown 源同时生成网页、PDF、EPUB 三种格式。

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
# 渲染所有格式（HTML + PDF + EPUB）
quarto render

# 仅渲染网页版（最快，日常预览推荐）
quarto render --to html

# 仅渲染 PDF（适合校对）
quarto render --to pdf

# 仅渲染电子书
quarto render --to epub
```

输出文件位于 `_book/` 目录。

### 实时预览

```bash
quarto preview
```

启动本地服务器，文件保存即自动刷新浏览器。

## 自动出版

每次 push 到 `main` 分支后，GitHub Actions 会自动用 Quarto 渲染网页版并部署到 GitHub Pages。

**首次启用步骤**（仅需做一次）：

1. push 到 `main` 触发首次构建（会自动创建 `gh-pages` 分支）
2. 仓库 `Settings → Pages → Build and deployment`，将 Source 设为 `Deploy from a branch`，分支选 `gh-pages` / `(root)`
3. 等 1-2 分钟，访问 `https://felixwayne0318.github.io/RandomEvolution/` 即可看到在线书（**GitHub Pages 启用后链接才生效**）

工作流文件见 [`.github/workflows/publish.yml`](./.github/workflows/publish.yml)。

## 写作约定

- 所有正文使用 Markdown，详见 [CLAUDE.md](./CLAUDE.md)
- 草稿/废弃版本放入 `drafts/` 目录（已在 `.gitignore` 中排除）
- 每完成一个章节或重大修改后提交 git commit，commit message 使用中文

## 评估提示词

`评估提示词.md` 收录了对引言/章节进行多维度审查的标准提示词，可用于自评或交叉评审。

## 版权

正文采用 [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh-Hans) 许可（署名–非商业–禁止演绎）。
构建配置（`_quarto.yml`、`filters/`、`theme.scss`、`.github/workflows/`）以 MIT 许可发布，可自由复用。
详见 [LICENSE](./LICENSE)。
