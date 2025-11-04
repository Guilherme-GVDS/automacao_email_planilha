import customtkinter as ctk
from imbox import Imbox
from datetime import datetime
import os
from pop_up_error import Login_error
from verif_col import Verif
from pop_up_nfound import Emailnfound
from center import centralizar_janela
import pathlib
from PIL import Image

class LoginApp:
    def __init__(self, janela):
        
        self.janela = janela
        self.interface()

    def interface(self):
        ctk.set_appearance_mode('dark')
        centralizar_janela(self.janela,800,500)        
        self.janela.title ('Login')

        self.images_foldes = pathlib.Path.cwd() /'imagens'

        self.bg = ctk.CTkImage(light_image= Image.open(
                                self.images_foldes/'main_interface.png'),
                               dark_image=Image.open(self.images_foldes/'main_interface.png'),
                               size=(800,500))
        self.bg_label = ctk.CTkLabel (self.janela, text='', image= self.bg)

        self.bg_label.pack()       


        self.email_entry = ctk.CTkEntry(self.janela, width=258,height=30,
                                                bg_color= '#27262C',fg_color='#27262C',
                                                placeholder_text='Email', border_color='#27262C',
                                                text_color='#ffffff')
        self.email_entry.place (x = 270, y=189)


        self.password_entry = ctk.CTkEntry(self.janela, width=258,height=30, 
                                                        fg_color='#27262C',
                                                bg_color= '#27262C', placeholder_text='Senha',
                                                border_color='#27262C', text_color='#ffffff',
                                                show= '*')
        self.password_entry.place (x = 270, y=226)


        self.key_word_entry = ctk.CTkEntry(self.janela, width=258,height=30,
                                                bg_color= '#27262C',fg_color='#27262C',
                                                placeholder_text='Assunto', border_color='#27262C',
                                                text_color='#ffffff')
        self.key_word_entry.place(x=270, y=264)
        self.botao_enviar()


    
    def botao_enviar(self):


        botao_login = ctk.CTkButton (self.janela, text=('Login'), width=250, height=30, 
                                     command=self.run, bg_color='#4044ED', fg_color= '#4044ED',
                                     hover_color='#4044ED')

        botao_login.place(x=275, y=320)
 

    def conection_test (self):
        email = self.email_entry.get().strip()
        senha = self.password_entry.get().strip()
        imap_server = 'imap.gmail.com'
            
        
        try:
            mail = Imbox(imap_server, username=email, password=senha, ssl=True)
            mail.logout()
            return True

        except Exception:
            return False


    def pop_error(self):
        error_pop = ctk.CTkToplevel()
        Login_error(error_pop)   

    def verif_colunas(self):
        colunas_verif = ctk.CTkToplevel()
        Verif(colunas_verif)       
        
    def nfound(self,assunto):
        nfound = ctk.CTkToplevel()
        Emailnfound(nfound,assunto)        



    def run (self):

        if self.conection_test():
            self.logar()    
        else:
            self.pop_error()

    def logar(self):
        find = False
        email = self.email_entry.get().strip()
        senha = self.password_entry.get().strip()
        imap_server = 'imap.gmail.com'

        key_word_filter = self.key_word_entry.get().strip().lower()


        with Imbox(imap_server, username=email, password=senha) as imbox:

            hoje = datetime.now()
            mensagens = imbox.messages(date__on=hoje)
            pasta_hoje = 'Planilha_Hoje'

            os.makedirs(pasta_hoje, exist_ok=True)

            for uid, mensagem in mensagens:
                assunto = mensagem.subject or ''
                if key_word_filter in assunto.lower():

                    find = True

                    for anexo in mensagem.attachments:
                        file_name = anexo.get('filename')
                        content = anexo.get('content').read()
                        if file_name.lower().endswith((".xlsx", ".xls", ".csv")):
                            folder = os.path.join(pasta_hoje, file_name)
                            with open(folder, 'wb') as f:
                                f.write(content)
                    
        if find:
            self.janela.withdraw()      
            self.verif_colunas()
        else:
            pass

            self.nfound(key_word_filter)
        
        


