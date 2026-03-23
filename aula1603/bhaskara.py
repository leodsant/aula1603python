import math

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta >= 0:
    raizDelta = math.sqrt(delta)
    x1 = float((-b) + raizDelta) / (2 * a)
    x2 = float((-b) - raizDelta) / (2 * a)
    print(f"o delta é: {delta}, o x1 é: {x1:.2f} e o x2 é: {x2:.2f}")
else:
    print("seu delta é negativo")