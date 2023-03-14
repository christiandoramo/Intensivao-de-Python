import pyautogui
import time

link1 = "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema"
pyautogui.PAUSE = .5  # pausa minima entre os comandos pyautogui


def pausar(tempo):
    time.sleep(tempo)


def escreva(texto):
    pyautogui.write(texto)
    pausar(.5)


def clique(posicaoX, posicaoY):
    pyautogui.click(x=posicaoX, y=posicaoY)
    pausar(.5)


def cliqueDireito(posicaoX, posicaoY):
    pyautogui.rightClick(x=posicaoX, y=posicaoY)


def aperte(tecla):
    pyautogui.press(tecla)
    pausar(.5)


def acharPosicaoMouse():
    pausar(5)
    print(pyautogui.position())


print("iniciou!!!!!!")
aperte("win")
escreva("chrome")
aperte("enter")
escreva(link1)
aperte("enter")
clique(544, 341)
escreva("meu_login")
clique(539, 419)
escreva("minha_senha")
clique(591, 499)
pausar(3)
cliqueDireito(404, 289)
clique(494, 646)
acharPosicaoMouse()
print("!!!!!encerrou")


# pyautogui.hotkey("ctrl", "t")  # abri aba
# pyautogui.pause = 5 print(pyautogui.position()) depois de 5 segundos retorna no console a posicao (x,y) do mouse
# pyautogui.click()
# pyautogui.write()
# pyautogui.press() pressiona igualmente as teclas
# pyautogui.hotkey() pressiona combinação ordenadamente
