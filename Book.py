# Реалізуйте клас «Книга». Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну. 
# Реалізуйте методи класу для введення-виведення даних та інших операцій.
class Book:
    name = "Стечение сложных обстоятельств"
    author = "Юрий Власов"
    publication_year = 1990
    jenre = "Документальная литература"
    price = 1000.0

    def __init__(self, name, author):
        self.name = name
        self.author = author
    
    
    # Getters
    def get_name(self):
        return self.name
    
    def get_author(self):
        return self.author
    
    def get_publication_year(self):
        return self.publication_year
    
    def get_jenre(self):
        return self.jenre
    
    def get_price(self):
        return self.price
    
    # Setters
    def change_name(self, value):
        self.name = value
    
    def change_author(self, value):
        self.author = value
    
    def change_publication_year(self, value):
        self.publication_year = value
    
    def change_jenre(self, value):
        self.jenre = value
    
    def change_price(self, value):
        self.price = value