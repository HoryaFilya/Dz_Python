r = 'Red' 
g = 'Green' 
b = 'Blue' 
print(g, r, b, r + r + g, b + g, g) 



name = input('Ваше имя:')
surname = input('Ваша фамилия:')
a = input('Укажите Ваше любимое блюдо:')
b = a + "."
print("Пользователь", name, surname, "любит есть", b)
print("Порадуемся за него!")



a = input('Пункт отправления?')
b = input('Пункт прибытия?')
c = a + "-" + b
print(c)



a = input('First word: ') 
b = input('Second word: ') 
print(a, b) 
T = a
E = b
a = E
b = T
print(a, b) 
 


num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
a = str(num1)
b = str(num2)
c = a[len(a) - 1]
d = b[len(b) - 1]
n1 = int(c)
n2 = int(d)
print(n1 + n2)



num1 = int(input("Введите четырёхзначное число:"))
num2 = num1
a = str(num2)
b1 = a[len(a) - 1]
b2 = a[len(a) - 2]
b3 = a[len(a) - 3]
b4 = a[len(a) - 4]
c = b1 + b2 + b3 + b4
d = int(c)
print(d)