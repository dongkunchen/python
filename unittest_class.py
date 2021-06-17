import unittest
from person import Person

class Test(unittest.TestCase):
    def test_init(self):
        p = Person("dongkun",20)
        self.assertEqual(p.name,"dongkun","屬性賦值有誤")
    def test_getAge(self):
        p = Person("dongkun",22)
        self.assertEqual(p.getAge(),p.age,"getAge函數有誤")

if __name__ == "__main__":
    unittest.main()
