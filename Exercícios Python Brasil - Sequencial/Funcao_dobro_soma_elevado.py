
def dobro(inteiro1,inteiro2):
    num1= int(inteiro1)
    num2= int(inteiro2)
    if num1 > 0 and num2 > 0:
        dobro = ((num1*num1)**2)*(num2/2)
    return dobro

def soma(inteiro1,real):
    num1= float(inteiro1)
    num3= float(real)
    if num1 > 0 and num3 > 0:
        soma= (inteiro1**3)+real
    return soma

def elevado(real):
    num3= float(real)
    if num3 > 0:
        elevado = real**3
    return elevado