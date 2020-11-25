# Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
#
# It should contain the following methods:
#
#     set(key, value, time): sets key to value for t = time.
#     get(key, time): gets the key at t = time.
#
# The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it
# gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for
# that key set at the most recent time.
#
# Consider the following examples:
#
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2
#
# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1
#
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 0) # get key 1 at time 0 should be 2
import unittest

import pandas as pd


class TimeDict:

    def __init__(self):
        self.multi_idx_df = pd.DataFrame(columns=['key', 'time', 'value'])
        self.multi_idx_df.set_index(['key', 'time'], inplace=True)

    def set(self, key, value, time):
        self.multi_idx_df.loc[(key, time), :] = value
        pass

    def get_latest(self, key, time):
        try:
            # for efficiency get the index first rather than creating a whole sub df with all columns
            idx = self.multi_idx_df.index[self.multi_idx_df.index.get_level_values('time') < time][-1]
            return self.multi_idx_df.at[idx, 'value']
        except IndexError:
            # raise Exception('Value not found')
            return None

    def get(self, key, time):
        try:
            return self.multi_idx_df.at[(key, time), 'value']
        except KeyError as e:
            # Expected when no idx for key-time pair, go back in time
            return self.get_latest(key, time)


class TestFn(unittest.TestCase):

    def test_find_past_val(self):
        """
        # d.set(1, 1, 0) # set key 1 to value 1 at time 0
        # d.set(1, 2, 2) # set key 1 to value 2 at time 2
        # d.get(1, 1) # get key 1 at time 1 should be 1
        # d.get(1, 3) # get key 1 at time 3 should be 2
        """
        d = TimeDict()
        d.set(1, 1, 0)
        d.set(1, 2, 2)

        val = (1, 1)
        expected = 1
        actual = d.get(*val)
        self.assertEqual(expected, actual)

        val = (1, 3)
        expected = 2
        actual = d.get(*val)
        self.assertEqual(expected, actual)

    def test_not_found(self):
        """
        # d.set(1, 1, 5) # set key 1 to value 1 at time 5
        # d.get(1, 0) # get key 1 at time 0 should be null
        # d.get(1, 10) # get key 1 at time 10 should be 1
        """
        d = TimeDict()
        d.set(1, 1, 5)

        val = (1, 0)
        expected = None
        actual = d.get(*val)
        self.assertEqual(expected, actual)

        val = (1, 10)
        expected = 1
        actual = d.get(*val)
        self.assertEqual(expected, actual)

    def test_rewrite(self):
        """
        # d.set(1, 1, 0) # set key 1 to value 1 at time 0
        # d.set(1, 2, 0) # set key 1 to value 2 at time 0
        # d.get(1, 0) # get key 1 at time 0 should be 2
        """
        d = TimeDict()
        d.set(1, 1, 0)
        d.set(1, 2, 0)

        val = (1, 0)
        expected = 2
        actual = d.get(*val)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
