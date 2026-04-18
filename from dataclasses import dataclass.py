from dataclasses import dataclass




@dataclass
class exersises:
    id: int
    name: str
    age: int
    number: int
    weight:int


GLOBAL_EXERSISE_ID = 0

def input_exersise_data():
    print("введите упражнение")

    name= input("название упражнения: ")
    weight = int(input("вес: "))
    age= int(input("возраст учащихся: "))
    number = int(input("количество раз"))
    return Exersise(
        0,  weight, age, number, name,
    )


def add_exersise_to_list(phones, phone):
    global GLOBAL_EXERSISE_ID
    GLOBAL_EXERSISE_ID += 1

    exersise.id= GLOBAL_EXERSISE_ID

    phones.append(exersise)


# 4) удалять мобильные телефоны из списка телефонов по ИД
def find_exersise_index_by_id(exersises, id):
    for i in range(len(exersises)):
        if exersises[i].id == id:
            return i

    return -1


def delete_exersise_by_id(exersises, id):
    delete_index = find_exersise_index_by_id(exersises, id)

    if delete_index != -1:
        exersises.pop(delete_index)
        return True

    return False



def print_exersises(exersises):
    print(
        f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
    )

    for item in phones:
        print(
            f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{item.status:<15}{item.price:<15}{item.amount:<15}"
        )


# 8) вывести мобильный телефон по ИД
def print_phone_by_id(phones, id):
    print_index = find_phone_index_by_id(phones, id)

    if print_index != -1:
        print(
            f"{'ИД':<10}{'название':<15}{'Вес':<10}{'количество раз':<15}{'Возраст':<15}"
        )
        item = exersises[print_index]
        print(
            f"{item.id:<10}{item.name:<15}{item.age:<16}{item.weight:<10}{item.number:<15.1f}"
        )
    else:
        print(f"Телефон с id = {id} не найден")


# 9) сохранить список мобильных телефонов в текстовый файл, в двух вариантах
#     для удобного чтения человеком
#     для последующей удобной загрузки компьютером в эту программу (по одному полю на строку)

# 10) загрузить список мобильных телефонов из текстового файла

exersises = []

# add_phone_to_list(phones, input_phone_data())
# add_phone_to_list(phones, input_phone_data())

add_exersise_to_list(
    exersises, Exersise(1, "pushups", "run", 30, 0, 50)
)
add_exersise_to_list(
    exersises,Exersise (2, "barbell press", "squats", 50, 80, 120)
)


print_exersise_by_id(exersises, 1)
