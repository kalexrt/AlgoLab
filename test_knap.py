import unittest
from knapsack import bruteforce
from knapsack import fracbruteforce
from knapsack import fracgreedy


class TestSum(unittest.TestCase):

    def test_bruteforce(self):
        val = [69,96,66,200,322,79]
        wt = [1,2,3,4,5,6]
        max_cap = 5

        output = 322
        input = bruteforce(val, wt, max_cap)

        self.assertEqual(input, output)

    def test_fracbruteforce(self):
        val = [69,96,66,200,322,79]
        wt = [1,2,3,4,5,6]
        max_cap = 5

        output = 326.6
        input = fracbruteforce(val, wt, max_cap)

        self.assertEqual(input, output)

    def test_fracgreedy(self):

        val = [69,96,66,200,322,79]
        wt = [1,2,3,4,5,6]
        max_cap = 5
        
        output = 326.6
        input = fracgreedy(val,wt,max_cap)

        self.assertEqual(input, output)

 
if __name__ == '__main__':
    unittest.main()