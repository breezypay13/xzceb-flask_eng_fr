import unittest

from machinetranslation.translator import french_to_english

null = ''


class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        b = 'Bonjour'
        self.assertEqual(french_to_english(text1=b), 'Hello')
        with self.assertRaises(TypeError):
            french_to_english(3)
        self.assertNotEqual(french_to_english(text1=b), 'Goodbye')

        pass

    def test_english_to_french(self):
        h = 'Hello'
        self.assertEqual(h[0].english_to_french(), 'Bonjour')
        with self.assertRaises(TypeError):
            h[0].english_to_french(5)
        self.assertNotEqual(h.english_to_french(), 8)

    pass


if __name__ == "__main__":
    unittest.main()
    print('Passed All Tests')
