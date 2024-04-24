texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper( ) in VOGAIS:
        print(letra, end=" ")
        
print()


## mais um for

for numero in range(100):
    
    if numero % 2 == 0:
        print(numero, end=" ")
        