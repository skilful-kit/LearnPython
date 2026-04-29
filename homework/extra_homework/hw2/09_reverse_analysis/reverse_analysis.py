nums = list(map(int, input("Введите список чисел: ").strip('[]').split(', ')))

print("Чётные числа в обратном порядке:")
for i in range(len(nums) - 1, -1, -1):
    if nums[i] % 2 == 0:
        print(nums[i])
