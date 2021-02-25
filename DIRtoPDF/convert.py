import fitz
import os


def single(input_path: str, output_path: str) -> None:
    entries = sorted(os.scandir(input_path), key=lambda x: x.name)
    doc_name = os.path.basename(input_path) + '.pdf'

    if len(entries) > 0:
        with fitz.open() as doc:
            for i, e in enumerate(entries):
                if e.is_file():
                    with fitz.open(e.path) as img:
                        rect = img[0].rect
                        img_pdf_stream = img.convertToPDF()
                    with fitz.open('pdf', img_pdf_stream) as img_pdf:
                        doc.newPage(width=rect.width, height=rect.height).showPDFpage(rect, img_pdf, 0)

            doc.save(os.path.join(output_path, doc_name))
            print(f"\"{doc_name}\" successfully saved to {output_path}")


def multiple(input_path: str, output_path: str) -> None:
    entries = os.scandir(input_path)

    for i, e in enumerate(entries):
        if e.is_dir():
            single(e.path, output_path)
