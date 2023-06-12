import unittest
from merge import merge_sort
 
class TestSum(unittest.TestCase):
 
    def test_merge_sort(self):
        input1 = [8,66,54,32,69,21,420,5,13]
        res1 = [5,8,13,21,32,54,66,69,420]
        input2 = [4,2,3,0,1]
        res2 = [0,1,2,3,4]

        merge_sort(input2,0,4)
        merge_sort(input1,0,12)

    
        self.assertListEqual(input1,res1)
        self.assertListEqual(input2,res2)
 
 
if __name__ == '__main__':
    unittest.main()