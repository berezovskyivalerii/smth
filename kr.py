# 1) Генератор паролів
# Завдання: Створити клас PasswordGenerator, який:
# при виклику генерує новий випадковий пароль (__call__),
# має @staticmethod для перевірки складності пароля,критерії:
#         - довжина ≥ 8
#         - містить цифру, велику та малу літери, спецсимвол

# має @classmethod для створення генератора з заданою довжиною.
import random
import string
        
class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length
        self.password = self.generate_password()

    def __call__(self):     # при виклику генерує новий випадковий пароль (__call__),
        return self.password

    @staticmethod
    def is_strong(password):    # має @staticmethod для перевірки складності пароля
        if len(password) < 8:
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c in "!@#$%^&[]{}-_=+*|;:(),.<>?/" for c in password):
            return False
        return True

    @classmethod    # має @classmethod для створення генератора з заданою довжиною.
    def with_length(cls, length: int):
        return cls(length)

    def generate_password(self):
        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?/"
        password = ''.join(random.choice(characters) for _ in range(self.length))
        
        while not self.is_strong(password):
            password = ''.join(random.choice(characters) for _ in range(self.length))
        
        return password

generator = PasswordGenerator.with_length(8)
print("Password:", generator())
print(PasswordGenerator.is_strong(generator()))

generator2 = PasswordGenerator()
print("Password 2:", generator2())
print(PasswordGenerator.is_strong(generator2()))

# 2) ЗАДАЧА Менеджер знижок
# Завдання: Створити клас DiscountManager, який:
# викликається для розрахунку нової ціни (__call__),
# має @staticmethod для перевірки знижки,
# має @classmethod для створення менеджера з типовою знижкою.
class DiscountManager:
    def __init__(self, discount=0.1):
        self.discount = discount

    def __call__(self, price):      # викликається для розрахунку нової ціни (__call__),
        return self.calculate_new_price(price)

    @staticmethod       # має @staticmethod для перевірки знижки,
    def is_valid_discount(discount):
        return 0 <= discount <= 1

    @classmethod        # має @classmethod для створення менеджера з типовою знижкою.
    def with_default_discount(cls):
        return cls(0.5)

    def calculate_new_price(self, price):
        if not self.is_valid_discount(self.discount):
            raise ValueError("Invalid discount value")
        return price * (1 - self.discount)
    
discount_manager = DiscountManager.with_default_discount()
print("Default discount:", discount_manager(181)) #90.5
