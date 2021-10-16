#!/usr/bin/env python
from objectionloltotxt import objectiontotxt
import argparse
import os
import sys


def main():
    commandline_interface = argparse.ArgumentParser(prog='objtotxt', description='Convert .objection files to txt')
    mutually_exclusive_arguments = commandline_interface.add_mutually_exclusive_group(required=True)
    mutually_exclusive_arguments.add_argument('--filename', metavar="file", type=str, nargs='+',
                                              help="Filename of the .objection file")
    mutually_exclusive_arguments.add_argument('-d', metavar="directory", type=str, nargs='+',
                                              help='convert the .objection files in a directory to readable text file')
    args = commandline_interface.parse_args()
    input_filename = args.filename
    input_directory = args.d

    if input_directory is not None: # if -d argument is used instead of --filename the code after the if condition is executed, since they are mutually exclusive
        for directory in input_directory:
            if str(directory) is not None and not os.path.isdir(str(directory)):
                print(f"{directory} directory doesn't exist")
                input_directory.remove(directory) 
                assert input_directory != (), "all the directories you provided are invalid"

        for folder in input_directory:
            list_of_file = os.listdir(folder)
            for file in list_of_file:
                full_path = os.path.join(folder, file)
                if file.endswith(".objection"):
                    objectiontotxt.convert_base64objection_to_readable_text_file(full_path)
                else:
                    print(f"please rename {full_path} to have .objection extension if the file is an objection file")


    else: 
        for file in input_filename:
            if not os.path.isfile(file):
                print("That file doesn't exist")
                sys.exit()
            elif file.endswith(".objection"):
                objectiontotxt.convert_base64objection_to_readable_text_file(file)
            else:
                print(f"please rename \"{file}\" to have .objection extension if the file is an objection file ")

if __name__ == "__main__":
    main()
