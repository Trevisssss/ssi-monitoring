import os
from playwright.sync_api import sync_playwright

# Este arquivo agora atua como um módulo de autenticação.
# Ele define a função para criar uma sessão, mas não a executa diretamente.
# A execução será controlada pelo script principal (o orquestrador).

# Constante com o caminho do arquivo de estado para ser usada por outros scripts
ARQUIVO_ESTADO = "playwright/.auth/estado_linkedin.json"

def criar_sessao_linkedin():
    """
    Abre um navegador para que o usuário faça o login manualmente.
    Após o login, o script aguarda a confirmação do usuário para salvar o estado
    de autenticação (cookies) em um arquivo.
    """
    with sync_playwright() as p:
        # Usamos um diretório persistente para o navegador
        contexto_usuario = p.chromium.launch_persistent_context(
            user_data_dir="playwright/user_data",
            headless=False,
            slow_mo=50
        )
        
        # Pega a primeira página que já vem aberta
        pagina = contexto_usuario.pages[0]

        # Navega para a página do SSI para o login
        pagina.goto("https://www.linkedin.com/sales/ssi")
        pagina.bring_to_front()

        print("\n" + "="*50)
        print(">>> AÇÃO MANUAL NECESSÁRIA <<<")
        print("1. Faça o login na sua conta do LinkedIn na janela do navegador que abriu.")
        print("2. Resolva qualquer CAPTCHA ou verificação de segurança.")
        print("3. Após o login, volte para este terminal.")
        input("4. Pressione Enter aqui para continuar e salvar a sessão...")
        print("="*50 + "\n")

        # Após o usuário pressionar Enter, o estado da sessão é salvo.
        contexto_usuario.storage_state(path=ARQUIVO_ESTADO)
        print(f"Sessão salva com sucesso em: {ARQUIVO_ESTADO}")
        
        # Fecha o navegador
        contexto_usuario.close()

# O bloco 'if __name__ == "__main__":' foi removido.
# Este script não fará nada se for executado diretamente.
# Ele deve ser importado e sua função deve ser chamada por outro script.
