from htmlnode import LeafNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text="", text_type="", url=None) -> None:
        self.text = text # The text content of the node
        self.text_type = text_type # Just a string like "bold" or "italic"
        self.url = url # The URL of the link or image, if the text is a link.

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(textnode: TextNode) -> LeafNode:
    if textnode.text_type == text_type_text:
        return LeafNode(None, textnode.text)
    if textnode.text_type == text_type_bold:
        return LeafNode("b", textnode.text)
    if textnode.text_type == text_type_italic:
        return LeafNode("i", textnode.text)
    if textnode.text_type == text_type_code:
        return LeafNode("code", textnode.text)
    if textnode.text_type == text_type_link:
        return LeafNode("a", textnode.text, {"href": textnode.url})
    if textnode.text_type == text_type_image:
        return LeafNode("img", "", {"src": textnode.url, "alt": textnode.text})
    raise ValueError(f"Invalid text type: {textnode.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        splitNodeText = node.text.split(delimiter)
        if len(splitNodeText) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: {node.text}")
        i = 0
        for newNodeText in splitNodeText:
            i += 1
            if i % 2 == 1:
                new_nodes.append(TextNode(newNodeText, text_type_text))
            else:
                new_nodes.append(TextNode(newNodeText, text_type))
    return new_nodes

def extract_markdown_images(text: str) -> list:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        
def extract_markdown_link(text: str) -> list:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    
def split_nodes_image(old_nodes) -> list:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        splitText = [old_node.text]
        for image_tup in images:
            splitText = old_node.text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if splitText[0] != "":
                new_nodes.append(TextNode(splitText[0], text_type_text))
            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
        if splitText[-1] != "":
            new_nodes.append(TextNode(splitText[-1], text_type_text))
    return new_nodes

def split_nodes_link(old_nodes) -> list:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_link(old_node.text)
        splitText = [old_node.text]
        for link_tup in links:
            splitText = old_node.text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if splitText[0] != "":
                new_nodes.append(TextNode(splitText[0], text_type_text))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
        if splitText[-1] != "":
            new_nodes.append(TextNode(splitText[-1], text_type_text))
    return new_nodes