from attcontabnacaria import ContaBancaria

conta = ContaBancaria("João", 100)
conta.depositar(-10)
print(conta.exibir_saldo())  
conta.depositar(50)
print(conta.exibir_saldo())  
conta.sacar(200)
print(conta.exibir_saldo())  