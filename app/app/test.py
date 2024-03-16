from django.test import SimpleTestCase

from app import calc


class CalTest(SimpleTestCase):

    def test_add_numbers(self):

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract(self):
        res = calc.sub(2, 1)

        self.assertEqual(res, 1)
