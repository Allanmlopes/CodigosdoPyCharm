from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")

ftp.login(usuario,senha)

print("Diretorio atual de trabalho: ", ftp.pwd())

ftp.cwd('pub')

print("Diretorio Corrente: ", ftp.pwd())

print(ftp.retrlines('List'))

ftp.quit()

