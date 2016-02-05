# import sys
# from os import path
# sys.path.append( path.dirname( path.abspath(__file__) ) )
import unittest
from src.main import IsOdd
from src.main import IsEven

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

    def testThree(self):
        self.failUnless(IsEven(0))

    def testFour(self):
        self.failIf(IsEven(1))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
