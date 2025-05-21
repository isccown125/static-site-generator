import re


def extract_markdown_images(text):
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r'(?<!\!)\[(.*?)\]\((.*?)\)'
    return re.findall(pattern, text)

def extract_title_from_markdown(text):
    pattern = r'^# (.*)'
    title = re.findall(pattern, text)
    if len(title) > 0:
        return title[0]
    raise ValueError("No title found in the markdown text")
        
