"""
exercise 8

Rajan ace Tapiru
"""
# list of name
names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Define the name we are searching
search_name =input("\nWhat name do you want to search? ")

if search_name in names: # Check if the searched name is in the list of names
    print(f"{search_name} was found in the list!")# If found, notify the user
else:
    print(f"{search_name} was not found in the list.")# If not found, notify the user
    