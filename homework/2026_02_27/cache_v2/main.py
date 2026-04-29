import json
import os

def cache(storage_file="cache.json", key_source="args"):
    def decorator(original_func):
        if os.path.exists(storage_file):
            with open(storage_file, 'r') as f:
                stored_cache = json.load(f)
        else:
            stored_cache = {}

        def wrapper(*args, **kwargs):
            if key_source == "args":
                cache_id = str(args)
            elif key_source == "kwargs":
                cache_id = str(sorted(kwargs.items()))
            else:
                cache_id = str(args) + str(sorted(kwargs.items()))

            if cache_id in stored_cache:
                return stored_cache[cache_id]

            computed = original_func(*args, **kwargs)
            stored_cache[cache_id] = computed

            with open(storage_file, 'w') as f:
                json.dump(stored_cache, f)

            return computed
        return wrapper
    return decorator

@cache(storage_file="sum_cache.json", key_source="args")
def my_sum(*numbers):
    return sum(numbers)

@cache(storage_file="greet_cache.json", key_source="kwargs")
def greet(**info):
    return f"Hello, {info.get('name', 'friend')}!"

print(my_sum(23, 20, -1))
print(my_sum(23, 20, -1))
print(greet(name="World"))
print(greet())
print(greet(name="World"))
