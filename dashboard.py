import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Ao ler o CSV, o Pandas não sabe que a coluna de data/hora deve ser tratada
# como um tipo Datetime, então ele a lê como texto (object).
# Para corrigir isso, usamos o parâmetro `parse_Datas`.

# Supondo que o nome da sua coluna de data/hora no CSV seja 'hora_coleta'
def carregar_dados():
    data = pd.read_csv('dados_ssi_raw.csv', parse_dates=['hora_coleta'])
    # Criar a coluna data, pois é apenas a data inicialmente que nos interessa:
    data['Data'] = data['hora_coleta'].dt.date
    return data

data = carregar_dados()


#Configuração da página
st.set_page_config(page_title="Dashboard SSI LinkedIn", layout="wide")

# Título principal do dashboard
st.title("📈 Dashboard de Evolução do LinkedIn SSI")
st.markdown("Acompanhe a sua pontuação do Social Selling Index ao longo do tempo.")

#Dataframes para plotar
pontuacaoGeral = data.groupby('Data').agg( Geral = pd.NamedAgg(column='pontuacao_geral', aggfunc='max')).reset_index()
pontuacaoMarca = data.groupby('Data').agg( Marca = pd.NamedAgg(column='pontuacao_marca', aggfunc='max')).reset_index()
pontuacaoPessoas = data.groupby('Data').agg( Pessoas = pd.NamedAgg(column='pontuacao_pessoas', aggfunc='max')).reset_index()
pontuacaoInsights = data.groupby('Data').agg( Insights = pd.NamedAgg(column='pontuacao_insights', aggfunc='max')).reset_index()
pontuacaoRelacionamentos = data.groupby('Data').agg( Relacionamentos = pd.NamedAgg(column='pontuacao_relacionamentos', aggfunc='max')).reset_index()


#--- Plotando os gráficos com Seaborn ---

# Define um estilo estético para os gráficos do Seaborn
sns.set_theme(style="darkgrid", palette='pastel', context='talk', font_scale=0.3)

# Gráfico 1: Pontuação Geral
st.subheader("Evolução da Pontuação 'Geral' ao longo do tempo")
fig_geral, ax_geral = plt.subplots(figsize=(4,2)) # Cria a figura
sns.lineplot(data=pontuacaoGeral, x='Data', y='Geral', ax=ax_geral, color="#41456b", marker='.', linewidth=0.5)
ax_geral.set_ylabel("Pontuação Geral")
ax_geral.set_xlabel("Data")
#Formato das Datas do Gráfico 1
date_format = mdates.DateFormatter('%d-%m-%Y')
ax_geral.xaxis.set_major_formatter(date_format)
fig_geral.autofmt_xdate() # Formata a data no eixo X
st.pyplot(fig_geral, width='content') # Exibe no Streamlit

st.divider() # Adiciona uma linha divisória visual

# --- Grade 2x2 para os outros gráficos ---
col1, col2 = st.columns(2)

with col1:
    # Gráfico 2: Pontuação Marca
    st.subheader("Evolução da Pontuação 'Marca Profissional'")
    st.caption("Complete seu perfil tendo o cliente em mente. Publique conteúdo útil para se tornar um líder inovador no setor.")
    fig_marca, ax_marca = plt.subplots(figsize=(4, 2))
    sns.lineplot(data=pontuacaoMarca, x='Data', y='Marca', ax=ax_marca, color="#ffa366", marker='.', linewidth=0.8)
    ax_marca.set_ylabel("Pontuação da Marca")
    ax_marca.set_xlabel("Data")
    date_format = mdates.DateFormatter('%d-%m-%Y')
    ax_marca.xaxis.set_major_formatter(date_format)
    fig_marca.autofmt_xdate()
    st.pyplot(fig_marca, width='content')

    # Gráfico 4: Pontuação Insights
    st.subheader("Evolução da Pontuação 'Insights'")
    st.caption("Compartilhe atualizações que promovam diálogos e fortaleçam relacionamentos.")
    fig_insights, ax_insights = plt.subplots(figsize=(4, 2))
    sns.lineplot(data=pontuacaoInsights, x='Data', y='Insights', ax=ax_insights, color="#3b9961", marker='.', linewidth=0.8)
    ax_insights.set_ylabel("Pontuação de Insights")
    ax_insights.set_xlabel("Data")
    date_format = mdates.DateFormatter('%d-%m-%Y')
    ax_insights.xaxis.set_major_formatter(date_format)
    fig_insights.autofmt_xdate()
    st.pyplot(fig_insights, width='content')

with col2:
    # Gráfico 3: Pontuação Pessoas
    st.subheader("Evolução da Pontuação 'Pessoas Certas'")
    st.caption("Encontre os clientes certos com mais precisão e em menos tempo utilizando ferramentas de pesquisa eficazes.")
    fig_pessoas, ax_pessoas = plt.subplots(figsize=(4, 2))
    sns.lineplot(data=pontuacaoPessoas, x='Data', y='Pessoas', ax=ax_pessoas, color="#127dd6", marker='.', linewidth=0.8)
    ax_pessoas.set_ylabel("Pontuação de Pessoas")
    ax_pessoas.set_xlabel("Data")
    date_format = mdates.DateFormatter('%d-%m-%Y')
    ax_pessoas.xaxis.set_major_formatter(date_format)
    fig_pessoas.autofmt_xdate()
    st.pyplot(fig_pessoas, width='content')

    # Gráfico 5: Relacionamentos
    st.subheader("Evolução da Pontuação 'Criar Relacionamentos'")
    st.caption("Crie relacionamentos de confiança com decisores para fortalecer sua rede.")
    fig_relacionamentos, ax_relacionamentos = plt.subplots(figsize=(4, 2))
    sns.lineplot(data=pontuacaoRelacionamentos, x='Data', y='Relacionamentos', ax=ax_relacionamentos, color="#c74444", marker='.', linewidth=0.8)
    ax_relacionamentos.set_ylabel("Pontuação de Relacionamentos")
    ax_relacionamentos.set_xlabel("Data")
    date_format = mdates.DateFormatter('%d-%m-%Y')
    ax_relacionamentos.xaxis.set_major_formatter(date_format)
    fig_relacionamentos.autofmt_xdate()
    st.pyplot(fig_relacionamentos, width='content')