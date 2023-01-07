IMPOSSIBLE = 'Impossible'
X_WINS = 'X wins'
O_WINS = 'O wins'
DRAW = 'Draw'
UNFINISHED = 'Game not finished'


class Board:
    def __init__(self, content: str):
        self.content = content

    def row(self, i: int) -> list[str]:
        return [self.content[j] for j in range(3 * i, 3 * i + 3)]

    def column(self, i: int) -> list[str]:
        return [self.content[j] for j in range(i, 9, 3)]

    def diagonal(self, i: int) -> list[str]:
        return [self.content[j] for j in (range(2, 7, 2) if i else range(0, 9, 4))]

    def x_placed_count(self) -> int:
        return self.content.count('X')

    def o_placed_count(self) -> int:
        return self.content.count('O')

    def has_triple(self, triple_set: set[str]) -> bool:
        for i in range(3):
            if triple_set in (set(self.row(i)), set(self.column(i)), set(self.diagonal(i))):
                return True
        return False

    def state(self) -> str:
        if abs(self.x_placed_count() - self.o_placed_count()) > 1:
            return IMPOSSIBLE
        has_triple_x = self.has_triple(set('X'))
        has_triple_o = self.has_triple(set('O'))
        if has_triple_o and has_triple_x:
            return IMPOSSIBLE
        if has_triple_x:
            return X_WINS
        if has_triple_o:
            return O_WINS
        return UNFINISHED if '_' in self.content else DRAW
