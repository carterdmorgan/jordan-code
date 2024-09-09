class Order:
    def __init__(self, purchase = {}) -> None:
        self.purchase = purchase

    def add_purchase(self, name, quantity):
        self.purchase[name] = quantity


class Inventory:
    ALLOWED_ACTIONS = ['1', '2', '3', '4', '5']

    def __init__(self, items = {}) -> None:
        self.items = items
    
    def add_product(self, name: str, quantity: int):
        if name in self.items.keys():
            self.items[name] += quantity
        elif name not in self.items.keys():
            self.items[name] = quantity
        print(f'{name} quantity: {self.items[name]}\n')

    def remove_product(self, name: str, quantity: int):
        if name not in self.items.keys() or self.items[name] < quantity:
            raise ValueError()
        elif name in self.items.keys():
            self.items[name] -= quantity
        print(f'{name} quantity: {self.items[name]}\n')

    def check_stock(self, name: str):
        if name not in self.items.keys():
            return 0
        elif name in self.items.keys():
           return self.items[name]

    def process_order(self, order: Order):
        for key, value in order.purchase.items():
            self.remove_product(key, value)

            
def main():
    main_inventory = Inventory({'apple': 10, 'banana': 10, 'orange': 10})

    while True:
        user_action = input('What would you like to do?\n1. Add Product\n2. Remove Product\n3. Check Stock\n4. Create Order\n5. Exit\n')

        # input validation for user_action
        if user_action not in Inventory.ALLOWED_ACTIONS:
            print('Invalid Action\n')
        elif user_action == '1':
            product_name = input('Please provide the name of the product you would like to add\n').lower()
            # input validation for product_quantity 
            while True:
                product_quantity = input('Please provide the product quantity\n')
                if product_quantity.isdigit() == False:
                    print('Product quantity must be a valid number.\n')
                elif product_quantity.isdigit() == True:
                    product_quantity = int(product_quantity)
                    break
            main_inventory.add_product(product_name, product_quantity)
        elif user_action == '2':
            product_name = input('Please provide the name of the product you would like to remove\n').lower()
            # input validation for product_quantity 
            while True:
                product_quantity = input('Please provide the product quantity\n')
                if product_quantity.isdigit() == False:
                    print('Product quantity must be a valid number.\n')
                elif product_quantity.isdigit() == True:
                    product_quantity = int(product_quantity)
                    break
            main_inventory.remove_product(product_name, product_quantity)
        elif user_action == '3':
            product_name = input('Please provide the name of the product you would like to check\n').lower()
            print(f'Current {product_name} stock: {main_inventory.check_stock(product_name)}\n')
        elif user_action == '4':
            # allow user to create order
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
                    while True:
                        order_quantity = input('Please provide the product quantity\n')
                        if order_quantity.isdigit() == False:
                            print('Product quantity must be a valid number.\n')
                        elif order_quantity.isdigit() == True:
                            order_quantity = int(order_quantity)
                            break
                    order.add_purchase(order_action, order_quantity)
                    print(f'Added product: {order_action}, quantity: {order_quantity}')
        elif user_action == '5':
            break

    print('End of line')

main()




        

    