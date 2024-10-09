import customtkinter as ctk  # O nome da biblioteca é 'customtkinter'


janela = ctk.CTk()  # Linha para criar uma janela vazia
janela.title('janela teste') # janela recebe um nome
janela.geometry('700*400') #janela recebe um tamanho
janela.maxsize(width=900, height=550)
janela.minsize(width=500,height=300)
janela.resizable(width=True, height=True) # janela pode ser flexivel ou nao

textbox= ctk.CTkTextbox(janela,width=400 ,height=200,scrollbar_button_hover_color="white", border_spacing=10, fg_color='teal', border_color='red', border_width=2)
textbox.pack()# criando uma botão no custontkinter
textbox.insert('0.0','texto para teste\n\n'+'este um teste de textbox com scroller de \n 20 linhas.\n\n'*20)

janela.mainloop()  # Loop para manter a janela aberta (corrigido)