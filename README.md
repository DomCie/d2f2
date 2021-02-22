# DIRtoPDF 1.0.0

A CLI tool written in Python to convert image folders to PDF files, using [PyMuPDF](https://github.com/pymupdf/PyMuPDF).

## Installation

You can install DIRtoPDF from [PyPI](https://pypi.org) using the command line:

```commandline
pip3 install DIRtoPDF -U
```

To use it:

```commandline
python3 -m DIRtoPDF
```

## Usage

DIRtoPDF offers two modes: "Single" and "Multiple"

### Single mode

The standard mode, converts each given directory that contains images into a PDF file.

```commandline
python3 -m DIRtoPDF /a/path /another/path ...
```

### Multiple mode

Useful for converting big batches of folders, this mode converts each image-containing folder within the given directories into a PDF file. To use it, add the ``-M``/``--multiple`` option to the command:

```commandline
python3 -m DIRtoPDF -M /a/path /another/path ...

python3 -m DIRtoPDF --multiple /a/path /another/path ...
```

## Specify an output path

By standard, DIRtoPDF saves the resulting PDF files to the current directory. If you wish to specify a certain output path to save your files to, add the ``-O``/``--output`` option to the command:

```commandline
python3 -m DIRtoPDF /a/path /another/path ... -O /an/output/path 
```

## TODO

- A standalone shell client
- A standalone GUI client

## Disclaimer

This tool uses the [PyMuPDF](https://github.com/pymupdf/PyMuPDF) library, which provides the core functionality of inserting images into PDF files. According to its licensing terms, this project is released under the AGPLv3 license (for more information, see LICENSE)