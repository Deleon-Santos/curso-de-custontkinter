import customtkinter as ctk  # O nome da biblioteca é 'customtkinter'


janela = ctk.CTk()  # Linha para criar uma janela vazia
janela.title('janela teste') # janela recebe um nome
janela.geometry('700*400') #janela recebe um tamanho
janela.maxsize(width=900, height=550)
janela.minsize(width=500,height=300)
janela.resizable(width=True, height=True) # janela pode ser flexivel ou nao


janela.mainloop()  # Loop para manter a janela aberta (corrigido)