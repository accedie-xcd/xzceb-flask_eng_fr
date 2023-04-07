import unittest
from translator import french_to_english, english_to_french

class test_translate(unittest.TestCase):
    def test_tf(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_null_tf(self):
        self.assertNotEqual(french_to_english("Bonjour"), None)

    def test_ef(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_null_ef(self):
        self.assertNotEqual(english_to_french("Hello"), None)

if __name__ == '__main__':
    unittest.main()