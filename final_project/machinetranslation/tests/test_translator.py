import unittest

from machinetranslation.translator import french_to_english
from machinetranslation.translator import english_to_french
null = ''


class TestTranslator(unittest.TestCase):
    def test_f2e(self):
        b = 'Bonjour'
        self.assertEqual(french_to_english(b), 'Hello')
        pass
        self.assertNotEqual(french_to_english(b), 'Goodbye')
        pass
        self.assertNotEqual(french_to_english('Null'), '')

    def test_e2f(self):
        h = 'Hello'
        self.assertEqual(english_to_french(h), 'Bonjour')
        pass
        self.assertNotEqual(english_to_french(h), 8)
        pass
        self.assertNotEqual(english_to_french('Null'), '')


if __name__ == "__main__":
    unittest.main()
    print('Passed All Tests')
