def contar_primos(limite):
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    for p in range(2, limite + 1):
        if es_primo[p]:
            for multiple in range(p*p, limite + 1, p):
                es_primo[multiple] = False
    return sum(es_primo)


limite = 16691*16699
cantidad_primos = contar_primos(limite)
print(f"Cantidad de primos hasta {limite}: {cantidad_primos}")