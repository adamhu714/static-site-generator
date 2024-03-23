import unittest

from blocks import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)

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

if __name__ == "__main__":
    unittest.main()