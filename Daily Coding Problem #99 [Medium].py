# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.

def get_longest_consec(my_arr):
    consecutive = []
    my_arr.sort()
    length_count = 1
    for i, e in enumerate(my_arr[:-1]):
        if my_arr[i + 1] - e == 1:
            length_count += 1
        else:
            consecutive.append(length_count)
            length_count = 1
    return max(consecutive)


import unittest


class TestConsec(unittest.TestCase):

    def test_longest_consec(self):
        """
        Test that fn returns expected output
        """
        inp = [100, 4, 200, 1, 3, 2]
        expected = 4
        actual = get_longest_consec(inp)
        self.assertEqual(expected, actual)

    def test_longest_consec_with_two_consecs(self):
        """
        Test that fn returns expected output
        """
        inp = [100, 101, 4, 102, 200, 103, 1, 104, 3, 105, 2, 106]
        expected = 7
        actual = get_longest_consec(inp)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
