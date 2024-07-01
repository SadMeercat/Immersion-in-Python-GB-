# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.


if __name__ == '__main__':
    my_list = [1, 2, 3, 1, 3, 4, 5, 6, 3, 5]
    result = []

    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] in result:
                break
            elif my_list[i] == my_list[j]:
                result.append(my_list[i])

    print(result)