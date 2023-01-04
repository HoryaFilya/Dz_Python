def foo(N, ch):
    i = 0
    while i/len(ch) < N:
        print(N*ch)
        i += 1



def foo():
    from random import randint
    lst = [randint(1, 100) for _ in range(5)]
    flag = True
    for i in lst:
        if i <= 50:
            return False
    return True



def foo():
    lst = []
    addpapa = ['молоко', 'огурцы', 'пиво', 'рыбка']
    addbabyshka = ['чай', 'сахар', 'сухарики']
    lst = addpapa + addbabyshka
    delmama = ['пиво', 'рыбка']
    i = 0
    while i < len(delmama):
        if delmama[i] in lst:
            lst.remove(delmama[i])
        i += 1
    print('Список покупок:', lst)
    print('Количество покупок:', len(lst))



def foo():
    lst = [1, -3, 4, 7, 9]
    a = int(input("Введите число"))
    if a in lst:
        return 'Число присутствует в списке'
    return 'Число отсутствует в списке'



def foo():
    lst = [4, -3, 4, 7, 4]
    a = int(input("Введите число"))
    sum = 0
    for i in lst:
        if i == a:
            sum += 1
    print('Число встречается', sum, 'раз')