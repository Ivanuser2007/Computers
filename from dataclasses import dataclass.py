from dataclasses import dataclass
@dataclass

class computers:
    id: int
    brand: str
    processor:str
    weight: int
    OZU: int
    videocard: str
    SSD: str
    price: int
    count: int
GLOBAL_COMPUTERS = 0

def inputcomputer_data():
    print("введите данные телефона")

    brand = input("марку: ")
    processor = input("процессор: ")
    weight = int(input("вес: "))
    videocard=(input("видеокарту: "))
    OZU= int(input("оперативная память: "))
    SSD=int(input("внутренняя память:"))
    price = int(input("цену: "))
    amount = int(input("количество на складе: "))

    return computers(
        0, brand,OZU, weight, videocard, SSD, processor, price, amount
    )
def add_computer_to_list(computers, computer):
    global GLOBAL_COMPUTER_ID
    GLOBALCOMPUTEER_ID += 1

    computer.id = GLOBAL_COMPUTER_ID

    computers.append(computer)
def find_computers_index_by_id(computers, id):
    for i in range(len(computers)):
        if computers[i].id == id:
            return i

    return -1


def delete_computers_by_id(computers, id):
    delete_index = find_computers_index_by_id(computers, id)

    if delete_index != -1:
        computers.pop(delete_index)
        return True

    return False
def print_computer(computers):
    print(
        f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
    )

    for item in computers:
        print(
            f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.processor:<15.1f}{item.battery:<15}{item.status:<15}{item.price:<15}{item.amount:<15}"
        )
def print_computer_by_id(computers, id):
    print_index = find_computers_index_by_id(computers, id)

    if print_index != -1:
        print(
            f"{'ИД':<10}{'Марка':<15}{'процессор':<16}{'Вес':<10}{'ОЗУ':<15}{'ПЗУ':<15}{'ВИДЕОКАРТА':<15}{'Цена(руб)':<15}{'В наличии':<15}"
        )
        item = computers[print_index]
        print(
            f"{item.id:<10}{item.brand:<15}{item.processor:<16}{item.weight:<10}{item.videocard:<15.1f}{item.OZU:<15}{item.SSD:<15}{item.price:<15}{item.amount:<15}"
        )
    else:
        print(f"компьютер с id = {id} не найден")
        phones = []

add_computer_to_list(
    computers, computers(1, "brand1", "model1", 10, 3.4, 228, "status1", 123, 10)
)
add_computer_to_list(
    computers, computers(2, "brand2", "model2", 10, 3, 228, "status2", 123, 10)
)
print_computer_by_id(computers, 1)

