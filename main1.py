import tkinter
from tkinter import messagebox
import customtkinter
import pyperclip

# Função para atualizar a cor do fundo
def atualizar_cor(event=None):
    vermelho = int(Svermelho.get())
    verde = int(Sverde.get())
    azul = int(SAzul.get())
    
    # Atualiza os labels com os valores atuais dos sliders
    Lvermelho.configure(text=f'Vermelho {vermelho}')
    Lverde.configure(text=f'Verde {verde}')
    LAzul.configure(text=f'Azul {azul}')
    
    # Converte os valores RGB para hexadecimal
    cor_hex = f'#{vermelho:02x}{verde:02x}{azul:02x}'
    
    # Atualiza a cor do fundo do Frame
    Cor.configure(fg_color=cor_hex)
    
    # Atualiza o valor do Entry com o hexadecimal
    EHexa.delete(0, customtkinter.END)
    EHexa.insert(0, cor_hex)

def Limpar():
    EHexa.delete(0, 'end')
    Lvermelho.configure(text='Vermelho 0')
    Lverde.configure(text='Verde 0')
    LAzul.configure(text='Azul 0')
    Svermelho.set(0)
    Sverde.set(0)
    SAzul.set(0)
    Cor.configure(fg_color='black')
    messagebox.showinfo("Valores", "Valores Limpos Com sucesso!")

def copiar():
    cor_hex = EHexa.get()  # Obtém o valor atual do Entry
    pyperclip.copy(cor_hex)  # Copia o valor para a área de transferência
    messagebox.showinfo("Copia", "Valores Copiados Com sucesso!")

def Sair():
    resposta = tkinter.messagebox.askyesno("Confirmação", "Deseja sair da aplicação?")
    if resposta:
        Janela.quit()  # Fecha a aplicação se a resposta for "Sim"

# Definir cores a usar ------------------------------------------------------------------------------
co0 = "#D3D3D3"

Janela = customtkinter.CTk()
Janela.geometry('800x300+100+100')
Janela.resizable(0, 0)
Janela.title('Meu Selector de Cores Versão 1 © Dev Joel 2024 Portugal')
Janela.config(bg=co0)

# Substituindo Canvas por CTkFrame
Cor = customtkinter.CTkFrame(Janela, width=290, height=200, corner_radius=0)
Cor.place(x=10, y=10)
Cor.configure(fg_color='black')

Lvermelho = customtkinter.CTkLabel(Janela, text='Vermelho 0', bg_color=co0, fg_color=co0)
Lvermelho.place(x=315, y=10)
Svermelho = customtkinter.CTkSlider(Janela, width=480, from_=0, to=255, command=atualizar_cor, bg_color=co0, fg_color=co0)
Svermelho.place(x=315, y=45)
Svermelho.set(0)  # Define o valor inicial como 0

Lverde = customtkinter.CTkLabel(Janela, text='Verde 0', bg_color=co0, fg_color=co0)
Lverde.place(x=315, y=75)
Sverde = customtkinter.CTkSlider(Janela, width=480, from_=0, to=255, command=atualizar_cor, bg_color=co0, fg_color=co0)
Sverde.place(x=315, y=105)
Sverde.set(0)  # Define o valor inicial como 0

LAzul = customtkinter.CTkLabel(Janela, text='Azul 0', bg_color=co0, fg_color=co0)
LAzul.place(x=315, y=135)
SAzul = customtkinter.CTkSlider(Janela, width=480, from_=0, to=255, command=atualizar_cor, bg_color=co0, fg_color=co0)
SAzul.place(x=315, y=170)
SAzul.set(0)  # Define o valor inicial como 0

# Corrigindo a sintaxe da fonte
EHexa = customtkinter.CTkEntry(Janela, font=('Arial', 18), width=90, bg_color=co0, fg_color=co0)
EHexa.place(x=10, y=230)

BCopiar = customtkinter.CTkButton(Janela, text='Copiar', width=100, command=copiar, bg_color=co0, fg_color=co0, text_color="#FFFFFF")
BCopiar.place(x=110, y=230)
BLimpar = customtkinter.CTkButton(Janela, text='Limpar', width=100, command=Limpar, bg_color=co0, fg_color=co0, text_color="#FFFFFF")
BLimpar.place(x=220, y=230)
BSair = customtkinter.CTkButton(Janela, text='Sair', width=100, command=Sair, bg_color=co0, fg_color=co0, text_color="#FFFFFF")
BSair.place(x=330, y=230)

# Chama a função para atualizar a cor com os valores iniciais
# Mas não insere nada no EHexa
Cor.configure(fg_color='black')

Janela.mainloop()
