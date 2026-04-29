def find_smallest_divisor(n: int) -> int:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

n = int(input("Введите число: "))
result = find_smallest_divisor(n)
print(f"Наименьший делитель, отличный от единицы: {result}")
