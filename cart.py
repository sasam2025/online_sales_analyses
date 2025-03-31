class Cart:
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product):
        self.cart_items.append(product)
    
    def total_cart_value(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total
    
    def display_cart(self):
        for product in self.cart_items:
            print(product.display_info())