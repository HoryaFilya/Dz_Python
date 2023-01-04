s1 = str(input("Введите первую строку")) 
s2 = str(input("Введите вторую строку")) 
if len(s1) >= 2 and len(s2) >= 2:
    if s1 == s2:
        print("Обе строки равны, выведем обе:")
        print(s1)
        print(s2)
    else:
        if s1 > s2:
            print(s1)
        else:
            print(s2)
else:
    print("ERROR")



s = str(input("Введите строку из четного числа символов")) 
if len(s) % 2 == 0:
    b = int((len(s))/2)
    print(s[:b:2]+s[b::2])
else:
    print("Вы ввели нечетное число символов")



s = str(input("Введите свой email")) 
if s.count("@") == 1 and s.count(".") == 1 and len(s) >= 9:
    print("Проверка пройдена")
else:
    print("ERROR")



s = str(input("Введите строку, при этом между словами ставьте только один пробел")) 
s1 = s.strip()
s2 = s1.replace(" ", "ss")
if len(s2)-len(s1) != 0:
    kolichesto = (len(s2)-len(s1)) + 1     
    print(kolichesto)
else:
    print("1")



s = str(input("Введите строку")) 
print(s.count("ch"))