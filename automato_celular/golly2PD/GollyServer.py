# encoding:utf-8
#copyleft Vilson Vieira

import sys, time, os
import threading
import OSC as osc

# endereço e porta do servidor OSC (esse código)
END_SERV = '127.0.0.1'
PORTA_SERV = 9000

def trata(addr, tags, dados, origem):
    m = "%s [%s] %s" % (addr, tags, str(dados))
    #t="%s enviou: %s\n" % (osc.getUrlStr(origem), m)
    t=str((osc.getUrlStr(origem), m))
    print t
    with open("log-golly.txt", "a") as f:
        f.write(t)

s = osc.OSCServer((END_SERV, PORTA_SERV))
s.addDefaultHandlers()
s.addMsgHandler("/golly", trata)

st = threading.Thread(target=s.serve_forever)
st.start()
print "Servidor OSC inicializado. Use ctrl-C para sair."

# loop principal
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

s.close()
st.join()
