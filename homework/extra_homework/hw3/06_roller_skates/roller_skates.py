skates_count = int(input("Кол-во коньков: "))
skates = []
for i in range(1, skates_count + 1):
    size = int(input(f"Размер {i}-й пары: "))
    skates.append(size)

people_count = int(input("Кол-во людей: "))
feet = []
for i in range(1, people_count + 1):
    size = int(input(f"Размер ноги {i}-го человека: "))
    feet.append(size)

skates.sort()
feet.sort()

result = 0
i = j = 0

while i < len(skates) and j < len(feet):
    if skates[i] >= feet[j]:
        result += 1
        i += 1
        j += 1
    else:
        i += 1

print(f"Наибольшее кол-во людей, которые могут взять ролики: {result}")
