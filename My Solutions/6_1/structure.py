import sys

class Structure:
    _fields = ()
    
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
    
    def __setattr__(self, name:str, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(getattr(self, field)) for field in self._fields)})"


