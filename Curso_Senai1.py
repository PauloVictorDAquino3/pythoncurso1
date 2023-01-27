# pythoncurso1
#apenas exercicios do meu curso

print ("Atividade Paulo e Nathan")
num=float(input("Digite um numero: "))
num_soma= num +1
num_ant= num - 1

print (f"o Sucessor do numero {num} é {num_soma} e o antecessor é {num_ant} ")

print ("======================================================================================================================================================================")
num=float(input("Digite um numero: "))
triplo= num * 3
dobro= num * 2
raiz= num ** 0.5

print (f" O numero informado foi {num} seu dobro é {dobro} seu triplo é {triplo} sua raiz quadrada é {raiz}")
print ("======================================================================================================================================================================")
nota1= float(input("digite a sua primeira nota: "))
nota2= float(input("digite a sua segunda nota: "))
media= nota1 + nota2
media2=media / 2

print (media2)
print ("======================================================================================================================================================================")
metro= float(input("digite o valor em metros: "))
centimetro= metro / 100
milimetro= metro / 1000

print (f"o valor informado em metros foi {metro} em centimetros seria {centimetro} em milimetros {milimetro}")

print ("======================================================================================================================================================================")
num_int= int(input("digite um numero inteiro: "))

for c in range (1, 11):
  print (f"{num_int} * {c} = {num_int * c} ")

print ("======================================================================================================================================================================")

vlr_real= float(input("Digite o valor em real que você quer converter: "))
cnvs_real= vlr_real * 5.19

print (f"O valor em dolar que você quer converter será de: {cnvs_real:.2f} R$")

print ("======================================================================================================================================================================")

cat_adj= float(input("Qual é o comprimento adjacente? "))
cat_opost= float(input("Qual é o comprimento do cateto oposto? "))
hip= (cat_opost ** 2) + (cat_adj **2)
raiz= hip ** 0.5
print (f" O comprimento da hipotenusa é: {hip}")

print ("======================================================================================================================================================================")

import math
a = float(input('Digite o valor do âgulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O seno, cosseno e tangente do ângulo {a} são respectivamente: {s:.2f}, {c:.2f}, {t:.2f}.')

print ("======================================================================================================================================================================")

velocidade = float(input('Digite A sua velocidade '))
multa = (velocidade - 80) * 7
if velocidade > 80:
  print(f'Você foi Multado em R$ {multa:.2f}')
else:
  print('Você não foi multado, a sua velocidade está no limite da via  ')
  
print ("======================================================================================================================================================================")

velocidade = float(input('Digite A sua velocidade '))
multa = (velocidade - 80) * 7
if velocidade > 80:
  print(f'Você foi Multado em R$ {multa:.2f}')
else:
  print('Você não foi multado, a sua velocidade está no limite da via  ')
  
print ("======================================================================================================================================================================")
(input('Digite Um Número para saber se ele é par ou impar '))
if numero %2 == 0:
  print('Esse Número é par ')
else:
  print('Esse número não é par ')

print ("======================================================================================================================================================================")

altura = float(input('Digite sua altura em cm '))
sexo = str(input('Digite seu sexo [M/F] '))
if sexo in 'M,m,masculino, Masculino, MASCULINO':
  print(f'Seu peso ideal é {altura - 58}')
else:
  print(f'Seu peso ideal é {altura - 44.7}')
print ("======================================================================================================================================================================")

quilos = float(input('Ei João Seu Danadinho me Diga Quantos quilos de peixe Você pescou '))
if quilos > 50:
  print(f'Ei João Você pescou mais de 50 quilos e vai ter que pagar uma multa De R$ {(quilos - 50)*7:.2f}')

print ("======================================================================================================================================================================")

ano = int(input('Digite o Ano Para Saber se Ele é bissexto ou não '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'O Ano {ano} é Um Ano Bissexto ')
else:
  print(f'O Ano {ano} Não é Um Ano Bissexto')

print ("======================================================================================================================================================================")

numero1 = int(input('Digite Um Número '))
numero2 = int(input('Digite Um Número '))
numero3 = int(input('Digite Um Número '))
maior = 0
menor = 0

if numero1>numero2 and numero1>numero3:
  maior = numero1
elif numero2>numero1 and numero2>numero3:
  maior = numero2
elif numero3>numero1 and numero3>numero2:
  maior = numero3
if numero2<numero1 and numero2<numero3:
  menor = numero1
elif numero2<numero1 and numero2<numero3:
  menor = numero2
elif numero3<numero1 and numero3<numero2:
  menor = numero3
print(f'O maior Número é {maior} E o Menor Número é {menor}')

print ("======================================================================================================================================================================")

salario = float(input('Digite O Valor do seu salario R$ '))
valor = float(input('Qual o valor do imovel que vossa Pessoa Deseja Comprar R$'))
tempo = int(input('Em quantos Anos Você Quer Pagar O Seu Imovel ? '))
prestação = (valor /tempo) /12
porcentagem = salario * 0.3 
print(f'A Prestação Do Imovel é de R$ {prestação:.2f}')
if prestação > porcentagem:
  print('Emprestimo Negado')
else:
  print('Emprestimo Aprovado')
  
print ("======================================================================================================================================================================")
  
numint1=int(input("Digite o valor do primeiro numero: "))
numint2=int(input("Digite o valor do segundo numero: "))

if numint1 > numint2:
  print ("O Valor do primeiro numero é maior!")
elif numint1 == numint2:
  print ("O valor dos dois são iguais!")
else:
  print ("O valor do segundo numero é maior! ")
  
print ("======================================================================================================================================================================")

from datetime import date

atual= date.today ().year
anoNasc= int(input("DIGITE O SUA DATA DE NASCIMENTO: "))
temp= atual - anoNasc

if  temp < 18:
  print ("Ainda não é a hora de se alistar")
  print (f"ainda faltam {18 - temp}")
elif temp == 18:
  qg=str(input("sua cidade tem qg? s/n  "))
  if qg == "s":
    print ("É hora de se alistar soldado kkkkkk ")
  elif qg== "n":
    print ("Se safou kkkkkkk")
else:
  print ("Já passou da hora de se alistar")
  print (f"você de deveria te rse alistado a {temp - 18 } atrás.")

print ("======================================================================================================================================================================")

nota1= float(input("digite a sua primeira nota: "))
nota2= float(input("digite a sua segunda nota: "))
media= nota1 + nota2
media2=media / 2

if media2 < 6:
  print ("Não está na media.")
elif media2 == 6:
  print ("Você está na media.")
else:
  print ("você está acima da média.")

print ("======================================================================================================================================================================")
