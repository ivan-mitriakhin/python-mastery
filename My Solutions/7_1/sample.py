from logcall import logged

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x- y

if __name__ == "__main__":
    print(add(3, 4))
    print(sub(2, 3))