from inspect import signature
from functools import wraps
import decimal

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = dict(func.__annotations__)
        return_check = annotations.pop('return', None)
        bound = signature(func).bind(*args, **kwargs)
        errors = []

        for name, annot in annotations.items():
            try:
                annot.check(bound.arguments[name])
            except Exception as e:
                errors.append(f'    {name}: {e}')
        
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        result = func(*args, **kwargs)

        if return_check:
            try:
                return_check.check(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result
    return wrapper

def enforce(**annotations):
    return_check = annotations.pop('return_', None)
    def decorator(func):
        def wrapper(*args, **kwargs):
            bound = signature(func).bind(*args, **kwargs)
            errors = []

            for name, val in annotations.items():
                try:
                    val.check(bound.arguments[name])
                except Exception as e:
                    errors.append(f'    {name}:{e}')

            if errors:
                raise TypeError('Bad Arguments\n' + '\n'.join(errors))
            
            result = func(*args, **kwargs)
            
            if return_check:
                try:
                    return_check.check(result)
                except Exception as e:
                    raise TypeError(f'Bad return: {e}') from None
                
            return result
        return wrapper
    return decorator


class Validator:
    def __init__(self, name=None):
        self.name = name
    @classmethod
    def check(cls, value):
        return value
    def __set__(self, instance,	value):
        instance.__dict__[self.name] = self.check(value)
    def __set_name__(self, cls, name):
        self.name = name
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
    
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)
    
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('Complex', complex),
    ('Decimal', decimal.Decimal),
    ('List', list),
    ('Bool', bool),
    ('String', str) ]

globals().update((name, type(name, (Typed,), {'expected_type':ty}))
                 for name, ty in _typed_classes)

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
    
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass