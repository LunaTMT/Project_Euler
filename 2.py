if __name__ == "__main__":
    f = [0, 1]
    even = []
    i = 1
    while f[i] <= 4000000:
        
        if f[i] % 2 == 0:
            even.append(f[i])

        i += 1
        f.append(f[i-1] + f[i-2])
        
    print(sum(even))