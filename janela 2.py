'''  
    python -m venv nome_do_ambiente
    nome_do_ambiente\Scripts\Activate

'''
import customtkinter as ctk  # O nome da biblioteca é 'customtkinter'

janela = ctk.CTk()  # Linha para criar uma janela vazia
janela.title('janela numero 2') # janela recebe um nome
janela.geometry('660*400') #janela recebe um tamanho
janela.maxsize(width=660, height=550)
janela.minsize(width=500,height=300)
janela.resizable(width=True, height=True) # janela pode ser flexivel ou nao

#crindo um frame no custonTkinter
frame1 = ctk.CTkFrame(master=janela,width=200,height=330, fg_color=('white'), bg_color='blue' ,corner_radius=10).place(x=10, y=60) # estou definindo a posição e tamanho do frame
frame2 = ctk.CTkFrame(janela, width=200 , height=330, fg_color='teal' ).place(x=230, y=60)
frame2 = ctk.CTkFrame(janela, width=200 , height=330,fg_color='red' ).place(x=450, y=60) 

btn = ctk.CTkButton(janela, text="ok")  # O botão recebe o comando CTkButton (corrigido) e integra a janela com o texto
btn.pack()# criando uma botão no custontkinter

#costumizando o tema da nossa aplicação
janela._set_appearance_mode("light")#comando para trocar o tema da aplicação

def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color='light')# a nova janela vais receber o toplevel da antiga janela
    nova_janela.geometry('700x400')
btn.nova_tela = ctk.CTkButton(master=janela, text='Nova Janela',command=nova_tela).place(x=40, y=90)#aqui foi crido uma botão para invocarmos uma nova janela
    
janela.mainloop()  # Loop para manter a janela aberta (corrigido)



