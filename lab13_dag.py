from typing import Dict, Optional

class DAGNode:
    def __init__(self, value: str, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class DAGBuilder:
    def __init__(self):
        self.node_map: Dict[str, DAGNode] = {}

    def add_node(self, op: str, left_val: str, right_val: Optional[str] = None) -> DAGNode:
        # Search for existing common subexpression
        signature = f"{op}_{left_val}_{right_val}"
        if signature in self.node_map:
            return self.node_map[signature]

        left_node = self.node_map.get(left_val, DAGNode(left_val))
        right_node = self.node_map.get(right_val, DAGNode(right_val)) if right_val else None
        
        new_node = DAGNode(op, left_node, right_node)
        self.node_map[signature] = new_node
        self.node_map[new_node.value] = new_node # Simplified reference
        return new_node

if __name__ == '__main__':
    dag = DAGBuilder()
    # a + a * (b - c) + (b - c) * d
    n1 = dag.add_node('-', 'b', 'c') # common
    n2 = dag.add_node('*', 'a', n1.value)
    print("DAG Nodes tracked for reuse:", len(dag.node_map))
