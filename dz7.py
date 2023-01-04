def read_last(lines: int, file: str):
    with open(file, 'r', encoding = 'utf-8') as f:
        lst = f.readlines()
        if len(lst) >= lines:
            i = len(lst) - lines
            lst_new = []
            while i < len(lst):
                lst_new.append(lst[i])
                i += 1
            return lst_new
        return lst



def longest_words(file: str):
    with open(file, 'r', encoding = 'utf-8') as f:
        lst = f.readlines()
        lst_new = []
        elem = ''
        for j in range(len(lst)):
            a = lst[j].split(' ')
            for i in a:
                if '\n' in i:
                    i = i[:-1]
                if len(i) > len(elem):
                    elem = i
                    lst_new.clear()
                    lst_new.append(i)
                elif len(i) == len(elem):
                    elem = i
                    lst_new.append(i)
        return lst_new



def get_basket_amount(file: str) -> int:
    with open(file, 'r', encoding = 'utf-8') as f:
        lst = f.readlines()
        sum = 0
        for i in range(len(lst)):
            j = 0
            while lst[i][j] != ' ':
                j += 1
            while lst[i][j] == ' ':
                j += 1
            k = j
            while lst[i][k] != ' ':
                k += 1
            kol = int(lst[i][j:k])
            while lst[i][k] == ' ':
                k += 1
            m = k
            while '0' <= lst[i][m] <= '9':
                m += 1
            price = int(lst[i][k:m])
            sum += kol * price
        return sum