def encontrar_extremos(lista):
    menor = min(lista)
    maior = max(lista)
    return menor, maior

lista = [(1,5),(2,4),(3,3),(4,2),(5,1)]
menor, maior = encontrar_extremos(lista)
print(f"Menor: {menor}")
print(f"Maior: {maior}")