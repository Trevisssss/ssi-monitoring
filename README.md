# 🤖 Monitor de SSI do LinkedIn

### 📄 Descrição

Este projeto é uma solução completa de ETL (Extração, Transformação e Carga) e Data Analytics desenvolvida em Python para automatizar a coleta da pontuação do Social Selling Index (SSI) do LinkedIn. O objetivo é extrair os dados diariamente, armazená-los e visualizar a evolução das métricas ao longo do tempo através de um dashboard interativo.

O projeto foi construído de forma modular, separando as responsabilidades de autenticação, extração de dados (scraping), orquestração e visualização.

### 🛠️ Tecnologias Utilizadas

- Linguagem: `Python 3.12`

- Automação Web (Autenticação e Scraping): `Playwright`

- Manipulação de Dados: `Pandas`

- Visualizações e Dashboard: `Matplotlib & Seaborn & Streamlit`


### 📂 Estrutura do Projeto

O projeto é dividido em módulos de forma com que seja mais fácil identificar erros e implementar melhorias no código em partes específicas.

- **auth.py:** Responsável por criar e salvar um estado de sessão autenticada, evitando a necessidade de fazer login a cada execução.

- **extraction_linkedin.py:** É responsável pelo web scraping. Usa a sessão salva para navegar até a página do SSI e extrair as cinco principais métricas.

- **orquestrador.py:** Como forma de centralizar todas as ações em um único local, o script orquestrador.py atua como o orquestrador do processo todo. Ele verifica se uma sessão de autenticação existe; se não, executa apenas o ETL, para coletar e salvar os dados do dia no arquivo `CSV`.

- **dashboard.py:** Utilizando o Streamlit em conjunto com pandas, matplotlib e seaborn, criei as visualizações necessárias para acompanhar a evolução dos indicadores do LinkedIn, que nativamente não possui esse acompanhamento histórico.

### 🎯 Desafios Superados

Durante o desenvolvimento, enfrentamos alguns desafios técnicos que são comuns em projetos de automação web e que serviram como grandes aprendizados:

⚠️ **Arquitetura da Solução:** Um dos desafios era qual a arquitetura a ser escolhida, pois até então só havia a ideia que resolveria um 'problema'.
Cheguei a cogitar Power BI e Looker Studio pela facilidade de criar as visualizações e também compartilhamento, mas como o projeto não exige que haja um compartilhamento mais robusto e seguro, preferi simplificar em um ambiente unificado, além de praticar conceitos mais novos.

💡**Solução:** Optei por uma stack 100% Python, pois a linguagem normamente é a referência quando se trata de web scraping em projetos de dados. Com bibliotecas especializadas tanto para a extração (como Playwright) quanto para a visualização (como Streamlit e Seaborn), permitiu manter todo o ciclo de vida do projeto em um ambiente único. 


⚠️**Login:** O LinkedIn não possui uma API pública para o SSI e utiliza mecanismos avançados para detectar e bloquear automação. A tentativa inicial de fazer login a cada execução falhou devido a CAPTCHAs e páginas em branco.

💡**Solução:** Implementei uma estratégia de 'persistência' de sessão. A biblioteca `playwright` possibilita o salvamento de cookies, tokens e outros elementos que podem ser reaproveitados pra que o login seja feito uma vez só manualmente, e os seguintes ocorram automaticamente. Isso permite uma maior simplificação na solução, ainda que não idealmente ocorra de forma dinâmica e automática.

> Nota: O projeto foi concluído em menos de 2 dias, e só foi possível pela simplificação das ideias comentadas, como a questão do login, e arquitetura escolhida. Mas a ideia é deixar o projeto mais robusto enquanto estudo os conceitos da próxima sessão ⬇️⬇️⬇️:

### 🚀 Próximos Passos

O projeto está funcional, mas há três melhorias principais planejadas para torná-lo uma solução de nível profissional:

**Melhorar o Processo de Autenticação:**

A abordagem de sessão persistente usando a biblioteca `playwright` é eficaz, mas a sessão pode expirar ou ser invalidada, exigindo a recriação manual do arquivo de autenticação. Um próximo passo importante é desenvolver uma rotina de login totalmente automatizada, capaz de detectar a necessidade de uma nova autenticação e realizá-la sem intervenção humana.


**Migração para Banco de Dados na Nuvem:**

Atualmente, os dados são salvos em um arquivo CSV local. Com o objetivo de deixar este projeto o mais próximo de um case real possíveo, o próximo passo é substituir o CSV por um banco de dados na nuvem, como Google BigQuery, Supabase (PostgreSQL) ou Neon. Isso trará mais escalabilidade, segurança e facilitará a conexão com outras ferramentas de BI.

**Automação Aprimorada:**

A execução do script ainda é manual. O objetivo final é automatizar a execução diária do script orquestrador.py sem depender de um computador local. A principal tecnologia a ser explorada para isso é o `GitHub Actions`, criando um workflow agendado (cron) que rodará o processo de ETL diretamente do repositório.

Existem outras formas de implementar essa solução, mas exigem um maior investimento de tempo e conhecimento, e o GitHub Actions parece ser a mais simples pra este projeto.


