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
        item = yield
        print(item)


if __name__ == '__main__':
    follow('Data/stocklog.csv',printer())