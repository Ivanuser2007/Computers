mport os
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

ASC = "ascending"
DESC = "descending"


# действия пользователя в программе
def clear_console():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
def get_computers_by_brand(computers, brand):
    finded_computers = []

    for item in computers:
        if item.brand == brand:
            finded_computers.append(item)

    return finded_computers

def is_swap(number_current, number_next, order):
    if order == ASC:
        if number_next < number_current:
            return True
        else:
            return False
    elif order == DESC:
        if number_next > number_current:
            return True
        else:
            return False


def sort_computers_by_id(computers, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(computers) - 1 - offset):
            if is_swap(computers[i].id, computers[i + 1].id, order):
                temp = computers[i + 1]
                computers[i + 1] = computers[i]
                computers[i] = temp
                is_sorted = False

        offset += 1

    print("список компьютеров по ИД успешно отсортирован")


#     Цена
def sort_computers_by_price(computers, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(computers) - 1 - offset):
            if is_swap(computers[i].price, computers[i + 1].price, order):
                temp = computers[i + 1]
                computers[i + 1] = computers[i]
                computers[i] = temp
                is_sorted = False

        offset += 1

    print("список телефонов по Цене успешно отсортирован")
def sort_phones_by_SSD(computers, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(computers) - 1 - offset):
            if is_swap(computers[i].SSD, computers[i + 1].SSD, order):
                temp = computers[i + 1]
                computers[i + 1] = computers[i]
                computers[i] = temp
                is_sorted = False

        offset += 1

    print("список телефонов по Диагонали экрана успешно отсортирован")


#     Ёмкость аккумултора
def sort_computers_OZU(computers, order):
    is_sorted = False
    offset = 0

    while is_sorted == False:
        is_sorted = True
        for i in range(len(computers) - 1 - offset):
            if is_swap(computers[i].OZU, computers[i + 1].OZU, order):
                temp = computers[i + 1]
                computers[i + 1] = computers[i]
                computers[i] = temp
                is_sorted = False

        offset += 1

    print("список компьютеров по озу успешно отсортирован")


#     Вес
def sort_computers_by_weight(computers, order):
    is_sorted = False
    offset = 0
    while is_sorted == False:
        is_sorted = True
        for i in range(len(computers) - 1 - offset):
            if is_swap(computers[i].weight, computers[i + 1].weight, order):
                temp = computers[i + 1]
                computers[i + 1] = computers[i]
                computers[i] = temp
                is_sorted = False

        offset += 1
        


#     Цена
def get_computers_by_price(computers, price):
    finded_computers = []

    for item in computers:
        if item.price == price:
            finded_computers.append(item)

    return finded_computers
def input_int(message, min_number, max_number):
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = int(input(message).strip())

            if number < min_number or number > max_number:
                print(
                    f"Ошибка ввода. Значение должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


def input_float(message, min_number, max_number):
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = float(input(message).strip())

            if number < min_number or number > max_number:
                print(
                    f"Ошибка ввода. Значение должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number


def input_str(message, min_length, max_length):
    is_correct_input = False

    while is_correct_input == False:
        str_data = input(message).strip()

        if len(str_data) < min_length or len(str_data) > max_length:
            print(
                f"Ошибка ввода. Количество символов должно быть в границах от {min_length} до {max_length}"
            )
            is_correct_input = False
        else:
            is_correct_input = True

    return str_data

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

