from src.splitnodes import split_nodes_link, split_nodes_image, split_nodes_delimiter
from src.textnode import TextType, TextNode

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)

    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_link(split_nodes_image([text_node])), "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE)