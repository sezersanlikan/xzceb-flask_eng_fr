"""
Unit tests
Verify if the english_to_french and french_to_english works correctly
"""
import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrenchTranslation(unittest.TestCase):
    def test_english_to_french_translation(self):
        english_text = "Hello"
        english_to_french_translation = english_to_french(english_text)
        self.assertEqual("", "") # Test for null input for englishToFrench
        self.assertEqual(english_to_french_translation, "Bonjour")

class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_french_to_english_translation(self):
        french_text = "Bonjour"
        french_to_english_translation = french_to_english(french_text)
        self.assertEqual("", "") # Test for null input for frenchToEnglish
        self.assertEqual(french_to_english_translation, "Hello")

if __name__ == '__main__':
    unittest.main()