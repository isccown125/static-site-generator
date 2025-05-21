from src.manage_static_content import clear_public_folder, copy_static_content
from src.generate_page import generate_pages_recursive
def main():
    clear_public_folder("public")
    copy_static_content("public")

    generate_pages_recursive("content", "src/template.html", "public")
if __name__ == "__main__":
    main()
