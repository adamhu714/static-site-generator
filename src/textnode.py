class TextNode:
    def __init__(self, text="", text_type="", url=None) -> None:
        self.text = text # The text content of the node
        self.text_type = text_type # Just a string like "bold" or "italic"
        self.url = url # The URL of the link or image, if the text is a link.

    def eq(self, other) -> bool:
        return (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url)
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"