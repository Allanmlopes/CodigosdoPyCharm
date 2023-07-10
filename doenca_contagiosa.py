nome=input("Digite seu nome:")
idade=int(input("Digite sua idade:"))
doenca_contagiosa=input("Você tem suspeita de doença contagiosa? ")
if idade>=65:
    print("O paciente",nome, "Possui prioridade")
elif doenca_contagiosa=="sim":
    print("O paciente" ,nome, "deve ser direcionado para sala de espera reservada")
else:
    print("O paciente",nome,"Não possui atendimento prioritario e pode aguardar na sala comum")
