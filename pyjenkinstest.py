'''Test pyJenkins module'''

import unittest
from pyjenkins import pyjenkins

class PyJenkinsTest(unittest.TestCase):
    def test_url_building_connector_irise(self):
        PJ = pyjenkins('a','b')
        url = PJ._url_builder('connector-irise')
        self.assertEqual(url, 'https://ci-comp.tasktop.com/job/connector-irise/build?delay=0sec')

    def test_url_building_irise(self):
        PJ = pyjenkins('a','b')
        url = PJ._url_builder('irise')
        self.assertEqual(url, 'https://ci-comp.tasktop.com/job/connector-irise/build?delay=0sec')

    def test_url_building_connector_leankit(self):
        PJ = pyjenkins('a','b')
        url = PJ._url_builder('connector-leankit')
        self.assertEqual(url, 'https://ci-comp.tasktop.com/job/connector-leankit/build?delay=0sec')

    def test_url_building_leankit(self):
        PJ = pyjenkins('a','b')
        url = PJ._url_builder('leankit')
        self.assertEqual(url, 'https://ci-comp.tasktop.com/job/connector-leankit/build?delay=0sec')

    def test_login_fail(self):
        PJ = pyjenkins('login-fail-test','b')
        self.assertFalse(PJ.login())

if __name__ == '__main__':
    unittest.main()

