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


import unittest
from unittest.mock import patch

class TestPlayer2Turn(unittest.TestCase):

    def setUp(self):
        # Инициализируем объект игры перед каждым тестом
        self.game = PoleChudesGame("ТЕСТ", "Тема", ["Подсказка"])

    @patch('builtins.input', return_value='Т')  # Заменяем функцию input для ввода буквы
    @patch('random.choice', return_value='Т')  # Заменяем функцию random.choice для предсказуемого выбора буквы
    def test_player_2_turn_correct_guess(self, mock_input, mock_random_choice):
        # Проверяем, что функция работает правильно, когда буква угадана
        self.game.player_turn = 2  # Устанавливаем ход игрока 2
        player_2_turn(self.game)
        self.assertEqual(self.game.guessed_letters, {'Т'})
        self.assertEqual(self.game.player2_score, 0)  # Поскольку буква 'Т' в слове 'ТЕСТ', очки не должны измениться

    @patch('builtins.input', return_value='Ф')  # Заменяем функцию input для ввода буквы
    @patch('random.choice', return_value='Ф')  # Заменяем функцию random.choice для предсказуемого выбора буквы
    def test_player_2_turn_incorrect_guess(self, mock_input, mock_random_choice):
        # Проверяем, что функция работает правильно, когда буква не угадана
        self.game.player_turn = 2  # Устанавливаем ход игрока 2
        player_2_turn(self.game)
        self.assertEqual(self.game.guessed_letters, {'Ф'})
        self.assertEqual(self.game.player2_score, 0)  # Поскольку буква 'Ф' не входит в слово, очки не должны измениться

if __name__ == '__main__':
    unittest.main()
