# 把 LaTeX 源码编译成 PDF（Windows）

本 skill 的下游产物固定是 **LaTeX 编译出来的 PDF**。这里放可直接复制的脚本。

## 一键编译脚本

保存为 `build_pdf.ps1`，参数：`-Tex <源文件> -Out <输出 pdf>`。

```pwsh
param(
  [Parameter(Mandatory)][string]$Tex,
  [Parameter(Mandatory)][string]$Out
)
$ErrorActionPreference = "Stop"
$tex    = (Resolve-Path $Tex).Path
$ws     = Split-Path $tex -Parent
$b      = Join-Path $ws "build_tmp"
New-Item -ItemType Directory -Force -Path $b | Out-Null

# xelatex 无法在同目录写非 ASCII 文件名的 .log，必须在 ASCII 目录里用 main.tex 编译
Copy-Item $tex (Join-Path $b "main.tex") -Force
& xelatex -interaction=nonstopmode -output-directory="$b" "$b\main.tex" | Out-Null
& xelatex -interaction=nonstopmode -output-directory="$b" "$b\main.tex" | Out-Null

$log = Join-Path $b "main.log"
$missing = Select-String -Path $log -Pattern "Missing character" 
$out = Select-String -Path $log -Pattern "Output written on (.+?) \((\d+) pages\)"

if (-not $out) {
  Write-Error "编译失败，请查看 $log"; exit 1
}
if ($missing) {
  Write-Warning "有 $($missing.Count) 个字符在该字体中缺失（会显示成方框），去日志里找 'Missing character'"
  $missing | Select-Object -First 5 | ForEach-Object { $_.Line }
}
Copy-Item (Join-Path $b "main.pdf") $Out -Force
Write-Output "OK -> $Out  ($($out.Matches[0].Groups[2].Value) pages)"
```

## 每次都要做的验证

```pwsh
# 1) 页数与缺字
Select-String -Path "$b\main.log" -Pattern "Missing character|Output written"

# 2) 目视检查：渲染前几页，用 read_image 看
& pdftoppm -r 80 -png -f 1 -l 2 "$Out" "$ws\preview"
```

## 常见编译错误 → 修法

| 报错 | 原因 | 修法 |
|---|---|---|
| `I can't write on file 'xxx.log'` | 源文件在同目录且文件名非 ASCII | 复制成 `build\main.tex` 再编 |
| `Command \heiti already defined` | ctex 已定义 | 删掉自己的 `\newcommand{\heiti}` / `\newfontfamily\heiti` |
| `Command \Im already defined` | amsmath 已定义 | 改名 `\Img`、`\Rr` 等 |
| `Package pgfkeys Error: ... /tcb/colwidth` | tcolorbox 无此键 | 去掉 `colwidth=\linewidth` |
| `Missing character: There is no ①` | 拉丁字体无圈码/全角符号 | 圈码换 `(i)(ii)`，全角括号换半角 |
| 页脚 `\pageref{LastPage}` 显示 `??` | 只编译了一次 | 编译两次 |
| `! Undefined control sequence \XeTeXglyph` | 字体设置残留 | 删掉冲突的 `\setCJK*font` |

## CTeX 中文样板（最省事的开头）

```latex
\documentclass[10pt]{ctexart}
\usepackage[a4paper,margin=2.1cm]{geometry}
\usepackage{amsmath,amssymb,amsthm,bm}
\usepackage[table]{xcolor}
\usepackage{tcolorbox}\tcbuselibrary{skins,breakable}
\usepackage{enumitem,array,booktabs,lastpage,fancyhdr}
\xeCJKsetup{CJKmath=true}
```

- 粗体中文用 `\heiti`，行内公式里的中文需要 `\text{}` 或 `CJKmath=true`。
- 代码/矩阵中的负号统一 `-`，不要混 `−`（U+2212）。
