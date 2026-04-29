class Component:
    def __init__(self, title):
        self.title = title
        self.found = False

class Formula:
    def __init__(self, first, second, outcome):
        self.first = first
        self.second = second
        self.outcome = outcome

    def check(self, a, b):
        return (a == self.first and b == self.second) or \
            (a == self.second and b == self.first)

class AlchemyLab:
    def __init__(self):
        self.components = {}
        self.found_set = set()
        self.formulas = []

        self._setup_components()
        self._setup_formulas()

    def _setup_components(self):
        starters = ["вода", "огонь", "воздух", "земля"]

        for name in starters:
            item = Component(name)
            self.components[name] = item
            self.found_set.add(name)

    def _setup_formulas(self):
        recipe_book = [
            ("вода", "земля", "грязь"),
            ("огонь", "земля", "камень"),
            ("вода", "огонь", "пар"),
            ("земля", "воздух", "пыль"),
            ("вода", "воздух", "облако"),
            ("огонь", "воздух", "энергия"),
            ("облако", "вода", "дождь"),
        ]

        for a, b, res in recipe_book:
            self.formulas.append(Formula(a, b, res))

    def mix(self, first_name, second_name):
        if first_name not in self.found_set:
            return f"Элемент {first_name} ещё не открыт!"
        if second_name not in self.found_set:
            return f"Элемент {second_name} ещё не открыт!"

        for formula in self.formulas:
            if formula.check(first_name, second_name):
                result_name = formula.outcome

                if result_name in self.found_set:
                    return f"Уже есть {result_name}!"
                if result_name not in self.components:
                    new_item = Component(result_name)
                    self.components[result_name] = new_item

                self.found_set.add(result_name)

                return f"Успех {first_name} + {second_name} = {result_name}!"
        return f"Ничего не вышло"

    def show_all(self):
        if not self.found_set:
            print(f"У вас ничего нет")
            return

        print("\nВаши элементы:")
        for name in sorted(self.found_set):
            print(f"- {name}")
        print()

    def run(self):
        print("АЛХИМИЯ")
        print("Команды: элементы, выход")

        while True:
            cmd = input("> ").strip().lower()

            if cmd == "элементы":
                self.show_all()

            elif cmd == "выход":
                print("\nКонец игры")
                break

            elif " " in cmd:
                parts = cmd.split()
                if len(parts) == 2:
                    a, b = parts[0], parts[1]
                    outcome = self.mix(a, b)
                    print(outcome + "\n")
                else:
                    print("Нужно 2 элемента через пробел")

            else:
                print("\nНеизвестная команда")

if __name__ == "__main__":
    game = AlchemyLab()
    game.run()
