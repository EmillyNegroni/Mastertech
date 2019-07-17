salario = float(input("Informe sua renda: "))
valor_emprestimo = float(input("Informe o valor desejado para o emprestimo: "))

if ((salario <= 1000) and ((valor_emprestimo > (salario * 15)) or (valor_emprestimo < 2000))):
    print("Emprestimo negado!")
else:
    print("Emprestimo liberado!")





