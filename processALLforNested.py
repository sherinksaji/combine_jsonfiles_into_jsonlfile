import json
import os


def get_json_files(root_folder):
    json_files = []
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.json'):
                filename.replace("\\", " /")
                json_files.append(os.path.join(dirpath, filename))
    return json_files


def process(currentJSON):

    # get current DN
    jsonNameSplit = currentJSON.split("_")
    jsonNameFirstPart = jsonNameSplit[0]

    jsonNameFirstPartCapitalised = jsonNameFirstPart.swapcase()

    jsonNameFirstPartCapitalisedSplit = jsonNameFirstPartCapitalised.split(
        "\\")
    # for creating a directory later on
    if (len(jsonNameFirstPartCapitalisedSplit) == 4):

        currentDN = jsonNameFirstPartCapitalisedSplit[3]

    else:

        currentDN = jsonNameFirstPartCapitalisedSplit[2]

    # Open the JSON file and read its contents
    with open(currentJSON, 'rb') as f:
        contents = f.read()

    # set encoding
    encoding = "utf-8"

    text = ""

    # Load the JSON data using the detected encoding
    with open(currentJSON, encoding=encoding) as f:
        data = json.load(f)

        # Access the values of the JSON file
        for i, value in enumerate(data.values()):

            text += value
            # placing a comma after every JSON value except for the last one
            if i != len(data) - 1:
                text += ","

    json_object = {
        "id": currentDN,
        "series": currentDN,
        "text": text
    }

    return json_object


root_folder = '.'
json_file_names = get_json_files(root_folder)

# Open a file for writing with UTF-8 encoding
with open("ANall.jsonl", "w", encoding="utf-8") as file:
    for filename in json_file_names:
        print(filename)
        json_object = process(filename)
        json_str = json.dumps(json_object, ensure_ascii=False)
        file.write(json_str + "\n")
print(len(json_file_names))
