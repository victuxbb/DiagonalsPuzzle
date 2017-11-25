class Diagonals:
    DIAGONAL_FROM_BOTTOM_LEFT_TO_TOP_RIGHT = 1
    DIAGONAL_FROM_BOTTOM_RIGHT_TO_TOP_LEFT = 2
    EMPTY = 0

    def __init__(self, size, diagonals):
        self.size = size
        self.diagonals = diagonals
        self.permutations = [-1] * size * size

    def start(self):
        self.extend(perm=self.permutations, start=0)

    def can_be_extended_to_solution(self, perm, last_inserted):
        current_diagonal_value = perm[last_inserted]

        if current_diagonal_value == self.DIAGONAL_FROM_BOTTOM_LEFT_TO_TOP_RIGHT:
            if self._is_left_cell_containing(
                    perm,
                    current_cell=last_inserted,
                    expected=self.DIAGONAL_FROM_BOTTOM_RIGHT_TO_TOP_LEFT
            ):
                return False
            if self.is_bottom_left_cell_containing(
                    perm,
                    current_cell=last_inserted,
                    expected=self.DIAGONAL_FROM_BOTTOM_LEFT_TO_TOP_RIGHT
            ):
                return False
            if self._is_bottom_cell_containing(
                    perm,
                    current_cell=last_inserted,
                    expected=self.DIAGONAL_FROM_BOTTOM_RIGHT_TO_TOP_LEFT
            ):
                return False
        if current_diagonal_value == self.DIAGONAL_FROM_BOTTOM_RIGHT_TO_TOP_LEFT:
            if self.is_top_left_cell_containing(
                    perm,
                    current_cell=last_inserted,
                    expected=self.DIAGONAL_FROM_BOTTOM_RIGHT_TO_TOP_LEFT
            ):
                return False
            if self._is_left_cell_containing(
                    perm,
                    current_cell=last_inserted,
                    expected=self.DIAGONAL_FROM_BOTTOM_LEFT_TO_TOP_RIGHT
            ):
                return False
            if self._is_bottom_cell_containing(
                    perm,
                    current_cell=last_inserted,
                    expected=self.DIAGONAL_FROM_BOTTOM_LEFT_TO_TOP_RIGHT
            ):
                return False

        return self._is_still_possible_to_achieve_desired_diagonals(perm, last_inserted)

    def extend(self, perm, start):
        total = perm.count(1) + perm.count(2)
        if total == self.diagonals:
            print(perm)
            exit()
        if start < len(perm):
            perm[start] = self.DIAGONAL_FROM_BOTTOM_LEFT_TO_TOP_RIGHT
            if self.can_be_extended_to_solution(perm, last_inserted=start):
                next_start = start + 1
                self.extend(perm, start=next_start)

            perm[start] = self.DIAGONAL_FROM_BOTTOM_RIGHT_TO_TOP_LEFT
            if self.can_be_extended_to_solution(perm, last_inserted=start):
                next_start = start + 1
                self.extend(perm, start=next_start)

            perm[start] = self.EMPTY
            next_start = start + 1
            self.extend(perm, start=next_start)

    def _is_still_possible_to_achieve_desired_diagonals(self, perm, last_inserted):
        current_number_of_diagonals = perm.count(1) + perm.count(2)
        if len(perm) - 1 - last_inserted < self.diagonals - current_number_of_diagonals:
            return False
        return True

    def _is_left_cell_containing(self, perm, current_cell, expected):
        left_cell = current_cell - self.size
        if perm[left_cell] == expected:
            return True
        return False

    def _is_bottom_cell_containing(self, perm, current_cell, expected):
        bottom_cell = current_cell - 1
        if bottom_cell / self.size >= 0 and perm[bottom_cell] == expected:
            return True
        return False

    def is_top_left_cell_containing(self, perm, current_cell, expected):
        top_left_cell = current_cell - self.size + 1
        current_row = current_cell / self.size
        if current_row != top_left_cell / self.size and perm[top_left_cell] == expected:
            return True
        return False

    def is_bottom_left_cell_containing(self, perm, current_cell, expected):
        bottom_left_cell = current_cell - self.size - 1
        current_row = current_cell / self.size
        if current_row - 1 == bottom_left_cell / self.size and perm[bottom_left_cell] == expected:
            return True
        return False
