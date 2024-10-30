"""
exercise 5 dictionqary

Rajan ace Tapiru
"""
days_in_month = {
    1: 31,    # January has 31 days
    2: 28,    # February has 28 days (not accounting for leap years)
    3: 31,    # March has 31 days
    4: 30,    # April has 30 days
    5: 31,    # May has 31 days
    6: 30,    # June has 30 days
    7: 31,    # July has 31 days
    8: 31,    # August has 31 days
    9: 30,    # September has 30 days
    10: 31,   # October has 31 days
    11: 30,   # November has 30 days
    12: 31    # December has 31 days
}
# Get the month number from the user
month_number = int(input("Enter the month number (1-12): "))  

# Check if the month number is valid
if month_number in days_in_month: 
    days = days_in_month[month_number]  
    print(f"There are {days} days in month {month_number}.") 
else:
   # Error message for invalid input
    print("Invalid month number! Please enter a number between 1 and 12.")