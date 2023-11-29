import unittest
from logic import Game, Player, Bot  # Replace 'logic' with the actual name of your Python file

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.bot = Bot("O")
        self.game = Game(self.player1, self.player2)

    def test_initial_board_empty(self):
        for row in self.game.board:
            self.assertTrue(all(cell is None for cell in row))

    def test_game_initialization(self):
        game_human_bot = Game(self.player1, self.bot)
        self.assertIsInstance(game_human_bot.other_player, Bot)

    def test_player_assignment(self):
        self.assertEqual(self.player1.symbol, "X")
        self.assertEqual(self.player2.symbol, "O")

    def test_turn_alternation(self):
        initial_player = self.game.current_player
        self.game.play_turn()  # Simulate a turn
        self.assertNotEqual(self.game.current_player, initial_player)

    def test_winning_conditions(self):
        # Test a row win
        self.game.board = [["X", "X", "X"], [None, None, None], [None, None, None]]
        self.assertEqual(self.game.get_winner(), "X")

        # Test a column win
        self.game.board = [["O", None, None], ["O", None, None], ["O", None, None]]
        self.assertEqual(self.game.get_winner(), "O")

        # Test a diagonal win
        self.game.board = [["X", None, None], [None, "X", None], [None, None, "X"]]
        self.assertEqual(self.game.get_winner(), "X")

    def test_draw_condition(self):
        self.game.board = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
        self.assertTrue(self.game.is_draw())

    def test_correct_winner(self):
        self.game.board = [["X", "X", "X"], [None, "O", None], [None, None, "O"]]
        self.assertEqual(self.game.get_winner(), "X")

if __name__ == '__main__':
    unittest.main()
