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


root_folder = '.'
json_file_names = get_json_files(root_folder)


count = 0


jsonLTextls = []
# Open the JSONL file
with open("ANall.jsonl", encoding="utf-8") as f:
    for line in f:
        currentData = json.loads(line)
        currentText = currentData["text"]
        jsonLTextls.append(currentText)

modelTextls = []
for modelFile in json_file_names:
    modelText = ""
    with open(modelFile, encoding="utf-8") as f:
        modelData = json.load(f)
        # Access the values of the JSON file
        for i, value in enumerate(modelData.values()):
            modelText += value
            # placing a comma after every JSON value except for the last one
            if i != len(modelData) - 1:
                modelText += ","
    modelTextls.append(modelText)

print(len(modelTextls))
print(len(jsonLTextls))
print("Both lists lengths are equal?", len(modelTextls) == len(jsonLTextls))
print("Both sets are equal?", set(modelTextls) == set(jsonLTextls))

for i in range(len(modelTextls)):

    print("i is now ", i)
    print(jsonLTextls[i][0:30])
    print(
        "First test: is modelTextls[i] and jsonLTextls equal for i = ", i, " ?")
    print(modelTextls[i] == jsonLTextls[i])
    if (modelTextls[i] != jsonLTextls[i]):
        break
    print("\n")
    print("Second test: compare character sets")
    modelTextSet = set(modelTextls[i])
    jsonLTextSet = set(jsonLTextls[i])
    print("character set of modelTextSet i = ", i, " : ", modelTextSet)
    print("character set of jsonLTextSet i = ", i, " : ", jsonLTextSet)
    print("modelTextSet - jsonLTextSet : ",
          modelTextSet.difference(jsonLTextSet))
    print("jsonLTextSet - modelTextSet : ",
          jsonLTextSet.difference(modelTextSet))
    if (jsonLTextSet != modelTextSet):
        break
    count += 1
    print("\n")

print(count)

character_set_json = set()
for filename in json_file_names:
    with open(filename, 'r', encoding="utf-8") as f:
        json_data = json.load(f)

    json_string = json.dumps(json_data, ensure_ascii=False)
    character_set_json.update(json_string)


# Open the JSONL file and read each line
with open("ANall.jsonl", 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Collect all unique characters in the file
character_set_jsonl = set()
for line in lines:
    data = json.loads(line)
    text = data['text']
    character_set_jsonl.update(text)


print(character_set_json)
print(character_set_jsonl)

print(character_set_jsonl == character_set_json)

print(character_set_json.difference(character_set_jsonl))
print(character_set_jsonl.difference(character_set_json))

print("ANall.jsonl" in json_file_names)
