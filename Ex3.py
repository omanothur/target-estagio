import json

def faturamento_calculo(dados):
    total_faturamento = sum(dado['valor'] for dado in dados)
    numero_dias = len(dados)

    media_mes = total_faturamento / numero_dias
    menor_valor = min(dado['valor'] for dado in dados)
    maior_valor = max(dado['valor'] for dado in dados)
    dia_superior_media = sum(1 for dado in dados if dado['valor'] > media_mes)
    
    return menor_valor, maior_valor, dia_superior_media

def main():
    with open("target-estagio/dados.json", 'r') as target_json:
        dados = json.load(target_json)

    menor_valor, maior_valor, dia_superior_media = faturamento_calculo(dados)

    print(f'Menor valor de faturamento no dia: R${menor_valor:.2f}')
    print(f'Maior valor de faturamento no dia: R${maior_valor:.2f}')
    print(f'Número de dias em que o faturamento diário foi superior a média: {dia_superior_media}')

main()

    