def sum_of_digits(n: int) -> int:
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

def count_of_digits(n: int) -> int:
    return len(str(n))

n = int(input("Введите число: "))

sum_digits = sum_of_digits(n)
count_digits = count_of_digits(n)
difference = sum_digits - count_digits

print(f"Сумма чисел: {sum_digits}")
print(f"Количество цифр в числе: {count_digits}")
print(f"Разность суммы и количества цифр: {difference}")
