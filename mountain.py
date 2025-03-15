# mountain.py 
# fills dictionary items form user inputs   
# code from https://nidhiashtikar.medium.com/python-day-22-using-a-while-loop-with-lists-and-dictionaries-010e742e56db


# Empty dictionary to store responses
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Ask if another user wants to respond
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete, display the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

print(responses)