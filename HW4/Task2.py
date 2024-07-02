# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs):
    result ={}
    for key in kwargs:
        value = kwargs[key]
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

result_dict = create_dict(tent=3, sleeping_bag=2, water_bottle=[1, 2, 3], food=4, stove=2)
print(result_dict)