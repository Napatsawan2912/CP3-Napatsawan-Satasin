class Customer:
    Name = ""
    LastName = ""
    Age = 0

    def addCart(self):
        print("Added to", self.Name, self.LastName, "'s cart")

customer1 = Customer()
customer1.Name = "Sommai"
customer1.LastName = "Diyiam"
customer1.Age = 96
customer1.addCart()

customer2 = Customer()
customer2.Name = "Sompong"
customer2.LastName = "Diloet"
customer2.Age = 83
customer2.addCart()

customer3 = Customer()
customer3.Name = "Somsak"
customer3.LastName = "Dingam"
customer3.Age = 74
customer3.addCart()

customer4 = Customer()
customer4.Name = "Somsri"
customer4.LastName = "Disut"
customer4.Age = 52
customer4.addCart()