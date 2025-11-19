#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Отец","Мать","Сестра","Брат"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Андрей',175],
    ['Мария',183],
    ['София',167],
    ['Георгий',171]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
def father_height():    
    print("Роста отца - " + f'{my_family_height[0][1]}' + " см") 
    

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
def total_height():
    total_height = 0
    for i in range(len(my_family_height)):
        total_height = total_height + my_family_height[i][1]
    print('Общий рост моей семьи - ' + f'{total_height}' + ' см')
def family_height():
    father_height()
    total_height()

