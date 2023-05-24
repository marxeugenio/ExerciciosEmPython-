pessoa = {
    "nome": "Marx",
    "idade": 18,
    "casa": "São Paulo"
}

pessoa["idade"] = 31
pessoa["profissão"] = "Programador"
del pessoa["casa"]



print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["profissão"])
