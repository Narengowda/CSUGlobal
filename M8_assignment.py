# Items to purchase class

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="Feb 8, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Error: Item can not be found in cart. nothing removed.")

    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            # compare lowercase as it helps to sanitize the input
            if item.item_name.lower() == item_to_modify.item_name.lower():
                # update whatever matches, if not ignore
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                return
        print("item not found in cart. no modification done.")

    def get_num_items_in_cart(self):
        # Lets use list comprehension instead of loops
        total_quantity = [item.item_quantity for item in self.cart_items]
        return sum(total_quantity)

    def get_cost_of_cart(self):
        # you can even do sum(iterator), instead of using list comprehension or for loop.
        # Shorter way to sum
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s shopping Cart - {self.current_date}")
        if not self.cart_items:
            print(">> SHOPPING CART IS EMPTY")
        else:
            total_items = self.get_num_items_in_cart()
            print(f"number of Items: {total_items}")
            for item in self.cart_items:
                # print individual costs
                # you could do that using [item.print_item_cost() for item in self.cart_items]
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: no proper description provided")




# Function to display menu
def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - add item to the cart")
        print("r - remove item from cart")
        print("c - change item quantity")
        print("i - output items' descriptions")
        print("o - output shopping cart")
        print("q - quit")
        option = input("choose an option:\n")

        # while comparing you can do lower() and compare or you can use 'or'
        # For eg: option == 'a' or option == 'A'
        #  or you can do option in ('a', 'A')
        if option.lower() == 'a': # step 8
            print("---- ADD AN ITEM TO CART -----")
            name = input("enter the Item name:\n")
            price = float(input("Enter the Item price:\n"))
            quantity = int(input("Enter the item quantities:\n"))
            new_item = ItemToPurchase(name, price, quantity)
            cart.add_item(new_item)
        elif option == 'r': # step 9
            print("-=---- REMOVE ITEM FROM CART -----")
            item_name = input("enter name of the item to remove:\n")
            cart.remove_item(item_name)
        elif option == 'c': # step 10
            print("------ CHANGE ITEM QUANTITY -------")
            item_name = input("enter the item name:\n")
            new_quantity = int(input("enter the new quantity:\n"))
            modified_item = ItemToPurchase(item_name, 0, new_quantity)
            cart.modify_item(modified_item)
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()
        elif option == 'q':
            break
        else:
            print("invalid option. please try again.")

# prog entry
if __name__ == "__main__":
    customer_name = input("enter customers name:\n")
    current_date = input("enter today's date:\n")
    print(f"customer name: {customer_name}")
    print(f"today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)