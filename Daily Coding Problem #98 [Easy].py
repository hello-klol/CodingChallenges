# Given a 2D board of characters and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example, given the following board:
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
import operator
import unittest
from typing import List, Tuple


class Board:
    BoardType = List[List[str]]
    Coordinate = Tuple[int, int]
    ALLOWED_MOVES = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def __init__(self, board: BoardType):
        self.board = board

    @staticmethod
    def _tuple_sum(a: Coordinate, b: Coordinate) -> Coordinate:
        return tuple(map(operator.add, a, b))

    def _verify_coord(self, coord: Coordinate) -> bool:
        x, y = coord
        return all([x >= 0, x <= len(self.board[0]),
                    y >= 0, y <= len(self.board)])

    def find_letter(self, letter: str) -> List[Coordinate]:
        for y, r in enumerate(self.board):
            for x, c in enumerate(r):
                if c == letter:
                    yield tuple((x, y))

    def lookup(self, coord: Coordinate) -> str:
        x, y = coord
        return self.board[y][x]

    def get_word_coords(self, word):
        for start in self.find_letter(word[0]):
            word_coords = [start]
            word_coords = self.find_word(start, word, word_coords)
            if len(word_coords) == len(word):
                return word_coords
        raise Exception('Word not found {}'.format(word))

    def find_word(self,
                  start: Coordinate,
                  word: str,
                  word_coords: List[Coordinate] = []) -> List[Coordinate]:
        last_coord = start
        next_letter = word[1]
        for move in self.ALLOWED_MOVES:
            try:
                new_coord = self._tuple_sum(last_coord, move)
                if new_coord in word_coords:
                    continue
                if not self._verify_coord(new_coord):
                    continue
                if self.lookup(new_coord) == next_letter:
                    word_coords.append(new_coord)
                    self.find_word(new_coord, word[1:], word_coords)
            except IndexError:  # invalid move
                pass
        return word_coords


def exists(board: Board.BoardType, word: str) -> bool:
    my_board = Board(board)
    try:
        word_coords = my_board.get_word_coords(word)
        print('Found word {} at co-oordinates'.format(word))
        print(word_coords)
        return True
    except Exception as e:
        print(e)
        return False


class TestConsec(unittest.TestCase):

    def test_exists(self):
        """
        Test that fn returns expected output
        """
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        expected = True
        actual = exists(board, "ABCCED")
        self.assertEqual(expected, actual)

    def test_not_exists(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        expected = False
        actual = exists(board, "SELDOM")
        self.assertEqual(expected, actual)

    def test_no_repeat_visit(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        expected = False
        actual = exists(board, "ABCB")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
