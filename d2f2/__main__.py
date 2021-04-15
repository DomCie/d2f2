from d2f2.convert import *

import d2f2.shell as shell
import getopt
import os
import sys


def main() -> int:
    argv = sys.argv

    help_msg = f"{argv[0]} [OPTIONS] PATH [PATH...]\nConvert image folders into files\n\nOPTIONS:\n-H, " \
               f"--help\t\t\t\tShow this help\n-B, --batch\t\t\t\tConvert each subfolder of PATH to a " \
               f"file\n-F, --format FORMAT\t\t\tSpecify an output format\n\t\t\t\t\tAVAILABLE FORMATS:\t[PDF] " \
               f"Portable Document Format (default)\n\t\t\t\t\t\t\t\t[CBZ] Comic Book Format, " \
               f"ZIP-compressed\n--shell\t\t\t\t\tOpen interactive shell\n-S, --sort MODE\t\t\t\tSpecify a sorting " \
               f"mode\n\t\t\t\t\tAVAILABLE MODES:\t[ 1] A-Z (default)\n\t\t\t\t\t\t\t\t[-1] Z-A\n\t\t\t\t\t\t\t\t" \
               f"[ 2] Last time modified, oldest first\n\t\t\t\t\t\t\t\t[-2] Last time modified, " \
               f"newest first\n\t\t\t\t\t\t\t\t[ 3] Time of creation / metadata change, " \
               f"oldest first\n\t\t\t\t\t\t\t\t[-3] Time of creation / metadata change, newest first\n-O, --output " \
               f"OUTPUT_PATH\t\tSave files to OUTPUT_PATH (default: current directory)"
    try:
        opts, args = getopt.getopt(argv[1:], 'BF:HO:S:', ['batch', 'format=', 'help', 'output=', 'shell', 'sort='])
    except getopt.GetoptError:
        print(help_msg)
        return 2

    converter = None
    is_batch = False
    output_path = os.getcwd()
    sorting_mode = 1

    for opt, par in opts:
        if opt in ('-B', '--batch'):
            is_batch = True
        elif opt in ('-F', '--format'):
            if par in ('PDF', 'CBZ'):
                converter = ConverterFactory.create(par)
            elif par == '':
                print("error: no output format given", file=sys.stderr)
                return 2
            else:
                print(f"error: {par} isn't a valid output format", file=sys.stderr)
                return 2
        elif opt in ('-H', '--help'):
            print(help_msg)
            return 0
        elif opt in ('-O', '--output'):
            if os.path.exists(par):
                output_path = par
            elif par == '':
                print("error: no output path given", file=sys.stderr)
                return 2
            else:
                print(f"error: {par} isn't a valid output path", file=sys.stderr)
                return 1
        elif opt == '--shell':
            shell.start()
            return 0
        elif opt in ('-S', '--sort'):
            if par in ('1', '-1', '2', '-2', '3', '-3'):
                sorting_mode = int(par)
            elif par == '':
                print("error: no sorting mode given", file=sys.stderr)
                return 2
            else:
                print(f"error: {par} isn't a valid sorting mode", file=sys.stderr)
                return 1

    if len(args) == 0:
        print(help_msg)
        return 2

    if converter is None:
        converter = ConverterFactory.create('PDF')

    for arg in args:
        if os.path.exists(arg):
            if is_batch:
                converter.batch(arg, output_path, sorting_mode)
            else:
                converter.single(arg, output_path, sorting_mode)
        else:
            print(f"warning: skipping \"{arg}\", invalid path...")

    return 0


if __name__ == "__main__":
    sys.exit(main())
