import numpy as np


def game_core(number):
    """Применяем бинарный поиск"""
    count = 0
    first = 1
    last = 100
    while True:
        count += 1
        predict = (first + last) // 2  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали
        elif number > predict:
            first = predict + 1
        else:
            last = predict - 1


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core)
