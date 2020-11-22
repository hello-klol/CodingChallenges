# You are in an infinite 2D grid where you can move in any of the 8 directions:
#
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
#
# You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
#
# Example:
#
# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2
#
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

def calc_steps(coord1, coord2):
    res = tuple(map(lambda i, j: abs(i - j), coord1, coord2))
    return max(res)


def get_num_steps(steps):
    num_steps = 0
    for i, s in enumerate(steps[:-1]):
        num_steps += calc_steps(s, steps[i+1])
    return num_steps


import unittest

class TestSum(unittest.TestCase):
    def test_step_count(self):
        """
        Test that fn returns expected output
        """
        inp = [(0, 0), (1, 1), (1, 2)]
        expected = 2
        actual = get_num_steps(inp)
        self.assertEqual(expected, actual)

    def test_list_int2(self):
        """
        Test that fn returns expected output
        """
        inp = [(0, 0), (10, 1), (1, 2)]
        expected = 19
        actual = get_num_steps(inp)
        self.assertEqual(expected, actual)

    def test_list_int3(self):
        """
        Test that fn returns expected output
        """
        inp = [(0, 0), (10, 5), (-1, 0)]
        expected = 21
        actual = get_num_steps(inp)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()