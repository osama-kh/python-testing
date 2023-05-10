import unittest
import Tic_Tac_Toe


class TestTicTacToe(unittest.TestCase):

    def test_Is_valid_move(self):
        """
      to chek if the player made a correct move or wrong one

        """

        Tic_Tac_Toe.board = [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 1]]
        self.assertFalse(Tic_Tac_Toe.is_valid_move(1,3,1))
        self.assertFalse(Tic_Tac_Toe.is_valid_move(2,1,7))
        self.assertTrue(Tic_Tac_Toe.is_valid_move(0,1,0))

    def test_has_won(self):
        """
        check if the player won by checking if the board have the same value in line
        """
        Tic_Tac_Toe.board = [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 1]]
        self.assertTrue(Tic_Tac_Toe.has_won(0,3,1))
        self.assertFalse(Tic_Tac_Toe.has_won(1,1,2))
        self.assertFalse(Tic_Tac_Toe.has_won(6,1,2))

    def test_validate_3_in_diagonal(self):
        """
        check if the board have the same value in the backward or the forward diagonal

        """
        Tic_Tac_Toe.board = [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 1]]
        self.assertFalse(Tic_Tac_Toe.validate_3_in_diagonal(1))
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(0))

    def test_backward_diagonal(self):
        """
        check if the board have the same value in the backward diagonal

        """
        Tic_Tac_Toe.board = [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 1]]

        self.assertFalse(Tic_Tac_Toe.backward_diagonal(1))
        self.assertTrue(Tic_Tac_Toe.backward_diagonal(0))

    def test_forward_diagonal(self):
        """
        check if the board have the same value in the forward diagonal

        """
        Tic_Tac_Toe.board = [
            [1, 0, 0],
            [0, 1, 1],
            [0, 1, 1]]

        self.assertFalse(Tic_Tac_Toe.forward_diagonal(0))
        self.assertTrue(Tic_Tac_Toe.forward_diagonal(1))

    def test_validate_3_in_column(self):
        """
        check if the board have the same value in  three places that make a column

        """
        Tic_Tac_Toe.board = [
            [1, 0, 1],
            [0, 1, 1],
            [0, 1, 1]]

        self.assertTrue(Tic_Tac_Toe.validate_3_in_column(2 , 1))
        self.assertFalse(Tic_Tac_Toe.validate_3_in_column(1 , 1))
        self.assertFalse(Tic_Tac_Toe.validate_3_in_column(1 , 0))

    def test_validate_3_in_row(self):
        """
        check if the board have the same value in  three places that make a row

        """
        Tic_Tac_Toe.board = [
            [1, 0, 1],
            [0, 0, 0],
            [0, 1, 1]]

        self.assertTrue(Tic_Tac_Toe.validate_3_in_row(1 , 0))
        self.assertFalse(Tic_Tac_Toe.validate_3_in_row(1 , 1))


if __name__ == '__main__':
    unittest.main()
