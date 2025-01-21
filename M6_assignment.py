

class Item:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020", cart_items=None):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items or []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart nothing removed")

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                return
        print("Item not found in cart nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        if not len(self.cart_items):
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name} Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")


def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'q':
            break
        elif choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = int(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = Item(name, description, price, quantity)
            cart.add_item(item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter the item name to remove: ")
            cart.remove_item(Item(name=item_name))
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            item = Item(name=item_name, quantity=quantity)
            cart.modify_item(item)
        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print(f"Customer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")
    print_menu(cart)
