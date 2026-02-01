import unittest

from htmlnode import HTMLNode, leafNode

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
        node = leafNode("<p>", "This is a paragraph", None)
        node2 = leafNode("<p>", "This is a paragraph", None)
        self.assertEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = leafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")



if __name__ == "__main__":
    unittest.main()


