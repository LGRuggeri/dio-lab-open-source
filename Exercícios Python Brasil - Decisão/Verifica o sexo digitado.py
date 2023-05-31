"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

qual_o_sexo= (input('Digite F(Feminino) ou M(Masculino):'))

if qual_o_sexo == 'F' or qual_o_sexo == 'f':
    print('Você seleciounou F(Feminino)')
elif qual_o_sexo == 'M' or qual_o_sexo == 'm':
    print('Você selecionou M(Masculino)')
else:
    print('O sexo selecionado errado!!!')
    