from DIRtoPDF.CONFIGURATIONS import *
import DIRtoPDF.convert as convert
import getopt
import os
import sys


def start() -> None:
    print(f"{MODULE_NAME} (Shell) v{VERSION}\nPlease enter a command, \"help\" for more info or \"exit\" to leave")

    while True:
        argv = parse_args('--' + input('\n> '))
        help_msg = "\nhelp\t\t\t\t\t\tShow this help.\n" \
                   "single DIR [DIR...]\t\t\tConvert each given directory into a PDF file\n" \
                   "multiple DIR [DIR...]\t\tConvert each directory WITHIN each given directory into a PDF file\n" \
                   "exit\t\t\t\t\t\tClose this programme"
        mode_selected = False
        is_mode_multiple = False

        try:
            opts, args = getopt.getopt(argv, '', ['exit', 'help', 'multiple', 'single'])

            for opt, par in opts:
                if opt == '--exit':
                    sys.exit(0)
                elif opt == '--help':
                    print(help_msg)
                elif opt == '--multiple':
                    mode_selected = True
                    is_mode_multiple = True
                elif opt == '--single':
                    mode_selected = True
                else:
                    print("error: invalid command\n")

            if mode_selected:
                if len(args) > 0:
                    output_path = input("\nEnter an output path (or nothing to save to the current directory): ")
                    output_path_given = False

                    while not output_path_given:
                        if output_path == '':
                            output_path = os.getcwd()
                        elif os.path.exists(output_path):
                            sorting_mode = input("\nAVAILABLE SORTING MODES:\n[1] A-Z (default)\n[2] Z-A\n[3] Last "
                                                 "time modified, oldest first\n[4] Last time modified, newest first\n["
                                                 "5] Time of creation / metadata change, oldest first\n[6] Time of "
                                                 "creation / metadata change, newest first\n\nEnter the number "
                                                 "associated with your preferred sorting mode (or "
                                                 "nothing to sort from A to Z): ")
                            sorting_mode_given = False

                            while not sorting_mode_given:
                                if sorting_mode == '':
                                    sorting_mode = '1'
                                elif sorting_mode in ('1', '2', '3', '4', '5', '6'):
                                    for arg in args:
                                        if os.path.exists(arg):
                                            if is_mode_multiple:
                                                convert.multiple(arg, output_path, int(sorting_mode))
                                            else:
                                                convert.single(arg, output_path, int(sorting_mode))
                                        else:
                                            print(f"\nwarning: skipping \"{arg}\", invalid path...")
                                    output_path_given = True
                                    sorting_mode_given = True
                                else:
                                    sorting_mode = input("Invalid sorting mode, try again: ")
                        else:
                            output_path = input("Invalid output path, try again: ")
                else:
                    print("\nerror: you need to enter at least one path!")
        except getopt.GetoptError:
            print(help_msg)


def parse_args(args_str: str) -> list:
    args_lst = []
    current_word = []
    enquote = False

    for c in args_str:
        if c == ' ' and not enquote:
            args_lst.append(''.join(current_word))
            current_word = []
        elif c == '\"':
            if enquote:
                enquote = False
            else:
                enquote = True
        else:
            current_word.append(c)

    if current_word:
        args_lst.append(''.join(current_word))

    return args_lst


if __name__ == '__main__':
    start()
