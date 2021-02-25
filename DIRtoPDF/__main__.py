import DIRtoPDF.convert as convert
import DIRtoPDF.shell as shell
import getopt
import os
import sys


def main(argv: list) -> None:
    help_msg = f"DIRtoPDF [OPTIONS] PATH [PATH...]\nConvert image folders to PDF files\n\nOPTIONS:\n-H, " \
               f"--help\t\t\t\t\tShow this help\n-M, --multiple\t\t\t\tConvert each folder within PATH to a PDF " \
               f"file\n-S, --shell\t\t\t\t\tOpen interactive shell\n-O, --output OUTPUT_PATH\tSave PDF files to " \
               f"OUTPUT_PATH instead of the current directory "
    try:
        opts, args = getopt.getopt(argv[1:], 'HMSO:', ['help', 'multiple', 'shell', 'output='])
    except getopt.GetoptError:
        print(help_msg)
        sys.exit(2)

    output_path = os.getcwd()
    is_multiple = False

    for opt, par in opts:
        if opt in ('-H', '--help'):
            print(help_msg)
            sys.exit(0)
        elif opt in ('-M', '--multiple'):
            is_multiple = True
        elif opt in ('-S', '--shell'):
            shell.start()
            sys.exit(0)
        elif opt in ('-O', '--output'):
            if os.path.exists(par):
                output_path = par
            else:
                print(f"error: output path {par} doesn't exist", file=sys.stderr)
                sys.exit(1)

    if len(args) == 0:
        print(help_msg)
        sys.exit(2)

    for arg in args:
        if os.path.exists(arg):
            if is_multiple:
                convert.multiple(arg, output_path)
            else:
                convert.single(arg, output_path)
        else:
            print(f"warning: skipping \"{arg}\", invalid path...")


if __name__ == "__main__":
    main(sys.argv)
