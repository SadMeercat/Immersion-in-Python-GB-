# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

from itertools import combinations

def find_all_combinations(items, max_capacity):
    all_combinations = []

    item_list = list(items.items())
    for i in range(1, len(item_list) + 1):
        for combo in combinations(item_list, i):
            total_weight = sum(item[1] for item in combo)
            if total_weight <= max_capacity:
                all_combinations.append(combo)
    return all_combinations

if __name__ == '__main__':
    items ={
        'food': 1,
        'tools': 3,
        'compass': 0.1,
        'map': 0.1,
        'flashlight': 1,
        'sleeping_bag': 2
    }

    max_capacity = 5

    all_combinations = find_all_combinations(items, max_capacity)
    
    counter = 1
    for combo in all_combinations:
        print(f'Набор {counter}')
        print(f'Общий вес: {sum(item[1] for item in combo)}')
        for i in combo:
            print(f'{i[0]}: {i[1]}')
        print()
        counter += 1