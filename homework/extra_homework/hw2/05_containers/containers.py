containers = []
n = int(input("Количество контейнеров: "))

for i in range(n):
    weight = int(input("Введите вес контейнера: "))
    while weight > 200:
        weight = int(input("Вес не должен превышать 200. Введите снова: "))
    containers.append(weight)

new_weight = int(input("Введите вес нового контейнера: "))
while new_weight > 200:
    new_weight = int(input("Вес не должен превышать 200. Введите снова: "))

position = 1
for weight in containers:
    if new_weight <= weight:
        position += 1
    else:
        break

print(f"Номер, который получит новый контейнер: {position}")
