from unittest import TestCase
from src.pencil import Pencil


class TestPencil(TestCase):
    def test_when_set_max_tip_durability_is_passed_a_number_it_sets_the_max_tip_durability_variable_in_the_pencil_instance(self):
        pencil = Pencil()
        pencil.set_max_tip_durability(1000)
        self.assertEqual(pencil.max_tip_durability, 1000)

    def test_when_sharpen_is_called_it_sets_the_current_tip_durability_variable_in_the_pencil_instance_to_max_tip_durability(self):
        pencil = Pencil()
        pencil.set_max_tip_durability(1000)

        self.assertEqual(pencil.current_tip_durability, 0)

        pencil.sharpen()

        self.assertEqual(pencil.current_tip_durability, 1000)
