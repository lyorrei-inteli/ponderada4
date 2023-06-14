
# Video Uploader

Este script captura vídeos da webcam, os salva como arquivos temporários, os envia para um bucket de armazenamento do Supabase e fornece a opção de visualizar os logs dos vídeos enviados. Ele é construído em Python e utiliza as seguintes bibliotecas:

- `os`: Fornece uma maneira de interagir com o sistema operacional, como remover arquivos.
- `keyboard`: Permite registrar e lidar com eventos do teclado.
- `cv2` (OpenCV): Usado para capturar frames de vídeo da webcam e escrevê-los em um arquivo.
- `time`: Usado para medir a duração da gravação de vídeo.
- `datetime`: Ajuda a gerar um carimbo de data/hora para o nome do arquivo de saída.
- `dotenv`: Carrega variáveis de ambiente de um arquivo `.env`.
- `supabase`: Fornece um cliente para interagir com a API do Supabase.

## Instalação

Siga estes passos para instalar e executar o script:

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python no site oficial: [python.org](https://www.python.org).
2. Clone ou faça o download do script a partir do repositório ou copie o código fornecido para um arquivo com a extensão `.py` (por exemplo, `video_uploader.py`).
3. Navegue até o diretório que contém o script em um terminal ou prompt de comando.
4. Instale os pacotes Python necessários executando o seguinte comando:

   ```
   pip install keyboard opencv-python python-dotenv supabase-py
   ```

   Isso irá instalar os pacotes necessários (`keyboard`, `opencv-python`, `python-dotenv` e `supabase-py`) para a execução do script.
5. Crie uma conta no Supabase em [supabase.io](https://supabase.io), caso ainda não tenha uma.
6. Crie um novo projeto no Supabase e obtenha a URL do projeto e a Chave de Acesso.
7. Crie um arquivo `.env` no mesmo diretório do script e adicione as seguintes linhas, substituindo o espaço reservado pela sua Chave de Acesso do Supabase:

   ```
   SUPABASE_KEY=sua_chave_de_acesso_aqui
   ```

   Salve o arquivo.
8. Execute o script usando o seguinte comando:

   ```
   python3 app.py
   ```

## Utilização

Uma vez em execução, o script permite o seguinte:

- Pressione "Enter" para iniciar a gravação de vídeo.
- Pressione "Espaço" para obter os logs dos vídeos enviados.

Ao pressionar "Enter" para iniciar a gravação, o script capturará o vídeo da webcam por 5 segundos e o salvará como um arquivo temporário. Em seguida, ele fará o upload do arquivo para o bucket de armazenamento do Supabase e excluirá o arquivo temporário. Você também poderá ver os logs dos vídeos enviados pressionando "Espaço". O script continuará em execução até que você pressione a tecla "Esc" para sair.

Lembre-se de que o script foi projetado para trabalhar com uma webcam conectada ao seu sistema. Certifique-se de ter uma webcam funcional disponível durante a execução do script.

## Vídeo do funcionamento do projeto

https://youtu.be/zwl_7AiBcPs
