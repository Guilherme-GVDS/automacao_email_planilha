
import pandas as pd
import pathlib
import glob
import os




def manipular(list_colunas):

    # Definir a Base de Análise
    pasta_analise = './Planilha_Analise'
    caminho_base_analise = glob.glob(os.path.join(pasta_analise, '*.xlsx'))
    base_analise = pd.read_excel(caminho_base_analise[0])


    # Definir a Base Diária

    pasta_hoje = './Planilha_Hoje'
    caminho_base_diaria = glob.glob(os.path.join(pasta_hoje, '*.xlsx'))
    base_dia = pd.read_excel(caminho_base_diaria[0])


    # Vamos modificar a base_dia para ter as mesmas colunas que a base_analise

    base_dia_final = base_dia.drop(columns=list_colunas)

    base_final = pd.concat([base_analise,base_dia_final],ignore_index=True)


    # Apagar a base_dia e salvar a base_final no desktop e atualizar na pasta Planilha_Analise


    for arquivo in caminho_base_diaria:
        os.remove(arquivo)    

    desktop = pathlib.Path.home() / "Desktop" / "Base_Análise.xlsx"
    caminho_base_final = pathlib.Path('Planilha_Analise/base_analise.xlsx')
    base_final.to_excel(desktop, index=False)
    base_final.to_excel(caminho_base_final, index=False)




