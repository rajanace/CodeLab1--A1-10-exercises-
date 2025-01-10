class Item:
    def __init__(self, name, price, category, stock):
        """Initialize an item with its name, price, category, and stock quantity."""
        # Item has a name, price in pesos, category, and how many are available
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def dispense(self):
        """Dispense the item if it is in stock."""
        # If we have the item, reduce stock by 1 and return True
        if self.stock > 0:
            self.stock -= 1
            return True
        return False

# Define the VendingMachine class
class VendingMachine:
    def __init__(self):
        """Initialize the vending machine with an empty list of items and categories."""
        # The machine has items, categories, and suggestions for extra stuff to buy
        self.items = []
        self.categories = {}
        self.suggestions = {
            "Coca Cola": "Would you like some chips with your drink?",
            "Pepsi": "Would you like some chips with your drink?",
            "Fanta": "Would you like some chips with your drink?",
            "Nestea": "Would you like a cookie to pair with your tea?",
            "Mountain Dew": "How about a snack to go with your drink?",
            "Water": "Stay hydrated! Would you like some fruit to go with it?",
            "Chips": "How about a drink to go with your chips?"
        }

    def add_item(self, item):
        """Add an item to the vending machine and categorize it."""
        # Add item to the machine and organize it by category
        self.items.append(item)
        if item.category not in self.categories:
            self.categories[item.category] = []
        self.categories[item.category].append(item)

    def display_menu(self):
        """Display the menu of items in the vending machine."""
        # Show all items with their prices and how many are left
        print("\nWelcome to the Vending Machine! Here is the menu:\n")
        for idx, item in enumerate(self.items):
            print(f"{idx + 1}. {item.name} - ₱{item.price:.2f} (Stock: {item.stock})")

    def display_categories(self):
        """Display available categories in the vending machine."""
        # Show the types of items available, like drinks or snacks
        print("\nAvailable categories:")
        for idx, category in enumerate(self.categories.keys()):
            print(f"{idx + 1}. {category}")

    def get_item(self, item_code):
        """Retrieve an item based on its code."""
        # Find the item by its number
        if 0 <= item_code < len(self.items):
            return self.items[item_code]
        return None

    def suggest_purchase(self, item_name):
        """Provide a suggestion for an additional purchase based on the selected item."""
        # Suggest something that goes well with the chosen item
        return self.suggestions.get(item_name, None)

# Main program logic
def main():
    # Create vending machine instance
    machine = VendingMachine()

    # Add items to the vending machine
    # Adding drinks with their prices in pesos and initial stock
    machine.add_item(Item("Coca Cola", 75.00, "Cold Drinks", 10))
    machine.add_item(Item("Pepsi", 75.00, "Cold Drinks", 8))
    machine.add_item(Item("Fanta", 75.00, "Cold Drinks", 10))
    machine.add_item(Item("Water", 50.00, "Cold Drinks", 20))
    machine.add_item(Item("Sprite", 75.00, "Cold Drinks", 10))
    machine.add_item(Item("7Up", 75.00, "Cold Drinks", 8))
    machine.add_item(Item("RC Cola", 65.00, "Cold Drinks", 7))
    machine.add_item(Item("Miranda", 75.00, "Cold Drinks", 6))
    machine.add_item(Item("Nestea", 85.00, "Cold Drinks", 5))
    machine.add_item(Item("Mountain Dew", 85.00, "Cold Drinks", 10))

    # Adding chips with their prices in pesos and initial stock
    machine.add_item(Item("Cracklings", 20.00, "Chips", 15))
    machine.add_item(Item("Chippy", 15.00, "Chips", 20))
    machine.add_item(Item("Piattos", 25.00, "Chips", 10))
    machine.add_item(Item("Moby", 15.00, "Chips", 18))
    machine.add_item(Item("Cheese It", 30.00, "Chips", 12))
    machine.add_item(Item("Tortillos", 20.00, "Chips", 15))
    machine.add_item(Item("Nova", 25.00, "Chips", 10))
    machine.add_item(Item("Clover", 20.00, "Chips", 12))

    while True:
        # Display menu
        machine.display_menu()

        # Get user choice
        try:
            # Ask the user to pick an item or exit
            choice = int(input("\nEnter the item number to purchase or 0 to exit: ")) - 1
        except ValueError:
            # Tell the user if they entered something that's not a number
            print("Invalid input. Please enter a number.")
            continue

        if choice == -1:
            # Exit the program
            print("Thank you for using the vending machine. Goodbye!")
            break

        # Get item
        item = machine.get_item(choice)
        if item is None:
            # Tell the user if they picked a wrong number
            print("Invalid selection. Please try again.")
            continue

        if item.stock <= 0:
            # Tell the user if the item is out of stock
            print(f"Sorry, {item.name} is out of stock.")
            continue

        # Handle payment
        try:
            # Ask for money and check if it's enough
            money_inserted = float(input(f"Please insert ₱{item.price:.2f}: "))
        except ValueError:
            # Tell the user if they entered something that's not a number
            print("Invalid input. Please enter a valid amount.")
            continue

        if money_inserted < item.price:
            # Return the money if it's not enough
            print(f"Insufficient funds. ₱{money_inserted:.2f} returned.")
            continue

        # Dispense item
        if item.dispense():
            # Give the item and return change if any
            change = money_inserted - item.price
            print(f"Dispensing {item.name}. Enjoy your purchase!")
            print(f"Change returned: ₱{change:.2f}")

            # Suggest an additional purchase
            suggestion = machine.suggest_purchase(item.name)
            if suggestion:
                # Show the suggestion to the user
                print(suggestion)
        else:
            # Tell the user if something went wrong with dispensing
            print(f"Unable to dispense {item.name}. Please try again.")

if __name__ == "__main__":
    main()
