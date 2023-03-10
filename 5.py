#Certainly not my code, to come back to because I don't fully understand it
# https://stackoverflow.com/a/22712191

from itertools import count, takewhile

def primes(n):
    "Generate prime numbers up to n"
    seen = list()
    for i in range(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            yield i

def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
        # we could just take last instead of max()
        result *= bprime
    return result

print(smallest(20))
