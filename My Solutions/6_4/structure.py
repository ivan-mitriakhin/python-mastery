import sys
import inspect

class Structure:
    _fields = ()
    
    # @staticmethod
    # def _init():
    #     locs = sys._getframe(1).f_locals
    #     self = locs.pop('self')
    #     for name, val in locs.items():
    #         setattr(self, name, val)

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)
    
    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for field in cls._fields:
            code += f'  self.{field} = {field}\n'
        print(code)
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']
    
    def __setattr__(self, name:str, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(getattr(self, field)) for field in self._fields)})"


