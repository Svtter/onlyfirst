import unittest
from onlyfirst import onlyfirst


class StrTest(unittest.TestCase):
    def test_str(self):
        test = """test = "hello" """
        self.assertEqual(
            onlyfirst.process_single(test),
            "test ="
        )

    def test_multiple_str(self):
        test = """
        test = "hello"
        world = "hello"
        """
        self.assertEqual(
            onlyfirst.process_paragraph(test),
            """test =\nworld =\n
            """
        )