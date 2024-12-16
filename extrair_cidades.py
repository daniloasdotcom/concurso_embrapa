import re
import pandas as pd

# Caminho para o arquivo .txt
file_path = "seu_arquivo.txt"

# Lê o conteúdo do arquivo com a codificação correta
with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

# Expressão regular para extrair cidade e estado
matches = re.findall(r"–\s([^/]+)/(\w{2})", text_content)

# Formata os resultados no formato "Cidade/Estado"
formatted_cities_states = [f"{city}/{state}" for city, state in matches]

# Remove duplicados e ordena os resultados
unique_formatted = sorted(set(formatted_cities_states))

# Salva os resultados em um arquivo CSV ou exibe no terminal
output_file = "cidades_formatadas.csv"
df_formatted_cities_states = pd.DataFrame(unique_formatted, columns=["City/State"])
df_formatted_cities_states.to_csv(output_file, index=False, encoding="utf-8-sig")

print("Os dados foram processados e salvos em 'cidades_formatadas.csv'.")
