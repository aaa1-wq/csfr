import io
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn


def iter_block_items(parent):
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, parent)
        elif child.tag == qn('w:tbl'):
            yield Table(child, parent)


def dump(path, out):
    doc = Document(path)
    lines = []
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            t = block.text.strip()
            if t:
                lines.append(f"[{block.style.name}] {t}")
        else:
            lines.append("=== TABLE ===")
            for row in block.rows:
                cells = [c.text.replace("\n", " / ").strip() for c in row.cells]
                lines.append(" | ".join(cells))
            lines.append("=== END TABLE ===")
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    return len(lines)


n1 = dump(r"C:\Users\dlwlrma\Downloads\政治章节基础题和思考题2026秋季.docx", "doc1_politics.txt")
n2 = dump(r"C:\Users\dlwlrma\Downloads\环境与资源简答题与讨论题2026秋季.docx", "doc2_env.txt")
with io.open("extract_log.txt", "w", encoding="utf-8") as f:
    f.write(f"doc1 blocks: {n1}, doc2 blocks: {n2}\n")
