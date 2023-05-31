#Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []
qtd = 3
for i in range(qtd):
    elemento = int(input('Digite um numero: '))
    lista.append(elemento)

lista.sort(reverse = True) #ordena os elementos
print(lista)

