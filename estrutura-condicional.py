conta_normal= True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
        
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial')
    else:
        print('Saldo insuficiente')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    else:
        print('Saldo insuficiente')
        
## Exemplo 2
## if ternário

status = 'Sucesso' if saldo >= saque else 'Saldo insuficiente'

print (f"{status} ao realizar o saque")