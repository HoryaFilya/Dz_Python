import random

class CardGame:

    players = {}        # игроки


    def __init__(self, name):
        CardGame.players[name] = {                  # {игрок: {'карта': [количество_карт, значимость_карты]}}
        '6': [0, 6],
        '7': [0, 7],
        '8': [0, 8],
        '9': [0, 9],
        '10': [0, 10],
        'jack': [0, 11],
        'lady': [0, 12],
        'king': [0, 13],
        'ace': [0, 14],
    }


    def creating_a_deck():
        CardGame.dict_map_quantity = {              # {колода_карт: {'карта': [количество_карт, значимость_карты]}}
        '6': [4, 6],
        '7': [4, 7],
        '8': [4, 8],
        '9': [4, 9],
        '10': [4, 10],
        'jack': [4, 11],
        'lady': [4, 12],
        'king': [4, 13],
        'ace': [4, 14],
    }
        print('Колода создана!')


    def distribution_of_cards():
        if len(CardGame.players.keys()) >= 2:       # проверка количества игроков
            for j in range(6):                      # раздача по 6 карт каждому игроку
                for i in CardGame.players:
                    map = random.choice(list(CardGame.dict_map_quantity.keys()))            # генерация случайной карты игроку
                    while CardGame.dict_map_quantity[map][0] == 0:                          # проверка, что карты остались
                        map = random.choice(list(CardGame.dict_map_quantity.keys()))
                    CardGame.players[i][map][0] += 1                                        # добавляем карту игроку
                    CardGame.dict_map_quantity[map][0] -= 1                                 # убираем отданную карту из колоды
            print('Карты розданы!')
        else:
            print('Для игры необходимо минимум 2 игрока')
    

    def print_info():
        for i in CardGame.players:
            print(i, CardGame.players[i])


    def map_comparison():
        number_of_points = []       # имена и очки всех игроков
        champions = []              # победитель игры
        maximum_points = 0
        for i in CardGame.players:
            sum = 0
            for j in CardGame.players[i].values():
                sum += (j[0] * j[1])
            number_of_points.append(f'Игрок: {i}; количество очков: {sum}')
            if sum > maximum_points:
                champions.clear()
                maximum_points = sum
                champions.append(f'Победитель игры - {i}, количество очков - {sum}')
            elif sum == maximum_points:
                maximum_points = sum
                champions.append(f'Победитель игры - {i}, количество очков - {sum}')
        print(number_of_points)
        print(champions)




class Shop:
    
    products = {}


    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Shop.products[name] = [price, quantity]
    

    def get_info(self):
        print(f'Товар - {self.name}, цена - {self.price}, количество на складе - {self.quantity}')


    def add_product(name, price, quantity):
        Shop.products[name] = [price, quantity]
    

    def delete_product(name):
        Shop.products.pop(name)
    

    def buy_product(name, money, quantity):
        if name in Shop.products and quantity > Shop.products[name][1]:
            print(f'В наличии осталось только {Shop.products[name][1]} товара')
        
        elif name in Shop.products and quantity <= 0:
            print(f'Вы ничего не купили')
        
        elif name in Shop.products and quantity <= Shop.products[name][1] and money < Shop.products[name][0] * quantity:
            print(f'Недостаточно денег')

        elif name in Shop.products and quantity <= Shop.products[name][1] and money >= Shop.products[name][0] * quantity:
            print(f'Держите {name}, сдача {money - Shop.products[name][0] * quantity} рублей')
            Shop.products[name][1] = Shop.products[name][1] - quantity
        
        else:
            print('Такого товара в магазине нет')


    def search_product_by_price(price):
        search_product_by_price = {}
        for i in Shop.products:
            if Shop.products[i][0] == price:
                search_product_by_price[i] = [price, Shop.products[i][1]]
        if len(search_product_by_price) != 0:
            print(f'По такой цене найдены товары:\n{search_product_by_price}')
        else:
            print('По такой цене товаров не найдено')
    



# 3) Реализовать алгоритм Дейкстры для нахождения кратчайшего пути в графе.

# class Algorithm:

#     connection = {}
#     points = []

#     def __init__(self, first_point, second_point, distance):
#         if isinstance(first_point, str) and isinstance(second_point, str) and isinstance(distance, (int, float)):
#             self.first_point = first_point
#             self.second_point = second_point
#             self.distance = distance
#             Algorithm.connection[first_point, second_point] = distance
#             Algorithm.points.append(first_point)
#             Algorithm.points.append(second_point)
#         else:
#             print('Error')
    

#     def shortest_path(first_point, second_point):
#         path = {}
#         if isinstance(first_point, str) and isinstance(second_point, str) and \
#             first_point in Algorithm.points and second_point in Algorithm.points:

#             for i in Algorithm.connection:
#                 if i[0] == first_point:
#                     path[first_point, i[1]] = Algorithm.connection[(first_point, i[1])]
#             print(path)

#             for i in Algorithm.connection:
#                 for j in path:
#                     if i[0] == j[1]:
#                         path[first_point, i[1]] = Algorithm.connection[(first_point, i[1])]
#             print(path)

#         else:
#             print('Error')

# pyth1 = Algorithm('a', 'b', 10)
# pyth2 = Algorithm('a', 'c', 5)
# pyth3 = Algorithm('b', 'd', 5)
# pyth4 = Algorithm('b', 'c', 5)
# print(Algorithm.connection)
# print(Algorithm.points)
# Algorithm.shortest_path('a', 'b')