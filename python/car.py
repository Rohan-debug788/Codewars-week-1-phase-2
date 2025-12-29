class Car:
    def __init__(self, model:str, year:int|str, color:str, for_sale:bool):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f'Awesome driving in your {self.color} {self.model}')

    def stop(self):
        print(f'Nice Brakes on your {self.color} {self.model} handler')

    def describe(self):
        print(f'{self.year} {self.color} {self.model}')
