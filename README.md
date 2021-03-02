# DIRtoPDF 1.2.0

A CLI tool written in Python to convert image folders to PDF files, using [PyMuPDF](https://github.com/pymupdf/PyMuPDF).

## Installation

You can install (and update) DIRtoPDF from [PyPI](https://pypi.org/project/DIRtoPDF):

```commandline
pip3 install DIRtoPDF -U
```

To use it:

```commandline
python3 -m DIRtoPDF
```

## Usage

DIRtoPDF offers two modes: "Single" and "Multiple".

### Single mode

The standard mode, converts each given directory that contains images into a PDF file.

```commandline
python3 -m DIRtoPDF /a/path /another/path ...
```

### Multiple mode

Useful for converting big batches of folders, this mode converts each image-containing folder within the given directories into a PDF file. To use it, add the ``-M``/``--multiple`` option to the command:

```commandline
python3 -m DIRtoPDF -M /a/path /another/path ...
```

### Output path

By standard, DIRtoPDF saves the resulting PDF files to the current directory. If you wish to specify an output path to save your PDF files to, add the ``-O``/``--output`` option to the command:

```commandline
python3 -m DIRtoPDF /a/path /another/path ... -O /an/output/path 
```

### Sorting modes

By default, DIRtoPDF sorts and saves the images in alphanumeric, ascending order (first special characters, then 0-9, then A-Z). If you wish for another way of sorting you can specify one by using the ``-S``/``--sort`` option:

```commandline
python3 -m DIRtoPDF /a/path /another/path ... -S MODE
```

To use a certain mode, enter the corresponding number from the following list as the MODE parameter:

1. Alphanumeric, ascending (A-Z) (_default_)
2. Alphanumeric, descending (Z-A)
3. Last time modified, oldest first
4. Last time modified, newest first
5. Time of creation / metadata change, oldest first
6. Time of creation / metadata change, newest first

### Shell

DIRtoPDF offers an interactive shell including all functions of the normal DIRtoPDF CLI tool.

It's designated use is accessing it through standalone clients for users that don't want to use the CLI tool. They'll be released on short notice.

Until then, you can already access the shell from the command line by entering the following:

```commandline
python3 -m DIRtoPDF --shell
```

## TODO

- Options to modify the order of images
- A standalone shell client
- A standalone GUI client

## Disclaimer

This tool uses the [PyMuPDF](https://github.com/pymupdf/PyMuPDF) library, which provides the core functionality of inserting images into PDF files. According to its licensing terms, this project is released under the AGPLv3 license (for more information, see LICENSE)