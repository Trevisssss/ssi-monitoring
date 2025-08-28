# Projeto SSI (Social Score Index)

## Objetivo

Este projeto tem por objetivo monitorar o indicador SSI do linkedin, de forma a acompanhar as tendências, para tentar entender melhor quais as ações mais geram diferença na pontuação.

A ideia é criar um script python que colete os dados dos indicadores, e armazene em um banco de dados, ou até mesmo um arquivo csv, para que um dashboard seja gerado a partir desses dados, que serão monitorados.

#Tecnologias utilizadas:

`Python`:

**Bibliotecas:**

- *Playwright:*
    - **Função:** Automação do acesso ao linkedin: Como não há uma API pública, o acesso tem de ser feito por meio de automação web, simulando o acesso de alguém. E essa biblioteca facilita lidar com a autenticação, por meio de um 'arquivo de sessão', que guarda as informações do login e senha, além de cookies etc.
    
- *Pandas e Numpy:*
    - **Função:** Manipulação de dados: Manipulação, tratamento, criação de métricas e salvar em arquivo *`.csv`*.

- *Plotly e Streamlit:*
    - **Função:** Criação das visualizações e possibilidade de criação de um dashboard local.