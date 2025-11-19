#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря
def distance():
    for city1, coord1 in sites.items():
        distances[city1] = {}  
        for city2, coord2 in sites.items():
            if city1 != city2:  
                x1, y1 = coord1
                x2, y2 = coord2
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city1][city2] = round(distance, 2) 
    print("РАССТОЯНИЯ МЕЖДУ ГОРОДАМИ:")
    for city1 in distances:
        print(f"Из {city1}:")
        for city2, dist in distances[city1].items():
            print(f"  до {city2}: {dist}")



#print(distances)




