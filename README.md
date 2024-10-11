# EtiquetaPro

**EtiquetaPro** é um software desenvolvido em Python que facilita a impressão de etiquetas a partir de arquivos Excel. Com uma interface gráfica amigável, ele permite que usuários leiam, manipulem e imprimam etiquetas de forma eficiente, conectando-se a impressoras matriciais via porta serial.

## Funcionalidades

> O software deve cumprir as seguintes etapas para ser considerado `"completo"`:

1. **Obter o diretório de um arquivo Excel**: O usuário pode selecionar um arquivo Excel a partir de seu sistema.
2. **Ler um arquivo Excel do diretório selecionado**: O programa lê os dados contidos no arquivo Excel escolhido.
3. **Obter informações do Excel**: Extrai informações relevantes e organiza os dados.
4. **Manipular essas informações**: Aplica expressões regulares (regex) se necessário, para formatar ou filtrar os dados.
5. **Deixar as informações no molde de impressão**: Prepara os dados em um formato adequado para impressão em etiquetas.
6. **Gerar um arquivo em PDF**: Cria um arquivo PDF formatado para impressão das etiquetas.
7. **Estabelecer uma conexão da impressora com o programa**: Configura a comunicação entre o software e a impressora.
8. **Conectar-se com a impressora serial selecionada**: Permite que o usuário selecione a porta serial correta para a impressora.
9. **Enviar o PDF gerado para a impressora selecionada**: Envia o arquivo PDF formatado para a impressora.
10. **Imprimir o PDF enviado**: Realiza a impressão do PDF através do programa.

## Tecnologias Utilizadas (WIP)

- **Python**: Linguagem de programação principal.
- **pandas**: Para leitura e manipulação de arquivos Excel.
- **pySerial**: Para comunicação com a impressora via porta serial.
- **Tkinter**: Para a interface gráfica.
- **ReportLab**: Para geração de arquivos PDF.

## Pré-requisitos

Antes de executar o programa, certifique-se de ter o Python instalado em sua máquina. Você também precisará instalar as dependências listadas no arquivo `requirements.txt`.
