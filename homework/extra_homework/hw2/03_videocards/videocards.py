cards = []
n = int(input("Количество видеокарт: "))

for i in range(1, n + 1):
    card = int(input(f"{i} Видеокарта: "))
    cards.append(card)

max_card = max(cards)

new_cards = [card for card in cards if card != max_card]

print(f"Старый список видеокарт: {cards}")
print(f"Новый список видеокарт: {new_cards}")
