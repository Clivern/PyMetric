import unittest

from pymetric import Backend_Provider

class TestBackend(unittest.TestCase):

    def test_get_name(self):
        self.assertEqual(Backend_Provider().get_name(), 'Backend')

if __name__ == '__main__':
    unittest.main()
