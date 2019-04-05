#!/usr/bin/env python
# coding: utf-8

import math

"""
Number letter counts
Euler Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage.
"""

under20 = ['','one','two','three','four','five','six','seven','eight','nine',
   'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',
           'eighteen','nineteen']
tenths = ['', '', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred = 'hundred'
thousand = 'thousand'
and_str = 'and'


class NumberGenerator:
    
    def __init__(self, under20, tenths, hundred, thousand, and_value):
        self.under20 = under20
        self.tenths = tenths
        self.hundred = hundred
        self.thousand = thousand
        self.and_value = and_value
        
    def get_number(self, i):
        
        if not isinstance(i, int):
            raise ValueError('Expected int. Value given was: {}'.format(i))
            
        if i<0:
            raise ValueError('Cannot be used with negative numbers. Value given was: {:,}'.format(i))
            
        if i>=100000:
            raise ValueError('Cannot be used with numbers greater than 10,000. Value given was: {:,}'.format(i))
        
        elif i<20:
            return self.under20[i]

        elif i<100:
            return self.tenths[math.floor(i/10)] + self.get_number(i%10)

        elif i<1000:
            hundreds = self.get_number(math.floor(i/100)) + self.hundred 
            # Case: "four hundred", not "four hundred and ..." 
            if i%100 is 0:
                return hundreds
            return hundreds + self.and_value + self.get_number(i%100) 

        else:
            return self.get_number(math.floor(i/1000)) + self.thousand + self.get_number(i%1000)


to_length = lambda x: len(x)
number_chars = NumberGenerator( 
    list(map(to_length, under20)), 
    list(map(to_length, tenths)), 
    len(hundred), 
    len(thousand), 
    len(and_str)
)
solution = sum(number_chars.get_number(n) for n in range(1,1001))
print(solution)
