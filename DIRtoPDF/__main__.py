#!/usr/bin/env python3

import convert
import getopt
import os
import sys


def main(argv: list) -> None:
    help_msg = f"DIRtoPDF [OPTIONS] PATH [PATH...]\nConvert image folders to PDF files\n\nOPTIONS:\n-H, " \
               f"--help\t\t\tShow this help\n-M, --multiple\t\t\tConvert each folder within PATH to a PDF file\n-O, " \
               f"--output OUTPUT_PATH\tSave PDF files to OUTPUT_PATH instead of the current directory"
    try:
        opts, args = getopt.getopt(argv[1:], 'HMO:', ['help', 'multiple', 'output='])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)

    if len(args) == 0:
        print(help_msg)
        sys.exit(2)

    output_path = os.getcwd()
    is_multiple = False

    for opt in opts:
        if opt[0] in ('-H', '--help'):
            print(help_msg)
            sys.exit(0)
        elif opt[0] in ('-M', '--multiple'):
            is_multiple = True
        elif opt[0] in ('-O', '--output'):
            if os.path.exists(opt[1]):
                output_path = opt[1]
            else:
                print(f"error: output path '{opt[1]}' doesn't exist", file=sys.stderr)
                sys.exit(1)

    for arg in args:
        if os.path.exists(arg):
            if is_multiple:
                convert.multiple(arg, output_path)
            else:
                convert.single(arg, output_path)
        else:
            print(f"Skipping \"{arg}\", invalid path...")


if __name__ == "__main__":
    main(sys.argv)
