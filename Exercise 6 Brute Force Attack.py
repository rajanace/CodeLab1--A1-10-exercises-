"""
exercise 6 

Rajan ace Tapiru
"""
# Set the correct password
correct_password = "12345"
user_input= ""

# Start a loop that continues until the correct password is entered
while user_input != correct_password: 
    user_input = input("Please enter the password: ")# Prompt the user to enter the password
    if user_input == correct_password:
        print("Access granted!")
    else:
        print("Incorrect password. Please try again.")# If incorrect, prompt to try again