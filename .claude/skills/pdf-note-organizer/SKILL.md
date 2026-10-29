---
name: pdf-note-organizer
description: 读取 PDF 或黑板板书图片，整理成结构化的 LaTeX 笔记，并按五层空间结构做多视角分析。当用户提到“整理 PDF 笔记”“把板书转成 LaTeX”“整理黑板照片”“用欧式空间和 Euclidean 空间分析定义/证明”“按上次的格式整理”时使用。
---

# PDF / 板书 笔记整理（LaTeX 输出，五层结构，带记忆）

## 0. 启动时先读记忆（每次必做）

在处理任何输入之前，先读取（存在才读，不存在跳过）：

1. `memory/preferences.md` —— 用户长期偏好（LaTeX 模板、命名习惯、是否自动编译、术语表风格、是否默认五层分析等）。
2. `memory/sessions/` 下与本任务相关的最近记录 —— 用户说“按上次的格式”“接着上次的”时优先读最近一个 session 文件。

读完后在回复开头用一句话确认：“已读取你的偏好：<摘要>。本次按此执行，如需调整请说。”**不要跳过直接开工。**

## 1. 术语归一化（识别前必做）

将以下拼写变体统一识别为 **欧几里得空间 / Euclidean space**：

- `eudiclean` / `euclidean` / `Euclidian` / `欧氏空间` / `欧几里得空间`
- 原文写作 `eudiclean` 时，笔记中首次出现标注：`Euclidean space（原文拼写 eudiclean）`

**层次消歧**：英文 `Euclidean space` 既可指具体空间也可指抽象类，需按上下文判定并在笔记中显式标注：

- 指具体坐标空间时写 `Euclidean space (\(\mathbb{R}^n\))`
- 指抽象有限维实内积空间时写 `Euclidean space (abstract finite-dim inner product space)`

## 2. 五层空间结构（分析框架）

所有定义/定理/证明，先定位其**最低成立层**，再逐层向上写具体化。层级由一般到特殊：

\[
\text{拓扑空间} \supset \text{度量空间} \supset \text{赋范空间} \supset \text{内积空间} \supset \text{Hilbert 空间}
\]

| 层次 | 英文 | 核心结构 | 能谈什么 | 不能谈什么 | \(\mathbb{R}^n\) 是否属于 |
|---|---|---|---|---|---|
| 拓扑空间 | topological space | 开集族 \(\tau\) | 连续性、连通性、紧性、闭包、分离公理 | 距离、长度、角度、线性运算 | 是 |
| 度量空间 | metric space | 距离 \(d(x,y)\) | 开球、收敛、Cauchy 列、完备性、一致连续 | 向量加法、数乘、范数、内积 | 是 |
| 赋范空间 | normed space | 范数 \(\|x\|\) | 线性运算连续性、有界线性算子、Banach 空间 | 内积、角度、正交 | 是 |
| 内积空间 | inner product space | 内积 \(\langle x,y\rangle\) | 正交、投影、Gram–Schmidt、Bessel 不等式 | 完备性不保证 | 是 |
| Hilbert 空间 | Hilbert space | 内积 + 完备 | 投影定理、Riesz 表示、正交分解、谱理论 | —— | 是（有限维自动完备） |

**降层关系**（每往左一层忘记一个结构）：

- Hilbert → 内积：忘记完备性，投影定理可能失效。
- 内积 → 赋范：忘记内积，失去正交/角度；平行四边形恒等式不再保证。
- 赋范 → 度量：忘记线性结构，失去向量运算与线性算子。
- 度量 → 拓扑：忘记距离，失去 Cauchy 列、完备性、一致连续；紧不再等价于有界闭。

**关键陷阱**：

- 紧 \(\Leftrightarrow\) 有界闭（Heine–Borel）只在 \(\mathbb{R}^n\) 成立；一般度量空间假，无限维赋范/Hilbert 空间假，拓扑空间无“有界”概念。
- Cauchy 列收敛只在完备层保证（Banach / Hilbert / \(\mathbb{R}^n\)）。
- 正交投影只在 Hilbert 层保证；非完备内积空间不一定；赋范及以下无定义。
- 连续 \(\Leftrightarrow\) 开集原像开在所有层都真（拓扑层即定义）。
- 任意两点可分离：拓扑空间需额外假设 Hausdorff；度量空间及以上自动成立。

## 3. 输入类型判断

| 输入类型 | 判断依据 | 处理路径 |
|---|---|---|
| 文本型 PDF | `.pdf` 且 `extract_pdf.py` 能提取到有效文本 | PDF 路径（第 4 节） |
| 扫描件 PDF / 图片 | `.pdf` 提取不到文本，或输入为 `.jpg/.png/.heic` | 板书视觉路径（第 5 节） |
| 混合输入 | 同时给了 PDF 和板书图片 | 对照路径（第 6 节） |
| 多张板书 | 多张图片 | 板书路径，逐张处理后再合并 |

## 4. PDF 路径

1. 检查依赖：若 `extract_pdf.py` 因缺少 `pypdf` 失败，先 `pip install pypdf`。
2. 运行 `scripts/extract_pdf.py <pdf路径>` 提取文本；失败则改用 Read 工具直接读 PDF。
3. 输出**大纲草稿**（章节划分、`\section` 层级、重点标记方式）给用户确认。
4. 按确认的大纲生成 LaTeX，保存到 **workspace 根目录** 下的 `<原文件名>-笔记.tex`（不要写进技能自己的 `notes/` 子目录）。
5. 询问是否运行 `xelatex -interaction=nonstopmode` 编译。

## 5. 板书视觉路径

### 5.1 视觉盘点（不急于转写）

先输出**视觉观察清单**给用户确认：

- 文字区域：主要文字块位置与大致内容
- 公式/推导：行内公式、独立公式、多步推导链
- 图形/标注：箭头、框选、下划线、圈注、颜色标记
- 表格/列表：表格结构或编号列表
- 不确定项：看不清的字、符号、箭头方向

**看不清的必须标“待确认”，不得根据常识猜测补全。**

### 5.2 用户确认

问：“以上是我识别到的内容，有需要修正或补充的吗？”确认后再继续。

### 5.3 重构为 LaTeX

- **保留推导链**：多步推导用 `align*` 逐步还原，不跳步。
- **图形用 TikZ 重绘或占位**：优先 TikZ；成本过高则 `figure` 占位，caption 写“板书原图：<简要描述>”。
- **标注关系用文字说明**：箭头/框选含义用 `\textbf{板书标注：}...`。
- **待确认项集中列出**：文末 `\section*{待确认内容}`。

### 5.4 多张板书

按顺序逐张盘点，全部确认后**合并成一份** LaTeX，用 `\section` 区分每张板书（或按内容逻辑合并），文件名 `<首张文件名>-板书笔记.tex`。

## 6. 混合输入路径（PDF + 板书）

1. 先走 PDF 路径提取大纲。
2. 再走板书路径做视觉盘点。
3. 输出**对照表**：板书内容对应 PDF 哪一章节、哪些是板书独有补充/批注。
4. 确认后以 PDF 结构为主干，板书内容作为 `\subsection*{板书补充}` 或旁注插入对应位置。
5. 文件名 `<PDF文件名>-含板书笔记.tex`。

## 7. LaTeX 输出格式

### 7.1 文档骨架

```latex
\documentclass[11pt]{ctexart}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{graphicx,booktabs,hyperref,geometry}
\usepackage{tikz}
\geometry{a4paper,margin=2.5cm}

\newenvironment{chaptersummary}
  {\par\medskip\noindent\textbf{本章小结：}\begin{quote}}
  {\end{quote}}

\title{<原文件名> 笔记}
\author{}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage
% 正文
\end{document}
```
