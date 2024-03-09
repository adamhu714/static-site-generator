import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(" class=\"greeting\" href=\"https://boot.dev\"", node.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            "HTMLNode(div, Hello, world!, children: None, {'class': 'greeting', 'href': 'https://boot.dev'})", repr(node)
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "This is a value")
        self.assertEqual("<p>This is a value</p>", node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a value")
        self.assertEqual("This is a value", node.to_html())


if __name__ == "__main__":
    unittest.main()
