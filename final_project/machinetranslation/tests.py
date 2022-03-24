import unittest

null = ''


class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        b = 'Bonjour'
        self.assertEqual(b.french_to_english(), 'Hello')
        with self.assertRaises(TypeError):
            b.french_to_english(3)
        self.assertNotEqual(b.french_to_english(), 4)

        pass

    def test_english_to_french(self):
        h = 'Hello'
        self.assertEqual(h.english_to_french(), 'Bonjour')
        with self.assertRaises(TypeError):
            h.english_to_french(5)
        self.assertNotEqual(h.english_to_french(), 8)

    pass


if __name__ == "__main__":
    unittest.main()
    print('Passed All Tests')
