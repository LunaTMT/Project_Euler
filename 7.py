def get_primes(num):
    prime = [True for i in range(num+1)]

    p = 2
    while (p ** 2 <= num):

        if (prime[p] == True):

            for i in range(p ** 2, num+1, p):
                prime[i] = False
        p += 1
    
    return [p for p in range(2, num+1) if prime[p]]



def get_nth_prime(n):


  size_fac = 2
  s = (n * size_fac)
  primes = []

  while len(primes) < n:
    primes = get_primes(s)
 
    size_fac += 1
    s = (n * size_fac)

  return primes[n-1]

if __name__ == "__main__":
    print(get_nth_prime(10001))