class Client:
    default_name = 'Ruslan'
    default_age = 24

    def __init__(self, name: str, age: int, bank=None) -> None:
        self.name = Client.default_name
        self.age = Client.default_age

        self.__account = bank.add_account(self) if bank else None
        self.__house = None

    def __str__(self) -> str:
        return (f'Имя: {self.name}\n'
                f'Возраст: {self.age}\n'
                f'Дома: {self.__house}\n'
                f'Количество доступных средств на счете: {self.__account.amount}')

    def info(self) -> None:
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}\n'
              f'Дома: {self.__house}\n'
              f'Количество доступных средств на счете: {self.__account.amount}')

    @classmethod
    def default_info(cls) -> None:
        print(f'default_name: {cls.default_name}\n'
              f'default_age: {cls.default_age}')

    def __make_deal(self, house, price) -> None:
        self.__account.amount -= price
        self.__house = house

    def earn_money(self, other: int):
        self.__account.amount += other
        return self

    def buy_house(self, house, discount) -> None:
        final_cost = house.final_price(discount)

        if final_cost > self.__account.amount:
            raise ValueError("Недостаточно средств на счете.\n"
                             f"Попытка купить дом за {final_cost}, но доступно только {self.__account.amount}.")
        self.__make_deal(house, final_cost)


class Account:
    default_amount: int = 30000

    def __init__(self, client, amount) -> None:
        self.client = client
        self.amount = Account.default_amount

    def __str__(self) -> str:
        return (f'Пользователь: {self.client}\n'
                f'На счете: {self.amount}')

    def __iadd__(self, other: int):
        self.amount += other
        return self

    def __isub__(self, other: int):
        if self.amount - other < 0:
            raise ValueError("Недостаточно средств на счете.\n"
                             f"Попытка снять {other}, но доступно только {self.amount}.")

        self.amount -= other
        return self


class Bank:
    def __init__(self):
        self.__accounts = []

    def __str__(self) -> str:
        return f'Клиенты банка: {[acc.name for acc in self.__accounts]}\n'

    def add_account(self, client: Client) -> Account:
        if client in self.__accounts:
            raise ValueError(f"Клиент {client.name} уже зарегистирован в банке")

        self.__accounts.append(client)

        account = Account(client, 100000)

        return account


class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount: int) -> int:
        sale = self.price - discount

        return sale


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=42, price=price)


