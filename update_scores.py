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
    
    def update_scores(self):
        return

import unittest

class TestPoleChudesGame(unittest.TestCase):
    def setUp(self):
        # Подготовка объекта PoleChudesGame для тестирования
        self.game = PoleChudesGame("PYTHON", "Programming", ["High-level", "Interpreted"])

    def test_update_scores_player1(self):
        # Проверка обновления счета для игрока 1
        self.game.current_turn_score = 10
        self.game.update_scores()
        self.assertEqual(self.game.player1_score, 10)
        self.assertEqual(self.game.player2_score, 0)

    def test_update_scores_player2(self):
        # Проверка обновления счета для игрока 2
        self.game.player_turn = 2
        self.game.current_turn_score = 15
        self.game.update_scores()
        self.assertEqual(self.game.player1_score, 0)
        self.assertEqual(self.game.player2_score, 15)

    def test_update_scores_both_players(self):
        # Проверка обновления счета для обоих игроков
        self.game.player_turn = 2
        self.game.current_turn_score = 5
        self.game.update_scores()
        self.assertEqual(self.game.player1_score, 0)
        self.assertEqual(self.game.player2_score, 5)

if __name__ == '__main__':
    unittest.main()
