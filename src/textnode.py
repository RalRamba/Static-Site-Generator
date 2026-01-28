from enum import Enum

class TextType(Enum):
    plain = 1
    bold = 2
    code = 3
    links = 4
    images = 5 

class TextNode():
    def __init__(self, text , text_type , url):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url


    __eq__ = lambda self, other: self.text == other.text and self.text_type == other.text_type and self.url == other.url

    __repr__ = lambda self: f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"

