import fitz
import os
import re


def single(input_path: str, output_path: str) -> None:
    entries = sorted(os.scandir(input_path), key=lambda x: x.name)

    path_split = re.split('/', input_path)
    if path_split[-1] == '':
        doc_name = path_split[-2] + '.pdf'
    else:
        doc_name = path_split[-1] + '.pdf'

    if output_path[-1] in ('/', '\\'):
        output_path = output_path[:-1]

    if len(entries) > 0:
        with fitz.open() as doc:
            for i, e in enumerate(entries):
                if e.is_file():
                    with fitz.open(e.path) as img:
                        rect = img[0].rect
                        img_pdf_stream = img.convertToPDF()
                    with fitz.open('pdf', img_pdf_stream) as img_pdf:
                        doc.newPage(width=rect.width, height=rect.height).showPDFpage(rect, img_pdf, 0)

            doc.save(f'{output_path}/{doc_name}')
            print(f"\"{doc_name}\" successfully saved to {output_path}")


def multiple(input_path: str, output_path: str) -> None:
    entries = os.scandir(input_path)

    for i, e in enumerate(entries):
        if e.is_dir():
            single(e.path, output_path)
