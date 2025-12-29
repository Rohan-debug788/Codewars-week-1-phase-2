# def process_items (prices: dict[str, float]):
#     for item_name, item_price in prices:
#         print(item_name)
#         print(item_price)

# def dict_list():
#     my_dict = {
#         'car': 'toyota',
#         'model': 'camry',
#         'year': '2004'
#     }
#     new_dict = {
#         'motor': 'cycle',
#         'type': 'hyundai',
#         'mwaka': '2015'
#     }

#     joined_dict = my_dict | new_dict #using union (|) to join both dictonaries

#     for car, model in joined_dict.items():
#         print(f'{car.capitalize()}:{model.title()}')
   

# dict_list()

# def say_hi(name):
#     name = input('input name : ')
#     if name:
#         print(f"Hey {name}!")
#     else:
#         print("Hello Guest")
# say_hi()

from car import Car

Car1 = Car('Dodge', 2012, 'Black', True)
Car2 = Car('Rolls Royce', 2025, 'White', False) 

Car1.describe()
Car2.describe()