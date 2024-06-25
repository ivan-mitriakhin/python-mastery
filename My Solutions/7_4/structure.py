import sys
import inspect
from validate import Validator, validated

class Structure:
    _fields = ()
    _types = ()
    
    # @staticmethod
    # def _init():
    #     locs = sys._getframe(1).f_locals
    #     self = locs.pop('self')
    #     for name, val in locs.items():
    #         setattr(self, name, val)

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

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
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']

    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)
    
    def __setattr__(self, name:str, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(getattr(self, field)) for field in self._fields)})"
    

def validate_attributes(cls):
    '''
    Class decorator that scans a class definition for Validators
    and builds a _fields variable that captures their definition order.
    '''
    validators = []
    for name, val in cls.__dict__.items():
        if isinstance(val, Validator):
            validators.append(val)

        if callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))

    cls._types = tuple([ getattr(v, 'expected_type', lambda x: x)
                   for v in validators ])
    cls._fields = tuple(val.name for val in validators)

    if cls._fields:
        cls.create_init()

    return cls

def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls

if __name__ == "__main__":
    from validate import String, PositiveInteger, PositiveFloat
    Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())
    s = Stock('GOOG', 100, 490.1)
    print(s.name)
    print(Structure.__bases__)