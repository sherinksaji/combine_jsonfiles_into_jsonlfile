import json
import os


def process(currentJSON):

    # making the TextFile name
    currentJSONSplit = currentJSON.split("_")
    currentDNLowerCase = currentJSONSplit[0]
    currentDN = currentDNLowerCase.swapcase()
    currentTextFile = currentDN+" Sutta (Passim Format).txt"

    # making the id, series string to be written to the beginning of the text file
    # includes opening quotation mark to the text component
    idSeriesStr = '"id": "'+currentDN+'", "series": "'+currentDN + '", "text": "'

    # Open the JSON file and read its contents
    with open(currentJSON, 'rb') as f:
        contents = f.read()

    # set encoding
    encoding = "utf-8"
    print(encoding)

    # Load the JSON data using the detected encoding
    with open(currentJSON, encoding=encoding) as f:
        data = json.load(f)

    # Open a file for writing
    with open(currentTextFile, 'w', encoding=encoding) as f:

        f.write(idSeriesStr)

        # Access the values of the JSON file
        for i, value in enumerate(data.values()):

            f.write(value)
            # placing a comma after every JSON value except for the last one
            if i != len(data) - 1:
                f.write(",")

        f.write('"')


def get_json_files(root_folder):
    json_files = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.json'):
                filename.replace("\\", " /")
                json_files.append(os.path.join(dirpath, filename))
    return json_files


root_folder = '.'
json_file_names = get_json_files(root_folder)


for filename in json_file_names:
    print(filename)
    process(filename)
