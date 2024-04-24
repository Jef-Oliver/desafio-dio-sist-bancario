def sacar (valor):
    saldo = 1000

    if saldo >= valor:
        print('Saque realizado com sucesso')
    
    print('Saldo insuficiente')
        
sacar(1100)

# Path: repeticao.py

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12 

idade = int(input('Digite sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você é maior de idade, pode tirar CNH')
else:
    print('Você é menor de idade, não pode tirar CNH')
    
if idade >= MAIOR_IDADE:
    print('Você é maior de idade, pode votar')
elif idade == IDADE_ESPECIAL:
    print('Você tem 12 anos, pode votar')
else:
    print("Não pode tirar CNH mas pode votar")