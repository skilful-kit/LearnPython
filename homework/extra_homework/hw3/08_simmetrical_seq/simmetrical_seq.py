n = int(input("Кол-во чисел: "))
seq = []
for i in range(n):
    num = int(input(f"Число: "))
    seq.append(num)

print(f"\nПоследовательность: {seq}")

for i in range(n):
    suffix = seq[i:]
    if suffix == suffix[::-1]:
        to_add = seq[:i][::-1]
        print(f"Нужно приписать чисел: {len(to_add)}")
        print(f"Сами числа: {to_add}")
        break
