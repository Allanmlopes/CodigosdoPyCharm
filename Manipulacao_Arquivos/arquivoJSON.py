import json

with open("db.jason", "r") as arq_jason:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + " | " + str(dados))

#Neste import json, estou importando a biblioteca do JSON.
#no codigo acima, quando aparece a palavra "arq_json", é porque na aula o professor estava importando um arquivo.json que estava instalado no pycharm dele, e este arquivo contia as seguintes informaçoes:

#db.json
# {
# "chaves": ["chaves do 8", "14/04", "recep_01"],
# "Quico": ["Quico das flores", "13/04", "recep_02"],
# "Florinda": ["Dona florinda", "11/04", "recep_03"]
# }

# a partir deste momento o professor quis gravar as informações do resultado da pesquisa e salvar em poutro arquivo, entao ele aparou e reescreveu:

# import json
#
# dicionario = {
# "chaves": ["chaves do 8", "14/04", "recep_01"],
# "Quico": ["Quico das flores", "13/04", "recep_02"],
# "Florinda": ["Dona florinda", "11/04", "recep_03"]
# }
#with open ("db1.json", "w") as json_file:
#   json.dump(dicionario,json_file)

#este codigo acima, eu criei um novo arquivo.json
