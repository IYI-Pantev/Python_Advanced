import time

ef_cache = {}

def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]
    print(f"Computing {num}...")
    time.sleep(1)
    result = num*num
    ef_cache[num] = result
    return result

print(expensive_func(4))
print(expensive_func(10))
print(expensive_func(4))
print(expensive_func(10))