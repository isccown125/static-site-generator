from src.manage_static_content import clear_public_folder, copy_static_content
from src.generate_page import generate_pages_recursive, generate_page
import sys

def main():
    base_path = sys.argv[1]
    
    clear_public_folder("public")
    copy_static_content("public")

    generate_pages_recursive("content", "src/template.html", "docs", base_path)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)
