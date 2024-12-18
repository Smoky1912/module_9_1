# ф-я кот. принимает список чисел и неогранич. кол-во ф-й
def apply_all_func(int_list, *functions):
    results = {} # пустой словарь для хран. рез-ов

    # перебираем все функции, переданные в *functions
    for func in functions:
        # вызов тек. ф-ии с переданным списком int_list
        result = func(int_list)
        # запис. рез-т ф-и в словарь results под ключом её названия
        results[func.__name__] = result

    # возврат словаря results
    return results

# пример
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))