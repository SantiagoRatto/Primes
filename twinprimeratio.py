from math import prod
import math

def criba_eratostenes(limite):                                      # Generates primes up to "limite" if i don't have an external prime list
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
limite_primos = 147995473                                               # Limit for the prime calculation

# primos = criba_eratostenes(limite_primos)                         # Calls for function but I have a list with the primes so it's faster

with open("Primes/PrimesListupto_982451653.txt", "r") as f:         # Fetches a prime list from a file if theres any
    for linea in f:
        numero_primo = int(linea.strip())  
        if numero_primo > limite_primos:   
            break
        primos.append(numero_primo)   


primos = [p for p in primos if p >= 3]                              # Takes away primes less than 3 (we start with the sieve with number 3)


def calcular_primos_gemelos(N_pares_impares, primos):               # Function to get the approximate number of twin primes after the sieve.
                                                                    # The first sieve discards 1/2 of the total because those would be all uneven pairs, ie. all potential twin primes that you could have to start with
    fraccion_restante = 1/2
                                                                    # We apply the sequential sieve (p-2)/p knowing that for each prime that appears in the secuence, 2 potential twin primes are discarded as posible for each cycle of said prime in the remaining pairs
    fracciones = [(1 - 2/p) for p in primos]                        # and we store all those fractions on an array
    
    
    producto = prod(fracciones)                                     # We get the product of all the fractions completing the sequence in a single operation
    
    
    N_gemelos_restantes = N_pares_impares * fraccion_restante * producto    # We get the product of the sequence with the original range to get the approximate value of how many twin primes are in the range

    
    return (f"{N_gemelos_restantes} with ratio {fraccion_restante * producto}")  # It returns the number of twin primes and their ratio with the range we are considering

N_Range = 10**8                                                     # We declare the size of the range


N_gemelos_restantes = calcular_primos_gemelos(N_Range, primos)      # We call the function to calculate the twin primes

print(N_gemelos_restantes)