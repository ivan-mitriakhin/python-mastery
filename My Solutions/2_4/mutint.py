from functools import total_ordering
import sys

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value})'

    def __format__(self, fmt):
        return format(self.value, fmt)
    
    def __add__(self, other):
        if isinstance(other, int):
            return self.value + other
        elif isinstance(other, MutInt):
            return self.value + other.value
        else:
            return NotImplemented
        
    __radd__ = __add__

    def __iadd__(self, other):
        if isinstance(other, int):
            self.value += other
            return self
        elif isinstance(other, MutInt):
            self.value += other.value
            return self
        else:
            return NotImplemented
        
    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        elif isinstance(other, MutInt):
            return self.value == other.value
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        elif isinstance(other, MutInt):
            return self.value < other.value
        else:
            return NotImplemented
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    __index__ = __int__

if __name__ == "__main__":
    a = MutInt(3)
    print(f"The value is {a:*^10d}")
    b = MutInt(5)
    c = 7
    print(a + b)
    print(a + c)
    print(c + a)
    a += 10
    print(a)
    print(a < b)
    print(int(a))
    print(float(a))
    names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis', 'Clara']
    print(names[b])