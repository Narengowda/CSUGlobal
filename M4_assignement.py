"""
Step 1: Build the ItemToPurchase class with the following specifications:

Attributes
item_name (string)
item_price (float)
item_quantity (int)
Default constructor
Initializes item's name = "none", item's price = 0, item's quantity = 0
Method
print_item_cost()
Example of print_item_cost() output:
Bottled Water 10 @ $1 = $10


Step 2: In the main section of your code, prompt the user for two items and create two objects of the ItemToPurchase class.

Example:

Item 1

Enter the item name:

Chocolate Chips

Enter the item price:

3

Enter the item quantity:

1

Item 2

Enter the item name:

Bottled Water

Enter the item price:

1

Enter the item quantity:

10


Step 3: Add the costs of the two items together and output the total cost.

Example:

TOTAL COST

Chocolate Chips 1 @ $3 = $3

Bottled Water 10 @ $1 = $10

Total: $13
"""

class ItemToPurchase:
    def __init__(self, item_name=None, item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(str(self.item_name) + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(self.item_price * self.item_quantity))


if __name__ == "__main__":
    print("----------Item 1 ----------")
    item_one_name = input("Enter the item name:\n")
    item_one_price = float(input("Enter the item price:\n"))
    item_one_quantity = int(input("Enter the item quantity:\n"))
    item_one = ItemToPurchase(item_one_name, item_one_price, item_one_quantity)

    print("------- Item two -------")
    item_two_name = input("Enter the item name:\n")
    item_two_price = float(input("Enter the item price:\n"))
    item_two_quantity = int(input("Enter the item quantity:\n"))
    item_two = ItemToPurchase(item_two_name, item_two_price, item_two_quantity)

    print("-------> TOTAL COST is <--------")
    item_one.print_item_cost()
    item_two.print_item_cost()

    total = (item_one_price * item_one_quantity) + (item_two_price * item_two_quantity)
    print(f"Total: $ {str(total)}")