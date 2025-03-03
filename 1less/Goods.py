class Item():
    def __init__(self, title, manufactor, price, quatity, decryption):
        self.title = title
        self.manufactor = manufactor
        self.price = price
        self.quatity = quatity
        self.decryption = decryption
        
    def set_title(self, title):
        self.title = title
    def set_manufactor(self, manufactor):
        self.manufactor = manufactor
    def set_price(self, price):
        if price < 0:
            return "Error price"
        else:
            self.price = price
            return True
    def set_quatity(self, quatity):
        if type(quatity) != int:
            return "Error quatity"
        else:
            self.quatity = quatity
            return True
    def set_decryption(self, decryption):
        self.decryption = decryption    
    
    
    def get_title(self):
        return self.title
    def get_manufactor(self):
        return self.manufactor
    def get_price(self):
        return self.price
    def get_quatity(self):
        return self.quatity
    def get_decryption(self):
        return self.decryption
    
    
    def Print(self):
        print(f"Items name: {self.get_title()}")
        print(f"Items manufactor: {self.get_manufactor()}")
        print(f"Items price: {self.get_price()}")
        print(f"Items quatity: {self.get_quatity()}")
        print(f"Items decryption: {self.get_decryption()}")
        

item1 = Item("Book", "Ukraine", 1000, 10, "Book about Python")
item2 = Item("Notebook", "China", 300, 100, "Notebook for notes")
item3 = Item("Pen", "Germany", 200, 1000, "Pen for writing")
item4 = Item("Pencil", "USA", 180, 1000, "Pencil for drawing")
item5 = Item("Eraser", "Japan", 150, 1000, "Eraser for erasing")


class Shop():
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
    
    def Print(self):
        for i in self.items:
            i.Print()
            print()
    
    def Print_names(self):
        item_names = []
        for i in self.items:
            item_names.append(i.get_title())
        print(item_names)

    def print_in_range(self, a, b):
        item_names = []
        for i in self.items:
            if i.get_price() >= a and i.get_price() <= b:
                item_names.append(i.get_title())
        return item_names

    def search_item(self, book_name):
        for i in self.items:
            if i.get_title() == book_name:
                return (f"We found {i.get_title()} in our shop")
        return "We didn't find this item" 
    
    def search_manufactor(self, manuf):
        for i in self.items:
            if i.get_manufactor() == manuf:
                return (f"We found {i.get_title()} in our shop")
        return "We didn't find this item"   

    def sort_by_name(self):
        item_names = []
        for i in self.items:
            item_names.append(i.get_title())
        item_names.sort()
        print(item_names)

    def sort_by_price(self):
        item_prices = {}
        for i in self.items:
            item_prices.update({i.get_title(): i.get_price()})
        item_prices = dict(sorted(item_prices.items(), key=lambda item: item[1])) # спросил у нейросети
        print(item_prices)
    
    def delete_item(self, item):
        print(f"Delete {item.get_title()}")
        self.items.remove(item)
    

shop1 = Shop()
shop1.add_item(item1)
shop1.add_item(item2)
shop1.add_item(item3)
shop1.add_item(item4)
shop1.add_item(item5)

# shop1.Print_names()

# print(shop1.print_in_range(300, 1000))
# print(shop1.search_item("Book"))
# print(shop1.search_manufactor("China"))
# shop1.sort_by_name()
# shop1.sort_by_price()

# shop1.delete_item(item1)
# shop1.Print_names()