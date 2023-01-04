def foo(s: str) -> dict:
    d = {}
    lst = s.lower().split()
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

s = str(input('Введите строку'))
print(foo(s))