import os
import time
from functools import wraps

def follow(filename, target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line != '':
                target.send(line)
            else:
                time.sleep(0.1)

def consumer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)
        return f
    return wrapper

@consumer
def printer():
        while True:
            try:
                item = yield
                print(item)
            except Exception as e:
                print(f'ERROR: {e}')


if __name__ == '__main__':
    p = printer()
    p.send('hello')
    p.send(42)
    p.throw(ValueError('It failed'))
    p.send(50)
    p.send('Hello')