'''
Created on 2013-11-9

@author: 灵箫
'''
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(1, 1)
        
    def test_2(self):
        self.assertEqual(1, 2)
        
if __name__ == '__main__':
    unittest.main()
