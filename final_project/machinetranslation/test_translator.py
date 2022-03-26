import unittest

from machinetranslation.translator import french_to_english
from machinetranslation.translator import english_to_french
null = ''


class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        b = 'Bonjour'
        self.assertEqual(french_to_english(b), 'Hello')

        self.assertNotEqual(french_to_english(b), 'Goodbye')

        pass

    def test_english_to_french(self):
        h = 'Hello'
        self.assertEqual(english_to_french(h), 'Bonjour')

        self.assertNotEqual(english_to_french(h), 8)

    pass


if __name__ == "__main__":
    unittest.main()
    print('Passed All Tests')
