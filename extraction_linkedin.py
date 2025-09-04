#Imports
import os
import csv
from datetime import datetime
from playwright.sync_api import sync_playwright

"""
--------------------------------------|--------------------------------------------
Este script de fato irá coletar os dados do SSI, enquanto que o outro script apenas
--------------------------------------|--------------------------------------------.
"""
# Constante com o caminho do arquivo de estado para ser usada por outros scripts
ARQUIVO_ESTADO = "playwright/.auth/estado_linkedin.json"

# URL da página do Social Selling Index
URL_SSI = "https://www.linkedin.com/sales/ssi"


def etl_ssi():
    """
    Carrega a sessão salva, navega para a página do SSI, extrai as pontuações
    e as armazena em um dicionário.
    """
    # 1. Inicia o dicionário para armazenar os dados
    dados_ssi = {}

    with sync_playwright() as p:
        # Usamos um diretório persistente para o navegador
        browser = p.chromium.launch_persistent_context(
            user_data_dir="playwright/user_data",
            headless=False,
            slow_mo=5000
        )
        
        # Pega a primeira página que já vem aberta
        pagina = browser.pages[0]

        # Navega para a página do SSI para o login
        pagina.goto("https://www.linkedin.com/sales/ssi")
        pagina.bring_to_front()

        # Full Xpaths das pontuações:

        xpath_pontuacao_geral = "/html/body/main/article/section[2]/div/figure/figcaption/p/span"
        xpath_pontuacao_marca = '/html/body/main/article/section[2]/div/section/ul/li[1]/div/label/strong'
        xpath_pontuacao_pessoas = '/html/body/main/article/section[2]/div/section/ul/li[2]/div/label/strong'
        xpath_pontuacao_insights = '/html/body/main/article/section[2]/div/section/ul/li[3]/div/label/strong'
        xpath_pontuacao_relacionamentos = '/html/body/main/article/section[2]/div/section/ul/li[4]/div/label/strong'


        # Espera o elemento aparecer na tela para garantir que a página carregou
        print("Aguardando o elemento da pontuação carregar...")
        pagina.wait_for_selector(f"xpath={xpath_pontuacao_geral}", timeout=5000)

        # 1. Localiza o elemento usando o XPath extrai a pontuação geral.
        elemento_pontuacao = pagina.locator(f"xpath={xpath_pontuacao_geral}")
        dados_ssi['pontuacao_geral'] = elemento_pontuacao.inner_text()

        # 2. Localiza o elemento usando o XPath extrai a pontuação da marca.
        elemento_pontuacao = pagina.locator(f"xpath={xpath_pontuacao_marca}")
        dados_ssi['pontuacao_marca'] = elemento_pontuacao.inner_text()

        # 3. Localiza o elemento usando o XPath extrai a pontuação de pessoas.
        elemento_pontuacao = pagina.locator(f"xpath={xpath_pontuacao_pessoas}")
        dados_ssi['pontuacao_pessoas'] = elemento_pontuacao.inner_text()

        # 4. Localiza o elemento usando o XPath extrai a pontuação geral.
        elemento_pontuacao = pagina.locator(f"xpath={xpath_pontuacao_insights}")
        dados_ssi['pontuacao_insights'] = elemento_pontuacao.inner_text()

        # 5. Localiza o elemento usando o XPath extrai a pontuação geral.
        elemento_pontuacao = pagina.locator(f"xpath={xpath_pontuacao_relacionamentos}")
        dados_ssi['pontuacao_relacionamentos'] = elemento_pontuacao.inner_text()

        dados_ssi['hora_coleta'] = datetime.now()
        browser.close()

        # Agora com os dados armazenados em um dicionário, tá na hora de colocar isso em um arquivo para salvar

        caminhocsv = 'dados_ssi_raw.csv'
        fileexists = os.path.exists(caminhocsv)

        with open(caminhocsv, 'a', newline='') as csvfile:
            fieldnames = ['pontuacao_geral', 'pontuacao_marca', 'pontuacao_pessoas', 'pontuacao_insights', 'pontuacao_relacionamentos','hora_coleta']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not fileexists:
                writer.writeheader()

            writer.writerow(dados_ssi)

            print(f"\nDados salvos com sucesso no arquivo '{caminhocsv}'")



