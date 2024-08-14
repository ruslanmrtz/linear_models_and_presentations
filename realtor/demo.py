from classes import Bank, Client, SmallHouse

green_bank = Bank()
red_bank = Bank()

Client.default_info()

student = Client('руслан', 34, green_bank)
teacher = Client('марья ивановна', 68, red_bank)

print()

student.info()
print()
print(teacher)

house = SmallHouse(400000)

# student.buy_house(house, 100)

student.earn_money(1000000)

student.buy_house(house, 100)

print()
print(student)
