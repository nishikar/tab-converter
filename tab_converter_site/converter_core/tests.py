import unittest
from converter import get_note


class ConverterTest(unittest.TestCase):

    def test_get_note(self):
        note = get_note('C', 5)
        self.assertEqual(note, 'F')
        note = get_note('c', 5)
        self.assertEqual(note, 'f')
