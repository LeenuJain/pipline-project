import unittest
from src.string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.str_utils = StringUtils()
        
    def test_reverse(self):
        self.assertEqual(self.str_utils.reverse("hello"), "olleh")
        self.assertEqual(self.str_utils.reverse(""), "")
        self.assertEqual(self.str_utils.reverse("a"), "a")
        
    def test_capitalize_words(self):
        self.assertEqual(self.str_utils.capitalize_words("hello world"), "Hello World")
        self.assertEqual(self.str_utils.capitalize_words("python testing"), "Python Testing")
        
    def test_count_vowels(self):
        self.assertEqual(self.str_utils.count_vowels("hello"), 2)
        self.assertEqual(self.str_utils.count_vowels("aeiou"), 5)
        self.assertEqual(self.str_utils.count_vowels("xyz"), 0)

if __name__ == '__main__':
    unittest.main()
