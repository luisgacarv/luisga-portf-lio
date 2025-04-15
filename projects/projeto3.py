import secrets
import string

def gerar_senha(tamanho=12):
    """Gera uma senha aleatória segura."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
    senha_gerada = gerar_senha(tamanho_senha)
    print("Senha gerada:", senha_gerada)
