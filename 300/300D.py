def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n + 1) if primes[i]]


def count_prime_combinations(n):
    primes = sieve_of_eratosthenes(n)
    count = 0
    for i in range(len(primes)):
        a = primes[i]
        for j in range(i + 1, len(primes)):
            b = primes[j]
            for k in range(j + 1, len(primes)):
                c = primes[k]
                if a ** 2 * b * c ** 2 > n:
                    break
                count += 1
    return count


N = int(input())
result = count_prime_combinations(N)
print(result)
