# Automação de planilha usando arquivos do email(Gmail / Outlook)

Este projeto foi criado para resolver uma tarefa que tenho diariamente, receber um e-mail contendo uma planilha da qual preciso extrair apenas alguns dados específicos para integrar à minha base principal. Embora seja uma tarefa simples, ela demanda atenção e tempo, recursos que podem ser melhor aproveitados em outras atividades.

### Bibliotecas Utilizadas

* CustomTkinter (Criação de Interface)
* Pandas (Manipulação de Planilhas)
* Imbox (Acesso ao Email)
* Glob
* Os
* Pathlib
* DateTime

### Como rodar o projeto

Primeiramente, deve-se executar o arquivo main.exe, o qual abrirá uma janela onde você deve inserir seu e-mail, senha (utilizando uma senha de aplicativo, é necessário acessar as configurações de segurança do e-mail para obter essa senha), o assunto para filtrar o e-mail correto (apenas os emails do dia atual são pesquisados) e selecionar a plataforma de e-mail (Gmail ou Outlook). Após isso, o programa acessa e localiza o respectivo e-mail usando o assunto fornecido, baixa a planilha, faz as modificações necessárias (essas modificações foram feitas para corresponder à base_analise utilizada como exemplo, para utilizar outras planilhas, é necessário alterar os códigos no arquivo manipulacao.py) e importa os dados para a Base final.

## Observações

Pode-se pensar: por que pedir informações se o objetivo é automatizar? Como pretendo deixar este projeto salvo no GitHub, não posso manter as informações de e-mail e senha, que são necessárias para o funcionamento do código, salvas no repositório. Por isso, optei por criar essa simples interface, para que outras pessoas também possam utilizá-lo. Porém, como mencionado na etapa "Como rodar o projeto", as manipulações feitas na planilha são baseadas em um exemplo. Ou seja, com outra planilha, o código apresentará erro, sendo necessário fazer alterações no arquivo manipulacao.py para que ele funcione corretamente. (Estou desenvolvendo uma nova versão que permitirá escolher quais colunas serão mantidas no manipulacao.py para que não seja necessário fazer alterações no código).

[Linkedin](https://www.linkedin.com/in/guilherme-v-848a1013a/)
