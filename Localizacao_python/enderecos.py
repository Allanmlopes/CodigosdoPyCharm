from pygeocoder import Geocoder

endereco = 'Avenida paulista, 1020 Sao paulo'
resultado = Geocoder("inserir sua chave API do google aqui").geocode(endereco)
print(resultado)

#resultado da saida do codigo:
#"Av, Paulista, 100  - Bela Vista, São Paulo - SP, Brazil"

#Na linha do codigo:
#resultado = Geocoder("inserir sua chave API do google aqui").geocode(endereco)
#se voce colocar .state no final da linha, trará a informação do estado, .postal_code (traz o CEP da Rua), country (retorna Brazil), coordinates (Latitude e longitude)

#se eu já estiver com a coordenada e quizer que o codigo realize a busca do endereço com base na coordenada, precisa mudar o final da linha de codigo 4, da sequinte forma:
#.reverse_geocode(-23.5703022, -46.6451267)


