from tkinter import *

# janela 
janela = Tk()
janela.title("My first GUI program")
janela.minsize(width=500,height=500)

#rótulo

rotulo = Label(text="Testando Rótulos")
rotulo.pack()

#botão
x = 0
def botao_clicado():
   x += 1
   str(x)
   rotulo.config(text=x)
   

botao = Button(text="Click-me",command=botao_clicado)
botao.pack() #metodo para mostrar um objeto na tela

#entrada 

entrada = Entry()
entrada.pack()





janela.mainloop()