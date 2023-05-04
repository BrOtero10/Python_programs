#Encontrar maior Número - Parar quando for digitado um negativo

great_number = 0
number = 0

while number >= 0:
    if number > great_number:
        great_number = number
    number = int(input("Digite um número: "))

print("O maior número é", great_number)
