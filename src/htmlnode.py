from textnode import TextType, TextNode

class HTMLNode():
    def __init__(self,tag = None,value = None ,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def props_to_html(self):
        propstring = ""
        for prop in self.props.keys():
            propstring += " " + propstring + prop + '=' + "\"" + self.props[prop] + " \" "
        return propstring.strip()
    
    __repr__ = lambda self: f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    __eq__ = lambda self, other: self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


class ParentNode(HTMLNode):
    def __init__(self,tag, children, props = None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if not self.tag:
            raise(ValueError("ERROR: No value present"))
        if not self.children:
            raise(ValueError("ERROR: No Child Nodes present"))
        else:
            node_string = f"<{self.tag}>"
            for child in self.children:
                node_string = node_string + (f"{child.to_html()}")
            node_string = node_string + (f"</{self.tag}>")
            return node_string.strip()


class LeafNode(HTMLNode):
    def __init__(self,tag = None,value = None ,props = None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        propstring = ""
        if self.props is not None:
            propstring = self.props_to_html()
        return f"<{self.tag}{propstring}>{self.value}</{self.tag}>"

    __repr__ = lambda self: f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"

#tests conversion from textnode class to a leafnode
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise(ValueError)
    if text_node.text_type is TextType.TEXT:
        return LeafNode(None,text_node.text)
    if text_node.text_type is TextType.BOLD:
        return LeafNode("b",text_node.text)
    if text_node.text_type is TextType.ITALIC:
        return LeafNode("i",text_node.text)
    if text_node.text_type is TextType.CODE:
        return LeafNode("code",text_node.text)
    if text_node.text_type is TextType.LINK:
        return LeafNode("a",text_node.text, {"href" : text_node.url})
    if text_node.text_type is TextType.IMAGE:
        return LeafNode("img",None, {"src" : text_node.url , "alt" : text_node.text})
