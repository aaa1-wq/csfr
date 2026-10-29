#!/usr/bin/env python3
"""Extract plain text from a PDF for the pdf-note-organizer skill.

Usage:
    python extract_pdf.py <path/to/file.pdf> [-o out.txt] [--pages 1-20]

Prints extracted text to stdout (or writes it to -o). Exits non-zero when no
usable text layer is found, so the caller can fall back to the visual path.
"""
import argparse
import sys


def extract(path, page_range=None):
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.stderr.write("ERROR: missing dependency 'pypdf'. Run: pip install pypdf\n")
        return 1

    try:
        reader = PdfReader(path)
    except Exception as exc:  # noqa: BLE001 - surface any reader failure verbatim
        sys.stderr.write("ERROR: cannot open PDF: %s\n" % exc)
        return 1

    if getattr(reader, "is_encrypted", False):
        try:
            reader.decrypt("")
        except Exception:
            sys.stderr.write("ERROR: PDF is encrypted; decrypt it before extraction.\n")
            return 1

    indices = range(len(reader.pages))
    if page_range:
        start_s, _, end_s = page_range.partition("-")
        start = max(int(start_s) - 1, 0)
        end = int(end_s) if end_s else start + 1
        indices = range(start, min(end, len(reader.pages)))

    chunks = []
    for i in indices:
        try:
            text = reader.pages[i].extract_text() or ""
        except Exception as exc:  # noqa: BLE001
            sys.stderr.write("WARN: page %d extraction failed: %s\n" % (i + 1, exc))
            text = ""
        chunks.append("=== page %d ===\n%s" % (i + 1, text.strip()))

    body = "\n\n".join(chunks)
    visible = "".join(body.split())
    if len(visible) < 40:
        sys.stderr.write(
            "ERROR: no usable text layer (only %d visible chars). "
            "Treat this as a scanned PDF and use the visual path.\n" % len(visible)
        )
        return 2
    return body


def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("pdf", help="path to the PDF file")
    parser.add_argument("-o", "--output", help="write text to this file instead of stdout")
    parser.add_argument("--pages", help="page range like 1-20")
    args = parser.parse_args()

    result = extract(args.pdf, args.pages)
    if isinstance(result, int):
        return result

    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(result)
        print("Wrote %d chars to %s" % (len(result), args.output))
    else:
        sys.stdout.write(result + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
