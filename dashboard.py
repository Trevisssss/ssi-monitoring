import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ao ler o CSV, o Pandas não sabe que a coluna de data/hora deve ser tratada
# como um tipo datetime, então ele a lê como texto (object).
# Para corrigir isso, usamos o parâmetro `parse_dates`.

# Supondo que o nome da sua coluna de data/hora no CSV seja 'hora_coleta'
def carregar_dados():
    data = pd.read_csv('dados_ssi_raw.csv', parse_dates=['hora_coleta'])
    # Criar a coluna data, pois é apenas a data inicialmente que nos interessa:
    data['data'] = data['hora_coleta'].dt.date
    return data

data = carregar_dados()


#Configuração da página
st.set_page_config(page_title="Dashboard SSI LinkedIn", layout="centered")

# Título principal do dashboard
st.title("📈 Dashboard de Evolução do LinkedIn SSI")
st.markdown("Acompanhe a sua pontuação do Social Selling Index ao longo do tempo.")

pontuacaoGeral = data.groupby('data').agg( Geral = pd.NamedAgg(column='pontuacao_geral', aggfunc='max'))

st.subheader("Evolução da Pontuação Geral ao longo do tempo", )
st.line_chart(pontuacaoGeral, color="#41456b")