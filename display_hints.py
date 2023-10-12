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
    
    def display_hints(self):
        return 

import unittest

class TestPoleChudesGame(unittest.TestCase):
    def setUp(self):
        # Подготовка объекта PoleChudesGame для тестирования
        self.game = PoleChudesGame("PYTHON", "Programming", ["High-level", "Interpreted"])

    def test_display_hints_initial(self):
        # Проверка отображения подсказок перед использованием
        self.assertEqual(self.game.display_hints(), "High-level, Interpreted")

    def test_display_hints_after_use(self):
        # Проверка отображения подсказок после использования
        self.game.hints.pop(0)
        self.assertEqual(self.game.display_hints(), "Interpreted")

    def test_display_hints_empty(self):
        # Проверка отображения подсказок, когда список подсказок пуст
        self.game.hints = []
        self.assertEqual(self.game.display_hints(), "")

if __name__ == '__main__':
    unittest.main()
