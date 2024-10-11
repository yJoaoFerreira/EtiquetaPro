# 03. Obter informações do Excel: Extrai informações relevantes e organiza os dados.
# 04. Manipular essas informações: Aplica expressões regulares (regex) se necessário, para formatar ou filtrar os dados.
# 05. Deixar as informações no molde de impressão: Prepara os dados em um formato adequado para impressão em etiquetas.
# 06. Gerar um arquivo em PDF: Cria um arquivo PDF formatado para impressão das etiquetas.
# 07. Estabelecer uma conexão da impressora com o programa: Configura a comunicação entre o software e a impressora.
# 08. Conectar-se com a impressora serial selecionada: Permite que o usuário selecione a porta serial correta para a impressora.
# 09. Enviar o PDF gerado para a impressora selecionada: Envia o arquivo PDF formatado para a impressora.
# 10. Imprimir o PDF enviado: Realiza a impressão do PDF através do programa.


# Importa a biblioteca Pandas:
import pandas as pd

# Checa a versão instalada da biblioteca Pandas:
pd.__version__

# Obter o diretório de um arquivo Excel:
diretorio = input('Digite o diretório do Excel: ')

# Ler um arquivo Excel:
pd.read_excel(diretorio)

# Caso seja executado sem erro:
print("Script executado com sucesso!")