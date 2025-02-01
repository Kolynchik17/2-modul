from task_1 import Komanda, Mashina, Table
if __name__ == "__main__":
    komanda = Komanda(9, 2)
    mashina = Mashina(1717.17 , 'BMW')
    table = Table('Granit', 90,60,90)
    try:
        komanda.play_off(mashina)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        mashina.clas(komanda)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        table.ploshad(mashina)
    except TypeError:
        print('Ошибка: неправильные данные')