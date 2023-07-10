basedados = []

with open("iris.data", "r") as arquivo: #este iris.data é um arquivo que eu vou baixar e colocar aqui no pycharm, nesta linha do codigo estou falando que vou abrir o arquivo em questão e ler ele
    for registro in arquivo.readline(): #neste for estou falando que vai pegar esse arquivo e ler linha a linha
        basedados.append(registro.split(",")) #nesta linha estou informando que vai me trazer a informação pegando o separador comum do arquivo iris.data, que é o ,

print(basedados)

#A partir deste momento vamos manipular o arquivo so para efeito de aprendizado, mas vamos somar alguma string deste arquivo:
#O resultado até aqui, rodando o comando sairia desta forma: [['5.1', '3.5', '1.4' '0.2' ...etc

print(float(basedados[0][0]) + float(basedados[0][1]))

# ao rodar este print acima ele somou com base neste aquivo: [['5.1', '3.5', '1.4' '0.2' ...etc
# retornou esse resultado: 8.6 que é a soma dos 2 primeiros 5.1 e 3.5

#Quando voce vai trabaçlhar com essas bases de dados para trabalhar o conhecimento, primeiro voce precisa entender a estrutura do texto dentro do arquivo e o separador em comum das informações, alem das linhas, porque cada linha representa um registro na base de dados
