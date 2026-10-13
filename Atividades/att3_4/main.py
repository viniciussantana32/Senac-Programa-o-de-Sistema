from attalunos import Aluno

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

aluno = Aluno(nome, nota1, nota2)
media = aluno.calcular_media()
resultado = aluno.verificar_aprovacao()

print(f"Aluno: {aluno.nome}")
print(f"Média: {media:.1f}")
print(f"Situação: {resultado}")
