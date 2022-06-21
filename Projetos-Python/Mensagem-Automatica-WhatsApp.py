import webbrowser
import pyautogui
import time

#***** PROGRAMANDO ENVIO DE MENSAGEM AUTOMÁTICA NO PYTHON ******
'''Abre o WhatsApp'''
webbrowser.open("https://web.whatsapp.com/")   #Abrindo uma página web

'''Recebe dados do contato e mensagem desejada'''
contato = input("Insira o nome do contato: ")
mensagem = input("Insira a mensagem que vai enviar: ")

'''Pesquisa o contato'''
time.sleep(10)                                  #Vai fazer a ação após 7 segundos
#print(pyautogui.position())                    #Vai pegar a posição(coordenadas) que meu mouse foi colocado na página
pyautogui.click(-1792,187)                      #Mandando clicar nas coordenadas que recebi anteriormente
pyautogui.typewrite(contato)                    #Pesquisando pelo nome do contato

'''Clica no contato'''
time.sleep(3)
#print(pyautogui.position())                    #Pegando as coordenadas do contato após ser pesquisado
pyautogui.click(-1731,319)                      #Clicando no contato a partir da coordenada fornecida

'''Escrevendo e enviando a mensagem'''
pyautogui.typewrite(mensagem)                #Mensagem que quero enviar
time.sleep(3)                                #Dando um tempinho para poder escrever a mensagem
#print(pyautogui.position())                 #Pegando a posição do botão de enviar
pyautogui.click(-677,593)                    #Clicando no botão de enviar a partir da coordenada fornecida anteriormente
