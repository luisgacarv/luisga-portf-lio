def calcular_media(lista):
    """Função que calcula a média de uma lista de números."""
    return sum(lista) / len(lista)

if __name__ == "__main__":
    numeros = [10, 20, 30, 40, 50]
    media = calcular_media(numeros)
    print(f"A média é: {media}")
