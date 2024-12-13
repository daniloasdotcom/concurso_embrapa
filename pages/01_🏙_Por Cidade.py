import streamlit as st
import pandas as pd
from io import BytesIO

# Carregar o arquivo Excel
def load_data(file_path):
    return pd.read_excel(file_path)

# Função para extrair o nome das cidades da coluna 'Localidade'
def extract_cities(localities_list):
    cities = []
    for localities in localities_list:
        for locality in localities:
            # Extrair o nome da cidade após o travessão ('–') e antes do estado ('/XX')
            if pd.notnull(locality):
                try:
                    city = locality.split('–')[-1].split('/')[0].strip()
                    cities.append(city)
                except IndexError:
                    continue
    return sorted(list(set(cities)))

# Função para extrair opções únicas da coluna 'Graduação'
def extract_graduation_options(graduations_list):
    options = []
    for graduations in graduations_list:
        for grad in graduations:
            if pd.notnull(grad):
                # Dividir por ponto e vírgula e adicionar cada item à lista
                options.extend([item.strip() for item in grad.split(';')])
    return sorted(list(set(options)))

# Função para extrair opções únicas da coluna 'Mestrado'
def extract_masters_options(masters):
    options = []
    for master in masters:
        if pd.notnull(master):
            # Dividir por ponto e vírgula e adicionar cada item à lista
            options.extend([item.strip() for item in master.split(';')])
    return sorted(list(set(options)))

# Função para gerar arquivo Excel em memória
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    processed_data = output.getvalue()
    return processed_data

# Função principal da aplicação
def main():
    st.title("Filtro de Localidades, Graduação e Mestrado")

    # Nome fixo dos arquivos Excel
    file_path_pesquisador = "pesquisador.xlsx"
    file_path_analista = "Analista.xlsx"

    try:
        # Carregar os dados do Excel
        df_pesquisador = load_data(file_path_pesquisador)
        df_analista = load_data(file_path_analista)

        # Remover vírgulas da coluna 'Opção nº' se ela existir
        if 'Opção nº' in df_pesquisador.columns:
            df_pesquisador['Opção nº'] = df_pesquisador['Opção nº'].astype(str).str.replace(",", "")

        if 'Opção nº' in df_analista.columns:
            df_analista['Opção nº'] = df_analista['Opção nº'].astype(str).str.replace(",", "")

        # Verificar se a coluna 'Localidade' existe
        if 'Localidade' not in df_pesquisador.columns or 'Localidade' not in df_analista.columns:
            st.error("Os arquivos não contêm a coluna 'Localidade'.")
            return

        # Extrair cidades únicas combinando os dois arquivos
        cities = extract_cities([df_pesquisador['Localidade'], df_analista['Localidade']])

        # Verificar se a coluna 'Graduação' existe
        if 'Graduação' not in df_pesquisador.columns or 'Graduação' not in df_analista.columns:
            st.error("Os arquivos não contêm a coluna 'Graduação'.")
            return

        # Extrair opções únicas de graduação combinando os dois arquivos
        graduation_options = extract_graduation_options([df_pesquisador['Graduação'], df_analista['Graduação']])

        # Verificar se a coluna 'Mestrado' existe
        if 'Mestrado' not in df_pesquisador.columns:
            st.error("O arquivo de Pesquisador não contém a coluna 'Mestrado'.")
            return

        # Extrair opções únicas de mestrado
        masters_options = extract_masters_options(df_pesquisador['Mestrado'])

        # Estado inicial das seleções
        reset_filters = st.button("Limpar Filtros")
        if reset_filters:
            st.session_state["selected_city"] = ""
            st.session_state["selected_graduation"] = ""
            st.session_state["selected_masters"] = ""

        if "selected_city" not in st.session_state:
            st.session_state["selected_city"] = ""

        if "selected_graduation" not in st.session_state:
            st.session_state["selected_graduation"] = ""

        if "selected_masters" not in st.session_state:
            st.session_state["selected_masters"] = ""

        # Adicionar lista suspensa para seleção de cidade
        selected_city = st.selectbox("Selecione uma cidade", [""] + cities, index=0, key="selected_city")

        # Adicionar segunda lista suspensa para seleção de graduação
        selected_graduation = st.selectbox("Selecione uma graduação", [""] + graduation_options, index=0, key="selected_graduation")

        # Adicionar terceira lista suspensa para seleção de mestrado
        selected_masters = st.selectbox("Selecione um mestrado", [""] + masters_options, index=0, key="selected_masters")

        # Filtrar os dados pela cidade selecionada
        filtered_pesquisador = df_pesquisador
        filtered_analista = df_analista

        if selected_city:
            filtered_pesquisador = filtered_pesquisador[filtered_pesquisador['Localidade'].str.contains(selected_city, na=False)]
            filtered_analista = filtered_analista[filtered_analista['Localidade'].str.contains(selected_city, na=False)]

        # Filtrar os dados pela graduação selecionada
        if selected_graduation:
            filtered_pesquisador = filtered_pesquisador[filtered_pesquisador['Graduação'].str.contains(selected_graduation, na=False)]
            filtered_analista = filtered_analista[filtered_analista['Graduação'].str.contains(selected_graduation, na=False)]

        # Filtrar os dados pelo mestrado selecionado (somente para Pesquisador)
        if selected_masters:
            filtered_pesquisador = filtered_pesquisador[filtered_pesquisador['Mestrado'].str.contains(selected_masters, na=False)]

        # Selecionar as colunas desejadas
        columns_to_display = ['Opção nº', 'Cargo', 'Área', 'Subárea', 'Total de Vagas', 'Mestrado', 'Graduação']

        # Verificar se as colunas existem no DataFrame
        existing_columns_pesquisador = [col for col in columns_to_display if col in df_pesquisador.columns]
        existing_columns_analista = [col for col in columns_to_display if col in df_analista.columns]

        if existing_columns_pesquisador:
            st.subheader("Resultados para vagas de pesquisador")

            # Botão para baixar os resultados como Excel
            excel_pesquisador = to_excel(filtered_pesquisador[existing_columns_pesquisador])
            st.download_button(
                label="Baixar resultados de pesquisador em Excel",
                data=excel_pesquisador,
                file_name="resultados_pesquisador.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            st.write(filtered_pesquisador[existing_columns_pesquisador])

        else:
            st.error("As colunas selecionadas não foram encontradas no arquivo de Pesquisador.")

        if existing_columns_analista:
            st.subheader("Resultados para vagas de analista")

            # Botão para baixar os resultados como Excel
            excel_analista = to_excel(filtered_analista[existing_columns_analista])
            st.download_button(
                label="Baixar resultados de analista em Excel",
                data=excel_analista,
                file_name="resultados_analista.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            st.write(filtered_analista[existing_columns_analista])

        else:
            st.error("As colunas selecionadas não foram encontradas no arquivo de Analista.")

    except FileNotFoundError as e:
        st.error(f"O arquivo não foi encontrado: {e.filename}. Certifique-se de que ele está no diretório correto.")

if __name__ == "__main__":
    main()
