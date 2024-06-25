import os
import time

def follow(filename):
    try:
        with open(filename) as f:
            f.seek(0, os.SEEK_END)

            while True:
                line = f.readline()
                if line == '':
                    time.sleep(0.1)
                    continue
                yield line
    except GeneratorExit:
        print('Following done')

if __name__ == '__main__':
    f = follow('Data/stocklog.csv')
    for line in f:
        print(line,end='')
        if 'IBM' in line:
            break
    print('#' * 25)
    for line in f:
        print(line,end='')
        if 'IBM' in line:
            break
