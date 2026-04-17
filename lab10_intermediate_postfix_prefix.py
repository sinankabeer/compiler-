class ExprTree:
    def __init__(self, op: str, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right

class IntermediateCodeConvertor:
    @staticmethod
    def to_postfix(node: ExprTree) -> str:
        if not node: return ""
        if not node.left and not node.right: return node.op
        return f"{IntermediateCodeConvertor.to_postfix(node.left)} {IntermediateCodeConvertor.to_postfix(node.right)} {node.op}".strip()

    @staticmethod
    def to_prefix(node: ExprTree) -> str:
        if not node: return ""
        if not node.left and not node.right: return node.op
        return f"{node.op} {IntermediateCodeConvertor.to_prefix(node.left)} {IntermediateCodeConvertor.to_prefix(node.right)}".strip()

if __name__ == '__main__':
    # Representing: a + b * c
    ast = ExprTree('+', ExprTree('a'), ExprTree('*', ExprTree('b'), ExprTree('c')))
    conv = IntermediateCodeConvertor()
    print("Postfix:", conv.to_postfix(ast))
    print("Prefix:", conv.to_prefix(ast))
