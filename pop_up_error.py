import customtkinter as ctk
from center import centralizar_janela

class Login_error:
    def __init__(self, janela):
        self.janela = janela
        self.interface()

    def interface(self):
        ctk.set_appearance_mode('dark')
        centralizar_janela(self.janela,200,100)
        self.janela.title ('Error')

        self.text_error = ctk.CTkLabel(self.janela, width= 70, height= 20,text='Erro na conexão',
                                       font=('', 20))
        self.text_error.pack(pady=35)
        self.janela.grab_set()
        self.janela.focus_force()
        self.janela.lift()

