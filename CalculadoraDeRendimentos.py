#variaveis
GanPHor= float(input("Quanto você ganha por hora? "))
HorTrab= float(input("Quantas horas você trabalha por mês? "))

#Fórmulas
TotalBruto= float(GanPHor*HorTrab)
ImpRenda=float((TotalBruto*11)/100)
INSS=float((TotalBruto*8)/100)
sindicato=float((TotalBruto*5)/100)
SaLiquído=TotalBruto-(ImpRenda+INSS+sindicato)



#Resultados
print("Seu Salario Bruto: ",TotalBruto,"R$")
print("Total imposto de renda: ",ImpRenda,"R$")
print("O INSS fica com: ", INSS,"R$")
print("VocÊ pagou aos sindicatos: ", sindicato,"R$")
print("Seu salario líquido: ",SaLiquído,"R$")