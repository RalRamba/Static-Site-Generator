

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


class leafNode(HTMLNode):
    def __init__(self,tag = None,value = None ,props = None):
        super().__init__(tag,value,None,props)
    
    def to_html(self):
        propstring = ""
        if self.props is not None:
            propstring = self.props_to_html()
        return f"<{self.tag}{propstring}>{self.value}</{self.tag}>"

    __repr__ = lambda self: f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"
