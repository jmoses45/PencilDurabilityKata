from unittest import TestCase
from src.paper import Paper


class TestPaper(TestCase):
    def test_when_write_is_passed_string_it_adds_string_to_text_variable_in_the_paper_instance(self):
        paper = Paper()
        paper.write("Hello World!")
        self.assertEqual(paper.text, "Hello World!")
