estados_faturamentos = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(estados_faturamentos.values())
percentual = {estado: (valor / faturamento_total) * 100 for estado, valor in estados_faturamentos.items()}

print(f'Faturamento total: R${faturamento_total:.2f}')
for estado, percentual in percentual.items():
    print(f'{estado}: {percentual:.2f}%')