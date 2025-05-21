import enum
import re
class BlockType(enum.Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str):
    block = block.strip()

    if block.startswith("#"):
        return BlockType.HEADING
    elif block.startswith("-") or block.startswith("*") or block.startswith("+"):
        return BlockType.UNORDERED_LIST
    elif re.match(r"^\d+\.\s", block):
        return BlockType.ORDERED_LIST
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif re.match(r"^>\s?", block):
        return BlockType.QUOTE
    else:
        return BlockType.PARAGRAPH
