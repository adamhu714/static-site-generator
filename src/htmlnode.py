class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag # html tag
        self.value = value # text within tags
        self.children = children # sub nodes
        self.props = props # tag attributes

    def to_html(self) -> str:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        propsString = ""
        for prop in self.props:
            propsString += f" {prop}=\"{self.props[prop]}\""
        return propsString


    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None: 
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, LeafNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.props == other.props

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ParentNode):
            return False
        return self.tag == other.tag and self.children == other.children and self.props == other.props