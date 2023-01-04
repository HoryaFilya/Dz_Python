num1 = int(input("Введите первое число:")) 
num2 = int(input("Введите второе число:")) 
num3 = int(input("Введите результат их произведения:")) 
c = num1 * num2
if c == num3:
    print("Вы правы")
else:
    print("Неправильный ответ!")



c = int(input("Введите номер дня недели:")) 
if c == 1:
    print("Расписание на понедельник: русский, математика")
elif c == 2:
    print("Расписание на вторник: русский, физика")
elif c == 3:
    print("Расписание на среду: английский, биология")
elif c == 4:
    print("Расписание на четверг: английский, история")
elif c == 5:
    print("Расписание на пятницу: химия, литература")
elif c == 6:
    print("Сегодня у тебя первый выходной!")
elif c == 7:
    print("Сегодня у тебя второй выходной!")
else:
    print("Введите число в диапазоне 1-7")



# y = 10
# y > x * x or y >= 2 * x and x < y

# Порядок:
# x * x = 25
# 2 * x = 10
# y > x * x = False
# y >= 2 * x = True
# x < y = True
# y >= 2 * x and x < y = True
# y > x * x or y >= 2 * x and x < y = True
# Ответ: True



c = int(input("Введите число")) 
if 10 <= c <= 99 or -99 <= c <= -10:
    print("Число двузначное!")
else:
    print("Число не двузначное!")



num1 = int(input("Введите первое число")) 
num2 = int(input("Введите второе число")) 
num3 = int(input("Введите третье число")) 
if num1 >= num2:
    if num1 >= num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 >= num3:
        print(num2)
    else:
        print(num3)



num1 = str(input("Введите первое число")) 
num2 = str(input("Введите второе число")) 
num3 = str(input("Введите операцию")) 
a = int(num1)
b = int(num2)
if num3 == ("+"):
    print(a + b)
elif num3 == ("-"):
    print(a - b)
elif num3 == ("/"):
    print(a / b)
elif num3 == ("*"):
    print(a * b)
elif num3 == ("mod"):
    print(a % b)
elif num3 == ("pow"):
    print(a ** b)
elif num3 == ("div"):
    print(a // b)
else:
    print("Вы ввели несуществующую операцию")



a = int(input("Введите первое число")) 
b = int(input("Введите второе число")) 
if a % b == 0:
    print("a на b делится нацело")
else:
    print("a на b НЕ делится нацело")
if b % a == 0:
    print("b на a делится нацело")
else:
    print("b на a НЕ делится нацело")



a = int(input("Введите трёхзначное число")) 
tmp1 = a //10
tmp2 = a //100
b3 = a % 10
b2 = tmp1 % 10
b1 = tmp2 % 10
if b3 == b2 or b3 == b1 or b2 == b1:
    print("Есть одинаковые цифры")
else:
    print("Нет одинаковых цифр")