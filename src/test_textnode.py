import unittest

from textnode import (TextNode,
                      split_nodes_delimiter,
                      extract_markdown_images,
                      extract_markdown_link,
                      split_nodes_image,
                      split_nodes_link,
                      text_type_bold,
                      text_type_code,
                      text_type_image,
                      text_type_italic,
                      text_type_link,
                      text_type_text)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        self.assertEqual(
            split_nodes_delimiter([node], "**", text_type_bold),
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word", "text"),
            ]
        )

    def test_split_nodes_delimiter_even_nodes(self):
        node = TextNode("This is text with a **bolded word", text_type_text)
        try:
            split_nodes_delimiter([node], "**", text_type_bold)
            raise TypeError("Should return error")
        except ValueError:
            pass
    
    def test_extract_markdown_images(self):
        text = "[image9](https://i.imgur.com/zjjcJKZ.png) This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png")
            ]
        )

    def test_extract_markdown_link(self):
        text = "[image9](https://i.imgur.com/zjjcJKZ.png) This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_link(text), [("image9", "https://i.imgur.com/zjjcJKZ.png")])

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes, 
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link!: [link1](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes, 
            [
                TextNode(
                    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link!: ",
                    text_type_text
                    ),
                TextNode(
                    "link1", text_type_link, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )


if __name__ == "__main__":
    unittest.main()
