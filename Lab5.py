import math

#Ex1

# class Shape:
#     def Perimeter(self):
#         pass
#
#     def Area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def Perimeter(self):
#         return 2*math.pi * (self.radius)
#
#     def Area(self):
#         return math.pi * self.radius**2
#
# class Rectangle(Shape):
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def Perimeter(self):
#         return 2*(self.width+self.length)
#
#     def Area(self):
#         return self.width*self.length
#
# class Triangle(Shape):
#     def __init__(self, a , b ,c ):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def Perimeter(self):
#         return self.a+self.b+self.c
#
#     def Area(self):
#         s = (self.a+self.b+self.c)/2 # s= semiperimeter
#         return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c)) #Formula lui Heron
#
# # Creating instances of shapes
# circle = Circle(radius=2)
# rectangle = Rectangle(width=5, length=5)
# triangle = Triangle(a=3, b=4, c=5)
#
# # Calculating and printing area and perimeter for each shape
# print("Circle - Radius:", circle.radius)
# print("Area:", circle.Area())
# print("Perimeter:", circle.Perimeter())
# print()
#
# print("Rectangle - Length:", rectangle.length, "Width:", rectangle.width)
# print("Area:", rectangle.Area())
# print("Perimeter:", rectangle.Perimeter())
# print()
#
# print("Triangle - Side1:", triangle.a, "Side2:", triangle.b, "Side3:", triangle.c)
# print("Area:", triangle.Area())
# print("Perimeter:", triangle.Perimeter())

#Ex2

# class Account:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount} RON. New balance: {self.balance} RON")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount} RON. New balance: {self.balance} RON")
#         else:
#             print("Insufficient funds")
#
#     def calculate_interest(self):
#         pass
#
# class SavingsAccount(Account):
#     def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
#         super().__init__(account_number, account_holder, balance)
#         self.interest_rate = interest_rate
#
#     def calculate_interest(self):
#         interest = self.balance * self.interest_rate
#         self.deposit(interest)
#         print(f"Interest calculated and deposited: {interest} RON")
#
# class CheckingAccount(Account):
#     def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
#         super().__init__(account_number, account_holder, balance)
#         self.overdraft_limit = overdraft_limit
#
#     def withdraw(self, amount):
#         if amount <= self.balance + self.overdraft_limit:
#             self.balance -= amount
#             print(f"Withdrew {amount} RON. New balance: {self.balance} RON")
#         else:
#             print("Withdrawal exceeds overdraft limit")
#
# # Example usage
# savings_account = SavingsAccount(account_number="123", account_holder="Ion Popa", balance=1000)
# checking_account = CheckingAccount(account_number="456", account_holder="Ioana Popa", balance=2000, overdraft_limit=500)
#
# savings_account.deposit(500)
# savings_account.calculate_interest()
#
# checking_account.withdraw(300)
# checking_account.withdraw(700)

#Ex3

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print(f"{self.year} {self.make} {self.model}")
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, fuel_efficiency, towing_capacity):
#         super().__init__(make, model, year)
#         self.fuel_efficiency = fuel_efficiency  # L/100km
#         self.towing_capacity = towing_capacity  # KG
#
#     def calculate_mileage(self, distance):
#         return (distance * self.fuel_efficiency) / 100
#
# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, fuel_efficiency,towing_capacity):
#         super().__init__(make, model, year)
#         self.fuel_efficiency = fuel_efficiency  # L/100km
#         self.towing_capacity = towing_capacity  # KG
#
#     def calculate_mileage(self, distance):
#         return (distance*self.fuel_efficiency)/100 # L/100km
#
#     def calculate_towing_capacity(self):
#         return self.towing_capacity
# class Truck(Vehicle):
#     def __init__(self, make, model, year, fuel_efficiency, towing_capacity):
#         super().__init__(make, model, year)
#         self.fuel_efficiency = fuel_efficiency
#         self.towing_capacity = towing_capacity # KG
#
#     def calculate_mileage(self, distance):
#         return (distance*self.fuel_efficiency)/100
#
#
#     def calculate_towing_capacity(self):
#         return self.towing_capacity
#
#
# car = Car(make="Audi", model="A5", year=2023, fuel_efficiency=10, towing_capacity= 1000)
# motorcycle = Motorcycle(make="Kawasaki ", model="Ninja 400", year=2023, fuel_efficiency=7, towing_capacity=200)
# truck = Truck(make="Ford", model="Raptor", year=2023,fuel_efficiency=15 ,  towing_capacity=3000)
#
# car.display_info()
# print(f"Car Mileage for 200 km: {car.calculate_mileage(200)} L")
#
# motorcycle.display_info()
# print(f"Motorcycle Mileage for 200 km: {motorcycle.calculate_mileage(200)} L")
#
# truck.display_info()
# print(f"Truck Mileage for 200 km: {truck.calculate_mileage(200)} L")
# print(f"Truck Towing Capacity: {truck.calculate_towing_capacity()} kg")

#Ex4

# class Employee:
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id
#
#     def display_info(self):
#         print(f"Employee ID: {self.employee_id}\nName: {self.name}")
#
# class Manager(Employee):
#     def __init__(self, name, employee_id, salary, department):
#         super().__init__(name, employee_id)
#         self.salary = salary
#         self.department = department
#
#     def display_info(self):
#         super().display_info()
#         print(f"Position: Manager\nSalary: {self.salary} RON \nDepartment: {self.department}")
#
#     def organize_team_meeting(self):
#         print("Organizing a team meeting.")
#
# class Engineer(Employee):
#     def __init__(self, name, employee_id, salary, programming_language):
#         super().__init__(name, employee_id)
#         self.salary = salary
#         self.programming_language = programming_language
#
#     def display_info(self):
#         super().display_info()
#         print(f"Position: Engineer\nSalary: {self.salary} RON \nProgramming Language: {self.programming_language}")
#
#     def write_code(self):
#         print(f"{self.name} is writing code in {self.programming_language}.")
#
# class Salesperson(Employee):
#     def __init__(self, name, employee_id, salary, sales_target):
#         super().__init__(name, employee_id)
#         self.salary = salary
#         self.sales_target = sales_target
#
#     def display_info(self):
#         super().display_info()
#         print(f"Position: Salesperson\nSalary: {self.salary} RON\nSales Target: {self.sales_target} RON")
#
#     def make_sale(self):
#         print(f"{self.name} made a sale and reached the sales target.")
#
# # Example usage
# manager = Manager(name="Andrei Manager", employee_id=1, salary=80000, department="Marketing")
# engineer = Engineer(name="Ramona Engineer", employee_id=2, salary=70000, programming_language="Python")
# salesperson = Salesperson(name="Ionut Salesperson", employee_id=3, salary=60000, sales_target=100000)
#
# manager.display_info()
# manager.organize_team_meeting()
# print()
#
# engineer.display_info()
# engineer.write_code()
# print()
#
# salesperson.display_info()
# salesperson.make_sale()

#Ex5

# class Animal:
#     def __init__(self, name, habitat):
#         self.name = name
#         self.habitat = habitat
#
#     def make_sound(self):
#         pass
#
#     def move(self):
#         print(f"{self.name} is moving.")
#
# class Mammal(Animal):
#     def __init__(self, name, habitat, fur_color):
#         super().__init__(name, habitat)
#         self.fur_color = fur_color
#
#     def make_sound(self):
#         print(f"{self.name} makes a mammalian sound.")
#
#     def give_birth(self):
#         print(f"{self.name} is giving birth.")
#
# class Bird(Animal):
#     def __init__(self, name, habitat, wing_span):
#         super().__init__(name, habitat)
#         self.wing_span = wing_span
#
#     def make_sound(self):
#         print(f"{self.name} chirps like a bird.")
#
#     def fly(self):
#         print(f"{self.name} is flying with a wingspan of {self.wing_span} cm.")
#
# class Fish(Animal):
#     def __init__(self, name, habitat, scale_color):
#         super().__init__(name, habitat)
#         self.scale_color = scale_color
#
#     def make_sound(self):
#         print(f"{self.name} makes a bubbling sound.")
#
#     def swim(self):
#         print(f"{self.name} is swimming with {self.scale_color} scales.")
#
#
# lion = Mammal(name="Lion", habitat="Savannah",  fur_color="Golden")
# sparrow = Bird(name="Colibri", habitat="Forest", wing_span=2)
# shark = Fish(name="Shark", habitat="Ocean", scale_color="Gray")
#
# lion.make_sound()
# lion.give_birth()
# lion.move()
# print()
#
# sparrow.make_sound()
# sparrow.fly()
# sparrow.move()
# print()
#
# shark.make_sound()
# shark.swim()
# shark.move()

#Ex6

# class LibraryItem:
#     def __init__(self, title, author_or_director, item_id):
#         self.title = title
#         self.author_or_director = author_or_director
#         self.item_id = item_id
#         self.checked_out = False
#
#     def display_info(self):
#         print(f"Item ID: {self.item_id}\nTitle: {self.title}\nAuthor/Director: {self.author_or_director}\nStatus: {'Checked Out' if self.checked_out else 'Available'}")
#
#     def check_out(self):
#         if not self.checked_out:
#             self.checked_out = True
#             print(f"{self.title} has been checked out.")
#         else:
#             print(f"{self.title} is already checked out.")
#
#     def return_item(self):
#         if self.checked_out:
#             self.checked_out = False
#             print(f"{self.title} has been returned.")
#         else:
#             print(f"{self.title} is not checked out.")
#
# class Book(LibraryItem):
#     def __init__(self, title, author, item_id, num_pages):
#         super().__init__(title, author, item_id)
#         self.num_pages = num_pages
#
#     def display_info(self):
#         super().display_info()
#         print(f"Type: Book\nNumber of Pages: {self.num_pages}")
#
# class DVD(LibraryItem):
#     def __init__(self, title, director, item_id, duration):
#         super().__init__(title, director, item_id)
#         self.duration = duration
#
#     def display_info(self):
#         super().display_info()
#         print(f"Type: DVD\nDuration: {self.duration} minutes")
#
# class Magazine(LibraryItem):
#     def __init__(self, title, publisher, item_id, issue_number):
#         super().__init__(title, publisher, item_id)
#         self.issue_number = issue_number
#
#     def display_info(self):
#         super().display_info()
#         print(f"Type: Magazine\nIssue Number: {self.issue_number}")
#
# # Example usage
# book = Book(title="Moara cu noroc", author="Ioan Slavici", item_id="123", num_pages=100)
# dvd = DVD(title="Inception", director="Christopher Nolan", item_id="456", duration=150)
# magazine = Magazine(title="National Geographic", publisher="National Geographic Society", item_id="789", issue_number=245)
#
# book.display_info()
# book.check_out()
# book.return_item()
# print()
#
# dvd.display_info()
# dvd.check_out()
# dvd.check_out()
# dvd.return_item()
# print()
#
# magazine.display_info()
# magazine.check_out()
# magazine.return_item()
