from src.markdown_to_blocks import markdown_to_blocks
from src.block import block_to_block_type, BlockType
from src.text_to_textnodes import text_to_textnodes
from src.textnode import text_node_to_html_node
from src.htmlnode import ParentNode
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlNodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        htmlNodes.append(block_to_html_node(block, block_type))
    return ParentNode("div", htmlNodes)


def format_list_item(item, block_type):
    match block_type:
        case BlockType.UNORDERED_LIST:
            return remove_unordered_list_prefix(item)
        case BlockType.ORDERED_LIST:
            return remove_ordered_list_prefix(item)

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            text = " ".join(block.splitlines())
            textNodes = text_to_textnodes(text)
            htmlNodes = [text_node_to_html_node(textNode) for textNode in textNodes]
            if len(htmlNodes) == 1:
                return htmlNodes[0]
            return ParentNode("p", htmlNodes)
        case BlockType.HEADING:
            return convert_block_to_heading(block)  
        case BlockType.UNORDERED_LIST:
            return convert_block_to_unordered_list(block)
        case BlockType.ORDERED_LIST:
            return convert_block_to_ordered_list(block)
        case BlockType.QUOTE:
            return convert_block_to_quote(block)
        case BlockType.CODE:
            textNodes = text_to_textnodes(block)
            htmlNodes = [text_node_to_html_node(textNode) for textNode in textNodes]
            if len(htmlNodes) == 1:
                return htmlNodes[0]
            return ParentNode("pre", htmlNodes)
        case _:
            raise ValueError(f"Unsupported block type: {block_type}")
    
def remove_unordered_list_prefix(line):
    return re.sub(r'^(\s*[-*+])\s+', '', line)

def remove_ordered_list_prefix(line) :
    return re.sub(r'^\s*\d+\.\s+', '', line)

def check_heading_level(line):
    return len(line) - len(line.lstrip('#'))

def remove_heading_prefix(line):
    return re.sub(r'^(#+)\s+', '', line)

def remove_quote_prefix(line):
    return re.sub(r'^(>+)\s+', '', line)


def convert_block_to_unordered_list(block):
    list_items = [text_to_textnodes(remove_unordered_list_prefix(item)) for item in block.split("\n")]

    nodes = []
    for item in list_items:
        textNodes = []
        for textNode in item:
            textNodes.append(text_node_to_html_node(textNode))
        nodes.append(ParentNode("li", textNodes))

    return ParentNode("ul", nodes)

def convert_block_to_ordered_list(block):
    list_items = [text_to_textnodes(remove_ordered_list_prefix(item)) for item in block.split("\n")]

    nodes = []
    for item in list_items:
        textNodes = []
        for textNode in item:
            textNodes.append(text_node_to_html_node(textNode))
        nodes.append(ParentNode("li", textNodes))

    return ParentNode("ol", nodes)

def convert_block_to_heading(block):
    level = check_heading_level(block)
    textNodes = text_to_textnodes(remove_heading_prefix(block))
    htmlNodes = [text_node_to_html_node(textNode) for textNode in textNodes]
    return ParentNode("h" + str(level), htmlNodes)

def convert_block_to_quote(block):
    textNodes = text_to_textnodes(remove_quote_prefix(block))
    htmlNodes = [text_node_to_html_node(textNode) for textNode in textNodes]
    return ParentNode("blockquote", htmlNodes)

