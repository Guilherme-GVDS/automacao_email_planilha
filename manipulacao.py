
import pandas as pd
import pathlib
import glob
import os


# Definir a Base de Análise

def manipular():

    caminho_base_analise = pathlib.Path('Planilha_Analise/base_analise.xlsx')
    base_analise = pd.read_excel(caminho_base_analise)

    # Definir a Base Diária

    folder = './Planilha_Hoje'
    caminho_base_diaria = glob.glob(os.path.join(folder, '*.xlsx'))
    base_dia = pd.read_excel(caminho_base_diaria[0])

    # Vamos modificar a base_dia para ter as mesmas colunas que a base_analise

    base_dia_final = base_dia.drop(columns=['Nome','CPF','Endereço','Telefone',])

    base_final = pd.concat([base_analise,base_dia_final],ignore_index=True)

    #base_final.to_excel(caminho_base_analise)

    desktop = pathlib.Path.home() / "Desktop" / "Base_Análise.xlsx"

    base_final.to_excel(desktop)
    base_final.to_excel(caminho_base_analise)




