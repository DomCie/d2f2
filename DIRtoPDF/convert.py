import fitz
import os


def single(input_path: str, output_path: str, sorting_mode: int) -> None:
    if sorting_mode == 1:
        entries = sorted(os.scandir(input_path), key=lambda x: x.name)
    elif sorting_mode == 2:
        entries = sorted(os.scandir(input_path), key=lambda x: x.name, reverse=True)
    elif sorting_mode == 3:
        entries = sorted(os.scandir(input_path), key=lambda x: x.stat.st_mtime_ns)
    elif sorting_mode == 4:
        entries = sorted(os.scandir(input_path), key=lambda x: x.stat.st_mtime_ns, reverse=True)
    elif sorting_mode == 5:
        entries = sorted(os.scandir(input_path), key=lambda x: x.stat.st_ctime_ns)
    elif sorting_mode == 6:
        entries = sorted(os.scandir(input_path), key=lambda x: x.stat.st_ctime_ns, reverse=True)

    if input_path[-1] == '/':
        input_path = input_path[:-1]

    doc_name = os.path.basename(input_path) + '.pdf'

    if len(entries) > 0:
        with fitz.open() as doc:
            file_ctr = 0
            for e in entries:
                if e.is_file():
                    with fitz.open(e.path) as img:
                        rect = img[0].rect
                        img_pdf_stream = img.convertToPDF()
                    with fitz.open('pdf', img_pdf_stream) as img_pdf:
                        doc.newPage(width=rect.width, height=rect.height).showPDFpage(rect, img_pdf, 0)
                    file_ctr = file_ctr + 1

            if file_ctr > 0:
                doc.save(os.path.join(output_path, doc_name))
                print(f"\n\"{doc_name}\" successfully saved to {output_path}")


def multiple(input_path: str, output_path: str, sorting_mode: int) -> None:
    entries = os.scandir(input_path)

    for e in entries:
        if e.is_dir():
            single(e.path, output_path, sorting_mode)
