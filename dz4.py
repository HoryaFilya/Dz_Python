t = 7
v = 1/2
sec = (100-t)/v
print("Вода закипит через", sec, "секунд")



t = 7
v = 1/2
sec = (100-t)/v
min = (sec/60) // 1
newsec = sec - min * 60
if min >= 1:
    if newsec > 0:
        print("Вода закипит через", min, "минут и", newsec, "секунд")
    else:
        print("Вода закипит через", min, "минут")
else:
    print("Вода закипит через", sec, "секунд")



N = int(input("Введите число"))
L = int(input("Введите начало диапазона"))
K = int(input("Введите конец диапазона"))
if L > K:
    L, K = K, L
while L <= K:
    otvet = N * L
    print(N, "*", L, "=", otvet)
    L += 1



s = 'helloworLd1'
flag = True
i = 0
while i < len(s):
    if s[i] < '0' or s[i] > '9':
        flag = False
        break
    i += 1
if flag == True:
    print("True")
else:
    print('False')



N = str(input("Выберите товар из списка: хлеб (100 р), молоко (120 р), огурцы (60 р), апельсины (450 р)"))
sum = 0
while N != "EXIT":
    sum1 = 0
    if N == "хлеб":
        sum1 = 100
    sum2 = 0
    if N == "молоко":
        sum2 = 120
    sum3 = 0
    if N == "огурцы":
        sum3 = 60
    sum4 = 0
    if N == "апельсины":
        sum4 = 450
    sum = sum + sum1 + sum2 + sum3 + sum4
    N = str(input("Выберите товар из списка: хлеб (100 р), молоко (120 р), огурцы (60 р), апельсины (450 р)"))
print("Вы должна заплатить за товары:", sum)



m = int(input("Введите сумму вклада"))
k = int(input("Введите процент годовых"))
s = int(input("Введите желаемую сумму"))
if m < s:
    vremya = 0
    while m <= s:
        vremya += 1
        m += 0.01*k*m
    print(vremya)
else:
    print("У Вас уже есть эта сумма")



s = str(input("Введите строку"))
i = 0
j = 0
stroka = ''
kolSUM = 0
while i <= len(s) - 1:
        n = s[j]
        kol = 0
        while j <= len(s) - 1 and n == s[j]:
            kol += 1
            j += 1
        stroka = stroka + (n + str(kol))
        kolSUM = kolSUM + kol
        i = kolSUM
        j = kolSUM
print(stroka)



s = str(input("Введите текст"))
i = 0
j = 0
v = ''
flag = False
stroka = ''
kolSUM = 0
while i <= len(s) - 1:
        n = s[j]
        if n == "(":
            flag = True
            while j <= len(s) and s[j] != ")":
                stroka = stroka + s[j]
                j += 1
            stroka = stroka + s[j] + ","
            kolSUM = kolSUM + (j)
        kolSUM = kolSUM + 1
        i = kolSUM
        j = kolSUM
if flag == False:
    print(s)
else:
    d = stroka.split(",")
    k = 0
    while k < len(d):
        v = s.replace(d[k], '')
        s = v
        k += 1
print(v)



s = int(input("Выберите высоту равнобедренного треугольника"))
i = 1
vid = '*'
while i < s + 1:
    print(i*vid)
    i += 1