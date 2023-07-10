import serial
from serial.tools import list_ports

# list as portas do arduino
for port in list_ports.comports():
    print('Dispositivos: {} - porta: {} '.format(port.description, port.device))

conexao = serial.serial('COM3', 115200)
#A porta COM3 é uma porta padrao do sistema operacional windows, ja no linux a porta a ser informada é a /dev/ttyUSB0

conexao = serial("Digite:\n<L> para ligar \n<D> para desligar:").upper()
while acao == "L" or acao == "D":
    if acao == "L":
        conexao.write(b'1')
    else:
        conexao.write(b'0')
        acao = input("Digite:\n<L> para Ligar \n <D> para Desligar: ").upper()
conexao.close()
print("Conexão Encerrada.")


#dentro do Arduino podemos configurar da seguinte forma:

# void setup() {
#     pínMode(10, OUTPUT);
#     Serial.begin(115200);
# }
#
# void loop() {
#     int valorRecebido;
#     if(serial.available()) {
#         valorRecebido == Serial.read();
#         if (valorRecebido == '0') {
#             digitalWrite(10, LOW);
#         } else {
#             digitelWrite(10, HIGH);
#         }
#     }
# }


