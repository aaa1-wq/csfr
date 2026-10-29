# csfr 使用指南

本文件说明如何在 DSH 里使用这个仓库: 找文件, 调用技能, 维持记忆, 以及日常维护

## 1. 仓库是什么

| 目录或文件 | 用途 |
| --- | --- |
| `Coursera/` | 学科笔记与课程资料, 按 `[N]学科/(N)课程` 组织 |
| `Annex/工具脚本/` | 生成文档与图片的 Python 脚本 |
| `Annex/杂项/` | 非学科资料与配图 |
| `.claude/skills/` | 技能存档, 共 23 个 |
| `Paper/` | 论文笔记 |
| `Skill/` | 环境配置备忘录 |
| `README.md` | 仓库总索引, 先看这里找资料 |
| `CLAUDE.md` | 仓库级提示词与用户输出契约 |
| `STYLES.md` | 笔记的版式与文风细则 |
| `GUIDE.md` | 本文件 |

## 2. 怎样使用文件

### 2.1 自己浏览

先看 `README.md` 的学科总表与学科明细, 再进入对应目录

目录名后面的 `#` 表示该目录已有笔记文件

### 2.2 在对话里引用文件

DSH 支持用 `@` 前缀引用文件或目录, 路径相对 workspace 根目录, 也可以给绝对路径

- 单个文件: `@Coursera/[1]数学#/(5)数学分析#/闭区间连续函数三定理_逐条讲解.md`
- 含空格的路径: `@"Coursera/[5]英语#/(1)影视文化#/week 3 Diversity.pptx"`
- 整个目录: `@Coursera/[1]数学#/(5)数学分析#`

提示词示例

- 读 `@Coursera/[1]数学#/(5)数学分析#/闭区间连续函数三定理_逐条讲解.md`, 用三句话总结
- 扫描 `@Coursera/[8]网安#`, 列出所有 pdf 与文件大小
- 对比 `@Coursera/[1]数学#/(4)线性代数#/线代期中2021_解答与对照.pdf` 与 `@.../线代期中2022_解答与对照.pdf` 的考点差异

### 2.3 路径注意

- 目录名含 `#` 与 `[ ]`, 在 PowerShell 或脚本里要用引号或 `-LiteralPath`
- 在 URL 里 `#` 会变成 `%23`, 不要直接拼链接
- 文件名含空格时, 提示词里用 `@"..."` 包起来

## 3. 怎样调用 skills

### 3.1 技能是什么

一个技能就是一个目录, 里面有一个 `SKILL.md`

`SKILL.md` 开头的 frontmatter 写 `name` 与 `description`, DSH 根据描述判断什么时候该用这个技能

### 3.2 仓库里的技能是存档

`.claude/skills/` 保存了 23 个技能的完整副本

DSH 运行时实际加载的技能目录通常是 `~/.dsh/skills` 与工作区 `.dsh/skills`

要把仓库里的技能启用, 复制到加载目录

```powershell
Copy-Item -Recurse -Force ".claude/skills/<技能名>" "$env:USERPROFILE\.dsh\skills\<技能名>"
```

也可以复制到工作区 `.dsh/skills/<技能名>`

复制后新开一轮对话, 让 DSH 重新扫描技能目录

### 3.3 在对话里调用

- 直接说: 用 `exam-cram-review` 整理这份材料
- 或说: 读 `.claude/skills/textbook-to-notes/SKILL.md`, 按里面的流程做
- 多技能可以串联: 先用 `pdf-page-image` 渲染页面, 再用 `pdf-figure-crop` 裁图

### 3.4 技能速查

| 场景 | 技能 |
| --- | --- |
| 期末突击复习 | `exam-cram-review` |
| 教材 PDF 转笔记 | `textbook-to-notes` |
| PDF 或板书整理成 LaTeX 笔记 | `pdf-note-organizer` |
| 试卷 PDF 转解答 PDF | `exam-paper-pdf-to-solution-pdf` |
| PDF 书签 / 页面渲染 / 裁图 / 超分 | `pdf-bookmark`, `pdf-page-image`, `pdf-figure-crop`, `super-resolution` |
| 图片上传图床 | `coscmd` |
| 生成演示文稿 | `ppt-master`, `ppt-master-deck` |
| Office 文档处理 | `office`, `office-docx`, `office-xlsx`, `office-pptx`, `office-render`, `office-export-pdf`, `office-recalculate` |
| 数学推理与验证 | `math-skill` |
| 中文润色 | `humanizer-zh` |
| Windows 沙箱权限诊断 | `diagnose-windows-sandbox-acl` |
| 本仓库提交约定 | `push` |

### 3.5 新增技能

1. 在 `.claude/skills/` 下新建目录
2. 写 `SKILL.md`, frontmatter 至少包含 `name` 与 `description`
3. 需要时把脚本放 `scripts/` 子目录
4. 参考 `CLAUDE.md` 的约定, 默认写 `user-invocable: false`, 除非希望用户直接点选

## 4. 记忆怎么用

仓库没有独立的数据库式记忆, 记忆由三类文件承担

| 类型 | 存放位置 | 作用 | 生命周期 |
| --- | --- | --- | --- |
| 会话记忆 | 当前对话上下文 | 记住本次任务的目标与中间结论 | 会话结束即失效 |
| 仓库级长期记忆 | `CLAUDE.md`, `STYLES.md`, `README.md` | 规定协作方式, 版式, 目录索引 | 每次进入仓库都会读取 |
| 知识记忆 | `Coursera/` 下的笔记与资料 | 可检索的学科知识 | 随仓库长期保存 |
| 操作记忆 | `Skill/` | 环境配置与复现步骤 | 随仓库长期保存 |

### 4.1 什么内容写到哪里

- 稳定的输出偏好与协作规则: 写进 `CLAUDE.md` 的「用户输出契约」
- 目录与文件索引: 写进 `README.md`
- 学科结论, 推导, 例题: 写进对应课程目录的笔记
- 装环境与配软件的步骤: 写进 `Skill/`
- 一次性的上下文: 留在对话里, 不要写进仓库

### 4.2 新会话怎样恢复记忆

1. 在 `csfr` 目录内工作, 先让 agent 读 `CLAUDE.md`
2. 读 `README.md` 找到需要的学科与文件
3. 重要但还没写下来的约定, 当场补进 `CLAUDE.md`
4. 不要指望模型自动记住上一次对话, 跨会话的约定必须落成文件

### 4.3 记忆维护建议

- 每周把新的稳定偏好合并进 `CLAUDE.md`, 避免重复条目
- 每次新增资料后更新 `README.md` 的文件数与索引
- 定期检查空目录与重复文件, 保持索引与磁盘一致

## 5. 典型工作流

### 5.1 新资料入库

1. 把文件放进对应 `Coursera/[学科]/(课程)` 目录
2. 大文件先判断是否超过 100 MB, 超过就不进 Git
3. 更新 `README.md` 的文件数与主要内容
4. 提交并推送

### 5.2 期末复习

1. 说: 用 `exam-cram-review` 整理 `@Coursera/[1]数学#/(5)数学分析#`
2. 技能会先读真题与作业, 再反查课本与 PPT
3. 产物是分章的讲解, 题库, 速查与总索引

### 5.3 教材转笔记

1. 说: 用 `textbook-to-notes` 把某本教材转成笔记
2. 技能依次调用 `pdf-page-image`, `pdf-figure-crop`, `coscmd`
3. 图片默认留空占位, 你确认后再补图

### 5.4 试卷转解答

1. 说: 用 `exam-paper-pdf-to-solution-pdf` 解这份试卷
2. 适合加密或扫描版试卷, 最终输出 LaTeX 编译的解答 PDF

### 5.5 做演示文稿

1. 说: 用 `ppt-master` 做一份关于某主题的 PPT
2. 技能会先建工作区, 再逐页生成与校验

## 6. 维护与提交

### 6.1 提交

```powershell
cd csfr
git add -A
git commit -m "说明本次改动"
git push origin main
```

也可以直接说: 用 `push` 技能提交

### 6.2 大文件

- 单文件超过 100 MB 无法直接推送到 GitHub
- 单文件超过 50 MB 会收到推荐使用 Git LFS 的警告
- 课本, 视频, 压缩包建议放网盘或对象存储, 仓库只留链接与索引

### 6.3 不要提交的内容

- `*.aux`, `*.log`, `*.out`, `*.toc` 等 LaTeX 构建产物, 已在 `.gitignore` 忽略
- 临时目录, 缓存, `__pycache__`
- `.dsh` 目录, 由 DSH 管理, 不要手动改

## 7. 常用提示词模板

- 读 `@Coursera/[学科]/(课程)/文件`, 用中文总结三点, 并给出仍不确定的地方
- 在 `@Coursera/[学科]` 下找所有与某主题相关的文件, 列成表格
- 用 `exam-cram-review` 整理 `@某目录`, 输出到 `Coursera/[学科]/(课程)/复习`
- 用 `textbook-to-notes` 把 `@某教材.pdf` 转成笔记, 版式按 `STYLES.md`
- 把这次讨论的稳定结论写进 `CLAUDE.md` 或对应笔记, 然后提交

------
本指南随仓库维护, 规则变化时同步更新
