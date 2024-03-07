class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag # html tag
        self.value = value # text within tags
        self.children = children # sub nodes
        self.props = props # tag attributes

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        propsString = ""
        for prop in self.props:
            propsString += f"{prop}=\"{self.props[prop]}\" "
        return propsString.rstrip()


    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"