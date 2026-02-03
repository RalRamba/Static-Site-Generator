import unittest
from textnode import TextType, TextNode


from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

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
        node = LeafNode("p", "This is a paragraph", None)
        node2 = LeafNode("p", "This is a paragraph", None)
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


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_bold(self):
        node = TextNode("This is a BOLD node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a BOLD node")

    def test_italic(self):
        node = TextNode("This is an Italicized node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is an Italicized node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "www.link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href" : "www.link.com"})

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "www.image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src" : "www.image.com", "alt":node.text})


if __name__ == "__main__":
    unittest.main()


