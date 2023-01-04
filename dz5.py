def k_isalpha(s: str) -> bool:
    i = 0
    while i < len (s):
        if not (s[i] >= 'A' and s[i] <= 'Z' or s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'А' and s[i] <= 'я'):
            return False
        i += 1
    return True



def k_islower(s: str) -> bool:
    i = 0
    while i < len (s): 
        if (s[i] >= 'A' and s[i] <= 'Z' or s[i] >= 'А' and s[i] <= 'Я'):
            return False
        i += 1
    j = 0
    kol = 0
    while j < len (s): 
        if (s[j] >= 'a' and s[j] <= 'z' or s[j] >= 'а' and s[j] <= 'я'):
            kol += 1
        j += 1
    if kol == 0:
        return False
    return True



def k_istitle(s: str) -> bool:
    s = s.lstrip()
    if not (s[0] >= 'A' and s[0] <= 'Z' or s[0] >= 'А' and s[0] <= 'Я'):
        return False
    i = 1
    while i < len(s):
        if (s[i] >= 'A' and s[i] <= 'Z' or s[i] >= 'А' and s[i] <= 'Я'):
            return False
        i += 1
    return True



def k_upper(s: str) -> str:
    i = 0
    s_new = ''
    while i < len (s):
        if (s[i] < 'a' or 'z' < s[i] < 'а' or 'я' < s[i]):
            s_new += s[i]
        elif 'a' <= s[i] <= 'z':
            nomer = ord(s[i]) - 32
            bykva = chr(nomer)
            s_new += bykva
        elif 'а' <= s[i] <= 'я':
            nomer = ord(s[i]) + 95
            bykva = chr(nomer)
            s_new += bykva
        i += 1
    s = s_new
    return s



def k_endswith(s: str, substring: str) -> bool:
    if (s[-1:-len(substring)-1:-1]) == substring[-1:-len(substring)-1:-1]:
        return True
    return False



def k_count(s: str, substring: str) -> int:
    i = 0
    sum = 0
    while i < (len (s) - len (substring)) + 1:
        if (s[i:i+len(substring):]) == substring:
            sum += 1
        i += 1
    return sum



def k_strip(s: str) -> str:
    k = 0
    s_new = ''
    while k < len(s):
        if ord(s[k]) == 92 and s[k+1] == 'n':
            s_new += "\n"
            k += 1
        elif ord(s[k]) == 92 and s[k+1] == 't':
            s_new += "\t"
            k += 1
        else:
            s_new += s[k]
        k += 1
    s = s_new
    i = 0
    while s[i] == ' ':
        i += 1
    j = -1
    while s[j] == ' ':
        j -= 1
    return s[i:len(s)+j+1:1]



def k_replace(s: str, oldvalue: str, newvalue: str, count: int) -> str:
    i = 0
    sum = 0
    s_new = ''
    if oldvalue == '':
        oldvalue = ' '
    if len(s) < len(oldvalue):
        return s
    while i < len(s):
        j = 0
        if s[i] == oldvalue[j]:
            while j < len(oldvalue):
                if s[i] == oldvalue[j]:
                    i += 1
                    j += 1
            sum += 1
            s_new += newvalue
            i -= 1
        else:
            s_new += s[i]
        i += 1
        if sum == count:
            s_new += s[i:len(s):]
            s = s_new
            return s
    s = s_new
    return s