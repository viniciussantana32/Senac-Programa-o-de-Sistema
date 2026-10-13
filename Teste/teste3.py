def calcular_desconto(preco, pct=0.1):
    #calcula o valor com desconto
    valor_desconto = preco * pct
    preco_final = preco - valor_desconto
    return preco_final
preco_produto = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto (em decimal, ex: 0.1 para 10%): "))
preco_com_desconto = calcular_desconto(preco_produto, desconto/100)
print(f"Preço com desconto: R${preco_com_desconto:.2f}")
