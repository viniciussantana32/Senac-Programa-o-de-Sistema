nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média final é: {media:.2f}")

if nota1 < media:
	print(f"A primeira nota ficou abaixo da média final: {nota1}")

if nota2 < media:
	print(f"A segunda nota ficou abaixo da média final: {nota2}")

if nota3 < media:
	print(f"A terceira nota ficou abaixo da média final: {nota3}")