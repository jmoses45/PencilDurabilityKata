from unittest import TestCase
from src.pencil import Pencil


class TestPencil(TestCase):
    def setUp(self):
        self.pencil = Pencil()

    def tearDown(self):
        self.pencil = None


class AttributeTestPencil(TestPencil):
    def test_when_set_length_is_passed_a_number_it_sets_the_current_length_variable_in_the_pencil_instance(self):
        self.pencil.set_length(10)
        self.assertEqual(self.pencil.current_length, 10)

    def test_when_set_max_tip_durability_is_passed_a_number_it_sets_the_max_tip_durability_variable_in_the_pencil_instance(self):
        self.pencil.set_max_tip_durability(1000)
        self.assertEqual(self.pencil.max_tip_durability, 1000)


class LongTestPencil(TestPencil):
    def setUp(self):
        super(LongTestPencil, self).setUp()
        self.pencil.set_length(10)
        self.pencil.set_max_tip_durability(1000)

    def test_when_sharpen_is_called_it_sets_the_current_tip_durability_variable_in_the_pencil_instance_to_max_tip_durability(self):
        self.assertEqual(self.pencil.current_tip_durability, 0)

        self.pencil.sharpen()

        self.assertEqual(self.pencil.current_tip_durability, 1000)


