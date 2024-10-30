"""
exercise 4 advance

Rajan ace Tapiru
"""
# Ask the user for the capital of France
answer=input("What is the capital of France? ")
if answer.lower() == "paris":  
    print("Correct! The capital of France is Paris.")
else:
    print("Wrong! The capital of France is Paris.")  
    
capitals = {
    # countries and their capitals
    "France": "Paris",
    "Belgium": "Brussels",
    "Italy": "Rome",
    "Norway": "Oslo",
    "Portugal": "Lisbon",
    "Greece": "Athens",
    "Germany": "Berlin",
    "Sweden": "Stockholm",
    "Ukraine": "Kyiv",
    "Ireland":"Dublin",
}
# Loop through the capitals and quiz the user
for country, capital in capitals.items():
    answer=input(f"What is the capital of {country}? ")
    if answer.lower() == capital.lower(): 
        print("Correct!") 
    else:
        print(f"Wrong! The capital of {country} is {capital}.") 
print("Quiz completed!")
