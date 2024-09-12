import unittest, sys, os

sys.path.append(os.path.abspath('..'))

from url import URL, URL_Shortener

class URLTest(unittest.TestCase):

    def setUp(self):
        self.long_url = 'www.homestarrunner.com'
        self.short_url = '4e0080'
        URL.url_dict = {}

    def test_shorten_url(self):
        test_short_url = URL_Shortener.shorten_url(self.long_url)
        self.assertEqual(self.short_url, test_short_url)

    def test_shorten_url_malformed(self):
        with self.assertRaises(ValueError):
            URL_Shortener.shorten_url('ww.homestarrunner.com')

    def test_get_long_url(self):
        test_short_url = URL_Shortener.shorten_url(self.long_url)
        test_long_url = URL_Shortener.get_long_url(test_short_url)
        self.assertEqual(self.long_url, test_long_url)

    def test_get_long_url_missing(self):
        with self.assertRaises(ValueError):
            URL_Shortener.get_long_url(self.short_url)
    
    def test_get_access_count(self):
        URL_Shortener.shorten_url(self.long_url)
        URL_Shortener.get_long_url(self.short_url)
        test_access_count = URL_Shortener.get_access_count(self.short_url)
        self.assertEqual(1, test_access_count)

    def test_get_access_count_missing(self):
        with self.assertRaises(ValueError):
            URL_Shortener.get_access_count(self.short_url)



    



