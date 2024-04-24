menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Valor a depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            # não pode depositar valor negativo
        else:
            print("Operação falhou!!!")           
     
    elif opcao == "s":
        valor = float(input("Valor a sacar: "))
        
        excedeu_saldo = valor > saldo # verifica se o valor a ser sacado excede o saldo
        excedeu_limite = valor > limite # verifica se o valor a ser sacado excede o limite
        excedeu_saques = valor > limite # verifica se o valor a ser sacado excede o limite de saques
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou, sem saldo suficiente!!!")
        elif excedeu_limite:
            print("Operação falhou, limite de saque excedido!!!")
        elif excedeu_saques:
            print("Operação falhou, limite de saques excedido!!!")  
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            # não pode sacar mais do que o saldo
            # não pode sacar mais do que o limite
            # não pode sacar mais do que 3 vezes
        else:
            print("Operação falhou!!!")
        
    elif opcao == "e":
        print("\n=================== EXTRATO ===================")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")
        
    elif opcao == "q":
        break
    else:
        print("Operação inválida!!!")