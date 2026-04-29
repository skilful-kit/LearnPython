names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

first_day = [names[i] for i in range(len(names)) if i % 2 == 0]

print(f"Первый день: {first_day}")
