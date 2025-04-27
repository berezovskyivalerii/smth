# Реалізуйте клас «Стадіон». Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість. 
# Реалізуйте методи класу для введення-виведення даних та інших операцій.

class Stadium:
    name = "Анекдотус"
    open_year = 1452
    country = "Приколяндия"
    city = "Рофлинка"
    capacity = 100000

    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    # Getters
    def get_name(self):
        return self.name
    
    def get_open_year(self):
        return self.open_year
    
    def get_country(self):
        return self.country
    
    def get_city(self):
        return self.city
    
    def get_capacity(self):
        return self.capacity
    
    # Setters
    def change_name(self, value):
        self.name = value
    
    def change_open_year(self, value):
        self.open_year = value
    
    def change_country(self, value):
        self.country = value
    
    def change_jenre(self, value):
        self.jenre = value
    
    def change_capacity(self, value):
        self.capacity = value