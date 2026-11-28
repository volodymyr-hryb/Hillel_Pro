class BankAccount:


    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

    def __str__(self):
        return f"Рахунок №{self.account_number} (власник: {self.owner}) — баланс: {self._balance}."

    def __eq__(self, other):
        return self.account_number == other.account_number

    def __lt__(self, other):
        return self._balance < other.balance

    def deposit(self, amount):
        if amount <= 0:
            print("Не можна поповнити рахунок від'ємною або нульовою сумою.")
        else:
            self._balance += amount
            print(f"Рахунок поповнено. Залишок на Вашому рахунку {self._balance}.")
        return self._balance


    def withdraw(self, amount):
        if self._balance < amount:
            print("Не можна зняти більше коштів, ніж є на рахунку.")
        elif amount <= 0:
            print("Сума списання повинна бути більше нуля.")
        else:
            self._balance -= amount
            print(f"З Вашого рахунку знято {amount}. Залишок на Вашому рахунку: {self._balance}.")
        return self._balance

    def transfer(self, other_account, amount):
        if self._balance < amount:
            print("Не можна переказати більше коштів, ніж є на Вашому рахунку.")
        elif amount <= 0:
            print("Сума переказу повинна бути більше нуля.")
        elif self.account_number == other_account.account_number:
            print("Не можна переказати кошти на той самий рахунок.")
        else:
            self._balance -= amount
            other_account.deposit(amount)
            print(f"{amount} переведено рахунок номер {other_account.account_number}. "
                  f"Залишок на Вашому рахунку: {self._balance}.")
        return self._balance

    def get_balance(self):
        print(f"Сума на Вашому рахунку {self._balance}.")
        return self._balance

    @property
    def balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, account_number, balance, interest_rate):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        if self.interest_rate <= 0:
            print("Відсоткова ставка повинна бути більше нуля.")
        else:
            self._balance += self._balance * self.interest_rate / 100
            print(f"Сума на Вашому рахунку {self._balance}.")
        return self._balance

class BusinessAccount(BankAccount):
    def __init__(self, owner, account_number, balance, credit_limit):
        super().__init__(owner, account_number, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if self._balance + self.credit_limit < amount:
            print("Перевищено дозволену суму.")
        elif amount <= 0:
            print("Сума списання повинна бути більше нуля.")
        else:
            self._balance -= amount
            print(f"З Вашого рахунку знято {amount}. Залишок на Вашому рахунку: {self._balance}.")
        return self._balance



obj_1 = BankAccount("Hryb", "A87656453G", 1000)
obj_2 = BankAccount("Hryb", "X87656453S", 1000)
obj_3 = SavingsAccount("Hryb", "S87656453M", 1000, 50)
obj_4 = BusinessAccount("Hryb", "B87656453K", 1000, 2000)

print("--- Початковий стан рахунків (__str__) ---")
print(obj_1)
print(obj_2)
print(obj_3)
print(obj_4)

print("--- Коректні операції ---")
obj_1.deposit(500)
obj_1.withdraw(200)
obj_1.transfer(obj_2, 300)
obj_3.add_interest()
obj_4.withdraw(2500)

print("--- Порівняння рахунків (__eq__ та __lt__) ---")
print("obj_1 == obj_2 (різні номери):", obj_1 == obj_2)
print("obj_1 < obj_3 (1000 < 1500):", obj_1 < obj_3)

print("--- Спроби заборонених дій ---")
obj_1.deposit(-100)
obj_1.deposit(0)
obj_1.withdraw(5000)
obj_4.withdraw(2000)
obj_1.transfer(obj_1, 100)

try:
    obj_1.balance = 999999
except AttributeError as e:
    print(f"Помилка інкапсуляції: неможливо змінити баланс напряму ({e})")
