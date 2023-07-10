from pygeocoder import Geocoder

endereço = '417, Jacinto Martins Garcia, Sao Paulo, SP'
print(Geocoder('JOGAR CHAVE API AQUI').geocode(endereço).coordinates)

#Ao rodar este codigo vai retornar:
#(-23.5740406, -46-6234089)

#este numero acima são a latitude e a longetude

#Lembrando que a chave API do geocoder voce pode pegar no site:
#https://console.cloud.google.com/marketplace/product/google/geocoding-backend.googleapis.com?q=search&referrer=search&hl=pt-br&project=aerobic-bonus-390521
