# D2F2 2.0.0

D2F2 (formerly _DIRtoPDF_) is a tool written in Python to convert image folders into files.

## Installation

You can install (and update) D2F2 from [PyPI](https://pypi.org/project/D2F2) via the command line

```commandline
pip install D2F2 -U
```

or use one of the standalone versions (see below).

## Usage

### Operation modes

D2F2 offers two modes of operation: "single" and "batch".

#### Single mode

The standard mode, converts each given directory into a file.

```commandline
D2F2 /a/path /another/path ...
```

#### Batch mode

Useful for converting big batches of folders, this mode converts each subdirectory within the given directories into a file. To use it, add the ``-B``/``--batch`` option to the command:

```commandline
D2F2 -B /a/path /another/path ...
```

### Output format

By default, D2F2 saves files in the PDF format. If you want to use another supported format, use the ``-F``/``--format`` option:

```commandline
D2F2 /a/path ... -F FORMAT
```

Currently, there are 2 supported formats (with more to be added in the future). Use the appropriate format as the FORMAT parameter:

* [PDF] - Portable Document Format (_default_)
* [CBZ] - Comic Book Format, ZIP-compressed

### Output path

By standard, D2F2 saves files to the current directory. If you want another output path, use the ``-O``/``--output`` option:

```commandline
D2F2 /a/path ... -O /an/output/path 
```

### Sorting mode

By default, D2F2 sorts the images in alphanumeric, ascending order (A-Z). If you want to use another sorting mode you can specify one by using the ``-S``/``--sort`` option:

```commandline
D2F2 /a/path ... -S MODE
```

Currently, there are 6 sorting modes available. Use the corresponding number from the following list as the MODE parameter:

* [ 1] Alphanumeric, ascending (_default_)
* [-1] Alphanumeric, descending
* [ 2] Last time modified, oldest first
* [-2] Last time modified, newest first
* [ 3] Time of creation / metadata change, oldest first
* [-3] Time of creation / metadata change, newest first

## Shell

D2F2 offers an interactive shell including all functions of the normal D2F2 CLI tool.

Standalone versions for the shell are available for Windows and Linux (see [Releases](https://github.com/DomCie/D2F2/releases))

You can also start the shell from the command line:

```commandline
D2F2 --shell
```

## TODO

* More output formats (EPUB, MOBI)
* Custom order for images
* Modify names of output files
* Standalone GUI client

## Disclaimer

This tool uses the [PyMuPDF](https://github.com/pymupdf/PyMuPDF) library, which provides the core functionality of inserting images into PDF files. According to its licensing terms, this project is released under the AGPLv3 license (for more information, see LICENSE)