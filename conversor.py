import requests

# Dicionário com as moedas que vamos utilizar
MOEDAS_DISPONIVEIS = {
    "BRL": "Real Brasileiro",
    "USD": "Dólar Americano",
    "EUR": "Euro",
    "ARS": "Peso Argentino",
    "CLP": "Peso Chileno",
    "UYU": "Peso Uruguaio",
    "GBP": "Libra Esterlina",
    "CAD": "Dólar Canadense"
}

# Função para mostrar as moedas disponíveis
def mostrar_moedas():
    print("\nMoedas disponíveis para conversão:")
    for codigo, nome in MOEDAS_DISPONIVEIS.items():
        print(f"{codigo} - {nome}")

# Função que faz a conversão usando a API "exchangerate.host"
def converter_moeda(base_currency, target_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={amount}"
    
    try:
        # Realizando a requisição para a API
        response = requests.get(url)
        
        # Verifica se a resposta da API foi bem-sucedida
        if response.status_code == 200:
            data = response.json()
            # Verifica se a chave "result" está na resposta, que indica sucesso
            if data.get("result"):
                return data["result"]
            else:
                print("⚠️ Erro ao obter a conversão.")
                return None
        else:
            print("⚠️ Erro ao se comunicar com a API.")
            return None
    except Exception as e:
        print(f"⚠️ Erro ao conectar à API: {e}")
        return None

# Função principal que roda o programa
def main():
    continuar = True
    while continuar:
        mostrar_moedas()

        # Recebe as entradas do usuário
        base = input("\nDigite o código da moeda de ORIGEM (ex: USD): ").upper()
        target = input("Digite o código da moeda de DESTINO (ex: BRL): ").upper()
        amount_str = input("Digite o valor a ser convertido: ")

        # Validações de moedas
        if base not in MOEDAS_DISPONIVEIS or target not in MOEDAS_DISPONIVEIS:
            print("\n⚠️ Moeda inválida! Use apenas os códigos listados.")
            continue

        # Validação de valor numérico
        try:
            amount = float(amount_str)
        except ValueError:
            print("\n⚠️ Valor inválido! Digite um número.")
            continue

        # Chama a função de conversão e mostra o resultado
        resultado = converter_moeda(base, target, amount)
        if resultado is not None:
            print(f"\n💱 {amount} {base} = {round(resultado, 2)} {target}\n")

        # Pergunta se o usuário deseja fazer outra conversão
        resposta = input("Deseja fazer outra conversão? (s/n): ").strip().lower()
        if resposta != "s":
            continuar = False
            print("\n✅ Encerrando o programa. Obrigado por usar o conversor!")

if __name__ == "__main__":
    main()
