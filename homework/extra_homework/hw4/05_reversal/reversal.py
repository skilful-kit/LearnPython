s = input("Введите строку: ")

first_h = s.find('h')
last_h = s.rfind('h')

middle = s[first_h + 1:last_h]
reversed_middle = middle[::-1]

result = s[:first_h + 1] + reversed_middle + s[last_h:]

print(f"Развёрнутая последовательность между первым и последним h: {reversed_middle}")
