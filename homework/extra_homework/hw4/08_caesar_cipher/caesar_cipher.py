message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

result = ""

for char in message:
    if 'а' <= char <= 'я':
        shifted = ord(char) + shift
        if shifted > ord('я'):
            shifted -= 32
        result += chr(shifted)
    elif 'А' <= char <= 'Я':
        shifted = ord(char) + shift
        if shifted > ord('Я'):
            shifted -= 32
        result += chr(shifted)
    else:
        result += char

print(f"Зашифрованное сообщение: {result}")
