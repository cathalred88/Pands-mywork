# testfileentry.py
# scrip to test the file name entry code

#import os & JSON modules
import os

def readFileName(message = "please enter filename.txt: (or blank to quit) "):
    isexist = False
    enteringTextFile = True 
    while enteringTextFile: 
        while (isexist != True) :
            try: 
                textFile = str(input(message))
                # check if response is empty, break if true
                if len(textFile) == 0: 
                    enteringTextFile = False 
                    break

                ## check if the file exists - returns true of false
                if (os.path.exists(textFile) == True):
                    isexist == True
                    print (f"{textFile} found in directory")
                    enteringTextFile = False
                    break 

                elif isexist == False:
                        print (f"{textFile} does not exist in directory")

            # While loop needs an alternative exit    
            except ValueError: 
                print("that was not an acceptable entry, ", end="")
                break
    return textFile
                
            

textFile = str(readFileName())
print (textFile)