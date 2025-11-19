#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [       
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99}

        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],    
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
    'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99}
        ]
}
# Указать надо только по 2 магазина с минимальными ценами
def minimal_costs():
    min_price = 99.99
    min_coockie = {'shop': 'name shop' , 'price' : 99.99}
    for i in sweets['печенье']:
        if i['price']< min_coockie['price']:
            min_coockie['shop'] = i['shop']
            min_coockie['price'] = i['price']
    print('В магазине ' + f'{min_coockie["shop"]}' + ' минимальная цена на печенье: ' + f'{min_coockie["price"]}')
    min_candies = {'shop': 'name shop' , 'price' : 99.99}
    for i in sweets['конфеты']:
        if i['price']< min_candies['price']:
            min_candies['shop'] = i['shop']
            min_candies['price'] = i['price']
    print('В магазине ' + f'{min_candies["shop"]}' + ' минимальная цена на конфеты: ' + f'{min_candies["price"]}')

