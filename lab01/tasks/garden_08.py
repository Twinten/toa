#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
# TODO здесь ваш код
def all_flowers():
    print(garden_set | meadow_set)

# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
def common_flowers():
    print(garden_set & meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
def uniq_garden_flowers():
    print(garden_set - meadow_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
def uniq_meadow_flowers():
    print(meadow_set - garden_set)

def flowers():
    print("Все виды цветов")
    all_flowers()
    print("Цветы, которые растут и там и там")
    common_flowers()
    print("Цветы, которые растут в саду, но не растут на лугу")
    uniq_garden_flowers()
    print("Цветы, которые растут на лугу, но не растут в саду")
    uniq_meadow_flowers()
