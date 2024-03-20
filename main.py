'''ex 01:
v = float(input("qual era a velocidade do carro: "))

if v <= 100:

elif v <= 120:
    multa = 0.2*v

elif v <= 150:
    multa = 0.2*120 + 0.3*v

else:
    multa = 0.2*120 + 0.3*150 + 0.4*v
    print(f"o valor da multa é de: R${multa:.2f}")


ex 02:
lados = int(input("diga a qnt de lados: "))
if lados < 3:
    print("não é um poligono")
elif lados > 5:
    print("poligono nao identificado")
else:
    medida = int(input("diga o tamanho de lados: "))
    if lados == 3:
        forma = "triangulo"
    elif lados == 4:
        forma = "quadrado"
    else:
        forma = "pentagono"
    perimetro = lados*medida
    print(f"você escolheu o {forma} com perimetro de {perimetro}")


num = int(input("diga um numero: "))
if num % 2 == 0:
    print("par")
else:
    print("impar")

senha = input("digite sua senha: ")
senha_correta = 'alekao223'
while senha != senha_correta:
    senha = input("digite sua senha: ")

qnt = 1
senha_correta = 'alex223'
senha = input("digite sua senha: ")
while qnt < 3 and senha != senha_correta:
    print("sai daí")
    senha = input("digite sua senha: ")
    qnt = qnt + 1
if senha == senha_correta:
    print("acesso liberado")
else:
    print("acesso negado")

i = 0
soma = 0
while i < 10:
    i += 1
    soma += i
print(soma)

i = 0
pares = 0
while i < 10:
    num = int(input("diga os numeros: "))
    if num%2==0:
        pares += 1
    i+=1
print(f"vc digitou {pares} pares e {i - pares} impares")'''




