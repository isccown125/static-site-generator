from src.utils import extract_title_from_markdown
from src.markdown_to_html_node import markdown_to_html_node
import os
def generate_page(from_path, template_path, destination_path, base_path = "/"):
    title = ""
    content = ""
    
    with open(from_path, "r") as file:
        content = file.read()

    with open(template_path, "r") as file:
        template = file.read()


    title = extract_title_from_markdown(content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", markdown_to_html_node(content).to_html())

    template = template.replace("href=\"/", f"href=\"{base_path}")
    template = template.replace("src=\"/", f"src=\"{base_path}")

    with open(destination_path, "w") as file:
        file.write(template)
    
    

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path = "/"):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    
    dir_list = os.listdir(dir_path_content)

    for dir in dir_list:
        if os.path.isdir(os.path.join(dir_path_content, dir)):
            print(f"Generating pages for {dir}")
            generate_pages_recursive(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, dir), base_path)
        else:
            print(f"Generating page for {dir}")
            generate_page(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, "index.html"), base_path)

