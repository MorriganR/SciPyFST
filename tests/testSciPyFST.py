import unittest
from devSciPyFST import fst, fstUtils

class TestSciPyFST(unittest.TestCase):
    def test_pass(self):
        pass

    # DEMO tests
    # https://docs.python.org/3/library/unittest.html
    def test_upper(self):
        testStr = 'foo'
        resustStr = 'FOO'
        error_string = 'Upper test expected {}, got {}'
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual(testStr.upper(), resustStr, 'comment at two line... ' +
            error_string.format(resustStr, testStr.upper()))

    @unittest.expectedFailure
    def test_fail(self):
        testStr = 'foo'
        resustStr = 'FOO'
        error_string = 'Upper test expected {}, got {}'
        self.assertNotEqual(testStr.upper(), resustStr, 'comment at two line... ' +
            error_string.format(resustStr, testStr.upper()))

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    # END DEMO tests

if __name__ == '__main__':
    unittest.main()
