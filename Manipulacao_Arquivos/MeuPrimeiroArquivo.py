############# Criando um arquivo .txt #######################

#arquivo = open("primeiro_arquivo.txt","w")

#arquivo.write("Meu Primeiro arquivo!")

#arquivo.close()

############ Manipular o arquivo #############################

with open("primeiro_arquivo.txt", "r") as arquivo:
#    arquivo.write("\nhakira matutu")
    for linha in arquivo.readlines():
        print(linha)



