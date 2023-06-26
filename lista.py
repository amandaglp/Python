numbers = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

#Imprima o maior elemento
print("O maior número é: ")
print(max(numbers))

#Imprima o menor elemento
print("O menor número é: ")
print(min(numbers))

#Imprima os números pares
lista2 = sorted(filter(lambda x: x % 2 == 0, numbers))

print("Os números pares são: " , lista2)

#Imprima o número de ocorrencia do primeiro elemento da lista
repeticoes = numbers.count(13)
print("O primeiro elemento da lista se repete: " , repeticoes , "vezes")

#Imprima a média dos elementos
soma = 0

for number in numbers:
    soma += number

qtd_de_numeros = len(numbers)

media_dos_numeros = soma / qtd_de_numeros
print("A média dos números é" , media_dos_numeros)

#Imprima a soma dos elementos de valor negativo
soma_dos_negativos = sum([i for i in numbers if i < 0])
print("A soma dos negativos é: " , soma_dos_negativos)

print('A soma dos elementos negativos é igual a {}'.format(soma_dos_negativos))