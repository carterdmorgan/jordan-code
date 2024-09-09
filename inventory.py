import textwrap

class Order:
    def __init__(self, purchase = {}) -> None:
        # Unclear naming here. I would assume add_purchase would replace this,
        # not update this. Even renaming it to `purchases` would be clearer
        self.purchase = purchase

    def add_purchase(self, name, quantity):
        self.purchase[name] = quantity

# This class was pretty well done, just added some syntax tricks to make it 
# read cleaner
class Inventory:
    ALLOWED_ACTIONS = ['1', '2', '3', '4', '5']

    def __init__(self, items = {}) -> None: 
        # Providing items here as an optional parameter instead of always initializing
        # it to an empty dictionary is a good design choice, but you need to be
        # able to explain why. Why did you choose this?
        self.items = items
    
    def add_product(self, name: str, quantity: int):
        # The dictionary has a .get() method that lets you provide a default
        # value as the second parameter if it doesn't exist. Much cleaner this way.
        initial_quantity = self.items.get(name, 0)
        self.items[name] =  initial_quantity + quantity
        print(f'{name} quantity: {self.items[name]}\n')

    def remove_product(self, name: str, quantity: int):
        # The original else was redundant
        if name not in self.items or self.items[name] < quantity:
            # Raising a ValueError is probably the best move here, but you
            # don't handle the error anywhere else in your code. As it stands, 
            # your code will just break if someone attempts this. You need a 
            # try/except block in the main loop logic
            raise ValueError(f'Cannot remove {quantity} of {name}')
        
        self.items[name] -= quantity
        print(f'{name} quantity: {self.items[name]}\n')

    def check_stock(self, name: str):
        # Use the .get() method here too. Look how much cleaner it makes it.
        return self.items.get(name, 0)

    def process_order(self, order: Order):
        for key, value in order.purchase.items():
            self.remove_product(key, value)

def get_valid_product_quantity():
    while True:
        product_quantity = input('Please provide the product quantity\n')
        if product_quantity.isdigit() == False:
            print('Product quantity must be a valid number.\n')
        elif product_quantity.isdigit() == True:
            return int(product_quantity)
        
def handle_new_order():
    order = Order()
    while True:
        order_action = input('Please provide the name of a product you would like to order. When finished, enter BUY or CANCEL to complete.\n').lower()
        if order_action == 'buy':
            main_inventory.process_order(order)
            break
        elif order_action == 'cancel':
            break
        elif order_action not in ['buy', 'cancel']:
            # input validation for order_quantity 
            # Again, remember DRY
            order_quantity = get_valid_product_quantity()
            order.add_purchase(order_action, order_quantity)
            print(f'Added product: {order_action}, quantity: {order_quantity}')

def main():
    main_inventory = Inventory({'apple': 10, 'banana': 10, 'orange': 10})

    while True:
        # Instead of having big long strings here with \n characters, you can actually use
        # triple quotes and Python will format it exactly as you write it
        initial_prompt = """
            What would you like to do?
            1. Add Product
            2. Remove Product
            3. Check Stock
            4. Create Order
            5. Exit
        """
        # You need to make sure to use the textwrap.dedent() function to remove the
        # white space at the beginning. This triple quote stuff is more a "nice to have"
        # than something I would expect everyone to know how to do
        initial_prompt_formatted = textwrap.dedent(initial_prompt)
        user_action = input(initial_prompt_formatted)

        # input validation for user_action
        if user_action not in Inventory.ALLOWED_ACTIONS:
            print('Invalid Action\n')
        elif user_action == '1':
            product_name = input('Please provide the name of the product you would like to add\n').lower()
            # These nested loops are making it hard to read. Move them into their own functions
            product_quantity = get_valid_product_quantity()
            main_inventory.add_product(product_name, product_quantity)
        elif user_action == '2':
            product_name = input('Please provide the name of the product you would like to remove\n').lower()
            # input validation for product_quantity 
            # Keep in mind the DRY principle: Don't Repeat Yourself. If you find yourself copying and pasting
            # code, it should probably be its own function
            product_quantity = get_valid_product_quantity()
            main_inventory.remove_product(product_name, product_quantity)
        elif user_action == '3':
            product_name = input('Please provide the name of the product you would like to check\n').lower()
            print(f'Current {product_name} stock: {main_inventory.check_stock(product_name)}\n')
        elif user_action == '4':
            # allow user to create order
            # You're getting too deep in one method. Pay attention to how far you're indenting. A lot of
            # people believe you shouldn't indent more than twice in a method. That means if you have these loops
            # or branching paths, you should move them to their own method.
            handle_new_order()
        elif user_action == '5':
            break

    print('End of line')

main()




        

    