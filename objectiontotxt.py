import base64
import json
import os


def base64_to_json(filename):
    """
    Opens the specified .objection or any base64 encoded file and converts it to prettyprint json. It will create the
    file to the directory of the file that is passed
    """
    if filename is None:
        filename = input("please enter the file name(for base64-json conversion): ")

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
    if filename is None:
        filename = input("please enter the file name(for input to readable text file): ")

    with open(filename.split(".", 1)[0] + "_readable_file.txt", 'w') as readable_file_output, open(filename, 'r') as objection_json_file:
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
    try:
        the_file_to_be_converted = input("please enter the objection file you want to convert to readable text file: ")
        assert os.path.isfile(the_file_to_be_converted)
    except AssertionError:
        print("The input needs to be a file")
        main()
    convert_base64objection_to_readable_text_file(the_file_to_be_converted)


if __name__ == "__main__":
    main()
