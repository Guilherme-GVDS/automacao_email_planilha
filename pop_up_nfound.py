import customtkinter as ctk
from center import centralizar_janela

class Emailnfound:
    def __init__(self, janela,assunto):
        self.janela = janela
        self.assunto = assunto
        self.interface()

    def interface(self):
        ctk.set_appearance_mode('dark')
        centralizar_janela(self.janela,300,100)
        self.janela.title ('Email não encontrado')

        self.text_error = ctk.CTkLabel(self.janela, width= 150, height= 75,
                                       text=f'Email com assunto \n{self.assunto}\n não encontrado',
                                       font=('', 15))
        self.text_error.pack(pady=15)
        self.janela.grab_set()
        self.janela.focus_force()
        self.janela.lift()

