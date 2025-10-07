import math
from datetime import datetime as dt
import random as rd
import decimal as dec
import numpy 
import pandas as pan
import matplotlib.pyplot as plt
import os
import sys
from PIL import Image

def lib_numpy():
    try:
        arr = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        print("NumPy: Розмір двовимірного масиву -", arr.shape)
    except Exception as e:
        print("Помилка у NumPy:", e)
def lib_pandas():
    try:
        students = {"Студент": ["Максим", "Артем", "Степан", "Анастасія"], "Оцінка": [12, 10, 8, 11]}
        result = pan.DataFrame(students)
        print("Pandas: Таблиця студентів та їх оцінок:")
        print(result)
    except Exception as e:
        print("Помилка у Pandas:", e) 

def lib_matplotlib():
    try:
        x = [5, 4, 3, 2, 1]
        y = [7, 3, 2, 9, 6]
        plt.plot(x, y)
        plt.title("Matplotlib: Графік")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
    except Exception as e:
        print("Помилка у Matplotlib:", e)


def lib_random():
    try:
        rand_arr = []
        for i in range(0, 10):
            rand_arr.append(rd.randint(1, 100))
        print("Random: Список рандомних чисел:")
        print(rand_arr)
    except Exception as e:
        print("Помилка у Random:", e)


def lib_datetime():
    try:
        time_now = dt.now()
        print("DateTime: Теперішня дата й час -", time_now)
    except Exception as e:
        print("Помилка у DateTime:", e)  
def main():
    print(" Демонстрація роботи бібліотек Python: ")
    lib_numpy()
    print()
    lib_pandas()
    print()
    lib_random()
    print()
    lib_datetime()
    print()
    lib_matplotlib()

    
    


if __name__ == "__main__":
    main()