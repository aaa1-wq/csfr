# 用户长期偏好

> 本文件由 `pdf-note-organizer` 技能在第 0 步读取。可直接编辑，技能会按此执行。
> 未填写的项视为“未指定”，技能会在首次遇到时询问并在当次结束后回填。

## 输出与命名
- 默认输出目录：workspace 根目录（不建 `notes/` 子目录）
- 命名规则：`<原文件名>-笔记.tex` / `<原文件名>-板书笔记.tex` / `<原文件名>-含板书笔记.tex`
- 是否默认自动编译：否（每次询问）

## LaTeX 模板
- 文档类：`ctexart`，11pt
- 页面：A4，边距 2.5cm
- 常用宏包：amsmath, amssymb, amsthm, graphicx, booktabs, hyperref, geometry, tikz
- 自定义环境：`chaptersummary`（本章小结）

## 内容风格
- 默认做五层空间结构分析：待询问（技术数学类输入建议默认开启）
- 术语归一化：欧氏空间 / 欧几里得空间 / euclidean / Euclidian / eudiclean
- 不确定内容一律标“待确认”，不猜测补全

## 其他
- 语言：中文正文，数学符号保留 LaTeX 原生写法
- 是否需要术语表：待询问
