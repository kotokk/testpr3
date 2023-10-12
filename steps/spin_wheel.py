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
    
    def switch_player_turn(self):
        self.player_turn = 3 - self.player_turn  # Переключение между 1 и 2 игроками

    def spin_wheel(self, guessed):
        wheel = [600, 600, 100, 1000, 0, 700, 700, 700, 200, 300, 500, "ПРИЗ", 0, 900, 400, 800, 13]
        result = random.choice(wheel)
        
        print("\nКрутим барабан...")
        print("Результат кручения барабана: {result}")

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


import unittest
from unittest.mock import patch

class TestSpinWheelMethod(unittest.TestCase):

    def setUp(self):
        # Метод setUp будет вызван перед каждым тестом и создаст экземпляр игры
        self.game = PoleChudesGame("TESTWORD", "Test Topic", ["Hint 1", "Hint 2"])

    @patch('random.choice')
    def test_spin_wheel_integer_result(self, mock_choice):
        # Проверка, что spin_wheel правильно обрабатывает целочисленный результат
        mock_choice.return_value = 500
        self.game.spin_wheel(guessed=True)
        self.assertEqual(self.game.current_turn_score, 500)

    @patch('builtins.print')
    @patch('random.choice')
    def test_spin_wheel_prize_result(self, mock_choice, mock_print):
        mock_choice.return_value = "ПРИЗ"
        with patch('builtins.print') as mock_print:
            self.game.spin_wheel(guessed=True)
            mock_print.assert_called_with("""⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⢀⠀⠀
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

    @patch('random.choice')
    def test_spin_wheel_letter_not_guessed(self, mock_choice):
        # Проверка, что spin_wheel переключает ход, если буква не угадана
        mock_choice.return_value = 300
        with patch('builtins.print') as mock_print:
            self.game.spin_wheel(guessed=False)
            mock_print.assert_called_with("Чтобы получить очки, надо букву угадать!")
        self.assertEqual(self.game.player_turn, 2)  # Проверяем, что ход переключен

if __name__ == '__main__':
    unittest.main()
