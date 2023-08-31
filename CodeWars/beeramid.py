# Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.

# A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

# Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:

# your referral bonus, and

# the price of a beer can

# For example:

# beeramid(1500, 2); // should === 12
# beeramid(5000, 3); // should === 16

import unittest


def sqr_sum(n):
    if n > 1:
        return n**2 + sqr_sum(n-1)
    return 1

def beeramid(bonus, price):
    max_cans = bonus // price  
    cur_level = 1
    
    while True:
        sum_of_cans = sqr_sum(cur_level)
        if sum_of_cans > max_cans:
            return cur_level - 1
        cur_level += 1

class TestBeeramid(unittest.TestCase):

    def test_beeramid(self):
        self.assertEqual(beeramid(9, 2),  1)
        self.assertEqual(beeramid(21, 1.5),  3)
        self.assertEqual(beeramid(-1, 4), 0)

if __name__ == '__main__':
    unittest.main()