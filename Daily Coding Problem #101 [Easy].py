# 
# Goldbach's conjecture states:
#     Every even integer greater than 2 is the sum of two primes
# 
# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number
# 
# Example:
# 
# Input: 4
# Output: 2 + 2 = 4
# 
# If there are more than one solution possible, return the lexicographically smaller solution.
# 
# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
# 
# [a, b] < [c, d]
# 
# If a < c OR a==c AND b < d.

# To save generating some of the smaller ones repeatedly
PRIMES = [2,3,5,7,11]

def is_prime(num):
    if num==1 or num==2:
        return True
    if num % 2 == 0:
        return False
    if has_factors(num):
        return False
    return True

def has_factors(num):
    for i in range(2,num//2):
        if (num % i) == 0:
            return True
    return False

def get_prime_pair(num):
    # pair = [(num//2) + 1]
    # if is_prime(pair[0]):
    #     pair.append(num-pair[0])
    #     if is_prime(pair[1]):
    #         pair.sort()
    #         return pair
    # else:
    for p in PRIMES:
        pair = [p, num-p]
        if is_prime(pair[1]):
            return pair
    ## TODO: add primes generator and extend list


def prime_sum_string(num):
    pair = get_prime_pair(num)
    if pair:
        return '{} + {} = {}'.format(*pair,num)       
    else:
        raise Exception('No match')


even_digits = [4,6,8,10,12,14,16,18,20]
for num in even_digits:
    try:
        print(prime_sum_string(num))
    except Exception as e:
        print('Failed to find match for {}'.format(num))
        print(e)



# import unittest

# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         """
#         Test that fn returns expected output
#         """
#         # Input: 4
#         # Output: 2 + 2 = 4
#         num = 4
#         expected = '2 + 2 = 4'
#         actual = get_prime_sum(num)
#         self.assertEqual(expected, actual)

# if __name__ == '__main__':
#     unittest.main()