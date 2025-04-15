import requests

def converter_moeda(de_moeda, para_moeda, quantia):
    """Converte uma quantia de uma moeda para outra."""
    url = f"https://api.exchangerate-api.com/v4/latest/{de_moeda}"
    response = requests.get(url)
    data = response.json()
    taxa_cambio = data['rates'][para_moeda]
    return quantia * taxa_cambio

if __name__ == "__main__":
    de_moeda = input("Converter de (ex: USD): ").upper()
    para_moeda = input("Converter para (ex: EUR): ").upper()
    quantia = float(input("Quantia: "))

    resultado = converter_moeda(de_moeda, para_moeda, quantia)
    print(f"{quantia} {de_moeda} = {resultado:.2f} {para_moeda}")
