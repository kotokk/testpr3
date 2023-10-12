import random


class PoleChudesGame:
    def __init__(self, word, topic, hints):
        self.word = word.upper()
        self.hidden_word = ['_' if char.isalpha() else char for char in self.word]
        self.topic = topic
        self.hints = hints
        self.guessed_letters = set()
        self.player1_score = 0
        self.player2_score = 0
        self.current_turn_score = 0
        self.total_score = 0
        self.player_turn = 1  # Игрок 1 начинает

    def display_word(self):
        return ' '.join(self.hidden_word)

    def display_hints(self):
        return ', '.join(self.hints)

    def spin_wheel(self, guessed):
        wheel = [600, 600, 100, 1000, 0, 700, 700, 700, 200, 300, 500, "ПРИЗ", 0, 900, 400, 800, 13]
        result = random.choice(wheel)
        
        print("\nКрутим барабан...")
        print(f"Результат кручения барабана: {result}")

        if(guessed):
            if isinstance(result, int):
                self.current_turn_score = result
                print(f"Очки игрока {self.player_turn} в текущем ходе: {self.current_turn_score}")
                self.switch_player_turn()
            elif result == "ПРИЗ":
                print("Вы выиграли ПРИЗ - клубничку!")
                print(f"""⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⢀⠀⠀
⠀⠀⠀⠀⠀⠀⣏⠓⠒⠤⣰⠋⠹⡄⠀⣠⠞⣿⠀⠀
⠀⠀⠀⢀⠄⠂⠙⢦⡀⠐⠨⣆⠁⣷⣮⠖⠋⠉⠁⠀
⠀⠀⡰⠁⠀⠮⠇⠀⣩⠶⠒⠾⣿⡯⡋⠩⡓⢦⣀⡀
⠀⡰⢰⡹⠀⠀⠲⣾⣁⣀⣤⠞⢧⡈⢊⢲⠶⠶⠛⠁
⢀⠃⠀⠀⠀⣌⡅⠀⢀⡀⠀⠀⣈⠻⠦⣤⣿⡀⠀⠀
⠸⣎⠇⠀⠀⡠⡄⠀⠷⠎⠀⠐⡶⠁⠀⠀⣟⡇⠀⠀
⡇⠀⡠⣄⠀⠷⠃⠀⠀⡤⠄⠀⠀⣔⡰⠀⢩⠇⠀⠀
⡇⠀⠻⠋⠀⢀⠤⠀⠈⠛⠁⠀⢀⠉⠁⣠⠏⠀⠀⠀
⣷⢰⢢⠀⠀⠘⠚⠀⢰⣂⠆⠰⢥⡡⠞⠁⠀⠀⠀⠀
⠸⣎⠋⢠⢢⠀⢠⢀⠀⠀⣠⠴⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠘⠷⣬⣅⣀⣬⡷⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        else:
            print("Чтобы получить очки, надо букву угадать!")
            self.switch_player_turn()

    def guess_letter(self, letter):
        letter = letter.upper()
        if letter.isalpha() and letter not in self.guessed_letters:
            self.guessed_letters.add(letter)
            if letter in self.word:
                for i, char in enumerate(self.word):
                    if char == letter:
                        self.hidden_word[i] = letter
                        self.update_scores()  # Обновляем очки текущего игрока
                
                return True  # Правильно угадана буква
        return False  # Буква не входит в слово

    def switch_player_turn(self):
        self.player_turn = 3 - self.player_turn  # Переключение между 1 и 2 игроками

    def update_scores(self):
        if self.player_turn == 1:
            self.player1_score += self.current_turn_score
        else:
            self.player2_score += self.current_turn_score


def player_2_turn(game):
    print("\nХод игрока 2:")
    available_letters = [letter for letter in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" if letter not in game.guessed_letters]
    if available_letters:
        guessed_letter = random.choice(available_letters)
        print(f"Игрок 2 называет букву: {guessed_letter}")
        result = game.guess_letter(guessed_letter)
        if result:
            print(f"ДАЙТЕ ПРОЧИТАТЬ СТИХ!")
            
        else:
            print(f"ВОТ ЧЕРТ!")
        game.spin_wheel(result)

def is_valid_letter(user_input, game):
    # Проверка на пустой ввод
    if not user_input:
        print("Вы ввели пустую строку. Пожалуйста, введите букву.")
        return False

    # Проверка на русскую букву
    if not user_input.isalpha() or user_input not in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
        print("Некорректный ввод. Введите русскую букву.")
        return False

    # Проверка, что буква еще не угадывалась
    if user_input in game.guessed_letters:
        print("Эта буква уже угадывалась. Пожалуйста, введите другую букву.")
        return False

    return True

    

# Пример использования:
def is_valid_player_name(player_name):
    try:
        # Проверка, что введено не пустое имя
        if not player_name.strip():
            raise ValueError("Имя не должно быть пустым. Пожалуйста, введите корректное имя.")

        # Проверка, что введено только буквенное имя
        if not player_name.isalpha():
            raise ValueError("Имя должно состоять только из букв. Пожалуйста, введите корректное имя.")

        # Если все проверки пройдены успешно, вернуть True
        return True

    except ValueError as e:
        # Обработка и вывод сообщения об ошибке
        print(f"Ошибка: {e}")
        # Вернуть False, если имя не соответствует критериям
        return False

# Пример использования
while True:
    player1_name = input("Введите имя игрока: ")
    if is_valid_player_name(player1_name):
        print("Добро пожаловать в игру, ", player1_name, "!")
        break

# Здесь вы можете продолжить выполнение кода с действительным именем игрока.

player2_name = "Денис"

print(f"\nИгрок 1: {player1_name}")
print(f"Игрок 2: {player2_name}")

word_to_guess = "ПИТОН"
game_topic = "Язык программирования"
game_hints = ["Интерпретируемый", "Создан Гвидо ван Россумом"]

game = PoleChudesGame(word_to_guess, game_topic, game_hints)

while True:
    print(f"\nТема: {game.topic}")
    print(f"Угаданное слово: {game.display_word()}")
    print(f"Доступные подсказки: {game.display_hints()}")
    
    if game.player_turn == 1:
        print(f"\nХод игрока {player1_name} (введите 'стоп' чтобы завершить игру):")
        while True:
            user_input = input("Введите букву: ").upper()

            if user_input == 'СТОП':
                break

            if is_valid_letter(user_input, game):
                result = game.guess_letter(user_input)
                break

            if user_input == 'СТОП':
                break

        game.spin_wheel(result)


    else:
        print(f"{player2_name} делает свой ход:")
        player_2_turn(game)

    if all(letter.isalpha() and letter != '_' for letter in game.hidden_word):
        print("\nПоздравляем! Вы угадали слово!")
        break

print(f"\nИгра завершена. Итоговые очки:")
print(f"Очки {player1_name}: {game.player1_score}")
print(f"Очки {player2_name}: {game.player2_score}")

