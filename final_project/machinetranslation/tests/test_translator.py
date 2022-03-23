import unittest

from machinetranslation.translator import french_to_english, english_to_french

null = ''


class TestTranslator(unittest.TestCase):
    def test_is_french_to_english(self):
        self.assertEqual('Bonjour'.french_to_english, 'Hello')

        self.assertNotEqual('Hello'.french_to_english, "Mon Aime")

        pass

    def test_is_english_to_french(self):
        self.assertEqual('Hello'.english_to_french, 'Bonjour')

        self.assertNotEqual('Hello'.english_to_french, "Je t'Adore")

        pass


if __name__ == "__main__":
    unittest.main()
    print('Passed All Tests')
