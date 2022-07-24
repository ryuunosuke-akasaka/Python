import unittest
import script


class DoTesting(unittest.TestCase):
    def testdo1(self):
        result = script.do_this(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script.do_this(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = script.do_this(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = script.do_this(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
