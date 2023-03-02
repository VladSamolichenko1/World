import  unittest
from bob import adder

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(adder(2, 2), 4)

    def test_kwargs(self):
        self.assertEqual(adder(a=5, b=10), 15)

    def test_mix(self):
        self.assertEqual(adder(10, a=20), 30)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, y, a=x), 5)

    def test_wrong_datatypes(self):
        self.assertEqual(adder("5", "abc", "10"), 15)

if __name__ == "__main__":
    unittest.main()