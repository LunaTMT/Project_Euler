

def is_even(n):
    if n%2 != 0:
        return 3*n + 1
    return n/2

chain = []

for n in (range(2, 999999)):
    print(n)
    temp = n
    counter = 0

    while n != 1:
        n = is_even(n)
        counter += 1
    
    chain.append((counter, temp))

print(max(chain))
print()