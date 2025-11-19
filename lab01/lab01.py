import os
from xml.sax.saxutils import prepare_input_source
import keyboard
from tasks import distance_00, circle_01, operations_02, favorite_movies_03, my_family_04, zoo_05, songs_list_06, secret_07, garden_08,shopping_09, store_10
def exit_prog():
    print("Выход из программы...")
    exit()
menu = {
    "1": ('Задача с городами', distance_00.distance),
    "2": ('Задача с кругом', circle_01.circle),
    "3": ('Задача с формулой', operations_02.operations),
    "4": ('Задача с любимыми фильмами', favorite_movies_03.favorite_movies),
    "5": ('Задача с семьёй', my_family_04.family_height),
    "6": ('Задача с зоопарком', zoo_05.zoo_),
    "7": ('Задача с песнями',songs_list_06.total_sound_time),
    "8": ('Задача с зашифрованным сообщением', secret_07.decrypted_message),
    "9": ('Задача с цветами', garden_08.flowers),
    "10": ('Задача с магазинами', shopping_09.minimal_costs),
    "11": ('Задача со складом', store_10.goods_info),
    "0": ('Выход из программы', exit_prog)
    }
def main():
    while True:
        print("="*40)
        print ('МЕНЮ ВЫБОРА ДЕЙСТВИЙ')
        print("="*40)
        for key, (descr, _) in menu.items():
            print(f'{key}. {descr}' )
        print("="*40)

        a = input("Выберите действие (0 - 11): \n")

        if a in menu:   
            os.system('cls')
            print("="*40)
            menu[a][1]()
            print("="*40)
            input("Нажмите Enter чтобы продолжить...")
            os.system('cls')          
                
        else:
            os.system('cls')
            print("Вы ввели неверное значение.")
main()





