import customtkinter as ctk
from imbox import Imbox
from datetime import datetime
import os
from pop_up_error import Login_error
from manipulacao import manipular
from pop_up_nfound import Emailnfound
from center import centralizar_janela


class LoginApp:
    def __init__(self, janela):
        
        self.janela = janela
        self.interface()

    def interface(self):
        ctk.set_appearance_mode('dark')
        centralizar_janela(self.janela,440,230)        
        self.janela.title ('Login')

        self.email_label = ctk.CTkLabel(self.janela, text='Email:', font=('', 20))
        self.email_label.place (x=20, y=20)

        self.email_entry = ctk.CTkEntry(self.janela, width=200, height=20)
        self.email_entry.place (x=20, y=50)

        self.password_label = ctk.CTkLabel(self.janela, text='Senha:', font=('', 20))
        self.password_label.place (x=20, y=100)

        self.password_entry = ctk.CTkEntry(self.janela, width=200, height=20, show='*')
        self.password_entry.place (x=20, y=130)

        self.key_word = ctk.CTkLabel(self.janela,text=('Assunto:'),
                                        width=60,height=20, font= ('', 20))
        self.key_word.place(x=270, y=20)

        self.key_word_entry = ctk.CTkEntry(self.janela, width=150, height=20)
        self.key_word_entry.place(x=270, y=50)
        self.botao_enviar()

        self.gmail_hotmail_menu = ctk.CTkOptionMenu (self.janela, values=['Hotmail','Gmail'],
                                                     width=100, height=20, font=('', 20),
                                                     fg_color= '#343638',
                                                     button_hover_color= '#343638',
                                                     button_color= '#343638')
        self.gmail_hotmail_menu.place(x=270, y=130)

    
    def botao_enviar(self):


        botao_login = ctk.CTkButton (self.janela, text=('Login'), width=40, height=30, 
                                     command=self.run)

        botao_login.place(x=100, y=170)
 

    def conection_test (self):
        email = self.email_entry.get().strip()
        senha = self.password_entry.get().strip()
        if self.gmail_hotmail_menu.get().strip() == 'Gmail':
            imap_server = 'imap.gmail.com'
        else:
            imap_server = 'outlook.office365.com'
            
        
        try:
            mail = Imbox(imap_server, username=email, password=senha, ssl=True)
            mail.logout()
            return True

        except Exception:
            return False


    def pop_error(self):
        error_pop = ctk.CTkToplevel()
        Login_error(error_pop)   

        
    def nfound(self,assunto):
        nfound = ctk.CTkToplevel()
        Emailnfound(nfound,assunto)        



    def run (self):

        if self.conection_test():
            self.logar()    
            manipular()
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
            hoje_dmy = datetime.now().strftime("%d-%b-%Y")
            mensagens = imbox.messages(date__on=hoje)
            pasta_hoje = 'Planilha_Hoje'

            os.makedirs(pasta_hoje, exist_ok=True)


            for uid, mensagem in mensagens:
                assunto = mensagem.subject or ''
                remetente = mensagem.sent_from[0]['email']
                data = mensagem.date
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
            self.janela.destroy()

        else:
            pass

            self.nfound(key_word_filter)
        


