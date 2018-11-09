from unittest import TestCase
from src.pencil import Pencil


class TestPencil(TestCase):
    def test_when_set_durability_is_passed_a_number_it_sets_the_durability_variable_in_the_pencil_instance(self):
        pencil = Pencil()
        pencil.set_durability(1000)
        self.assertEqual(pencil.durability, 1000)
