# Programa para calcular a média de 4 números fornecidos pelo usuário

# 1. Solicitar os 4 números do usuário (um por vez)
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")
num4 = input("Digite o quarto número: ")

# 2. Converter as strings recebidas para float (números com decimais)
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

# 3. Calcular a média aritmética (soma dividida por 4)
media = (num1 + num2 + num3 + num4) / 4

# 4. Exibir o resultado formatado com duas casas decimais
print(f"A média dos números é: {media:.2f}")
