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
import tkinter as tk
from tkinter import messagebox
from Final import InventoryManagementSystem


class InventoryGUI:
    def __init__(self, root, inventory_system):
        self.root = root
        self.inventory_system = inventory_system
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Inventory Management System")
        tk.Label(self.root, text="Product Name:").grid(row=0, column=0)
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.grid(row=0, column=1)
        tk.Label(self.root, text="Price:").grid(row=1, column=0)
        self.price_entry = tk.Entry(self.root)
        self.price_entry.grid(row=1, column=1)
        tk.Label(self.root, text="Stock:").grid(row=2, column=0)
        self.stock_entry = tk.Entry(self.root)
        self.stock_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Add Product", command=self.add_product).grid(row=3, column=0, columnspan=2)
        tk.Label(self.root, text="Product ID:").grid(row=4, column=0)
        self.delete_id_entry = tk.Entry(self.root)
        self.delete_id_entry.grid(row=4, column=1)
        tk.Button(self.root, text="Delete Product", command=self.delete_product).grid(row=5, column=0, columnspan=2)
        tk.Label(self.root, text="Product ID:").grid(row=6, column=0)
        self.product_id_entry = tk.Entry(self.root)
        self.product_id_entry.grid(row=6, column=1)
        tk.Label(self.root, text="Quantity:").grid(row=7, column=0)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=7, column=1)
        tk.Button(self.root, text="Sell", command=self.sell_product).grid(row=8, column=0, columnspan=2)
        tk.Button(self.root, text="Restock", command=self.restock_product).grid(row=9, column=0, columnspan=2)
        tk.Button(self.root, text="Display Inventory", command=self.display_inventory).grid(row=10, column=0, columnspan=2)
        tk.Button(self.root, text="Display Sales", command=self.display_sales).grid(row=11, column=0, columnspan=2)
        tk.Button(self.root, text="Display Restocks", command=self.display_restocks).grid(row=12, column=0, columnspan=2)

    def add_product(self):
        name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        stock = int(self.stock_entry.get())
        message = self.inventory_system.add_product(name, price, stock)
        messagebox.showinfo("Add Product", message)
        self.clear_entries()

    def delete_product(self):
        product_id = int(self.delete_id_entry.get())
        message = self.inventory_system.delete_product_by_id(product_id)
        messagebox.showinfo("Delete Product", message)
        self.clear_entries()

    def sell_product(self):
        product_id = int(self.product_id_entry.get())
        quantity = int(self.quantity_entry.get())
        message = self.inventory_system.sell_product_by_id(product_id, quantity)
        messagebox.showinfo("Sell Product", message)
        self.clear_entries()

    def restock_product(self):
        product_id = int(self.product_id_entry.get())
        quantity = int(self.quantity_entry.get())
        message = self.inventory_system.restock_product_by_id(product_id, quantity)
        messagebox.showinfo("Restock Product", message)
        self.clear_entries()

    def display_inventory(self):
        inventory_data = self.inventory_system.display_inventory()
        self.display_window("Inventory", inventory_data)
        self.clear_entries()

    def display_sales(self):
        sales_data = self.inventory_system.display_sales()
        self.display_window("Restocks", sales_data)
        self.clear_entries()

    def display_restocks(self):
        restocks_data = self.inventory_system.display_restocks()
        self.display_window("Restocks", restocks_data)
        self.clear_entries()

    def display_window(self, title, data):
        display_window = tk.Toplevel(self.root)
        display_window.title(title)
        display_label = tk.Label(display_window, text=data)
        display_label.pack()
        self.clear_entries()

    def clear_entries(self):
        self.product_name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.delete_id_entry.delete(0, tk.END)
        self.product_id_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    inventory_system = InventoryManagementSystem()
    app = InventoryGUI(root, inventory_system)
    root.mainloop()