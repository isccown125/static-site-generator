import unittest
from src.block import block_to_block_type, BlockType

class TestBlock(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- This is a list item"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. This is a list item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("2. This is a list item"), BlockType.ORDERED_LIST)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("``` This is a code block ```"), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
