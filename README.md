# combine_jsonfiles_into_jsonlfile

processALLforNested.py:

Creates a json lines file which has one json object on every line.
Each json object maps to a json file in the folders and subfolders of the current directory.
Each json object has variables id, series and text.
The id and series variable of the json object is the name of the json file.
All of the json file's values are written into the text variable of the json object.
To sum up, all json files in the current directory are written as json objects into a single json lines file.
Thus, the json files are combined into one json lines file.

testForNested.py:
Includes some tests to ensure data integrity
