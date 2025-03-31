from productmanager import ProductManager
from product import Product

def main():
    manager = ProductManager()
    
    # Dodavanje nekoliko proizvoda
    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Smartphone", 500, 10)
    product3 = Product("Headphones", 100, 20)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    # Prikaz svih proizvoda
    manager.display_all_products()
    
    # Ukupna vrednost inventara
    total_value = manager.total_inventory_value()
    print(f"Total inventory value: {total_value}")

if __name__ == "__main__":
    main()