limit = 100

# assume that every number is prime (besides 0 and 1)
primes = [False, False] + [True] * (limit-1)

for i in range(2, limit):
    if primes[i]:
        k = 2
        while i * k <= limit:
            # mark multiples of i as composite (non-prime)
            primes[i*k] = False
            k += 1

print([idx for idx, is_prime in enumerate(primes) if is_prime])
