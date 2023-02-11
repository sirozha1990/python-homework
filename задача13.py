# Задача13.Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def exp(a, b): 
    if b == 0: 
        return 1 
    elif b == 1: 
        return a 
    else: 
        return a * exp(a, b - 1) 
  
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print("A в степени B: ", exp(a, b))
