#dumpJSON.py 
# script to read the contents of a JSON file
# Author Andrew Beatty; Transcribed by Cathal Redmond 19 Mar 2025

import json
FILENAME="testdict.json"
sample= dict(name='fred', age=31, grades=[1,34,55])

def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

#test the function
writeDict(sample)