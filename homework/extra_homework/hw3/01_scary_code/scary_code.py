a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count_five = a.count(5)
print(f"Кол-во цифр 5 при первом объединении: {count_five}")

a = [x for x in a if x != 5]

a.extend(c)
count_three = a.count(3)
print(f"Кол-во цифр 3 при втором объединении: {count_three}")

print(f"Итоговый список: {a}")
