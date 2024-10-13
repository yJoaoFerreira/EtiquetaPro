# 03. Obter informações do Excel: Extrai informações relevantes e organiza os dados.
# 04. Manipular essas informações: Aplica expressões regulares (regex) se necessário, para formatar ou filtrar os dados.
# 05. Deixar as informações no molde de impressão: Prepara os dados em um formato adequado para impressão em etiquetas.
# 06. Gerar um arquivo em PDF: Cria um arquivo PDF formatado para impressão das etiquetas.
# 07. Estabelecer uma conexão da impressora com o programa: Configura a comunicação entre o software e a impressora.
# 08. Conectar-se com a impressora serial selecionada: Permite que o usuário selecione a porta serial correta para a impressora.
# 09. Enviar o PDF gerado para a impressora selecionada: Envia o arquivo PDF formatado para a impressora.
# 10. Imprimir o PDF enviado: Realiza a impressão do PDF através do programa.


import tkinter as tk
from tkinter import filedialog
import pandas as pd

pd.__version__

def selecionar_arquivo():
    # Abre a caixa de diálogo para escolher um arquivo
    arquivo_excel = filedialog.askopenfilename(
        title="Selecione um arquivo Excel",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )

    if arquivo_excel:
        try:
            # Exibe o diretório do arquivo selecionado no terminal
            print(f"Arquivo selecionado: {arquivo_excel}")

            # Lê o arquivo Excel
            df = pd.read_excel(arquivo_excel)
            print("Script executado com sucesso!")
            print(df.head())
        except Exception as e:
            print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
    else:
        print("Nenhum arquivo foi selecionado")

# Criando a janela principal do Tkinter
root = tk.Tk()
root.title("EtiquetaPro")

# Tamanho da janela
root.geometry("300x150")

# Botão para selecionar o arquivo
botao = tk.Button(root, text="Selecionar Arquivo Excel", command=selecionar_arquivo)
botao.pack(pady=20)

# Rodando a interface
root.mainloop()
