# Automação de planilha usando arquivos do email (Gmail)

Este projeto foi criado para resolver uma tarefa que tenho diariamente, receber um e-mail contendo uma planilha da qual preciso extrair apenas alguns dados específicos para integrar à minha base principal. Embora seja uma tarefa simples, ela demanda atenção e tempo, recursos que podem ser melhor aproveitados em outras atividades.

### Bibliotecas Utilizadas

* [CustomTkinter](https://customtkinter.tomschimansky.com/) (Criação de Interface)
* [Pandas](https://pandas.pydata.org/) (Manipulação de Planilhas)
* [Imbox](https://pypi.org/project/imbox/) (Acesso ao Email)
* [Pillow](https://pypi.org/project/pillow/) (Utilização de imagens)
* Glob
* Os
* Pathlib
* DateTime
* Sys


### Como rodar o projeto

Inicialmente, é necessário inserir na pasta Planilha_analise o arquivo no formato .xlsx que receberá os dados extraídos das bases obtidas via Gmail.

Em seguida, deve-se executar o arquivo main.exe, o qual iniciará o sistema e abrirá uma interface gráfica solicitando três informações:

* Endereço de e-mail (Gmail)
* Senha ([senha de aplicativo](https://support.google.com/accounts/answer/185833?hl=pt-BR))
* Assunto do e-mail que contém a planilha a ser baixada

⚠️ Importante: O sistema realiza a verificação apenas dos e-mails recebidos na data atual.

Após o preenchimento das informações solicitadas, o programa fará o download da planilha correspondente e exibirá suas colunas, permitindo ao usuário selecionar aquelas que deseja manter.  Ao clicar em "Escolher Colunas", o sistema importará exclusivamente as colunas selecionadas para a planilha de análise. Uma cópia do arquivo será salva na área de trabalho, e a planilha na pasta Planilha_analise será atualizada com os dados processados.


## Observações

Pode-se pensar: por que pedir informações se o objetivo é automatizar? Como pretendo deixar este projeto salvo no GitHub, não posso manter as informações de e-mail e senha, que são necessárias para o funcionamento do código, salvas no repositório. Por isso, optei por criar essa interface.


[Linkedin](https://www.linkedin.com/in/guilherme-v-848a1013a/)
