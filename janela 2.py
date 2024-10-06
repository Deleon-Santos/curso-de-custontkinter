'''  
    python -m venv nome_do_ambiente
    nome_do_ambiente\Scripts\Activate

'''
import customtkinter as ctk  # O nome da biblioteca é 'customtkinter'

janela = ctk.CTk()  # Linha para criar uma janela vazia
janela.title('janela numero 2') # janela recebe um nome
janela.geometry('700*400') #janela recebe um tamanho
janela.maxsize(width=900, height=550)
janela.minsize(width=500,height=300)
janela.resizable(width=True, height=True) # janela pode ser flexivel ou nao

btn = ctk.CTkButton(janela, text="ok")  # O botão recebe o comando CTkButton (corrigido) e integra a janela com o texto
btn.pack()

#costumizando o tema da nossa aplicação
janela._set_appearance_mode("light")#comando para trocar o tema da aplicação

def nova_tela():
    
janela.mainloop()  # Loop para manter a janela aberta (corrigido)



