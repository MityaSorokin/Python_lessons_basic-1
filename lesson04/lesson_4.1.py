from sys import argv

script_name, first_param, second_param, third_param = argv

print('Имя скрипта: ', script_name)
print('Параметр 1', first_param)
print('Параметр 2', second_param)
print("Параметр 3", third_param)
# -----------------------------------1-----------------------------
'''
Реализовать скрипт, в котором должна быть предусмотрена
 функция расчета заработной платы сотрудника. В расчете
 необходимо использовать формулу:
 (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо
 запускать скрипт с параметрами.
'''

# ------------------------------------2-----------------------------
'''
Представлен список чисел. Необходимо вывести элементы
исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить
в виде списка. Для формирования списка использовать генератор.
'''
# ------------------------------------3----------------------------
'''
Для чисел в пределах от 20 до 240 найти числа,
кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''
# ------------------------------------4----------------------------
'''
Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''
# ------------------------------------5----------------------------
'''
Реализовать формирование списка, используя
функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000
(включая границы). Необходимо получить результат
вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
# ------------------------------------6----------------------------
'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
начиная с указанного,
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.
'''
# ------------------------------------7----------------------------
'''
Реализовать генератор с помощью функции с ключевым
словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом:
for el in fibo_gen().
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые 15 чисел.
Подсказка: факториал числа n — произведение
чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''