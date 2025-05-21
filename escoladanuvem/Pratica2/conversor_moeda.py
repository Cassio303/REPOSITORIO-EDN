"""Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
- Valor em reais: R$ 100.00
- Taxa do dólar: R$ 5.70
- Taxa do euro: R$ 6.40
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""


valor_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40

converter_em_dolar = valor_reais / taxa_dolar
converter_em_euro = valor_reais / taxa_euro

print(f"O valor original em reais era: R${valor_reais:.2f}")
print(f"O valor em dólares é: ${converter_em_dolar:.2f}")
print(f"O valor em euros é: €{converter_em_euro:.2f}")

