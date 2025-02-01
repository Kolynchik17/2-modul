# TODO
class Komanda:
    def __init__(self, kol: int, pobed: int):
        self.kol=kol
        self.pobed=pobed
        if not (isinstance(self.kol,int) and isinstance(self.pobed, int) ):
            raise TypeError #число игроков в команде и количество побед должны быть типа int
        if (self.kol<0 and self.pobed<0):
            raise TypeError #число игроков в команде и количество побед должны быть положительными числами
    def dobavlenie_igroka(self, dob): #Проверяет можно ли добавить dob игроков в команду
        if (self.kol>=5 and self.kol<=11):
            self.kol= self.kol+ dob
            if (self.kol >= 5 and self.kol <= 11):
                return self.kol
            else:
                return TypeError
        else:
            return TypeError
    def proverka_komandi(self):
        if (self.kol>=5 and self.kol<=12 and isinstance(self.kol, int)): #проверяет количество человек в команде лежит в диапозоне от 5 до 12 человек включительно
            return True
        else:
            return False
    def play_off(self): # проверяет прошла ли команда в следующий раунд
        if self.pobed>=17:
            return 'Popala v play off'
        else:
            return ('Ne xvatilo ', 17-self.pobed, ' pobed dly vixoda v play off')

class Mashina:
    def __init__(self, probeg: float, marka: str):
        self.probeg= probeg
        self.marka = marka
        if not (isinstance(self.probeg, (float, int)) and isinstance(self.marka, str) ):
            raise TypeError # пробег должен быть либо float либо int, а марка должна быть типа str
        if self.probeg<0:
            raise TypeError #пробег не может быть отрицательным
    def sostoynie(self):
        """
        проверяет состояние машины
        """
        if (self.probeg>=250000):
            return "Staray machina"
        else:
            return "Novay machina"
    def clas(self):
        """
        проверяет какого класса является машина
        """
        if (self.marka=='BMW' or self.marka=='AUDI' or self.marka=='Mersedes-Bens'):
            return "Bisnes class"
        else:
            return ' Econom class'
class Table:
    def __init__(self, material: str, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height
        self.material = material
         # проверит правильные ли типы данных
        if not isinstance(self.material, str):
            raise TypeError("Материал должен быть строкой")

        if not all(isinstance(dim, (int, float)) for dim in (self.length, self.width, self.height)):
            raise TypeError("Длина, ширина и высота должны быть типа int или float")

        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            raise ValueError("Длина, ширина и высота должны быть положительными числами")

    def ploshad (self): # вычисляет площадь стола
        return self.length * self.width
    def opisanie (self): # возращает описание стола
        return f'Стол из материала {self.material} размером {self.length} см х {self.width} см х {self.height} см.'

import doctest
if __name__ == "__main__":
    doctest.testmod()
# TODO
