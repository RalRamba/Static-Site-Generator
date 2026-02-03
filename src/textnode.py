from enum import Enum

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6 

class TextNode():
    def __init__(self, text , text_type , url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url


    __eq__ = lambda self, other: self.text == other.text and self.text_type == other.text_type and self.url == other.url

    __repr__ = lambda self: f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"
