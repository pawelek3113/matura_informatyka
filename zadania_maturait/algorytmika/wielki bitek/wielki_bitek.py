n = 10_000
primes = [False, False] + [True] * (n-1)

# sieve of eratosthenes
for i in range(2, n+1):
    if primes[i]:
        k = 2
        while i*k <= n:
            primes[i*k] = False
            k += 1

# all prime numbers

prime_numbers = [idx for idx, val in enumerate(primes) if val]
print(prime_numbers)

result = ";".join(map(str, prime_numbers[:-6:-1]))

print(result)