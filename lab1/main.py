import time


# 1. Передача параметров в функции происходит через присваивание (pass-by-assignment)
# те. в момент вызова ф-ции параметр как бы связывается с объектом из сигнатуры ф-ции и дальше уже всё зависит
# от типа, точнее от того, является этот тип изменяемым или неизменяемым. То есть при передаче изменяемого в ф-цию
# при изменении этого объекта в функции изменится и он сам, в то время как передавая int, str и тд. даже при изменении
# создастся новый объект. А при присваивании в любом случае создастся новый объект внутри функции.
# Попытался так сделать в ф-ции myLensort, но функция sorted по-видимому не изменяет массив, а где-то у себя внутри
# совершает присваивание, да это и логично. Не правда ли? И правда.
# << функция sorted возвращает новый отсортированный список, который получен из итерируемого объекта,
# который был передан как аргумент >>

# 2. Ну и собственно. Как будто в предыдущем ответе я к этому как раз и подвёл.
# sort() сортирует список на месте, изменяя его индексы и возвращая None, тогда как sorted() -> см. предыдущий ответ
# Ну это уже из сигнатуры видно. Что один array.sort(...), а второй sorted(array, ...)

# 3. Ну. Лихо. Лихо их использовать надо

def my_lensorted(array) -> []:
    return sorted(array, key=lambda element: len(element))


def my_lensort(array):
    array.sort(key=lambda element: len(element))


def task_1():
    print("Результат Задания №1:")
    array = ['python', 'perl', 'java', 'c', 'haskel', 'ruby']
    print(my_lensorted(array))
    my_lensort(array)
    print(array)
    print()


#
#
#

# 1. Set представляет из себя множество состоящее из неповторяющихся элементов неизменяемых типов!
# Те. неупорядоченная коллекция уникальных элементов иммутабельных типов, основанная на ХЭШ-ТАБЛИЦАХ, вот так!
# Ну, это всё так, знаете ли. Ежели по-научному размовлять.
# Ну и кроме этого. Если говорить про скорость поиска элементов, то вот кое-что об этом:
# Данный метод работает так: каждый элемент присваивается какому-то классу элементов (например, класс элементов,
# имеющих одинаковый остаток от деления на модуль). Все элементы каждого класса хранятся в отдельном списке.
# В таком случае мы заранее знаем, в каком списке должен находиться элемент,
# и можем за короткое время выполнить необходимые операции.
# Дубликаты он сам удаляет. То есть просто не добавляет

def my_unique(array) -> []:
    return set(array)


def task_2():
    print("Результат Задания №2:")
    array = [1, 2, 1, 3, 2, 5]
    print(my_unique(array))
    print()


#
#
#

# 1. range([start], stop[, step]) - генерирует список чисел
# 2. функция zip позволяет пройтись одновременно по нескольким итерируемым объектам:
# zip(a, b) создает объект-итератор, из которого при каждом обороте цикла извлекается кортеж,
# состоящий из двух элементов

ListOfTuples = list[tuple]


def my_enumerate(array) -> ListOfTuples:
    list_tuples = list()
    for i in range(len(array)):
        tuple = (i, array[i])
        list_tuples.append(tuple)
    return list_tuples


def my_enumerate_with_zip(array):
    list_tuples = list(zip(range(len(array)), array))
    return list_tuples


def task_3():
    print("Результат Задания №3:")
    array = ['a', 'b', 'c']
    # array_1 = my_enumerate(array)
    # print(array_1)
    array_2 = my_enumerate_with_zip(array)
    print(array_2)
    print()


#
#
#

# 1. dict - неупорядоченные коллекции произвольных объектов с доступом по ключу
# 3. Функция split сканирует всю строку и разделяет ее в случае нахождения разделителя. Иначе помещает всё в массив
# под нулевым индексом
def task_4(filename):
    print("Результат Задания №4:")
    # print("sdkv;ansvn".split())
    dict_count_words = dict()
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.replace("\n", " ").split()
        for word in words:
            dict_count_words.setdefault(word, 0)
            dict_count_words[word] += 1
            # if word not in return_dict.keys():
            # return_dict[word] = 1
            # else:
            #     return_dict[word] += 1
    print(dict_count_words)
    print(dict(sorted(dict_count_words.items(), key=lambda element: element[1], reverse=True)))
    print()


#
#
#


def time_decorator(func):
    def wrapper(*args, **kwargs):
        print("Вызов функции: ", func.__name__)

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        # print(result)

        elapsed_time = end_time - start_time
        print('Время выполнения ф-ции: ', elapsed_time)
        print()

        return result

    return wrapper


@time_decorator
def square_for(list_nums) -> list:
    list_square = list()
    for num in list_nums:
        list_square.append(num**2)
    return list_square

@time_decorator
def square_list(list_nums) -> list:
    return [num**2 for num in list_nums]

@time_decorator
def square_map(list_nums) -> list:
    return list(map(lambda x: x**2, list_nums))

def square_variations(count):
    list_nums = range(count)
    print("Количество значений: ", count)
    print()

    square_for(list_nums)
    square_list(list_nums)
    square_map(list_nums)


def task_5():
    print("Результат Задания №5:")
    print()

    square_variations(10000)
    # 0.0019979476928710938
    # 0.0019996166229248047
    # 0.0020003318786621094

    # square_variations(10000000)
    # 3.1948530673980713
    # 2.7440342903137207
    # 3.207818031311035

    # square_variations(100000000)
    # 34.24076008796692
    # 27.57021975517273
    # 32.81210684776306




#
#
#

if __name__ == '__main__':
    task_1()
    # task_2()
    # task_3()
    # task_4("task4.txt")
    # task_5()
    print("THE HAPPY END!")
