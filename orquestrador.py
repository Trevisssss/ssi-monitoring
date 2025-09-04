import os
from sessao_linkedin import criar_sessao_linkedin
from extraction_linkedinv2 import etl_ssi

# --- Configuração ---
# Nome da pasta onde a sessão do Playwright será salva.
# Usar um nome sem a barra no início o torna relativo ao projeto.
PASTA_SESSAO_NOME = 'playwright'

# Monta o caminho completo para a pasta de sessão.
# O resultado de os.path.join é atribuído a uma nova variável.
PASTA_SESSAO_CAMINHO = os.path.join(os.getcwd(), PASTA_SESSAO_NOME)

def orquestrar_etl():
    """
    Função principal que orquestra a execução do projeto.
    Verifica se a sessão de login existe e decide qual função chamar.
    """
    print("--- Iniciando Processo de ETL ---")

    # 1. Checa se o arquivo de autenticação/sessão existe.
    if not os.path.exists(PASTA_SESSAO_CAMINHO):
        print(f"\nArquivo de sessão '{PASTA_SESSAO_CAMINHO}' não encontrado.")
        print("Iniciando o processo de criação de sessão pela primeira vez...")
        # Se não existe, chama a função para criar a sessão
        criar_sessao_linkedin()
        print("\nSessão criada com sucesso!")
    else:
        print(f"\nArquivo de sessão '{PASTA_SESSAO_CAMINHO}' encontrado.")

    # 2. Com a sessão garantida, executa a coleta de dados.
    print("Iniciando a coleta de dados do SSI...")
    try:
        etl_ssi()
        print("\n--- Processo concluído com sucesso! ---")
    except Exception as e:
        print(f"\n--- Ocorreu um erro durante a coleta de dados: {e} ---")
        print("Isso pode ser devido a uma sessão expirada.")
        print(f"Tente deletar o arquivo '{PASTA_SESSAO_CAMINHO}' e executar o script novamente para fazer um novo login.")

if __name__ == "__main__":
    orquestrar_etl()
