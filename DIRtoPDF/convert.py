from abc import ABC, abstractmethod
import fitz
import os
import pathlib
import zipfile


class Converter(ABC):

    @abstractmethod
    def __init__(self):
        self.file_extension = None

    @staticmethod
    def __sorted_entries(entries, sorting_mode: int) -> list[os.DirEntry]:
        res = []

        if sorting_mode == 1:
            res = sorted(entries, key=lambda x: x.name)
        elif sorting_mode == 2:
            res = sorted(entries, key=lambda x: x.name, reverse=True)
        elif sorting_mode == 3:
            res = sorted(entries, key=lambda x: x.stat.st_mtime_ns)
        elif sorting_mode == 4:
            res = sorted(entries, key=lambda x: x.stat.st_mtime_ns, reverse=True)
        elif sorting_mode == 5:
            res = sorted(entries, key=lambda x: x.stat.st_ctime_ns)
        elif sorting_mode == 6:
            res = sorted(entries, key=lambda x: x.stat.st_ctime_ns, reverse=True)

        return res

    def single(self, input_path: str, output_path: str, sorting_mode: int) -> None:
        entries = list(filter(lambda x: x.is_file(), self.__sorted_entries(os.scandir(input_path), sorting_mode)))

        if input_path[-1] in ('/', '\\'):
            input_path = input_path[:-1]

        if len(entries) > 0:
            doc_name = os.path.basename(input_path) + self.file_extension
            self.convert(entries, doc_name, output_path)
        else:
            print(f"\nskipping {os.path.basename(input_path)}, empty directory...")

    def multiple(self, input_path: str, output_path: str, sorting_mode: int) -> None:
        directories = list(filter(lambda x: x.is_dir(), os.scandir(input_path)))

        for d in directories:
            self.single(d.path, output_path, sorting_mode)

    @abstractmethod
    def convert(self, entries: list, doc_name: str, output_path: str) -> None:
        pass


class PDFConverter(Converter):

    def __init__(self):
        super().__init__()
        self.file_extension = '.pdf'

    def convert(self, entries: list, doc_name: str, output_path: str) -> None:
        with fitz.open() as doc:
            for e in entries:
                with fitz.open(e.path) as img:
                    rect = img[0].rect
                    img_as_pdf = img.convertToPDF()
                with fitz.open('pdf', img_as_pdf) as page:
                    doc.newPage(width=rect.width, height=rect.height).showPDFpage(rect, page, 0)

            doc.save(os.path.join(output_path, doc_name))

        print(f"\n\"{doc_name}\" saved to {output_path}")


class CBZConverter(Converter):

    def __init__(self):
        super().__init__()
        self.file_extension = '.cbz'

    def convert(self, entries: list, doc_name: str, output_path: str) -> None:
        with zipfile.ZipFile(os.path.join(output_path, doc_name), 'w', zipfile.ZIP_DEFLATED) as zf:
            for i, e in enumerate(entries):
                suffix = pathlib.Path(e.path).suffix
                zf.write(e.path, f"{i + 1}{suffix}", compress_type=zipfile.ZIP_DEFLATED)

        print(f"\n\"{doc_name}\" saved to {output_path}")


class EPUBConverter(Converter):

    def __init__(self):
        super().__init__()
        self.file_extension = '.epub'

    def convert(self, entries: list, doc_name: str, output_path: str) -> None:
        pass


class MOBIConverter(Converter):

    def __init__(self):
        super().__init__()
        self.file_extension = '.mobi'

    def convert(self, entries: list, doc_name: str, output_path: str) -> None:
        pass


class ConverterFactory:

    @staticmethod
    def get(converter_type: str) -> Converter:
        converter_dct = {
            'PDF': PDFConverter,
            'CBZ': CBZConverter
        }

        return converter_dct[converter_type]()
