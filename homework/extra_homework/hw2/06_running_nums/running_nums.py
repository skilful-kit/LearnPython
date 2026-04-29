nums = list(map(int, input("Изначальный список: ").strip('[]').split(', ')))
k = int(input("Сдвиг: "))

n = len(nums)
k = k % n

for _ in range(k):
    last = nums[-1]
    for i in range(n - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = last

print(f"Сдвинутый список: {nums}")
