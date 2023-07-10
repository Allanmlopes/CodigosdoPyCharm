tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do numero", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " X " + str(valor) + " = " + str((tabuada*valor)))