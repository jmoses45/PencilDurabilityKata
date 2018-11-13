from src.paper import Paper
from test.test_pencil import TestPencil


class AttributeTestEraser(TestPencil):

    def test_when_eraser_set_durability_is_passed_a_number_it_sets_the_current_durability_variable_in_the_pencil_eraser_instance(self):
        self.pencil.eraser.set_durability(1000)
        self.assertEqual(self.pencil.eraser.current_durability, 1000)

    def test_when_eraser_is_given_a_string_to_erase_it_losses_durability_matching_amount_erased(self):
        self.pencil.eraser.set_durability(1000)

        paper = Paper()
        paper.text = "Hello World!"

        self.pencil.eraser.erase(paper, "World")

        self.assertEqual(self.pencil.eraser.current_durability, 995)

    def test_when_eraser_is_given_a_string_with_spaces_to_erase_it_losses_durability_matching_amount_erased(self):
        self.pencil.eraser.set_durability(1000)

        paper = Paper()
        paper.text = "Hello World!"

        self.pencil.eraser.erase(paper, " World")

        self.assertEqual(self.pencil.eraser.current_durability, 995)

    def test_when_eraser_is_given_a_string_to_erase_and_has_enough_durability_to_do_so(self):
        self.pencil.eraser.set_durability(1000)

        paper = Paper()
        paper.text = "Hello World!"

        self.pencil.eraser.erase(paper, "World")

        self.assertEqual(paper.text, "Hello      !")

    def test_when_eraser_is_given_a_string_to_erase_and_does_not_have_enough_durability_to_do_so(self):
        self.pencil.eraser.set_durability(3)

        paper = Paper()
        paper.text = "Hello World!"

        self.pencil.eraser.erase(paper, "World")

        self.assertEqual(paper.text, "Hello Wo   !")

    def test_when_eraser_is_given_a_complex_string_to_erase_multiple_parts_of(self):
        self.pencil.eraser.set_durability(1000)

        paper = Paper()
        paper.text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

        self.pencil.eraser.erase(paper, "chuck")

        self.assertEqual(paper.text, "How much wood would a woodchuck chuck if a woodchuck could       wood?")

        self.pencil.eraser.erase(paper, "woodchuck")

        self.assertEqual(paper.text, "How much wood would a woodchuck chuck if a           could       wood?")
