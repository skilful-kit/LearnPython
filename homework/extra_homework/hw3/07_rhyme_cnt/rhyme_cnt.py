n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))

people = list(range(1, n + 1))
index = 0

print(f"\nЗначит, выбывает каждый {k}-й человек")

while len(people) > 1:
    print(f"\nТекущий круг людей: {people}")
    print(f"Начало счёта с номера {people[index]}")
    
    index = (index + k - 1) % len(people)
    removed = people.pop(index)
    
    print(f"Выбывает человек под номером {removed}")
    
    if index == len(people):
        index = 0

print(f"\nОстался человек под номером {people[0]}")
