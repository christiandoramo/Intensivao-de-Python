# Automação
# Importar Bases de Dados
# Controlar Mouse e Teclado
#  Enviar Email Automático


import pyautogui
import pyperclip
import time
import pandas

link1 = "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema"

pyautogui.PAUSE = 1  # pausa minima entre os comandos pyautogui


def pausar(tempo):
    time.sleep(tempo)  # atenção o sleep não é somado com o pause do pyautogui


def escreva(texto):
    pyautogui.write(texto)


def clique(posicaoX, posicaoY):
    pyautogui.click(x=posicaoX, y=posicaoY)


def cliqueDireito(posicaoX, posicaoY):
    pyautogui.rightClick(x=posicaoX, y=posicaoY)


def aperte(tecla):
    pyautogui.press(tecla)


def acharPosicaoMouse():
    pausar(7)
    print(pyautogui.position())


def duasTeclas(tecla1, tecla2):
    pyautogui.hotkey(tecla1, tecla2)


def copiar(campo):
    pyperclip.copy(campo)


aperte("win")
escreva("chrome")
aperte("enter")
duasTeclas("win", "up")

escreva(link1)
aperte("enter")
pausar(3)
clique(544, 341)
escreva("meu_login")
clique(539, 419)
escreva("minha_senha")
clique(591, 499)
pausar(3)
cliqueDireito(383, 266)
clique(460, 640)
pausar(5)


tabela = pandas.read_csv(
    r"compras.csv", sep=";", thousands='.', decimal=',')
print(tabela)

total = tabela["ValorFinal"].sum()
qte = tabela["Quantidade"].sum()
media = (total / qte)

print("\n\tINDICADORES: \n")
print("Valor Total: ", total)
print("Quantidade total: ", qte)
print("media por produto: ", media)

duasTeclas("ctrl", "t")
link2 = "https://mail.google.com/mail/u/1/#inbox"
escreva(link2)
aperte("enter")
pausar(5)
clique(83, 168)
pausar(3)
escreva("email_chefe@gmail.com")
aperte("tab")  # para preencher proximo email destinatario
escreva("christiandoramo@gmail.com")
aperte("tab")
aperte("tab")  # para pular o campo do formulario
copiar("Relatorio de Vendas")
duasTeclas("ctrl", "v")
aperte("tab")


texto = f"""
Bom dia! Aqui está o relatório

Valor Total: R${total:,.2f}
Quantidade total: {qte}
Media por produto: R${media:,.2f}

Atenciosamente, chris do python!         
"""

copiar(texto)
duasTeclas("ctrl", "v")

# pyautogui.typewrite(texto, interval=0.02) escrevendo pausadamente

duasTeclas("ctrl", "enter")
