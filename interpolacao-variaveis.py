PI = 3.14159

print(f"Valor de PI: {PI: .2f}") # utiliza-se : .2f para formatar o número com duas casas decimais
# Saída: Valor de PI:  3.14

print(f"Valor de PI: {PI: .4f}") # utiliza-se : .4f para formatar o número com quatro casas decimais
# Saída: Valor de PI:  3.1416


profissao = "programador"
linguagem = "Python"
nome = "Jeferson"
idade = 31

print(f"Eu sou {profissao} e programo em {linguagem}.")

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0} Nome: {1} {1}".format(nome, idade))