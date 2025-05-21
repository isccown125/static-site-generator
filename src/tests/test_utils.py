import unittest
from src.utils import extract_markdown_images, extract_markdown_links, extract_title_from_markdown

class TestUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_title_from_markdown(self):
        self.assertRaises(ValueError, extract_title_from_markdown, "This is a test title")

    def test_extract_title_from_markdown_with_title(self):
        title = extract_title_from_markdown(
            "# This is a test title"
        )
        self.assertEqual("This is a test title", title)
