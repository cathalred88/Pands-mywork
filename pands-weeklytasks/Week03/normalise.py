# normalise.py
# used to strip any leading or trailing spaces from a test string, and converts all letters to lowercase.
# Author Cathal Redmond

entry = str(input('Please enter a string: '))
origLen = len(entry)

a = entry.lower()
b = a.lstrip("  ,. ")
normalised = b.rstrip(" ,. ")

newLen = len(normalised)

print("Normalised string :{}".format(normalised))
print("We reduced the input string from {} to {} charachters ".format(origLen,newLen))