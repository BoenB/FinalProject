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
import unittest
from Final import InventoryManagementSystem


class TestInventoryManagementSystem(unittest.TestCase):

    def setUp(self):
        self.inventory_system = InventoryManagementSystem()

    def test_add_product(self):
        self.inventory_system.add_product("Apple", 1.0, 50)
        self.assertIn(1, self.inventory_system.products)

    def test_delete_product_by_id(self):
        self.inventory_system.add_product("Apple", 1.0, 50)
        self.inventory_system.delete_product_by_id(1)
        self.assertNotIn(1, self.inventory_system.products)

    def test_sell_product_by_id(self):
        self.inventory_system.add_product("Apple", 1.0, 50)
        self.inventory_system.sell_product_by_id(1, 20)
        self.assertEqual(self.inventory_system.products[1].stock, 30)

    def test_restock_product_by_id(self):
        self.inventory_system.add_product("Apple", 1.0, 50)
        self.inventory_system.restock_product_by_id(1, 30)
        self.assertEqual(self.inventory_system.products[1].stock, 80)

    def test_display_inventory(self):
        self.inventory_system.add_product("Apple", 1.0, 50)
        self.inventory_system.add_product("Banana", 2.0, 70)
        self.inventory_system.add_product("Orange", 1.5, 40)
        self.inventory_system.display_inventory()

    def test_display_sales(self):
        self.inventory_system.add_product("Apple", 1.0, 50)
        self.inventory_system.sell_product_by_id(1, 20)
        self.inventory_system.display_sales()

    def test_display_restocks(self):
        self.inventory_system.add_product("Apple", 1.0, 50)
        self.inventory_system.restock_product_by_id(1, 30)
        self.inventory_system.display_restocks()


if __name__ == '__main__':
    unittest.main()