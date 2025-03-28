# readJSON.py 
# script to read the contents of a JSON file
# Author Andrew Beatty; Transcribed by Cathal Redmond 19 Mar 2025



import json
FILENAME ="testdict.json"
def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty dict
    # we can do this later
    with open(FILENAME) as f:
        return json.load(f)

# test the function
somedict = readDict()
print(somedict)