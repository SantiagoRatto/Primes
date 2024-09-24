def criba_eratostenes(limite):
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    for p in range(2, int(limite**0.5) + 1):
        if es_primo[p]:
            for multiple in range(p*p, limite + 1, p):
                es_primo[multiple] = False
    return [p for p in range(2, limite + 1) if es_primo[p]]
rango_final = 16691*16699
primos = []
with open("Primes/PrimesListupto_982451653.txt", "r") as f:
    for linea in f:
        numero_primo = int(linea.strip())  
        if numero_primo > rango_final:   
            break
        primos.append(numero_primo)   

def contar_primos_gemelos(rango_final):
    # Generar todos los primos en el rango
    # primos = [p for p in criba_eratostenes(rango_final) if p >= rango_inicial]

    
    # Contar los pares de primos gemelos
    gemelos = 0
    print("contando")
    for i in range(len(primos) - 1):
        if rango_final < primos[i+1]:
            break
        if primos[i+1] - primos[i] == 2:
            gemelos += 1

    return gemelos

# Ejemplo: Contar primos gemelos en el rango de 1 a 10^6

print(contar_primos_gemelos(rango_final))