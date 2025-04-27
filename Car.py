
# Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, 
# об'єм двигуна, колір машини, ціну. Реалізуйте методи класу для введення-виведення даних та інших операцій. 
class Car:
    model = "Sequoia"
    production_year = "2025"
    manufacturer = "Tayota"
    engine_cap = 0.0
    color = "black"
    price = 0.0

    def __init__(self, model, production_year, manufacturer):
        self.model = model
        self.production_year = production_year
        self.manufacturer = manufacturer

    # Getters
    def get_model(self):
        return self.model
    
    def get_production_year(self):
        return self.production_year
    
    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_cap(self):
        return self.engine_cap

    def get_color(self):
        return self.color
    
    def get_price(self):
        return self.price

    # Setters
    def change_model(self, value): 
        self.model = value
    
    def change_production_year(self, value):
        self.production_year = value
    
    def change_manufacturer(self, value):
        self.manufacturer = value
    
    def change_engine_cap(self, value):
        self.engine_cap = value
    
    def change_color(self, value):
        self.color = value
    
    def change_price(self, value):
        self.price = value
