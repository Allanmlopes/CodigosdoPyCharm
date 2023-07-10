texto = "Eu amo python!"
        #012345
print(texto.find("o")) #rodando este codigo ele retornou 5, porque é a primeira ocorrencia da letra o
print(texto.split(" ")) #Estou informando que eu quero que me traga a informação do texto separando pelo espaço
print(texto[texto.find("o")+1:].find("o")) #Nesta linha estou informando que eu quero que ele passe a primeira ocorrencia da letra o e comece a contar a partir dela, e me mostre resultado

