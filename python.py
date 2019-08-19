#-----------------Exercicios Python sequencial---------------------------#
#1)Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Olá,mundo!')

#2)Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int( input('Informe um número: '))
print('O número informado foi', numero)

#3)Faça um Programa que peça dois números e imprima a soma.
number1 = int(input('Informe o primeiro número a ser somado: '))
number2 = int(input('Informe o segundo número a ser somado: '))
resultado = number1 + number2
print('O resultado da soma é de: ' , resultado)

#04)Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nome_aluno = input('Olá aluno, informe seu nome:')
print(nome_aluno, 'agora vamos calcular sua média bimestral!')
nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
nota3 = float(input('Informe a terceira nota:'))
nota4 = float(input('Informe a quarta nota:'))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(nome_aluno , 'Sua média é de: ' , media)

#05)Faça um Programa que converta metros para centímetros e de centimetros para metro.
metro = float(input('Informe o valor do metro a ser convertido:'))
conversao = metro * 100
print(metro , ' metro, convertido em centimetros é de: ' , conversao)
centimetro = float(input('Informe o valor do centimetro a ser convertido á metros:'))
converter = centimetro / 100
print(centimetro, 'centimetro convertido em metros é de: ', converter)

#06)Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
pi = 3.14
raio = float(input('Informe o valor do raio do circulo:'))
circulo = pi * (raio * raio)
print('A área do circulo é de: ',circulo)

#07)Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input('Informe o valor do lado do quadrado:'))
area = lado * lado
dobro = area * area
print('O valor da área é de:' , area)
print('O dobro da área é de:' , dobro)

#08)Faça um Programa que pergunte quanto você ganha por hora e o número 
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
nome_funcionario = input('Olá, informe seu nome: ')
print(nome_funcionario , 'você está prestes a saber o valor do seu sálario!')
horas_trabalhadas = float(input('informe a quantidade de horas trabalhadas nesse mês:'))
valor_hora = float(input('Agora, informe o valor hora:'))
salario = horas_trabalhadas * valor_hora
print(nome_funcionario , 'seu sálario este mês será de: ' , salario)

#09)Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).
temperatura_f = float(input('Informe a temperatura em graus Farenheit:'))
C = (5 * (temperatura_f-32) / 9)
print(' A temperatura em graus Farenheit convertida a graus Celsius é de: ' , C)

#10)Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
# nome_funcionario = input('Olá, informe seu nome: ')
# horas_trabalhadas = float(input('informe a quantidade de horas trabalhadas nesse mês:'))
# valor_hora = float(input('Agora, informe o valor hora:'))
# salario_bruto = horas_trabalhadas * valor_hora
# IR = salario_bruto - 0.11
# INSS = IR - 0.08
# sindicato = INSS - 0.05
# salario_liquido = sindicato
# print(salario_liquido)

#------------------------EXERCICIO ESTRUTURA DE DECISÃO----------------------------------------------#
#01)Faça um Programa que peça dois números e imprima o maior deles.
numero01 = int(input('Informe o primeiro número:'))
numero02 = int(input('Informe o segundo número: '))
if numero01 >= numero02:
    print(' Número maior é o:' , numero01)
    
else:
    print('Número maior é o:' , numero02)

#02)Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
nota1 = float(input('Informe sua primeira nota:'))
nota2 = float(input('Informe sua segunda nota:'))
nota3 = float(input('Informe sua terceira nota:'))
nota4 = float(input('Informe sua quarta nota:'))
nota5 = float(input('Informe sua quinta nota:'))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print('Sua média é :' , media)
if (media >= 7):
    print('Parabens voce foi aprovado!')
    # elif (media == 10):
    #     print ('Aprovado com distinção!')
else:
    print ('Reprovado!')

#03) Positivo ou negativo
number1 = float(input(' Informe um  número: '))
if number1 > 0:
    print(number1 ,'Positivo')
else:
    print(number1 , 'Negativo')