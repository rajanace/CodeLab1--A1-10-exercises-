"""
exercise 3 advance

Rajan ace Tapiru
"""
name = input("Enter your name: ")  # Prompt the user to enter their name
hometown = input("Enter your hometown: ") # Prompt the user to enter their hometown
age = int(input("Enter your age: ")) # Prompt the user to enter their age

# Print the collected information: name, hometown, and age
print(name,hometown,age)

if age is not None:  
    # If age is valid (not None), print the information again
    print(name, hometown, age)
else: 
    # If age is None, print an error message
    print("Your answer is not valid")