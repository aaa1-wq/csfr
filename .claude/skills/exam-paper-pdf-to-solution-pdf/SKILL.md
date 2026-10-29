---
name: exam-paper-pdf-to-solution-pdf
description: Turn an encrypted or scanned exam/question-paper PDF (password-protected, or image-only with no usable text layer) into a complete solutions document, delivered as a LaTeX-built PDF. Use when the user supplies a PDF of an exam, midterm, homework or problem set and wants the problems read and solved, or wants a worked-answer PDF; covers decryption, page rendering, image reading, exact-arithmetic verification, and the xelatex build on Windows; the final deliverable is always a LaTeX-compiled PDF (see references/latex-pdf-output.md).
whenToUse: The user points at a .pdf of an exam/试卷/题集 (possibly password-protected, possibly a phone scan) and asks to extract the questions and produce answers, explanations, multiple solution variants, or a formatted answer booklet / 答题纸 PDF.
---

# Exam PDF → Solution PDF

Pipeline with two hard parts: **getting the questions out of a possibly-encrypted scan**, and **never shipping a wrong number**. Follow the phases in order; do not skip verification.

## Phase 0 — Inventory (30 seconds)

1. Confirm the file exists and note its size: `Get-Item <pdf> | Select-Object Length`.
2. Look for Poppler tools — they are usually present on Windows with TeX Live:
   `Get-Command pdftotext,pdftoppm,pdfinfo`. If absent, check `D:\texlive\<year>\bin\windows`.
3. Read the DSH runtime paths once: `load_workspace_dependencies` (gives the bundled `python.exe`).

Do **not** start `pip install` of PyMuPDF/pypdf as the first move: on a slow network it hangs for minutes and is unnecessary while Poppler exists.

## Phase 1 — Text layer with the password

```pwsh
& pdftotext -upw <PASSWORD> -layout "<pdf>" "<work>\probe.txt"
```

Judge the result before trusting it:

- **Full sentences of natural language** → real text layer. Read `probe.txt` directly, skip to Phase 4.
- **Only a few stray glyphs plus a watermark such as `扫描全能王 创建`** → phone scan with a fake text layer. It is a scan: go to Phase 2.
- Error `Permission`/`encrypted` → wrong password, or the PDF needs `-opw` (owner password) instead of `-upw`. Retry once with `-opw`; otherwise ask the user.

Never modify or re-save the user's source PDF.

## Phase 2 — Render pages to images and read them

```pwsh
New-Item -ItemType Directory -Force -Path "<work>\pages" | Out-Null
for ($i = 1; $i -le <N_PAGES>; $i++) {
  & pdftoppm -upw <PASSWORD> -r 150 -png -f $i -l $i "<pdf>" "<work>\pages\p$i"
}
```

- Get `N_PAGES` from `& pdfinfo -upw <PASSWORD> "<pdf>"` (line `Pages:`), or just render 1..12 and stop when files stop appearing.
- 150 dpi is the sweet spot for print/handwriting OCR by vision. Drop to 110 only if images are huge; raise to 200 for dense small print.
- Use the **`read_image`** tool on each PNG (the `read` tool refuses binaries). Read pages **in order, one at a time**, and transcribe each question verbatim into a working list before moving on:
  - keep the original symbols (λ, α, x₁, superscripts) and matrix shapes exactly;
  - keep the points per sub-question — they drive how much detail each answer needs;
  - note deliberately ambiguous glyphs (`λ` vs `1`, `0` vs `O`, subscript `n−r`) and re-render that single page at 200–250 dpi to settle them.
- Scan the header/sidebar (school, course code, exam term, total pages) — it goes in the document title.
- Keep a page → question map; some pages contain only half a question.

## Phase 3 — Inventory the questions

Write down, for every question: statement (clean math), points, and expected deliverable (prove / compute / discuss cases / give basis+dimension). Flag the traps you already see — they become "扣分点" in the answer:

- discussion problems that secretly have **no** no-solution case (or unexpectedly do);
- "prove dim = k" that needs both an upper and a lower bound;
- theorem applications whose hypothesis does not literally cover the ask (e.g. basis extension does not guarantee the new vectors avoid a given subspace);
- direction conventions for transition matrices.

## Phase 4 — Solve, then verify with exact arithmetic (mandatory)

Write a script into the workspace and run it with the bundled Python; do not verify by re-reading your own derivation.

```python
from fractions import Fraction as Q          # exact rationals, never floats for proofs
```

Verify each numeric answer **three independent ways** where possible:

1. **Symbolic/exact solve** — Gaussian elimination over `Fraction`, or plug the closed form back into the original equation and compare exactly (`assert residual == [1, lam, lam**2]`).
2. **Second method** — Cramer vs elimination; projection vs least-squares; direct expansion vs determinant identity; matrix coordinates vs least squares. If two methods disagree, the answer is wrong — find out which.
3. **Spot values** — check 3–5 concrete parameter values and confirm the claimed general formula reproduces them.

Pitfalls that actually bite:

- A determinant's **root set** (e.g. `(λ+1)(λ²−λ+2)`) decides the case discussion; compute the roots exactly instead of assuming a familiar factorisation.
- Cross-products, minors and sign patterns: compute components individually and compare against a second formula.
- Verify list/array equality with the same numeric type, and always **print the results table** so you read real values instead of trusting an assertion.
- Avoid `-` vs `−` and full-width characters inside formulas you will paste into LaTeX later.

Shell quoting: PowerShell mangles Python here-strings that contain quotes or CJK. Always `Set-Content` a `.py` file, then run it. Set `$env:PYTHONIOENCODING="utf-8"` for Chinese output.

## Phase 5 — Write the answer document (LaTeX → PDF)

Deliver **a PDF built from LaTeX**, not just markdown text. Structure that works well:

- per question: *standard version* (fastest in an exam), *second version* (different method / 视角), then a boxed **对比点评** (which is safer, which step loses points);
- a final page: **一页速查** with boxed final answers, traps, and must-write sentences;
- keep verification values in a small table so the reader can trust them.

### Skeleton (XeLaTeX + ctex, works on TeX Live 2026)

```latex
\documentclass[10pt]{ctexart}
\usepackage[a4paper,margin=2.1cm]{geometry}
\usepackage{amsmath,amssymb,amsthm,bm}
\usepackage[table]{xcolor}
\usepackage{tcolorbox}\tcbuselibrary{skins,breakable}
\usepackage{enumitem,array,booktabs,lastpage,fancyhdr}
\xeCJKsetup{CJKmath=true}
\newcommand{\qq}{\operatorname{rank}}
\newcommand{\dm}{\dim}
\newcommand{\Img}{\operatorname{Im}}   % never \Im: already defined
```

### Build (Windows, non-ASCII paths)

`xelatex` cannot write beside a non-ASCII `.tex` filename. Build in an ASCII scratch dir and copy out:

```pwsh
$ws = "<workspace>"; $b = "$ws\build_tmp"
New-Item -ItemType Directory -Force -Path $b | Out-Null
Copy-Item "$ws\<name>.tex" "$b\main.tex" -Force
& xelatex -interaction=nonstopmode -output-directory="$b" "$b\main.tex"
& xelatex -interaction=nonstopmode -output-directory="$b" "$b\main.tex"   # 2nd pass for LastPage
Copy-Item "$b\main.pdf" "$ws\<name>.pdf" -Force
```

Full build script, error table (`\heiti`/`\Im` already defined, `colwidth`, missing circled numerals, non-ASCII `.log`) and a copy-pasteable CTeX template: read [references/latex-pdf-output.md](references/latex-pdf-output.md).

Then **check the log**: `Select-String -Path "$b\main.log" -Pattern "Missing character"` must be empty, and `Output written on ... (N pages)` must exist. Render page 1 (and any page with matrices) with `pdftoppm -r 80 -png` and look at it with `read_image` before declaring success.

## Phase 6 — Deliver

- Keep the `*.tex` source and the final `*.pdf` in the workspace; delete the scratch build dir and probe scripts.
- Call `present` with the PDF so the user gets a preview card.
- In the reply give per-question one-line answers, name the traps, and offer extras (blank answer-sheet template, Word version).

## Hard-won LaTeX rules

1. **Never redefine** `\heiti`, `\songti`, `\Im`, `\Re` — `ctexart`/`amsmath` own some of them (use `\Img`, `\Rr`).
2. `tcolorbox` has no `colwidth` key; the box is already `\linewidth`. Use `boxrule=0pt,leftrule=3pt` for the thin accent look.
3. **No curly quotes and no circled numerals** `① ② ③` in Latin fonts — they print as empty boxes (`Missing character: There is no ①`). Use `(i)`, `(ii)`.
4. Compile **twice** whenever `lastpage`/`hyperref` is used.

## Anti-patterns

- Writing answers straight from the images without an exact-arithmetic check — one sign error in a determinant destroys the whole discussion problem.
- Installing Python PDF libraries before trying Poppler.
- Overwriting or "fixing" the user's source PDF.
- Running `Get-Content -Raw | Set-Content` over a `.tex` to do replacements: it rewrites the encoding and mangles CJK irreversibly. Use a Python script with `encoding="utf-8"` and `newline="\n"`, then re-read the head of the file to confirm.
