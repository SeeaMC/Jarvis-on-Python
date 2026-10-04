import AppOpener
import time



def abrir():
    AppOpener.open(aplicativo)

def fechar():
    AppOpener.close(aplicativo)

def reiniciar():
    AppOpener.close(aplicativo)
    time.sleep(3)
    AppOpener.open(aplicativo)    

while True:
    mensagem = str(input("Qual aplicativo quer abrir? "))

    if "abrir" in mensagem:
        aplicativo = mensagem.replace('abrir', '')
        abrir()
    elif "fechar" in mensagem:
        aplicativo = mensagem.replace('fechar', '')
        fechar()
    elif "reiniciar" in mensagem:
        aplicativo = mensagem.replace('reiniciar', '')
        reiniciar()