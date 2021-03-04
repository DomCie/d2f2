from DIRtoPDF.CONFIGURATIONS import *
import DIRtoPDF.convert as convert
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
        opts, args = getopt.getopt(argv[1:], 'HMS:O:', ['help', 'multiple', 'shell', 'sort=', 'output='])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)

    output_path = os.getcwd()
    sorting_mode = 1
    is_multiple = False

    for opt, par in opts:
        if opt in ('-H', '--help'):
            print(help_msg)
            sys.exit(0)
        elif opt in ('-M', '--multiple'):
            is_multiple = True
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
        elif opt in ('-O', '--output'):
            if os.path.exists(par):
                output_path = par
            elif par == '':
                print("error: no output path given", file=sys.stderr)
                sys.exit(2)
            else:
                print(f"error: output path {par} doesn't exist", file=sys.stderr)
                sys.exit(1)

    if len(args) == 0:
        print(help_msg)
        sys.exit(2)

    for arg in args:
        if os.path.exists(arg):
            if is_multiple:
                convert.multiple(arg, output_path, sorting_mode)
            else:
                convert.single(arg, output_path, sorting_mode)
        else:
            print(f"warning: skipping \"{arg}\", invalid path...")


if __name__ == "__main__":
    main(sys.argv)
