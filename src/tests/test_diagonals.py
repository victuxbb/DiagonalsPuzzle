from unittest import TestCase

from src.com.victuxbb.diagonals.diagonals import Diagonals


class TestDiagonals(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._diagonals = Diagonals(size=3, diagonals=6)

    def test_given_BL_TR_with_left_cell_diagonal_error_it_should_return_false(self):
        given_permutation = [2, 2, 2, 1, -1, -1, -1, -1, -1]
        self.assertFalse(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=3))

    def test_given_BL_TR_with_bottom_left_cell_diagonal_error_it_should_return_false(self):
        given_permutation = [2, 2, 2, 0, 1, -1, -1, -1, -1]
        self.assertFalse(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=4))

    def test_given_BL_TR_with_bottom_cell_diagonal_error_it_should_return_false(self):
        given_permutation = [2, 1, -1, -1, 1, -1, -1, -1, -1]
        self.assertFalse(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=1))

    def test_given_BR_TL_with_left_cell_diagonal_error_it_should_return_false(self):
        given_permutation = [1, 1, 1, 1, 2, -1, -1, -1, -1]
        self.assertFalse(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=4))

    def test_given_BR_TL_with_bottom_cell_diagonal_error_it_should_return_false(self):
        given_permutation = [1, 2, -1, -1, -1, -1, -1, -1, -1]
        self.assertFalse(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=1))

    def test_given_BR_TL_with_top_left_cell_diagonal_error_it_should_return_false(self):
        given_permutation = [0, 2, 2, 1, 2, -1, -1, -1, -1]
        self.assertFalse(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=4))

    def test_given_number_of_cells_not_processed_it_should_not_try_to_extend(self):
        given_permutation = [1, 0, 0, 0, 0, -1, -1, -1, -1]
        self.assertFalse(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=4))

    def test_given_number_of_cells_not_processed_it_should_try_to_extend(self):
        given_permutation = [1, 1, 1, 0, 0, 0, 1, -1, -1]
        self.assertTrue(self._diagonals.can_be_extended_to_solution(perm=given_permutation, last_inserted=6))
