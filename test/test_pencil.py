from unittest import TestCase
from src.paper import Paper
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
        self.assertEqual(self.pencil.current_length, 10)

        self.pencil.sharpen()

        self.assertEqual(self.pencil.current_tip_durability, 1000)
        self.assertEqual(self.pencil.current_length, 9)


class ShortTestPencil(TestPencil):

    def setUp(self):
        super(ShortTestPencil, self).setUp()
        self.pencil.set_length(0)
        self.pencil.set_max_tip_durability(1000)

    def test_when_sharpen_is_called_when_there_is_no_length_left_to_sharpen_it_leaves_the_current_tip_durability_variable_in_the_pencil_instance_as_is(self):
        self.assertEqual(self.pencil.current_tip_durability, 0)
        self.assertEqual(self.pencil.current_length, 0)

        self.pencil.sharpen()

        self.assertEqual(self.pencil.current_tip_durability, 0)
        self.assertEqual(self.pencil.current_length, 0)


class LowDurabilityTestPencil(TestPencil):

    def setUp(self):
        super(LowDurabilityTestPencil, self).setUp()
        self.pencil.set_length(1)
        self.pencil.set_max_tip_durability(10)

        self.pencil.sharpen()

    def test_when_pencil_write_is_passed_a_paper_instance_and_a_string_to_write_it_will_degrade_the_pencil_durability_and_write_the_resulting_string_on_the_paper(self):
        paper = Paper()

        self.assertEqual(self.pencil.current_tip_durability, 10)

        self.pencil.write(paper, "This is a string to be written.")

        self.assertEqual(paper.text, "This is a st                   ")
        self.assertEqual(self.pencil.current_tip_durability, 0)


class HighDurabilityTestPencil(TestPencil):

    def setUp(self):
        super(HighDurabilityTestPencil, self).setUp()
        self.pencil.set_length(10)
        self.pencil.set_max_tip_durability(1000)

        self.pencil.sharpen()

    def test_when_pencil_write_is_passed_a_paper_instance_and_a_string_to_write_it_will_degrade_the_pencil_durability_and_write_the_resulting_string_on_the_paper(self):
        paper = Paper()

        self.assertEqual(self.pencil.current_tip_durability, 1000)

        self.pencil.write(paper, "This is a string to be written.")

        self.assertEqual(paper.text, "This is a string to be written.")
        self.assertEqual(self.pencil.current_tip_durability, 974)

    def test_when_pencil_write_at_is_passed_a_string_and_an_index_it_will_write_the_string_on_the_paper_at_that_index_on_white_space(self):
        paper = Paper()
        paper.text = "An       a day keeps the doctor away"

        self.pencil.write_at(paper, "onion", 3)

        self.assertEqual(paper.text, "An onion a day keeps the doctor away")

    def test_when_pencil_write_at_is_passed_a_string_and_an_index_it_will_write_the_string_on_the_paper_at_that_index_and_overwrite_filled_spaces_with_symbol(self):
        paper = Paper()
        paper.text = "An       a day keeps the doctor away"

        self.pencil.write_at(paper, "artichoke", 3)
        
        self.assertEqual(paper.text, "An artich@k@ay keeps the doctor away")

    def test_when_pencil_write_at_is_passed_a_string_and_an_index_less_than_zero_raises_index_error(self):
        paper = Paper()
        paper.text = "An apple a day keeps the doctor away"

        self.assertRaises(IndexError, lambda: self.pencil.write_at(paper, "Remember, a", -10))

    def test_when_pencil_write_at_is_passed_a_string_and_an_index_greater_than_paper_text_length_it_adds_text_to_end(self):
        paper = Paper()
        paper.text = "An apple a day keeps the doctor away"

        self.pencil.write_at(paper, ", don't you know.", 40)

        self.assertEqual(paper.text, "An apple a day keeps the doctor away, don't you know.")

    def test_when_pencil_write_at_is_passed_a_string_and_an_index_that_is_in_bounds_but_string_len_plus_index_is_greater_than_paper_text_length_it_overwrites_and_addes_on(self):
        paper = Paper()
        paper.text = "An apple a day keeps the doctor away"

        self.pencil.write_at(paper, "from coming around.", 32)

        self.assertEqual(paper.text, "An apple a day keeps the doctor @@@@ coming around.")
