import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        self.assertEqual(node.to_html(), "<p>This is a value</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a value")
        self.assertEqual(node.to_html(), "This is a value")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("p", "This is a child value")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><p>This is a child value</p></div>')
    
    def test_to_html_with_grand_children(self):
        grandchild_node = LeafNode("p", "This is a grandchild value")
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), '<div><div><p>This is a grandchild value</p></div></div>')
    
    def test_to_html_with_many_children(self):
        child_nodes = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        parent_node = ParentNode("p", child_nodes)
        self.assertEqual(parent_node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

if __name__ == "__main__":
    unittest.main()
