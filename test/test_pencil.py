from unittest import TestCase
from src.pencil import Pencil


class TestPencil(TestCase):
    def test_set_durability(self):
        pencil = Pencil()
        pencil.set_durability(1000)
        self.assertEqual(pencil.durability, 1000)
