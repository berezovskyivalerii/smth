#Напиши функцію, яка приймає рядок і повертає найдовше слово.
def longestWord(s):
    return max(s.split(), key=len)

print(longestWord("wwww www wwwwwww ww w"))

#Модель оцінювання працівників: Клас Employee із закритими атрибутами name, ratings (список оцінок 0–5). Перевірка через дескриптор.
class RatingDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_ratings', [])
    
    def __set__(self, instance, value):
        if not all(isinstance(x, int) and 0 <= x <= 5 for x in value):
            raise ValueError("не должно быть больше 5 или меньше 0")
        instance.__dict__['_ratings'] = value
        
class Employee:
    __name = "Valerii"
    ratings = RatingDescriptor()    
    
    def __init__(self, name: str, ratings: list):
        self.__name = name
        self.ratings = ratings
        
    def avg_rating(self):
        return sum(self.ratings) / len(self.ratings)
    
    @property
    def name(self):
        return self.__name

#Клас Company, який містить список працівників. Реалізувати: Метод add_employee(employee) — додає працівника,
#якщо він ще не доданий. Метод top_performer() — повертає працівника з найвищою середньою оцінкою.
#Метод average_company_rating() — повертає середню оцінку по компанії. Зробити Company функтором — при виклику повертати:
#"У компанії <n> працівників, середній рейтинг: <avg>"</avg>

class Company: 
    def __call__(self):
        return f'У компанії {len(self._employees)} працівників, середній рейтинг: {self.average_company_rating()}'
        
    def __init__(self, employees):
        self._employees = employees if employees else []
        
    def add_employee(self, employee):
        if employee not in self._employees:
            self._employees.append(employee)
        
    def top_performer(self):
        return max(self._employees, key=lambda x: x.avg_rating())
    
    def average_company_rating(self):
        s = sum(x.avg_rating() for x in self._employees)
        return s / len(self._employees)
    
e1 = Employee("димон", [4, 5, 5])
e2 = Employee("антон", [4,5, 4]) # OK
#e2 = Employee("антон", [4,65, 4]) # NE OK
e3 = Employee("амон", [2, 3])

company = Company(None)
company.add_employee(e2)
company.add_employee(e3)
company.add_employee(e1) 

print(company()) # __call__
print(company.top_performer().name) 
print(company.average_company_rating())

#Напиши функцію, яка приймає список чисел і повертає новий список із сумою префіксів: (тобто [a, b, c] → [a, a+b, a+b+c])

def add_pref(l: list):
    j = 0
    for i in range(0, len(len)):
        for k in range(0, j):
            
    return None
