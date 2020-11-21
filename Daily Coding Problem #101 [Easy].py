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
PRIMES = [1,2,3,5,7,11]

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



even_digits = [4,6,8,10,12,14,16,18]

for dig in even_digits:
    found_pair = False
    pair = [(dig//2) + 1]
    if is_prime(pair[0]):
        pair.append(dig - pair[0])
        if is_prime(pair[1]):
            found_pair = True
            pair.sort()
            print('{},{}'.format(*pair))
    else:
        for p in PRIMES:
            guess = p
            counterpart = dig - guess
            if is_prime(counterpart):
                found_pair = True
                print('{},{}'.format(guess, counterpart))
                break
        ## add primes generator and extend list
    if found_pair == False:
        print('Failed to find match for {}'.format(dig))