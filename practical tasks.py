from collections import Counter


#  1. Разбить число на цифры


def get_numerals(some_number):
    return print([int(numeral) for numeral in str(some_number)])


#  2. Посчитать кол-во четных и нечетных цифр в числе

def get_odds_events(some_number):
    odds = [int(numeral) for numeral in str(some_number) if int(numeral) % 2 == 0]
    events = [int(numeral) for numeral in str(some_number) if int(numeral) % 2 != 0]

    return print(len(events), len(odds))


#  3. Переворачиваем список

def reverse_some_list(some_list):
    return print(some_list[::-1])


# 4. Вывести элементы первого, которые отсутствуют во втором
# добавить сохранение порядка

def delete_different_elements(list1, list2):
    return print(set(list1) - set(list2))


# 5. Убрать дубликаты в списке


def delete_similar_elements(some_list):
    # способ 1

    good_list = []
    for elem in some_list:
        if elem not in good_list:
            good_list.append(elem)

    return print(good_list)

    # способ 2
    return print(list(set(some_list)))


# 6. Посчитать количество неуникальных элементов в списке/кортеже

def get_nonunique_number(some_list):

    # способ 1 (без collections)
    nonunique_elements = []
    good_list = []
    counter = 0

    for elem in some_list:
        if some_list.count(elem) > 1:
            nonunique_elements.append(elem)
            if nonunique_elements.count(elem) <= 1:
                counter += 1
    return print('В спсике {} неуникальных элементов'.format(counter))

    # способ 2 (Counter/ Collections)
    return print(Counter(some_list.strip().lower().split()).most_common())

    #  способ 3 ( dict.fromkeys() )
    elems = some_list.lower().strip().split()
    counter = dict.fromkeys(elems, 0)
    for elem in elems:
        counter[elem] += 1

    return print(counter)

    #  способ 4

    elems = some_list.lower().strip().split()
    counter = {}
    for elem in elems:
        counter[elem] = counter.get(elem, 0) + 1
    return print(counter)

# 7. Удаление элементов из списка, не удовлетворяющих условию


def delete_elem_i_dontwant(some_list):

    good_list = [elem for elem in some_list if elem > 10]
    return print(good_list)


delete_elem_i_dontwant([3, 5, 6, 11])


# 8. Разбить строку на слова и посчитать

def split_some_str(some_str):
    return print(Counter(some_str.lower().strip().split()))

# 9. Удалить ненужные пробелы


def delete_bad_spaces(some_str):
    new_str = ''
    str_list = some_str.strip().split()
    for elem in str_list:
        new_str += str(elem) + ' '
    return print(new_str)

# 10. Оставить строки, которые содержат подстроку


def get_good_str(some_list):
    good_list = [elem for elem in some_list if elem.find('ha') >= 0]
    return print(good_list)


get_good_str(['hahaha', 'hh,', 'hhhhhhha', 'gffff', '7ha'])

# 11. Дан список пар координат. Найдите те, которые заданы неверно


def delete_bad_geo(geo_list):
    good_geo = []
    for elem in geo_list:
        numbers = elem.strip().split()
        if -90 < int(numbers[0]) < 90 and -180 < int(numbers[1]) < 180:
            good_geo.append(elem)
    return print(good_geo)


# 12. Найти неверно закрывающуюся скобку в выражении

def get_badly_closed_bracket(string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return i
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                return i
    return 'OK'


print(get_badly_closed_bracket('{)'))




























