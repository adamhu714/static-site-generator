import unittest

from blocks import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    block_to_html_node,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)

from htmlnode import ParentNode, LeafNode

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = "This is **bolded** paragraph\n\n\n\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n"
        self.assertEqual(
            markdown_to_blocks(text),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ]
        )

    def test_block_to_block_type(self):
        texts = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
            "1. This is a list\n2. with items",
            "1 This is a list\n2 without dots",
            "1. This is a list\n2. with items\n2. hi",
            "```This is code\n* with lines```",
            "### headings fdsag",
            "# # grijsgij",
            ">grwijgi4w\n>fnrwugnruwg\n>girjigr"
        ]  
        expected = [
            block_type_paragraph,
            block_type_paragraph,
            block_type_unordered_list,
            block_type_ordered_list,
            block_type_paragraph,
            block_type_paragraph,
            block_type_code,
            block_type_heading,
            block_type_heading,
            block_type_quote,
        ]
        for i in range(len(texts)):
            self.assertEqual(
            block_to_block_type(texts[i]),
            expected[i]
        )
            
    def test_block_to_html_node(self):
        texts = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items",
            "1. This is a list\n2. with items",
            "1 This is a list\n2 without dots",
            "1. This is a list\n2. with items\n2. hi",
            "```This is code\n with lines```",
            "### headings fdsag",
            "# # grijsgij",
            ">grwijgi4w\n>fnrwugnruwg\n>girjigr"
        ]  
        expected = [
            ParentNode("p", [
                LeafNode(None, "This is "),
                LeafNode("b", "bolded"),
                LeafNode(None, " paragraph"),
            ]),
            ParentNode("p", [
                LeafNode(None, "This is another paragraph with "),
                LeafNode("i", "italic"),
                LeafNode(None, " text and "),
                LeafNode("code", "code"),
                LeafNode(None, " here\nThis is the same paragraph on a new line"),
            ]),
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "This is a list")]),
                ParentNode("li", [LeafNode(None, "with items")]),
            ]),
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "This is a list")]),
                ParentNode("li", [LeafNode(None, "with items")]),
            ]),
            ParentNode("p", [LeafNode(None, "1 This is a list\n2 without dots")]),
            ParentNode("p", [LeafNode(None, "1. This is a list\n2. with items\n2. hi")]),
            ParentNode("pre", [ParentNode("code", [
                LeafNode(None, "This is code\n with lines")
            ])]),
            ParentNode("h3", [
                LeafNode(None, "headings fdsag")
            ]),
            ParentNode("h1", [
                LeafNode(None, "# grijsgij")
            ]),
            ParentNode("blockquote", [
                LeafNode(None, "grwijgi4w\nfnrwugnruwg\ngirjigr")
            ]),
        ]
        for i in range(len(texts)):
            print()
            print(block_to_html_node(texts[i]))
            print(expected[i])
            self.assertEqual(
            block_to_html_node(texts[i]),
            expected[i]
        )

if __name__ == "__main__":
    unittest.main()