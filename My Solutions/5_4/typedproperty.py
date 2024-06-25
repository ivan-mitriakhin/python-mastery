def typedproperty(expected_type, name):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)
    
    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value

String = lambda name: typedproperty(str, name)
Integer = lambda name: typedproperty(int, name)
Float = lambda name: typedproperty(float, name)

if __name__ == "__main__":
    
    class Stock:
        name = String('name')
        shares = Integer('shares')
        price = Float('price')
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
    print(Stock.__dict__)