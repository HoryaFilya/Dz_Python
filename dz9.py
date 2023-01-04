import json

def foo():
    d = {}
    lst = []
    k = 0
    kol = 0
    with open('./log_100.json') as f:
        text = json.load(f)
    for i in range(len(text)):
        if text[i]['ip'] in d:
            d[text[i]['ip']] += 1
        else:
            d[text[i]['ip']] = 1
    d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
    for i in d:
        if k == 3:
            vklad = (sum(lst)/sum(d.values()))*100
        lst.append(d[i])
        if d[i] == 1:
            kol += 1
        k += 1
    return f'Общий вклад топ-3 всех IP по количеству посещений: {vklad} %\nКоличество уникальных IP: {kol}'

print(foo())





import csv

def foo():
    with open('./log_full.csv') as f:
        reader = csv.reader(f)
        d = {}
        lst = []
        for i in reader:
            lst.append(i)
            if i[1] in d:
                d[i[1]] += 1
            else:
                d[i[1]] = 1
        d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        for i in d:
            ip = i
            fraction = (d[i]/(sum(d.values()) - 1))*100
            count = d[i]
            break  
        lst.reverse()
        for j in lst:
            if j[1] == i:
                agent = j[2]
                timestamp = j[0]
                break
    suspicious_agent = {
    "ip": ip,                                                
    'fraction': fraction,           
    'count': count,                                    
    'last': {                                               
        'agent': agent,                                    
        'timestamp': timestamp,                                  
        }
    }
    return suspicious_agent

print(foo())