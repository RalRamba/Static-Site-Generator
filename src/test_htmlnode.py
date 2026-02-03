import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "This is a paragraph", None, None)
        node2 = HTMLNode("<p>", "This is a paragraph", None, None)
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("<p>", "This is a paragraph", None, None)
        node2 = HTMLNode("<p>", "This is a paragraph", None, None)
        self.assertEqual(node, node2)
    
    def test_node_to_html_childless(self):
        node = HTMLNode("p", "Hello, world!")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_dif_tag(self):
        node = HTMLNode("<p>", "This is a paragraph", None, None)
        node2 = HTMLNode("<b>", "This is a paragraph", None, None)
        self.assertNotEqual(node, node2)

    def test_dif_value(self):
        node = HTMLNode("<p>", "This is a paragraph", None, None)
        node2 = HTMLNode("<p>", "This is a different paragraph", None, None)
        self.assertNotEqual(node, node2)

    def test_dif_(self):
        node = HTMLNode("<p>", "This is a paragraph", None, None)
        node2 = HTMLNode("<p>", "This is a different paragraph", None, None)
        self.assertNotEqual(node, node2)



class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("<p>", "This is a paragraph", None)
        node2 = LeafNode("<p>", "This is a paragraph", None)
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()


