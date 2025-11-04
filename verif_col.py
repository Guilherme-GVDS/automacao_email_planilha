import customtkinter as ctk
from center import centralizar_janela
import pandas as pd
import glob
import os
from manipulacao import manipular
import sys

class Verif:
    def __init__(self, janela):
        self.janela = janela
        self.count_col()


    def interface(self,col):
        ctk.set_appearance_mode('dark')
        centralizar_janela(self.janela,470,(120+col*40))

        df = self.planilha()

        self.janela.title ('Escolher Colunas')

        self.desc = ctk.CTkLabel(self.janela, width=40, height=15, 
                                 text='Escolha as colunas que serão mantidas', font=('',15))
        self.desc.place(x=20, y=10)

        self.variav= {}
        linha = 40
        for i,coluna in enumerate (df.columns):

            self.check_col_var = ctk.BooleanVar()
            self.check_col = ctk.CTkCheckBox(self.janela, text=coluna, variable= self.check_col_var)
            
            self.check_col.place(x = 20, y = linha)
            self.variav[coluna] = self.check_col_var  

            linha+=45

    def planilha(self):
        folder = './Planilha_Hoje'         
        caminho_base_diaria = glob.glob(os.path.join(folder, '*.xlsx'))
        df = pd.read_excel(caminho_base_diaria[0])
        return df            


    def count_col(self):
        col_num = 0
        df = self.planilha()

        for coluna in df.columns:
            col_num+=1

        self.interface(col_num)
        self.botoes()

    def botoes(self):
        self.botao_esc = ctk.CTkButton(self.janela, width=100, height=15, text= 'Escolher Colunas',
                                       font=('', 15), command=self.choice, bg_color= '#4044ED',
                                       fg_color= '#4044ED', hover_color='#4044ED')
        self.botao_esc.place(x= 310, y=10)

    def choice (self):
        self.lista_colunas = []
        for col,var in self.variav.items():
            if not var.get():
                self.lista_colunas.append(col)
        manipular(self.lista_colunas)     
        self.janela.destroy()       
        sys.exit()            
        

       