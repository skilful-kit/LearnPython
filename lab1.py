class Player:
    def __init__(self, name, wins=0, played=0, item=0):
        self.name = name
        self.wins = wins
        self.played = played
        self.item = item

    @property
    def winrate(self):
        if self.played == 0:
            return 0
        return round((self.wins / self.played) * 100, 2)

    def __str__(self):
        return f"Игрок: {self.name} | Побед: {self.wins} | Игр: {self.played} | Винрейт: {self.winrate}%"


def determine_winner(item1, item2):
    if item1 == item2:
        return 0
    if (item1 == 1 and item2 == 2) or (item1 == 2 and item2 == 3) or (item1 == 3 and item2 == 1):
        return 1
    return 2


def game_round(player1, player2):
    p1_item = player1.item
    p2_item = player2.item
    winner = determine_winner(p1_item, p2_item)
    
    if winner == 0:
        print(f"Ничья! {player1.name} и {player2.name} выбрали одинаково")
    elif winner == 1:
        player1.wins += 1
        print(f"Победил {player1.name}!")
    else:
        player2.wins += 1
        print(f"Победил {player2.name}!")
    
    player1.played += 1
    player2.played += 1


def count_of_players():
    count_players = int(input("Сколько игроков будет играть? "))
    player_list = []
    for i in range(count_players):
        name = input(f"Введите никнейм {i + 1}-го игрока: ")
        new_player = Player(name)
        print("Игрок создан!")
        player_list.append(new_player)
    return player_list


def stats(player_list):
    print("\n--- СТАТИСТИКА ИГРОКОВ ---")
    for p in player_list:
        print(p)
    print("----------------------------\n")


def choose(player_list):
    for p in player_list:
        while True:
            try:
                p.item = int(input(p.name + ", выбери чем играешь (1 - камень, 2 - ножницы, 3 - бумага): "))
                match p.item:
                    case 1:
                        print("  Выбран камень")
                        break
                    case 2:
                        print("  Выбраны ножницы")
                        break
                    case 3:
                        print("  Выбрана бумага")
                        break
                    case _:
                        print("Неправильный выбор! Введите 1, 2 или 3")
            except ValueError:
                print("Введите число!")


def start_game():
    players = count_of_players()
    
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            print(f"\n--- РАУНД: {players[i].name} против {players[j].name} ---")
            choose([players[i], players[j]])
            game_round(players[i], players[j])
    
    print("\n=== ИТОГОВАЯ СТАТИСТИКА ===")
    stats(players)
    
    winner = max(players, key=lambda p: p.wins)
    print(f"ПОБЕДИТЕЛЬ: {winner.name} с {winner.wins} победами!")


def main_menu():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1 - Играть")
        print("2 - Смотреть статистику")
        print("3 - Выход")
        
        try:
            choice = int(input("Выберите действие: "))
            match choice:
                case 1:
                    start_game()
                case 2:
                    print("Сначала сыграйте!")
                case 3:
                    print("До свидания!")
                    break
                case _:
                    print("Неверный выбор!")
        except ValueError:
            print("Введите число!")


main_menu()
