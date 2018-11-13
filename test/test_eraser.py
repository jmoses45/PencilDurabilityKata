from test.test_pencil import TestPencil


class AttributeTestEraser(TestPencil):

    def test_when_eraser_set_durability_is_passed_a_number_it_sets_the_current_durability_variable_in_the_pencil_eraser_instance(self):
        self.pencil.eraser.set_durability(1000)
        self.assertEqual(self.pencil.eraser.current_durability, 1000)
