from htmlnode import ParentNode

from textnode import (
    text_node_to_html_node,
    text_to_textnodes,
)

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    blocks_html_nodes = []
    for block in blocks:
        blocks_html_nodes.append(block_to_html_node(block))
    return ParentNode("div", blocks_html_nodes)
    

def markdown_to_blocks(text: str) -> list:
    strings = text.split("\n\n")
    for i in range(len(strings)):
        strings[i] = strings[i].strip()
    strings = list(filter(None, strings))
    return strings

def block_to_block_type(text: str) -> str:
    if is_heading(text):
        return block_type_heading
    if len(text) >= 6:
        if text[:3] == "```" and text[-3:] == "```":
            return block_type_code
        
    lines = text.split("\n")

    is_quote = True
    is_unordered_list = True
    is_ordered_list = True

    for i in range(len(lines)):
        if len(lines[i]) == 0:
            is_quote = False
            is_unordered_list = False
            is_ordered_list = False
            break
        if len(lines[i]) > 1 and is_ordered_list == True:
            if lines[i][0] != str(i+1) or lines[i][1] != ".":
                is_ordered_list = False
        else:
            is_ordered_list = False
        if lines[i][0] != ">":
            is_quote = False
        if lines[i][0] != "*" and lines[i][0] != "-":
            is_unordered_list = False
        if not is_quote and not is_unordered_list and not is_ordered_list:
            break
    
    if is_quote:
        return block_type_quote
    if is_unordered_list:
        return block_type_unordered_list
    if is_ordered_list:
        return block_type_ordered_list
    
    return block_type_paragraph


def is_heading(text):
    if len(text) == 1:
        return False
    if text[0] == "#":
        # checks if there is a space following the hashes (max 6 hashes)
        for i in range(len(text[1:])):
            if i == 7:
                return False
            if text[i+1] == " ":
                return True
            if text[i+1] != "#":
                return False
    return False

def paragraph_block_to_html_node(block: str) -> ParentNode:
    textnodes = text_to_textnodes(block)
    inline_children = [text_node_to_html_node(node) for node in textnodes]
    return ParentNode("p", inline_children)

def heading_block_to_html_node(block: str) -> ParentNode:
    for i in range(1, len(block)):
        if block[i] == " ":
            num_of_hashes = i
            break
    textnodes = text_to_textnodes(block[num_of_hashes+1:])
    inline_children = [text_node_to_html_node(node) for node in textnodes]
    return ParentNode(f"h{num_of_hashes}", inline_children)

def code_block_to_html_node(block: str) -> ParentNode:
    textnodes = text_to_textnodes(block[3:-3])
    inline_children = [text_node_to_html_node(node) for node in textnodes]
    return ParentNode("pre", [ParentNode("code", inline_children)])

def quote_block_to_html_node(block: str) -> ParentNode:
    stripped = "\n".join([line[1:].strip() for line in block.split("\n")])
    textnodes = text_to_textnodes(stripped)
    inline_children = [text_node_to_html_node(node) for node in textnodes]
    return ParentNode("blockquote", inline_children)

def unordered_list_block_to_html_node(block: str) -> ParentNode:
    stripped_lists = [line[1:].strip() for line in block.split("\n")]
    list_children = []
    for item in stripped_lists:
        textnodes = text_to_textnodes(item)
        inline_children = [text_node_to_html_node(node) for node in textnodes]
        list_children.append(ParentNode("li", inline_children))
    return ParentNode("ul", list_children)

def ordered_list_block_to_html_node(block: str) -> ParentNode:
    stripped_lists = [line[2:].strip() for line in block.split("\n")]
    list_children = []
    for item in stripped_lists:
        textnodes = text_to_textnodes(item)
        inline_children = [text_node_to_html_node(node) for node in textnodes]
        list_children.append(ParentNode("li", inline_children))
    return ParentNode("ol", list_children)

def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_block_to_html_node(block)
    if block_type == block_type_heading:
        return heading_block_to_html_node(block)
    if block_type == block_type_code:
        return code_block_to_html_node(block)
    if block_type == block_type_quote:
        return quote_block_to_html_node(block)
    if block_type == block_type_unordered_list:
        return unordered_list_block_to_html_node(block)
    if block_type == block_type_ordered_list:
        return ordered_list_block_to_html_node(block)
