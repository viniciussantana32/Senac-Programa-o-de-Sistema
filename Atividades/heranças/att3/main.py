from attConta import ContaCorrente, ContaPoupanca

corrente = ContaCorrente()
poupanca = ContaPoupanca()

print("Conta Corrente:")
corrente.exibir_saldo()
print()

print("Conta Poupança:")
poupanca.exibir_saldo()
print()
poupanca.render_juros()