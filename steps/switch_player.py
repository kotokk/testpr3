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

import unittest

class TestSwitchPlayerTurn(unittest.TestCase):
    def setUp(self):
        self.word_to_guess = "example"
        self.game_topic = "topic"
        self.game_hints = ["hint1", "hint2"]
        self.game = PoleChudesGame(self.word_to_guess, self.game_topic, self.game_hints)

    def test_switch_player_turn_from_player1(self):
        initial_player_turn = self.game.player_turn
        self.game.switch_player_turn()
        new_player_turn = self.game.player_turn
        self.assertEqual(new_player_turn, 2 if initial_player_turn == 1 else 1)

    def test_switch_player_turn_from_player2(self):
        # Set player_turn to 2 to simulate the second player's turn
        self.game.player_turn = 2
        initial_player_turn = self.game.player_turn
        self.game.switch_player_turn()
        new_player_turn = self.game.player_turn
        self.assertEqual(new_player_turn, 2 if initial_player_turn == 1 else 1)

if __name__ == '__main__':
    unittest.main()
