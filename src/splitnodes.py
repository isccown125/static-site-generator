from src.textnode import TextNode, TextType
from src.utils import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)

        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid delimiter usage in text: '{text}'")

        for i, part in enumerate(parts):
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        else:
            text = node.text

            links = extract_markdown_links(text)


            if len(links) > 0:
                rest_of_text = text
                for link_alt, link_url in links:
                    split_text = rest_of_text.split(f"[{link_alt}]({link_url})", 1)

                    rest_of_text = split_text[1]

                    if len(split_text) > 1:
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                        new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))

                    else:
                        new_nodes.append(node)
                if len(rest_of_text) > 0:
                    new_nodes.append(TextNode(rest_of_text, TextType.TEXT))
            else:
                new_nodes.append(node)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        else:
            text = node.text

            images = extract_markdown_images(text)


            if len(images) > 0:
                rest_of_text = text
                for image_alt, image_url in images:
                    split_text = rest_of_text.split(f"![{image_alt}]({image_url})", 1)

                    rest_of_text = split_text[1]

                    if len(split_text) > 1:
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                        new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

                    else:
                        new_nodes.append(node)
                if len(rest_of_text) > 0:
                    new_nodes.append(TextNode(rest_of_text, TextType.TEXT))
            else:
                new_nodes.append(node)

    return new_nodes

