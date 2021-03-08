from abc import ABC, abstractmethod
import fitz
import os
import pathlib
import zipfile


class Converter(ABC):

    @property
    @abstractmethod
    def file_extension(self) -> str:
        pass

    @staticmethod
    def sorted_entries(entries, sorting_mode: int) -> list[os.DirEntry]:
        """Returns a list of directory entries sorted in a certain pattern.

        :param entries: An iterable of the directory entries that are to be sorted
        :type entries: Any
        :param sorting_mode: The indicator for the desired sorting mode
        :type sorting_mode: int
        :return: A new, sorted list of all directory entries
        :rtype: list[os.DirEntry]
        """

        res = []

        if sorting_mode == 1:
            res = sorted(entries, key=lambda x: x.name)
        elif sorting_mode == -1:
            res = sorted(entries, key=lambda x: x.name, reverse=True)
        elif sorting_mode == 2:
            res = sorted(entries, key=lambda x: x.stat.st_mtime_ns)
        elif sorting_mode == -2:
            res = sorted(entries, key=lambda x: x.stat.st_mtime_ns, reverse=True)
        elif sorting_mode == 3:
            res = sorted(entries, key=lambda x: x.stat.st_ctime_ns)
        elif sorting_mode == -3:
            res = sorted(entries, key=lambda x: x.stat.st_ctime_ns, reverse=True)

        return res

    def single(self, input_path: str, output_path=os.getcwd(), sorting_mode=1) -> None:
        """Converts a directory into a file.

        :param input_path: The path of the directory to be converted
        :type input_path: str
        :param output_path: The path to save the file to
        :type output_path: str
        :param sorting_mode: The indicator for the desired sorting mode
        :type sorting_mode: int
        """

        entries = list(filter(lambda x: x.is_file(), self.sorted_entries(os.scandir(input_path), sorting_mode)))

        if input_path[-1] in ('/', '\\'):
            input_path = input_path[:-1]

        if len(entries) > 0:
            doc_name = os.path.basename(input_path) + self.file_extension
            self.convert(entries, doc_name, output_path)
        else:
            print(f"\nskipping {os.path.basename(input_path)}, empty directory...")

    def batch(self, input_path: str, output_path=os.getcwd(), sorting_mode=1) -> None:
        """Converts each subdirectory of a directory into a file.

        :param input_path: The path of the directory whose subdirectories are to be converted
        :type input_path: str
        :param output_path: The path to save the files to
        :type output_path: str
        :param sorting_mode: The indicator for the desired sorting mode
        :type sorting_mode: int
        """

        directories = list(filter(lambda x: x.is_dir(), os.scandir(input_path)))

        for d in directories:
            self.single(d.path, output_path, sorting_mode)

    @abstractmethod
    def convert(self, entries: list[os.DirEntry], doc_name: str, output_path: str) -> None:
        """Hook method for the Converter methods. Each Converter subclass overwrites this method with the
        implementation of its format-specific conversion routine.

        :param entries: List of directory entries to be transferred to the output file
        :type entries: list[os.DirEntry]
        :param doc_name: Name for the output file
        :type doc_name: str
        :param output_path: Path to save the output file to
        :type output_path: str
        :return:
        """

        pass


class PDFConverter(Converter):

    @property
    def file_extension(self) -> str:
        return '.pdf'

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

    @property
    def file_extension(self) -> str:
        return '.cbz'

    def convert(self, entries: list, doc_name: str, output_path: str) -> None:
        with zipfile.ZipFile(os.path.join(output_path, doc_name), 'w', zipfile.ZIP_DEFLATED) as zf:
            for i, e in enumerate(entries):
                suffix = pathlib.Path(e.path).suffix
                zf.write(e.path, f"{i + 1}{suffix}", compress_type=zipfile.ZIP_DEFLATED)

        print(f"\n\"{doc_name}\" saved to {output_path}")


class ConverterFactory:

    @staticmethod
    def create(converter_type: str) -> Converter:
        return {
            'PDF': PDFConverter,
            'CBZ': CBZConverter
        }[converter_type]()
