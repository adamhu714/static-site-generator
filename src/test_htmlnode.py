import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual("class=\"greeting\" href=\"https://boot.dev\"", node.props_to_html())

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


if __name__ == "__main__":
    unittest.main()
