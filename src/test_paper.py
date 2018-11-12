import io
import unittest.mock

from unittest import TestCase
from src.paper import Paper


class TestPaper(TestCase):
    def test_when_write_is_passed_string_it_adds_string_to_text_variable_in_the_paper_instance(self):
        paper = Paper()
        paper.write("Hello World!")
        self.assertEqual(paper.text, "Hello World!")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_when_print_text_is_called_it_prints_text_variable_to_stdout(self, mock_output):
        paper = Paper()
        paper.write("Hello World!")
        paper.print_text()
        self.assertEqual(mock_output.getvalue(), "Hello World!\n")
