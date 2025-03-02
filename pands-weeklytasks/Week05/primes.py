# primes.py
# checkes if numbers are prime. 
# script encoded by Cathal Redmond, based on Work show in lab by Andrew Beatty. 1 Mar 2025

primes = []
upto = 100000

for candidate in range(2,upto):
    # print (candidate)
    isprime = True
    # ony need to check if number is divisible by primes
    for divisor in primes:
        # if divisible by an int it is not a prime number
        if (candidate % divisor == 0):
            isprime = False
            # so there is no reason to keep checking once we have found a divisor
            break

    if isprime:
        primes.append(candidate)

print (primes)