equipamento = []
valores = []
seriais = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamento.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamento)):
    print("\nEquipamentos..:", (indice+1))
    print("Nome............:", equipamento[indice])
    print("Valor...........:", valores[indice])
    print("Serial..........:", seriais[indice])
    print("Departamento.....:", departamento[indice])