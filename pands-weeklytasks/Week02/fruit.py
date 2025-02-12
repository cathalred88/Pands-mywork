# fruit.py
# This program introduced the f-string
# Author: functions lifted from w3 python page

fruit = input("Please enter your favourite fruit: ")
fruittxt = f"I love {fruit.upper()}"
print(fruittxt)

#i am trying to include the previous input in the prompt for this value.
price = int(input("How much is one "  + fruit +  "? "))
pricetxt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(pricetxt)