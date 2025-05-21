from src.splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType
import unittest



class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [TextNode("Hello **World**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [TextNode("Hello ", TextType.TEXT), TextNode("World", TextType.BOLD), TextNode("", TextType.TEXT)])

    def test_split_nodes_delimiter_invalid_closing_delimiter(self):
        nodes = [TextNode("Hello **World", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_split_nodes_delimiter_invalid_opening_delimiter(self):
        nodes = [TextNode("Hello World**", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_split_nodes_delimiter_to_code(self):
        nodes = [TextNode("Hello `World`", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [TextNode("Hello ", TextType.TEXT), TextNode("World", TextType.CODE), TextNode("", TextType.TEXT)])


    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
    
    def test_split_links(self):
        node = TextNode(
        "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
        