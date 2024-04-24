nome = input("Digite seu nome: ")

idade = 30

print("Olá, meu nome é", nome, "e tenho", idade, "anos.", end="...")


limite_saque_diario = 1000

if limite_saque_diario > 0:
    print("Você ainda pode sacar", limite_saque_diario, "reais.")


STATES = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Minas Gerais"} # constantes 


print(STATES["SP"]) # São Paulo


## Operadores aritméticos

print(5 // 2) # Divisão inteira

print(10 - 5 * 2)# Aqui a multiplicação é feita primeiro, depois a subtração. 0

print((10 - 5) * 2) # 10  Aqui a subtração é feita primeiro, depois a multiplicação.

print(10 ** 2 * 2) # 200 Aqui a potenciação é feita primeiro, depois a multiplicação.

print(10 ** (2 * 2)) # 10000 Aqui a multiplicação é feita primeiro, depois a potenciação.

print(10 / 2 * 4) # 20.0 Aqui a divisão é feita primeiro, depois a multiplicação.


## Operadores de comparação

# == Igualdade

saldo = 450
saque = 200

print(saldo == saque) # False
print(saldo != saque) # True
print(saldo > saque) # True
print(saldo < saque) # False
print(saldo >= saque) # True

## Operadores de atribuição

# = Atribuição simples
saldo = 500
print(saldo) # 500

# += Adição
saldo += 100
print(saldo) # 600

# /= Divisão
saldo = 500
saldo /= 5
print(saldo) # 100.0

# //= Divisão inteira
saldo = 500
saldo //= 5
print(saldo) # 100, retorna o mesmo valor que a divisão normal, mas sem as casas decimais.

# **= Potenciação
saldo = 80
saldo **= 2
print(saldo) # 6400

# %= Resto da divisão
saldo = 10
saldo %= 3
print(saldo) # 1

## Operadores lógicos

saldo = 1000
saque = 500
limite = 200

saldo > saque and saldo > limite # True
saldo > saque and saldo < limite # False
limite > saldo or saque > saldo # False
limite >= saldo or saque <= saldo # True
not saldo > saque # False

contatos_emergencia = []

not 1000 > 1500 # True
not contatos_emergencia # True, porque a lista está vazia
not "saque 1500;" # False, porque a string não está vazia
not "" # True, porque a string está vazia

saldo = 1000
saque = 500
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque # True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # True


## Operadores de associação

curso = "Python"
frutas = ["laranja", "limão", "uva"]
saques = {"saque1": 1500, "saque2": 100}

"Python" in curso # True

"maçã" not in frutas # True

200 in saques # False

## Operadores de identidade

saldo = 1000
saque = 500
limite = 200

saldo is saque # False
saldo is not saque # True
