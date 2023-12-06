# ***************************************************************
# * Name : Final Project
# * Author: Boen Bily
# * Created : 12/5/2023
# * Course: CIS 152 - Data Structure
# * Version: 1.0
# * OS: Windows 10
# * IDE: eclipse PyCharm
# * Copyright : This is my own original work
# * based onspecifications issued by our instructor
# * Description : An app that Creates a object than output the object
# *            Input: inventory_system.sell_product("Apple", 20)
# *            Ouput: 20 Apples sold
# * Academic Honesty: I attest that this is my original work.
# * I have not used unauthorized source code, either modified or
# * unmodified. I have not given other fellow student(s) access
# * to my program.
# ***************************************************************
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id  # Unique ID for each product
        self.name = name  # Name of the product
        self.price = price  # Price of the product
        self.stock = stock  # Quantity of the product in stock


class InventoryManagementSystem:
    def __init__(self):
        self.products = {}  # Dictionary to store products (product_id: Product)
        self.sales = []  # List to store sales history
        self.restocks = []  # List to store restocking history
        self.next_product_id = 1  # Initializing product ID starting value

    def add_product(self, name, price, stock):
        # Check if a product with the same name already exists
        for product_id, product in self.products.items():
            if product.name == name:
                return "Product already exists in inventory."

        product_id = self.next_product_id
        self.products[product_id] = Product(product_id, name, price, stock)
        self.next_product_id += 1  # Increment product ID for the next product
        return f"Product '{name}' successfully added to inventory."

    def delete_product_by_id(self, product_id):
        # Delete a product based on its ID if it exists in the inventory
        if product_id in self.products:
            del self.products[product_id]
            return f"Product ID {product_id} deleted."
        else:
            return "Product not found."

    def sell_product_by_id(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        # Sell a certain quantity of a product if it exists in the inventory and has enough stock
        if not product:
            return "Product not found."
        elif product.stock < quantity:
            return "Insufficient stock."
        else:
            product.stock -= quantity
            total_value = product.price * quantity
            formatted_total_value = "${:.2f}".format(total_value)
            self.sales.append(f"{quantity} {product.name} sold, total value: {formatted_total_value}")
            return f"{quantity} {product.name} sold, total value: {formatted_total_value}"

    def restock_product_by_id(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        # Restock a certain quantity of a product if it exists in the inventory
        if not product:
            return "Product not found."
        else:
            product.stock += quantity
            total_value = product.price * quantity
            formatted_total_value = "${:.2f}".format(total_value)
            self.restocks.append(f"{quantity} {product.name} restocked, total value: {formatted_total_value}")
            return f"{quantity} {product.name} restocked, total value: {formatted_total_value}"

    def get_product_by_id(self, product_id):
        # Function to retrieve product details by product_id
        for product in self.products.values():
            if product.product_id == product_id:
                return product
        return None  # Return None if product_id not found

    def display_sales(self):
        # Display sales history
        sales_data = "Sales:\n"
        for sale in self.sales:
            sales_data += sale + "\n"
        return sales_data

    def display_restocks(self):
        # Display restocking history
        restocks_data = "Restocks:\n"
        for restock in self.restocks:
            restocks_data += restock + "\n"
        return restocks_data

    def display_inventory(self):
        # Display current inventory data
        inventory_data = "Current Inventory:\n"
        sorted_products = sorted(self.products.values(), key=lambda x: x.name)
        for product in sorted_products:
            formatted_price = "${:.2f}".format(product.price)
            total_value = product.price * product.stock
            formatted_total_value = "${:.2f}".format(total_value)
            inventory_data += f"Product ID: {product.product_id}, Product: {product.name}, Price: {formatted_price}, Stock: {product.stock}, Total Value: {formatted_total_value}\n"
        return inventory_data

