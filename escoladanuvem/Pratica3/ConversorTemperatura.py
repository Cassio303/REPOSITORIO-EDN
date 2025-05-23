"""4- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

def celsius_pra_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_pra_kelvin(c):
    return c + 273.15

def fahrenheit_pra_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_pra_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_pra_celsius(k):
    return k - 273.15

def kelvin_pra_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

if origem == destino:
    resultado = temperatura
elif origem == "C" and destino == "F":
    resultado = celsius_pra_fahrenheit(temperatura)
elif origem == "C" and destino == "K":
    resultado = celsius_pra_kelvin(temperatura)
elif origem == "F" and destino == "C":
    resultado = fahrenheit_pra_celsius(temperatura)
elif origem == "F" and destino == "K":
    resultado = fahrenheit_pra_kelvin(temperatura)
elif origem == "K" and destino == "C":
    resultado = kelvin_pra_celsius(temperatura)
elif origem == "K" and destino == "F":
    resultado = kelvin_pra_fahrenheit(temperatura)
else:
    resultado = None

if resultado is not None:
    print(f"{temperatura:.2f}°{origem} equivale a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida. Use C, F ou K.")
