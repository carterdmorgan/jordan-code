import unittest, sys, os

sys.path.append(os.path.abspath('..'))

from url import URL

class URLTest(unittest.TestCase):

    def setUp(self):
        self.long_url = 'www.homestarrunner.com'
        self.short_url = '4e0080'
        URL.URL_DICT = {}

    def test_shorten_url(self):
        test_short_url = URL.shorten_url(self.long_url)
        self.assertEqual(self.short_url, test_short_url)

    def test_shorten_url_malformed(self):
        with self.assertRaises(ValueError):
            URL.shorten_url('ww.homestarrunner.com')

    def test_get_long_url(self):
        test_short_url = URL.shorten_url(self.long_url)
        test_long_url = URL.get_long_url(test_short_url)
        self.assertEqual(self.long_url, test_long_url)

    def test_get_long_url_missing(self):
        with self.assertRaises(ValueError):
            URL.get_long_url(self.short_url)
    
    def test_get_access_count(self):
        URL.shorten_url(self.long_url)
        URL.get_long_url(self.short_url)
        test_access_count = URL.get_access_count(self.short_url)
        self.assertEqual(1, test_access_count)

    def test_get_access_count_missing(self):
        with self.assertRaises(ValueError):
            URL.get_access_count(self.short_url)



    



