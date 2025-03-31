

def main():
    manager = ProductManager()
    
    # Dodavanje nekoliko proizvoda
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Smartphone", 500, 10)
    product3 = Product("Headphones", 100, 20)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    # Kreiranje korpe
    cart = Cart()
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    
    # Prikaz vrednosti korpe
    cart.display_cart()
    print(f"Total cart value: {cart.total_cart_value()}")