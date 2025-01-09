import pandas as pd

def filtrar_por_codigo_municipio(caminho_csv, codigo_municipio, nome_arquivo_saida):
  """
  Lê um arquivo CSV, filtra os dados com base em um código de município específico
  na coluna 'CO_MUNICIPIO' e salva o resultado em um novo arquivo CSV.

  Args:
    caminho_csv: O caminho para o arquivo CSV de entrada.
    codigo_municipio: O código do município a ser filtrado (ex: 2704302).
    nome_arquivo_saida: O nome do arquivo CSV de saída (ex: microdados_ed_basica_2016_alagoas).
  """
  try:
    # Lê o arquivo CSV usando o pandas, assumindo que o separador é ';'
    # e o encoding é 'ISO-8859-1', comum em arquivos do INEP.
    # Usa-se low_memory=False para evitar problemas com tipos de dados mistos nas colunas.
    df = pd.read_csv(caminho_csv, sep=';', encoding='ISO-8859-1', low_memory=False)

    # Filtra o DataFrame pela coluna 'CO_MUNICIPIO'
    df_filtrado = df[df['CO_MUNICIPIO'] == codigo_municipio]

    # Salva o DataFrame filtrado em um novo arquivo CSV
    # index=False evita que o índice do DataFrame seja salvo no arquivo.
    df_filtrado.to_csv(f'{nome_arquivo_saida}.csv', sep=';', encoding='ISO-8859-1', index=False)

    print(f"Arquivo '{nome_arquivo_saida}.csv' criado com sucesso!")

  except FileNotFoundError:
    print(f"Erro: Arquivo '{caminho_csv}' não encontrado.")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")


# Exemplo de uso:
caminho_arquivo_entrada = 'microdados_ed_basica_2023.csv' # Substitua pelo caminho do seu arquivo
codigo_municipio_alagoas = 2704302
nome_arquivo_saida = 'microdados_ed_basica_2023_alagoas'

filtrar_por_codigo_municipio(caminho_arquivo_entrada, codigo_municipio_alagoas, nome_arquivo_saida)