from enum import Enum

class TextType(Enum):
    PLAIN = 1
    BOLD = 2
    CODE = 3
    LINKS = 4
    IMAGES = 5 

class TextNode():
    def __init__(self, text , text_type , url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url


    __eq__ = lambda self, other: self.text == other.text and self.text_type == other.text_type and self.url == other.url

    __repr__ = lambda self: f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"

