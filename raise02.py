def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
    else:
        print("Pode acessar o conteúdo restrito.")

try:
    verificar_idade(18)
except ValueError as erro:
    print(erro)