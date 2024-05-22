#!/usr/bin/env python3


def print_fibonacci(length):
    zer = 0
    one = 1
    fibonacci_list = []

    if length == 0:
        print(fibonacci_list)
    elif length == 1:
        fibonacci_list.append(zer)
        print(fibonacci_list)
    elif length == 2:
        fibonacci_list.append(zer)
        fibonacci_list.append(one)
        print(fibonacci_list)
    else:
        fibonacci_list.append(zer)
        fibonacci_list.append(one)

        for i in range(2, length):
            nv = zer + one
            fibonacci_list.append(nv)
            zer = one
            one = nv

        print(fibonacci_list)

print_fibonacci(10)
            
    
    
