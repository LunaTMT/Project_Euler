#I have no idea how this algorithm works in depth (mathematically), 
#I used the explanation found here
#(https://rpubs.com/Rob_Mac/284102#:~:text=Now%20let's%20find%20the%20answer,to%20be%20more%20than%20500.&text=And%20the%20number%2C%2076%2C576%2C500%20(the,with%20more%20than%20500%20divisors.) 
# as a guide for the psuedo code

import primefac
from functools import reduce

def generate_triangle_number():
    num = 1
    while True:
        yield sum([i for i in range(num)])
        num += 1


if __name__ == "__main__":
    for TN in generate_triangle_number():

        prime_factors = [i+1 for i in list(primefac.primefac(TN))]
        count = [prime_factors.count(i) + 1 for i in set(prime_factors)]
        num_divisors =  reduce(lambda x, y: x * y, count) if count else 0

        if num_divisors > 500:
            print(TN)
            break
