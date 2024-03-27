import os
import shutil
from blocks import markdown_to_html_node, markdown_to_blocks, block_to_block_type, block_type_heading

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for content in contents:
        item = os.path.join(dir_path_content, content)
        dest = os.path.join(dest_dir_path, content)
        if os.path.isdir(item):
            generate_pages_recursive(item, template_path, dest)
        if item.lower().endswith(('.md', '.markdown')):
            base_name, _ = os.path.splitext(dest)
            dest = base_name + ".html"
            generate_page(item, template_path, dest)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as markdown_file:
        markdown = markdown_file.read()
        md_html = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)
        
    with open(template_path, "r") as template:
        final_file = template.read().replace(" {{ Title }} ", title)
    final_file = final_file.replace("{{ Content }}", md_html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as target:
        target.write(final_file)

def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading and block[:2] == "# ":
            return block[2:]
    raise ValueError("markdown file requires at least one h1 header")

def copy_static_dir():
    if not os.path.exists("./static/"):
        raise FileNotFoundError("static folder not found")
    if os.path.exists("./public/"):
        shutil.rmtree("./public/")
    os.mkdir("./public/")
    copy_recursion("./static/", "./public/", os.listdir("./static/"))

def copy_recursion(from_path, target_path, contents):
    for content in contents:
        if os.path.isdir(from_path + content):
            os.mkdir(target_path + content)
            print(f"made directory {target_path + content}")
            copy_recursion(from_path + content + "/", target_path + content + "/", os.listdir(from_path + content))
        if os.path.isfile(from_path + content):
            shutil.copy(from_path + content, target_path + content)
            print(f"copied file to {target_path + content}")