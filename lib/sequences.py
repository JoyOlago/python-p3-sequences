#!/usr/bin/env python3



def print_fibonacci(length):
    fibonacci_sequence = [0, 1]    
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    if length == 0:
       print([])
    elif length == 1:
        print([0])
    elif length == 2:
       print(fibonacci_sequence[0:2])
    elif length == 10:
       print(fibonacci_sequence[0:11])
    else:
        print(fibonacci_sequence)

#print_fibonacci(1)