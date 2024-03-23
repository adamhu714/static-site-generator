block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

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
    # if text[:2] == "# ":
    #     return True
    # if len(text) == 2:
    #     return False
    # if text[:3] == "## ":
    #     return True
    # if len(text) == 3:
    #     return False
    # if text[:4] == "### ":
    #     return True
    # if len(text) == 4:
    #     return False
    # if text[:5] == "#### ":
    #     return True
    # if len(text) == 5:
    #     return False
    # if text[:6] == "##### ":
    #     return True
    # if len(text) == 6:
    #     return False
    # if text[:7] == "###### ":
    #     return True
    # return False