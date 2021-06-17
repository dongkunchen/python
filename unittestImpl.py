import unittest

from unitTest_fun import mySum
from unitTest_fun import mySub

class Test(unittest.TestCase):
    def setUp(self):
        print("開始測試時自動調用")
    def testDown(self):
        print("結束測試時自動調用")
    #為了測試mySum
    def test_mySum(self):
        self.assertEqual(mySum(1,2),3,"加法有誤")
    def test_mySub(self):
        self.assertEqual(mySub(2,1),1,"加法有誤")

if __name__ == "__main__":
    unittest.main()