import DIRtoPDF.convert as convert
import getopt
import os
import sys


def start():
    print("DIRtoPDF interactive shell v1.1.0\nPlease enter a command, \"help\" for more info or \"exit\" to leave\n")

    while True:
        argv = parse_args('--' + input('> '))
        help_msg = "help\t\t\t\t\t\tShow this help.\n" \
                   "single DIR [DIR...]\t\t\tConvert each given directory into a PDF file\n" \
                   "multiple DIR [DIR...]\t\tConvert each directory WITHIN each given directory into a PDF file\n" \
                   "exit\t\t\t\t\t\tClose this programme\n"
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
                    print("error: you must enter a valid command!\n")

            if mode_selected:
                if len(args) > 0:
                    output_path = input("Enter an output path (or nothing to save to the current directory): ")
                    output_path_given = False

                    while not output_path_given:
                        if output_path == '':
                            output_path = os.getcwd()
                        elif os.path.exists(output_path):
                            for arg in args:
                                if os.path.exists(arg):
                                    if is_mode_multiple:
                                        convert.multiple(arg, output_path)
                                    else:
                                        convert.single(arg, output_path)
                                else:
                                    print(f"warning: skipping \"{arg}\", invalid path...")
                            output_path_given = True
                        else:
                            output_path = input("Invalid path, try again: ")
                else:
                    print("error: you need to enter at least one path!\n")
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

    args_lst.append(''.join(current_word))
    return args_lst


if __name__ == '__main__':
    start()
