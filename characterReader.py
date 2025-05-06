# characterReader.py
# Script to count the number of a certain character in a text file. 
# Author Cathal Redmond 20 March 2025
# References: str.count from https://docs.python.org/3/library/stdtypes.html#str.count

# Instructions: 
# The user is asked to enter the name of a file to be opened, and to enter a character (or string) to count the instances of that character within that file. 

# Assumptions: 
# This script will ask the user to enter a file name to be opened and read- no list of files will be available. File name will need to be known ny the user. 
# It assumed that the selected file will contain text / numbers only, and be saved as .txt format. special charachters within the files may break the coding. 
# Files to be analysed will be stored in the same directory as the script - no directory switch operations will be available. 
# The script will count the instances of the ntered character, and display the result as a message at the conclusion of the program. No record of the count/output will be saved etc. 

# references: 
# https://stackoverflow.com/questions/69319005/count-a-string-in-a-text-file-with-python 
# https://www.geeksforgeeks.org/python-os-path-exists-method/

# import modules
import os
import sys

# Define Functions
def readFileName(message = "please enter filename.txt: (or blank to quit) "):
    isexist = False
    enteringTextFile = True 
    textFile = sys.argv[1]
    while enteringTextFile: 
        while (isexist != True) :
            
            
            #try: 
                #textFile = str(input(message))
                # first we need to check if user response is empty, and break if true
                #if len(textFile) == 0: 
                    #enteringTextFile = False 
                    #break

                ## then we need to check if the file exists - returns true or false. 
                ## EDIT: i also need to control the files to only accept .txt files
                if (os.path.exists(textFile) == True):
                    isexist == True
                    print (f"{textFile} found in directory")
                    enteringTextFile = False
                    break 

                #elif isexist == False:
                        #print (f"{textFile} does not exist in directory")

            # While loop needs an alternative exit    
            #except ValueError: 
                #print("that was not an acceptable entry, ", end="")
                #break
    return textFile

# i will not perform error handling on character input
def readCharacter(message = "please enter the character to count: "):
    character = str(input(message))
    return character


## Main body of Program 

# Collect user inputs
textFile = str(readFileName())  # this also checks if the file is present in the folder
character = str(readCharacter()) # this assumes all strings are valid entrys

# Open file
with open(textFile, "r") as in_file:
    #Execute countng function
    characterCount = sum(line.count(character) for line in in_file)

# print the output
print(f"\nThe number of times \"{character}\" appears in \"{textFile}\" is {characterCount}\n\n")