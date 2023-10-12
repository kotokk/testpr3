import unittest
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

class TestIsValidLetter(unittest.TestCase):
    def setUp(self):
        # Создаем объект игры для использования в тестах
        self.game = PoleChudesGame("ПРИМЕР", "ТЕМА", ["ПОДСКАЗКА1", "ПОДСКАЗКА2"])

    def test_empty_input(self):
        self.assertFalse(is_valid_letter("", self.game))

    def test_non_alpha_input(self):
        self.assertFalse(is_valid_letter("123", self.game))
        self.assertFalse(is_valid_letter("!", self.game))

    def test_non_russian_letter_input(self):
        self.assertFalse(is_valid_letter("A", self.game))
        self.assertFalse(is_valid_letter("Q", self.game))

    def test_already_guessed_letter(self):
        self.game.guessed_letters.add("Б")  # Предполагаем, что "Б" уже угадывалась
        self.assertFalse(is_valid_letter("Б", self.game))

    def test_valid_input(self):
        self.assertTrue(is_valid_letter("Г", self.game))

if __name__ == '__main__':
    unittest.main()
