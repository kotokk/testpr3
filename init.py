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


class TestPoleChudesGameInitialization(unittest.TestCase):
    def test_initialization(self):
        word_to_guess = "example"
        game_topic = "topic"
        game_hints = ["hint1", "hint2"]

        game = PoleChudesGame(word_to_guess, game_topic, game_hints)

        # Проверка инициализации слова
        self.assertEqual(game.word, "EXAMPLE")

        # Проверка инициализации скрытого слова
        self.assertEqual(game.hidden_word, ['_', '_', '_', '_', '_', '_', '_'])

        # Проверка инициализации темы
        self.assertEqual(game.topic, "topic")

        # Проверка инициализации подсказок
        self.assertEqual(game.hints, ["hint1", "hint2"])

        # Проверка инициализации угаданных букв
        self.assertEqual(game.guessed_letters, set())

        # Проверка инициализации счетов игроков
        self.assertEqual(game.player1_score, 0)
        self.assertEqual(game.player2_score, 0)

        # Проверка инициализации текущего счета и общего счета
        self.assertEqual(game.current_turn_score, 0)
        self.assertEqual(game.total_score, 0)

        # Проверка инициализации текущего игрока
        self.assertEqual(game.player_turn, 1)

if __name__ == '__main__':
    unittest.main()
