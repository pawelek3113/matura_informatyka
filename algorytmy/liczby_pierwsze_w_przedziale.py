from liczby_pierwsze import is_prime_faster

n = 100

# 0 is not prime
# decide whether i is prime (use previous algorithm)

primes = [x for x in range(2, n+1) if is_prime_faster(x)]
print(primes)
