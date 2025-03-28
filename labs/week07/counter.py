# count.py
# counts the number of charachters in a text file
# Author: Andrew Beatty; Transcribed by Cathal Redmond 19 Mar 2025 

FILENAME = "count.txt"
def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running
        # ie 0 previous runs
        print ("count.txt file does not exist, it will be be created now")
        return 0

def writeNumber(number):
    with open(FILENAME, "wt") as f:
    # write takes a string so we need to convert
        f.write(str(number))

#main

num = readNumber()
num += 1
print (f"we have run this program {num} times") 
writeNumber(num)