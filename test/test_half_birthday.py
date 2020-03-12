import unittest
from happy_birthday_assignment import half_birthday as half

class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):  # pass input
        birthday = 10/10/2019
        self.assertEqual(half.half_birthday(10/10/2019), 4/10/2019)




if __name__ == '__main__':
    unittest.main()
