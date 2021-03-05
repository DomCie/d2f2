from DIRtoPDF.CONFIGURATIONS import *
from DIRtoPDF.convert import *

import DIRtoPDF.shell as shell
import getopt
import os
import sys


def main(argv: list) -> None:
    help_msg = f"{MODULE_NAME} [OPTIONS] PATH [PATH...]\nConvert image folders to PDF files\n\nOPTIONS:\n-H, " \
               f"--help\t\t\t\tShow this help\n-M, --multiple\t\t\t\tConvert each folder within PATH to a PDF " \
               f"file\n--shell\t\t\t\t\tOpen interactive shell\n-S, --sort MODE\t\t\t\tSpecify a sorting " \
               f"mode\n\t\t\t\t\tAVAILABLE MODES: [1] A-Z (default)\n\t\t\t\t\t\t\t [2] Z-A\n\t\t\t\t\t\t\t " \
               f"[3] Last time modified, oldest first\n\t\t\t\t\t\t\t [4] Last time modified, " \
               f"newest first\n\t\t\t\t\t\t\t [5] Time of creation / metatime change, " \
               f"oldest first\n\t\t\t\t\t\t\t [6] Time of creation / metatime change, newest first\n-O, " \
               f"--output OUTPUT_PATH\t\tSave PDF files to OUTPUT_PATH (default: current directory)"
    try:
        opts, args = getopt.getopt(argv[1:], 'F:HMO:S:', ['format=', 'help', 'multiple', 'output=', 'shell', 'sort='])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)

    converter = None
    is_multiple = False
    output_path = os.getcwd()
    sorting_mode = 1

    for opt, par in opts:
        if opt in ('-F', '--format'):
            if par in ('PDF', 'CBZ'):
                converter = ConverterFactory.get(par)
            elif par == '':
                print("error: no output format given", file=sys.stderr)
                sys.exit(2)
            else:
                print(f"error: {par} isn't a valid output format", file=sys.stderr)
                sys.exit(2)
        elif opt in ('-H', '--help'):
            print(help_msg)
            sys.exit(0)
        elif opt in ('-M', '--multiple'):
            is_multiple = True
        elif opt in ('-O', '--output'):
            if os.path.exists(par):
                output_path = par
            elif par == '':
                print("error: no output path given", file=sys.stderr)
                sys.exit(2)
            else:
                print(f"error: {par} isn't a valid output path", file=sys.stderr)
                sys.exit(1)
        elif opt == '--shell':
            shell.start()
            sys.exit(0)
        elif opt in ('-S', '--sort'):
            if par in ('1', '2', '3', '4', '5', '6'):
                sorting_mode = int(par)
            elif par == '':
                print("error: no sorting mode given", file=sys.stderr)
                sys.exit(2)
            else:
                print(f"error: {par} isn't a valid sorting mode", file=sys.stderr)
                sys.exit(1)

    if len(args) == 0:
        print(help_msg)
        sys.exit(2)

    if converter is None:
        converter = ConverterFactory.get('PDF')

    for arg in args:
        if os.path.exists(arg):
            if is_multiple:
                converter.multiple(arg, output_path, sorting_mode)
            else:
                converter.single(arg, output_path, sorting_mode)
        else:
            print(f"warning: skipping \"{arg}\", invalid path...")


if __name__ == "__main__":
    main(sys.argv)
