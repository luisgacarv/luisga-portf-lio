def saudacao(nome):
    """Função que retorna uma saudação."""
    return f"Olá, {nome}!"

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))
