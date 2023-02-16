
from itertools import combinations
  
from functools import reduce

# Driver Function
if __name__ == "__main__":
    #palindrome = [i for i in list(combinations([i for i in range(0, 9)], 3)) if i == i[::-1]]
    palindrome = []

    for comb in combinations(range(100, 1000), 2):
        mult =  str(reduce(lambda x, y: x*y, list(comb)))
        if mult == mult[::-1]:
            palindrome.append(int(mult))


    print(max(palindrome))


