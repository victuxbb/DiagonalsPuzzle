class Diagonals:
    def __init__(self, size, diagonals):
        self.size = size
        self.diagonals = diagonals
        self.permutations = [-1] * size * size

    def start(self):
        self.extend(perm=self.permutations, start=0)

    def can_be_extended_to_solution(self, perm, last_inserted):
        current_diagonal_value = perm[last_inserted]
        current_row = last_inserted / self.size

        if current_diagonal_value == 1:  # / BL-TR
            left_cell = last_inserted - self.size
            bottom_left_cell = last_inserted - self.size - 1
            bottom_cell = last_inserted - 1
            if perm[left_cell] == 2:
                return False
            if current_row - 1 == bottom_left_cell / self.size and perm[bottom_left_cell] == 1:
                return False
            if bottom_cell / self.size >= 0 and perm[bottom_cell] == 2:
                return False
        if current_diagonal_value == 2:  # \ BR-TL
            top_left_cell = last_inserted - self.size + 1
            left_cell = last_inserted - self.size
            bottom_cell = last_inserted - 1
            if current_row != top_left_cell / self.size and perm[top_left_cell] == 2:
                return False
            if perm[left_cell] == 1:
                return False
            if bottom_cell / self.size >= 0 and perm[bottom_cell] == 1:
                return False

        return True

    def extend(self, perm, start):
        if -1 not in perm:
            total = perm.count(1) + perm.count(2)
            if total == self.diagonals:
                print(perm)
        if start < len(perm):
            perm[start] = 1
            if self.can_be_extended_to_solution(perm, last_inserted=start):
                next_start = start + 1
                self.extend(perm, start=next_start)

            perm[start] = 2
            if self.can_be_extended_to_solution(perm, last_inserted=start):
                next_start = start + 1
                self.extend(perm, start=next_start)

            perm[start] = 0
            next_start = start + 1
            self.extend(perm, start=next_start)