text = input("Введите текст: ")

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowel_list = []

for char in text:
    if char in vowels:
        vowel_list.append(char)

print(f"Список гласных букв: {vowel_list}")
print(f"Длина списка: {len(vowel_list)}")
