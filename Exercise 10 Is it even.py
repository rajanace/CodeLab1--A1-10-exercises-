"""
Exercise 10

Rajan ace R Tapiru
"""
def check_number(num):
    # Check if the number is divisible by 2
    if num % 2 == 0:
        return "This is an even number."  
    else:
        return "This is an odd number."  

def main():
    # Welcome message for the user
    print("Welcome to Even or Odd Checker!") # Ask the user to enter a number and convert it to an integer
    number = int(input("Please enter a number: "))
     # Call the check_number function and store the result
    result = check_number(number)
    print(result)
main()
