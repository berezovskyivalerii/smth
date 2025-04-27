# 🧩 Варіант 17
# Рівень 1 (Легкий)

# Знайти всі символи, які не є літерами в рядку.
def isNotLetter(s):
    return [letter for letter in s if not letter.isalpha()]
print(isNotLetter("dfsd1212kh1@@@@[][]afaf"))

# Вивести довжину кожного слова у списку слів.
def wordsLength(words):
    return [len(word) for word in words]
print(wordsLength(['umba', 'tumba', 'prikol']))

# Порахувати кількість входжень рядка в списку рядків.
def countEnters(string, lst):
    return lst.count(string)
print(countEnters("umba", ['umba', 'tumba', 'prikol', 'umba']))


# Рівень 2 (Середній)

# Написати функцію, яка сортує список словників за певним ключем.
def sortDicts(lst, key):
    return sorted(lst, key=lambda x: x[key])
lst = [{"one": 1, "two": 2}, {"one": 1, "two": 3}, {"one": 1, "two": 1}, {"one": 1, "two": 6}]
print(sortDicts(lst, "two"))

# Об'єднати два списки в список пар (елемент з першого, з другого).
def connectLists(lst1, lst2):
    res = {}
    for i in range(len(lst1)):
        res[lst1[i]] = lst2[i]
    return res

lst1 = ["one1", "two1", "three1"]
lst2 = ["one2", "two2", "three2"]
print(connectLists(lst1, lst2))

# Видалити з рядка всі повторення символів, залишивши тільки перше входження.
def deleteExceptFirst(s: str):
    return "".join(set(s))
print(deleteExceptFirst("dffdfddddffdfd"))

# Рівень 3 (Складний)
# Зчитати текстовий файл, створити словник частоти пар літер (біграми).
# def buhrammTextfile():
#     res = {}
#     with open("music_collection.txt", 'r', encoding='utf-8') as file:
#         text = file.read()
#         # -------------------

#     return res

# print(buhrammTextfile())

# Написати декоратор, який вимірює час виконання функції і виводить його.
import time

def messureTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start}")
        return result
    return wrapper

@messureTime
def testFunc():
    time.sleep(2)
    return

print(testFunc())

# Типізована функція: приймає список словників з ключами "price" і "quantity" і повертає загальну вартість.
def countPrice(lst: list) -> int:
    res = 0
    for d in lst:
        res += d["price"] * d["quantity"]
    return res

lst10 = [{"price": 2, "quantity": 2}, {"price": 1, "quantity": 4}, {"price": 5, "quantity": 4}]
print(countPrice(lst10))
