import math

# Define the Hardy-Littlewood constant (approximate value)
C2 = 0.6601618


# Function to calculate the expected number of twin primes up to a given number N
def hardy_littlewood_twin_primes(N):
    # The formula for the number of twin primes up to N:
    # C2 * integral from 2 to N of 1 / (log(x)^2) dx
    # Approximation using N / (log(N)^2)
    outcome = int(C2 * N / (math.log(N)**2))
    return outcome

# Ranges from 10^2 to 10^16
ranges = [10**i for i in range(2, 17)]
results = [(hardy_littlewood_twin_primes(N)) for N in ranges]

print(results)