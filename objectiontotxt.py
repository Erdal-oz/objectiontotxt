import base64
import json
import os
import argparse
import sys

def base64_to_json(filename):
    """
    Opens the specified .objection or any base64 encoded file and converts it to prettyprint json. It will create the
    file to the directory of the file that is passed
    """
    with open(filename + "_converted.json", 'w') as output_file, open(filename, 'r') as input_file:
        base64_input = input_file.read()
        base64_decoded_input = base64.b64decode(base64_input).decode()
        json_input = json.loads(base64_decoded_input)
        json.dump(json_input, output_file, sort_keys=True, indent=0)
        output_file.close()
        input_file.close()


def convert_objection_json_to_readable_text_file(filename):
    """
    Opens the specified converted objection file and converts it to readable text file. It will create the file to
    the directory of the file that is passed
    """

    with open(filename + "_readable_file.txt", 'w') as readable_file_output, open(filename, 'r') as objection_json_file:
        objection_python_dict = json.loads(objection_json_file.read())
        for frame in objection_python_dict["frames"]:
            readable_file_output.write(frame["username"] + ": " + frame["text"] + "\n\n")
        readable_file_output.close()
        objection_json_file.close()
    


def convert_base64objection_to_readable_text_file(filename):
    """
    Combines the other functions
    """
    base64_to_json(filename)
    convert_objection_json_to_readable_text_file(filename + "_converted.json")


def main():
    commandline_interface = argparse.ArgumentParser(prog='objtotxt', description='Convert .objection files to txt')
    mutually_exclusive_arguments = commandline_interface.add_mutually_exclusive_group(required=True)
    mutually_exclusive_arguments.add_argument('--filename',metavar="file", type=str, nargs='+', help="Filename of the .objection file")
    mutually_exclusive_arguments.add_argument('-d', metavar="directory", type=str, help='convert the .objection files in a directory to readable text file')
    args = commandline_interface.parse_args()
    input_filename = args.filename
    input_directory = args.d
    if input_filename is not None:
        for file in input_filename:
            if not os.path.isfile(file):
                print("That file doesn't exist")
                sys.exit()
    
    
    if  input_directory is not None and not os.path.isdir(input_directory):
        print("that directory doesn't exist")
        sys.exit()
    if input_directory is not None:
        list_of_file = os.listdir(input_directory)
        for file in list_of_file:
            full_path = os.path.join(input_directory, file)
            convert_base64objection_to_readable_text_file(full_path)
    else:
        for file in input_filename:
            convert_base64objection_to_readable_text_file(file)


if __name__ == "__main__":
    main()
