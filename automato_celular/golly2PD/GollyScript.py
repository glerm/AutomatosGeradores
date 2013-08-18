# encoding:utf-8
# copyleft Vilson Vieira
# enviando células de um pattern carrega no Golly por OSC

# passos:
# 0. instale o pyosc (sudo easy_install pyosc)
# 1. inicializa o servidor OSC (pode rodar o testosc_serv.py como exemplo)
# 2. move este arquivo para /usr/share/golly/Scripts/Python
# 3. roda o Golly e carrega um pattern, depois File -> Show Scripts
# 4. procura o testosc.py na pasta de Scripts e clica nele, irá rodar

import golly as g
import OSC as osc
from time import sleep

# para quem enviaremos as msgs OSC
END_SERV = '127.0.0.1'
PORTA_SERV = 9000

# criamos um cliente OSC e enviamos a mensagem com as céluas
cliente = osc.OSCClient()
cliente.connect((END_SERV, PORTA_SERV))

# reinicia tudo (pattern, contador de gerações, ...)
g.reset()

i = 0
while True:
    # mostramos no status a geração atual
    g.show("Geração: %s" % (int(g.getgen()) + 1))

    # pegamos todas as células do retângulo atual mostrado na tela
    celulas = g.getcells(g.getrect())

    # criamos uma msg OSC e enviamos usando o cliente OSC
    msg = osc.OSCMessage()
    msg.setAddress("/golly")
    msg.append(celulas)
    cliente.send(msg)
    
    # avança N gerações
    g.run(1)
    # atualiza desenho
    g.update()
    # espera um segundo
    sleep(1)
    i += 1
