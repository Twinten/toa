#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
def zoo_lion():
    print('Добавление медведя')
    zoo.insert(1, 'bear')    
    print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
def zoo_birds():
    print("Добавление птиц")
    zoo.extend(birds)
    print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
def zoo_elephant():
    print("Удаление слона")
    zoo.remove('elephant')
    print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
def zoo_info():
    print ('Лев сидит в клетке номер ' + f'{zoo.index("lion") + 1}' '\nЖаворонок сидит в клетке номер '+ f'{zoo.index("lark") + 1}')
def zoo_():
    zoo_lion()
    zoo_birds()
    zoo_elephant()
    zoo_info()
