#import primesieve
#primos = primesieve.n_primes(100)
from fractions import Fraction
from math import prod

def criba_eratostenes(limite):                                          # Generates primes up to "limite" if i don't have an external prime list

    primos = []
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    for p in range(2, limite + 1):
        if es_primo[p]:
            primos.append(p)
            for multiple in range(p*p, limite + 1, p):
               es_primo[multiple] = False
    return primos
primos =[]
e = 16
n = e-3
r = 0.23
rd = 7*1123*29383/2**6*5**10
r = r*rd**n
limite_primos = 982451653                                              # Limit for the prime calculation, it can come from the formula or from the specific values in the txt file

# primos = criba_eratostenes(limite_primos)                             # Calls for function but I have a list with the primes so it's faster

with open("Primes/PrimesListupto_982451653.txt", "r") as f:             # Fetches a prime list from a file if theres any
    for linea in f:
        numero_primo = int(linea.strip())  
        if numero_primo > limite_primos:   
            break
        primos.append(numero_primo)   


def calcular_primos_ratio(primos):                                      # Function to get the approximate number of primes after the sieve.

    fracciones = [((p-1)/p) for p in primos]                            # We apply the sequential sieve (p-1)/p knowing that for each prime that appears in the secuence, 1 potential primes are discarded as posible for each cycle of said prime in the remaining numbers
                                                                        # and we store all those fractions on an array

    producto = prod(fracciones)                                         # We get the product of all the fractions completing the sequence in a single operation

    
    return producto                                                     # Returns the prime ratio for that range

N_rango_numeros = 10**18                                                 # We declare the size of the range


N_gemelos_restantes = calcular_primos_ratio(primos)                     # Call the function
N_primos_total = N_rango_numeros * N_gemelos_restantes                  # Get the amount of primes in the range multiplying the range with the found ratio

# Mostrar el resultado
print(f"The ratio of primes in range 1 - {N_rango_numeros} is: {N_gemelos_restantes}, that is {N_primos_total} primes.")    # Prints out the outcome
