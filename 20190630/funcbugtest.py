#!/usr/bin/env python3
# coding=utf-8

#!/usr/bin/env python3

result = 0
start = 1
end = 100

def compute():
    global result
    global start
    global end
    while start < end:
        result += start
        start += 1
    print(result)

if __name__ == '__main__':
    compute()


