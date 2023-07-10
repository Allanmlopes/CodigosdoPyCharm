import telebot

bot = telebot.TeleBot('6201575464:AAFIop4zaHg0u2nphiuy4tL6NSjlO94kWn4')
bot.delete_webhook()
updates = bot.get_updates()

CHAVE_API = "6201575464:AAFIop4zaHg0u2nphiuy4tL6NSjlO94kWn4"
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Calabresa"])
def Calabresa(mensagem):
        bot.send_message(mensagem.chat.id, """
        Composição da Pizza Calabresa: 
        Massa ultra fina com MUITO recheio, Calabresa, Cebola, Azeitona Verde, Bacon e Oregano.
        Deseja retirar alguma desses componentes?""")

        @bot.message_handler(func=lambda mensagem: mensagem.text == "Cebola")
        def cebola_retirada(mensagem):
        bot.send_message(mensagem.chat.id, "Cebola retirada!")


#      componentes = mensagem.text.upper()
 #      if mensagem=="Cebola":
 #      bot.send_message(mensagem.chat.id, "CEBOLA RETIRADA!")
 #      else:
#       bot.send_message(mensagem.chat.id, "Fresco!!!")

@bot.message_handler(commands=["QuatroQueijos"])
def QuatroQueijos(mensagem):
    pass

@bot.message_handler(commands=["Hamburguesa"])
def HAMBURGUER(mensagem):
    pass


@bot.message_handler(commands=["PIZZA"])
def PIZZA(mensagem):
    texto = """
    Vamos ao sabores : (Clique nas Opções:)
    /Calabresa
    /QuatroQueijos
    /Hamburguesa"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["HAMBURGUER"])
def HAMBURGUER(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a Hamburguer para a sua cara: Tempo de espera em 20 min")

@bot.message_handler(commands=["Salada"])
def Salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não tem Salada XD, Clique aqui para /iniciar")


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que voce quer: (CLIQUE EM UMA OPÇÃO)
    /PIZZA
    /HAMBURGUER
    /Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.reply_to(mensagem, "Para enviar uma reclamação, mande um e-mail para o nosso SAC: sac@telium.com.br")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Valeu, Lê mandou abraço de volta \o/ ")
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraco pro Le
    Responder qualquer outra coisa nao vai funcionar, clique em uma das opcões"""
    bot.reply_to(mensagem, texto)

bot.polling()

