# завдання 1
# class Zoo:
#
#     total_animals = 0
#
#     def __init__(self, name, species, color, can_fly=False, can_swim=False):
#         # Атрибути об'єкта
#         self.name = name
#         self.species = species
#         self.color = color
#         self.can_fly = can_fly
#         self.can_swim = can_swim
#         Zoo.total_animals += 1
#
#     def make_sound(self):
#         if self.name == "Тигр":
#             return "Ррррр!"
#         elif self.name == "Слон":
#             return "Фу-фу!"
#         elif self.name == "Папуга":
#             return "Привіт, пташечка!"
#         elif self.name == "Акула":
#             return "Джоу!"
#
#
#     def move(self):
#         if self.can_fly:
#             return "Полетіли..."
#         elif self.can_swim:
#             return "Пливемо..."
#         else:
#             return "Біжимо..."
#
# # Створення об'єктів
# tiger = Zoo("Тигр", "Тигр сибірський", "Полосатий", can_fly=False, can_swim=False)
# elephant = Zoo("Слон", "Слон африканський", "Сірий", can_fly=False, can_swim=False)
# parrot = Zoo("Папуга", "Ара", "Барвистий", can_fly=True, can_swim=False)
# shark = Zoo("Акула", "Велика біла акула", "Сіра", can_fly=False, can_swim=True)
#
# # Виклик методів для об'єктів
# print(tiger.move())
# print(tiger.make_sound())
# print(elephant.move())
# print(elephant.make_sound())
# print(parrot.move())
# print(parrot.make_sound())
# print(shark.move())
# print(shark.make_sound())
# print(f"Загальна кількість тварин у зоопарку: {Zoo.total_animals}")

# завдання 2
# class Car:
#     # Атрибути рівня класу
#     total_cars = 0  # Загальна кількість створених автомобілів
#     fuel_type = "Gasoline"  # Тип пального за замовчуванням
#
#     def __init__(self, make, model, year, color, fuel_level=100):
#         # Атрибути рівня об'єкту
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.fuel_level = fuel_level
#
#         Car.total_cars += 1
#
#     def start_engine(self):
#         print(f"{self.make} {self.model} запустив двигун.")
#
#     def stop_engine(self):
#         print(f"{self.make} {self.model} зупинив двигун.")
#
#     def drive(self, distance):
#         if self.fuel_level > 0:
#             print(f"{self.make} {self.model} поїхав на відстань {distance} км.")
#             self.fuel_level -= distance / 10  # Припустимо, що автомобіль споживає 10 літрів пального на 100 км
#         else:
#             print(f"Пального в {self.make} {self.model} закінчилося. Зупинка автомобіля.")
#
#     def refuel(self, amount):
#         self.fuel_level += amount
#         print(f"{self.make} {self.model} поповнив пальне. Поточний рівень пального: {self.fuel_level} л.")
#
# # Створення об'єктів класу Car
# car1 = Car("Toyota", "Camry", 2020, "Срібний")
# car2 = Car("Honda", "Civic", 2022, "Червоний")
#
# # Виклик методів для зміни поведінки об'єктів
# car1.start_engine()
# car1.drive(50)
# car1.stop_engine()
#
# car2.start_engine()
# car2.drive(75)
# car2.refuel(20)
# car2.drive(100)
# car2.stop_engine()
#
# print(f"Загальна кількість автомобілів: {Car.total_cars}")