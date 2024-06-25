import inspect
from .validate import Validator, validated
from collections import ChainMap

__all__ = ['Structure']

class StructureMeta(type):
    @classmethod
    def __prepare__(metacls, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(metacls, clsname, bases, methods):
        methods = methods.maps[0]
        return super().__new__(metacls, clsname, bases, methods) # type: ignore

class Structure(metaclass=StructureMeta):
    _fields = ()
    _types = ()

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
    
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
        
    def __iter__(self):
        for field in self._fields:
            yield getattr(self, field)
    
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)

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

