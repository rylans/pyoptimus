'''test pyoptimus'''

import unittest
from pyoptimus import pyoptimus

class PyOptimusTest(unittest.TestCase):
    def test_request_irise_id(self):
        instance = pyoptimus('raw_list')
        results = instance.build_results('com.tasktop.connector.irise', 1)
        self.assertEquals(int(results[0][0]), 16)

    def test_request_irise_last_fails(self):
        instance = pyoptimus('raw_list')
        fails = instance.last_fails('com.tasktop.connector.irise')
        self.assertEquals(fails, 0)

if __name__ == '__main__':
    unittest.main()

