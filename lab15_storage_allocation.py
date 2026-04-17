from typing import Dict, Any

class AllocationSystem:
    def __init__(self, memory_size: int = 1024):
        self.memory = [0] * memory_size
        self.stack_ptr = memory_size - 1
        self.heap_ptr = 0
        self.static_ptr = 0
        self.symbol_table: Dict[str, int] = {}

    def alloc_static(self, name: str, size: int) -> int:
        addr = self.static_ptr
        self.static_ptr += size
        self.symbol_table[name] = addr
        return addr

    def alloc_stack(self, size: int) -> int:
        self.stack_ptr -= size
        if self.stack_ptr <= self.heap_ptr:
            raise MemoryError("Stack Overflow")
        return self.stack_ptr

    def pop_stack(self, size: int):
        self.stack_ptr += size

    def alloc_heap(self, size: int) -> int:
        # Simplistic bump-pointer heap allocation
        addr = self.heap_ptr
        self.heap_ptr += size
        if self.heap_ptr >= self.stack_ptr:
            raise MemoryError("Out of Heap Memory")
        return addr

if __name__ == '__main__':
    mem = AllocationSystem()
    print("Static var at:", mem.alloc_static('global_x', 4))
    print("Heap var at:", mem.alloc_heap(16))
    print("Stack frame at:", mem.alloc_stack(32))
