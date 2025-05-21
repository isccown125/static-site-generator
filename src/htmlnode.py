class HtmlNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html must be implemented by subclasses")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " "+" ".join([f"{key}=\"{value}\"" for key, value in self.props.items()])


class LeafNode(HtmlNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)

        if tag != "img" and value is None:
            raise ValueError("value cannot be None for a LeafNode")

    def to_html(self):
        if self.tag is None:
            return self.value

        if self.tag == "img":
            return f"<{self.tag} {self.props_to_html()} />"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Provide a tag for a ParentNode")
        if self.children is None:
            raise ValueError("Provide children for a ParentNode")
        
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
