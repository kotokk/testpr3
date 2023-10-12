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
        if self.player_turn == 1:
            self.player1_score += self.current_turn_score
        else:
            self.player2_score += self.current_turn_score

    def guess_letter(self, letter):
        return
    
import unittest

class TestPoleChudesGame(unittest.TestCase):
    def setUp(self):
        # Подготовка объекта PoleChudesGame для тестирования
        self.game = PoleChudesGame("PYTHON", "Programming", ["High-level", "Interpreted"])

    def test_guess_letter_correct(self):
        # Проверка правильного угадывания буквы
        result = self.game.guess_letter("P")
        self.assertTrue(result)  # Ожидается, что буква P угадана
        self.assertEqual(' '.join(self.game.hidden_word), "P _ _ _ _ _")
        self.assertEqual(self.game.player1_score, 0)  # Счет не должен измениться, так как это был первый ход

    def test_guess_letter_incorrect(self):
        # Проверка неправильного угадывания буквы
        result = self.game.guess_letter("Z")
        self.assertFalse(result)  # Ожидается, что буква Z не угадана
        self.assertEqual(' '.join(self.game.hidden_word), "_ _ _ _ _ _")
        self.assertEqual(self.game.player1_score, 0)  # Счет не должен измениться, так как буква была неверной

    def test_guess_letter_duplicate(self):
        # Проверка угадывания уже угаданной буквы
        self.game.guess_letter("P")  # Угадали букву P
        result = self.game.guess_letter("P")
        self.assertFalse(result)  # Ожидается, что буква P уже угадана
        self.assertEqual(' '.join(self.game.hidden_word), "P _ _ _ _ _")
        self.assertEqual(self.game.player1_score, 0)  # Счет не должен измениться, так как это была дублирующая буква

    def test_guess_letter_update_scores(self):
        # Проверка обновления счета после угадывания правильной буквы
        self.game.guess_letter("P")
        self.game.guess_letter("Y")
        self.assertEqual(' '.join(self.game.hidden_word), "P Y _ _ _ _")
        self.assertEqual(self.game.player1_score, 0)  # Счет не должен измениться, так как это был первый ход

if __name__ == '__main__':
    unittest.main()
