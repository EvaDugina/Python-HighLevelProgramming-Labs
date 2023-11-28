from random import randrange

from Logger import MyLogger
from Vector import MyVector
import Figures
from Decorators import HtmlDecorator, TimerDecorator


### ЗАДАНИЕ 1

def task1():
    print("Task1")
    testSum()
    testDiff()
    testCmp()
    testMultKoeff()
    testMultScalar()
    testLength()
    print()

def testSum():
    print("testSum()")
    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_1 = MyVector(rand_x, rand_y)

    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_2 = MyVector(rand_x, rand_y)

    sum_vector = my_vector_1 + my_vector_2
    print(f"{my_vector_1} + {my_vector_2} = {sum_vector}")
    print()

def testDiff():
    print("testDiff()")
    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_1 = MyVector(rand_x, rand_y)

    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_2 = MyVector(rand_x, rand_y)

    diff_vector = my_vector_1 - my_vector_2
    print(f"{my_vector_1} - {my_vector_2} = {diff_vector}")
    print()

def testCmp():
    print("testCmp()")
    rand_x = randrange(3)
    rand_y = randrange(3)
    my_vector_1 = MyVector(rand_x, rand_y)

    rand_x = randrange(3)
    rand_y = randrange(3)
    my_vector_2 = MyVector(rand_x, rand_y)

    cmp_result = my_vector_1 == my_vector_2
    print(f"{my_vector_1} == {my_vector_2} ? {cmp_result}")
    print()

def testMultKoeff():
    print("testMultKoeff()")
    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_1 = MyVector(rand_x, rand_y)

    koeff = randrange(10)

    mult_koeff_vector = my_vector_1 * koeff
    print(f"{my_vector_1} * {koeff} = {mult_koeff_vector}")
    print()

def testMultScalar():
    print("testMultScalar()")
    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_1 = MyVector(rand_x, rand_y)

    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_2 = MyVector(rand_x, rand_y)

    mult_scalar_vector = my_vector_1 * my_vector_2
    print(f"{my_vector_1} * {my_vector_2} = {mult_scalar_vector}")
    print()

def testLength():
    print("testLength()")
    rand_x = randrange(10)
    rand_y = randrange(10)
    my_vector_1 = MyVector(rand_x, rand_y)

    length = my_vector_1.length()
    print(f"{my_vector_1}.length() = {length}")
    print()



### ЗАДАНИЕ 2

def task2():
    print("Task2:")
    testRectangle()
    testTriangle()
    testCircle()
    print()


def testRectangle():
    width = randrange(10)
    height = randrange(10)

    my_rectangle = Figures.MyRectangle(width, height)
    print(my_rectangle.type() + f"({width}, {height}): ")
    print("S = " + str(my_rectangle.square()))
    print()

def testTriangle():
    rand_x = randrange(10)
    rand_y = randrange(10)
    triangle_vector_1 = MyVector(rand_x, rand_y)

    rand_x = randrange(10)
    rand_y = randrange(10)
    triangle_vector_2 = MyVector(rand_x, rand_y)

    my_triangle = Figures.MyTriangle(triangle_vector_1, triangle_vector_2)
    print(my_triangle.type() + f"({triangle_vector_1}, {triangle_vector_2}): ")
    print("S = " + str(my_triangle.square()))
    print()

def testCircle():
    radius = randrange(10)

    my_circle = Figures.MyCircle(radius)
    print(my_circle.type() + f"({radius}): ")
    print("S = " + str(my_circle.square()))
    print()


### ЗАДАНИЕ 3

def task3():
    list_nums = range(1000000)

    square_for(list_nums)
    square_list(list_nums)
    square_map(list_nums)


@HtmlDecorator
@TimerDecorator
def square_for(list_nums) -> list:
    list_square = list()
    for num in list_nums:
        list_square.append(num**2)
    return list_square

@HtmlDecorator
@TimerDecorator
def square_list(list_nums) -> list:
    return [num**2 for num in list_nums]

@HtmlDecorator
@TimerDecorator
def square_map(list_nums) -> list:
    return list(map(lambda x: x**2, list_nums))


### ЗАДАНИЕ 4

def task4():
    new_log = MyLogger("log.txt")
    new_log.critical("Критическая ошибка!")
    new_log.debug("Дебажная муть!")
    new_log.error("Пустяковая, но явно надлежащая для увидения, ошибка!")
    new_log.warn("Банальное, иногда иногдаигнорируемое предупреждение.")
    new_log.info("Мелко-сводочная информации о ходе дела.")


