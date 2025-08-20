import unittest
from crawl import normalize_url
from parse_html import get_urls_html
import sys
class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        
        self.assertEqual(actual, expected)
    def test_get_url_html_absolute(self):
        input_url = "https://blog.root.et"
        input_body = '<html><body><a href="https://blog.root.et"><span>Boot.dev></span></a></body></html>'
        actual = get_urls_html(input_body, input_url)
        expected = ["https://blog.root.et"]
        self.assertEqual(actual, expected)
    def test_get_urls_html_absolute(self):
        input_url = "https://blog.root.et"
        input_body = '<html><body><a href="https://blog.root.dev"><span>Boot.dev></span></a></body></html>  <html><body><a href="https://blog.boot.dev"><span>Boot.dev></span></a></body></html>'
        actual = get_urls_html(input_body, input_url)
        expected = ["https://blog.root.dev","https://blog.boot.dev"]
        self.assertEqual(actual, expected)
   
if __name__ == "__main__":
    unittest.main()