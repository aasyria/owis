import unittest
import owis.core.app as owis


class OwisTest(unittest.TestCase):
    def test_scan(self):
        result = owis.scan()
        self.assertEqual("hello world", result)