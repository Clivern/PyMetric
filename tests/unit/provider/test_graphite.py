import unittest

from pyumetric import Graphite_Provider

class TestGraphite(unittest.TestCase):

    def test_get_name(self):
        self.assertEqual(Graphite_Provider().get_name(), 'Graphite')

if __name__ == '__main__':
    unittest.main()
