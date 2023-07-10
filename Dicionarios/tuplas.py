usuario = {}

emails = ["xpto@xyz.com", "xkcd@pgd.com"]

tuple = list(enumerate(emails))

print(tuple)

for chave in range (0,len(tuple)):
    print("Email: ", tuple[chave][1])
    usuario[tuple[chave]]=[input("Digite o nome"), input("Digite o nivel")]

for chave, dado in usuario.items():
    print("Usuario...: ", chave[0])
    print("E-mail....: ", chave[1])
    print("Nome......: ", dado[0])
    print("Nivel.....: ", dado[1])
