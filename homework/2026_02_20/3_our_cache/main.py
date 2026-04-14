def cache(func):
    storage = {}

    def wrapper(a, b):
        key = (a, b)

        if key in storage:
            return storage[key]

        result = func(a, b)
        storage[key] = result
        return result

    return wrapper


@cache
def my_sum(a, b):
    print("Подсчет")
    return a + b


print(my_sum(2, 3))
print(my_sum(2, 3))
print(my_sum(5, 1))