'''  
    python -m venv nome_do_ambiente
    nome_do_ambiente\Scripts\Activate

'''
import customtkinter as ctk  # O nome da biblioteca é 'customtkinter'

janela = ctk.CTk()  # Linha para criar uma janela vazia
janela.title('janela teste') # janela recebe um nome
janela.geometry('700*400') #janela recebe um tamanho
janela.maxsize(width=900, height=550)
janela.minsize(width=500,height=300)
janela.resizable(width=True, height=True) # janela pode ser flexivel ou nao

#janela.iconify() comandos para esconder as janela
#janela.deiconify() comando para mostrar a janela

"""tabview=ctk.CTkTabview(janela,width=500,corner_radius=20, border_width=1,border_color='red', #atribuiçoes dentro dos botões do tabview
fg_color='teal', segmented_button_fg_color='red', segmented_button_selected_color= 'green')
tabview.pack() #comando para mostra o tabveiw dentro da janela
tabview.add('idade')
tabview.add('nome')
tabview.add('genero')
tabview.tab('idade').grid_columnconfigure(0,weight=1)
tabview.tab('idade').grid_columnconfigure(0,weight=1)
tabview.tab('idade').grid_columnconfigure(0,weight=1)"""

"""btn = ctk.CTkButton(janela, text="ok")  # O botão recebe o comando CTkButton (corrigido) e integra a janela com o texto
btn.pack() #mostra o botao dentro da janela"""

#costumizando o tema da nossa aplicação
janela._set_appearance_mode("light")#comando para trocar o tema da aplicação
janela.mainloop()  # Loop para manter a janela aberta (corrigido)
