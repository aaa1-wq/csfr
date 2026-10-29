# -*- coding: utf-8 -*-
"""Build the study-handbook DOCX (politics + environment chapters)."""
import os
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image

BODY_FONT = "Microsoft YaHei"
HEAD_FONT = "SimHei"
ACCENT = RGBColor(0x1F, 0x4E, 0x79)
ACCENT2 = RGBColor(0x9C, 0x4A, 0x00)
GREY = RGBColor(0x59, 0x59, 0x59)
CONTENT_W = 16.0  # cm usable width


def set_run(run, size=10.5, bold=False, color=None, font=None, italic=False):
    font = font or BODY_FONT
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.name = font
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    rf.set(qn("w:ascii"), font)
    rf.set(qn("w:hAnsi"), font)
    rf.set(qn("w:eastAsia"), font)


def para(doc, text="", size=10.5, bold=False, color=None, font=None,
         space_before=0, space_after=4, indent=0.0, line=1.35, align=None,
         first_line=0.0):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line
    if indent:
        pf.left_indent = Cm(indent)
    if first_line:
        pf.first_line_indent = Cm(first_line)
    if align is not None:
        p.alignment = align
    if text:
        set_run(p.add_run(text), size=size, bold=bold, color=color, font=font)
    return p


def rich(doc, parts, size=10.5, indent=0.0, space_before=0, space_after=4,
         line=1.35, first_line=0.0, align=None):
    """parts: list of (text, bold, color_or_None)."""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line
    if indent:
        pf.left_indent = Cm(indent)
    if first_line:
        pf.first_line_indent = Cm(first_line)
    if align is not None:
        p.alignment = align
    for text, bold, color in parts:
        set_run(p.add_run(text), size=size, bold=bold, color=color)
    return p


def h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.2
    set_run(p.add_run(text), size=16, bold=True, color=ACCENT, font=HEAD_FONT)
    pPr = p._element.get_or_add_pPr()
    bd = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "12")
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), "1F4E79")
    bd.append(bottom)
    pPr.append(bd)
    return p


def h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.2
    set_run(p.add_run(text), size=13, bold=True, color=ACCENT, font=HEAD_FONT)
    return p


def h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.25
    set_run(p.add_run(text), size=11.5, bold=True, color=ACCENT2, font=HEAD_FONT)
    return p


def q(doc, label, text):
    """Question line."""
    return rich(doc, [(label, True, ACCENT), ("  " + text, True, None)],
                size=11, space_before=8, space_after=3)


def a(doc, text, first_line=0.75):
    return para(doc, text, indent=0.0, first_line=first_line, space_after=3)


def bullets(doc, items, size=10.5):
    for it in items:
        if isinstance(it, tuple):
            rich(doc, [("• ", False, ACCENT2), (it[0], True, None), (it[1], False, None)],
                 size=size, indent=0.75, space_after=2)
        else:
            rich(doc, [("• ", False, ACCENT2), (it, False, None)],
                 size=size, indent=0.75, space_after=2)


def note(doc, text, color=ACCENT2):
    return rich(doc, [("说明：", True, color), (text, False, color)],
                size=9.5, indent=0.75, space_after=6, line=1.25)


def figure(doc, path, caption, width_cm=CONTENT_W):
    with Image.open(path) as im:
        w, h = im.size
    if width_cm > CONTENT_W:
        width_cm = CONTENT_W
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Cm(width_cm))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(10)
    set_run(cap.add_run(caption), size=9, color=GREY)


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear")
    sh.set(qn("w:fill"), hexcolor)
    tcPr.append(sh)


def speech_block(doc, title, paras_with_time, key_line, words):
    """Render the 5-minute speech as a shaded single-cell table."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    cell = tbl.cell(0, 0)
    cell.width = Cm(CONTENT_W)
    shade(cell, "F4F8FC")
    first = cell.paragraphs[0]
    first.paragraph_format.space_after = Pt(6)
    set_run(first.add_run(f"【五分钟演讲稿】{title}"), size=12, bold=True,
            color=ACCENT, font=HEAD_FONT)
    for t, text in paras_with_time:
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.4
        set_run(p.add_run(f"{t} "), size=10.5, bold=True, color=ACCENT2, font=HEAD_FONT)
        set_run(p.add_run(text), size=10.5)
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.35
    set_run(p.add_run("可以反复使用的一句话："), size=10, bold=True, color=ACCENT, font=HEAD_FONT)
    set_run(p.add_run(key_line), size=10.5, italic=True, color=ACCENT)
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(0)
    set_run(p2.add_run(f"全稿约{words}字，按每分钟250—280字计算，讲完大约5分钟。"),
            size=9, color=GREY)
    return tbl
