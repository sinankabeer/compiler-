from typing import Set, Dict, List

class BasicBlock:
    def __init__(self, bid: int, gen: Set[int], kill: Set[int], predecessors: List['BasicBlock']):
        self.id = bid
        self.gen = gen
        self.kill = kill
        self.preds = predecessors
        self.in_set: Set[int] = set()
        self.out_set: Set[int] = set(gen)

class ReachingDefinitions:
    def __init__(self, blocks: List[BasicBlock]):
        self.blocks = blocks

    def analyze(self):
        changed = True
        while changed:
            changed = False
            for block in self.blocks:
                new_in = set()
                for p in block.preds:
                    new_in.update(p.out_set)
                
                block.in_set = new_in
                new_out = block.gen.union(block.in_set - block.kill)
                
                if new_out != block.out_set:
                    block.out_set = new_out
                    changed = True

if __name__ == '__main__':
    b1 = BasicBlock(1, {1, 2}, {3}, [])
    b2 = BasicBlock(2, {3}, {1}, [b1])
    rd = ReachingDefinitions([b1, b2])
    rd.analyze()
    print("Block 2 IN:", rd.blocks[1].in_set)
