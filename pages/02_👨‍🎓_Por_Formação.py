import streamlit as st
import pandas as pd
from fpdf import FPDF

# Função para carregar os dados da planilha Excel
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Função para processar os cursos de graduação e criar uma lista única
def extract_courses(df, column):
    all_courses = []
    for cell in df[column].dropna():
        courses = [course.strip() for course in cell.split(';')]
        all_courses.extend(courses)
    return sorted(set(all_courses))

# Obter lista única de Mestrados a partir da coluna, dividindo os valores por ";"
def extract_unique_mestrados(df, column):
    all_mestrados = []
    for cell in df[column].dropna():
        mestrados = [mestrado.strip() for mestrado in cell.split(';')]  # Dividir e remover espaços extras
        all_mestrados.extend(mestrados)
    return sorted(set(all_mestrados))  # Garantir unicidade e ordenaçã

# Função para filtrar áreas e subáreas por curso
def filter_areas_subareas(df, course_column, area_column, subarea_column, selected_course):
    filtered_df = df[df[course_column].str.contains(selected_course, na=False, case=False)]
    areas_subareas = filtered_df[["Opção nº", area_column, subarea_column]].drop_duplicates()
    return areas_subareas


# Função para gerar relatório em PDF
class PDF(FPDF):
    def cell_with_wrapping(self, w, h, text, highlight=False):
        # Adiciona células que respeitam as margens automaticamente quebrando linhas
        if highlight:
            self.set_fill_color(255, 255, 0)  # Define o fundo amarelo
        if self.get_string_width(text) < w:
            self.cell(w, h, text.encode('latin-1', 'replace').decode('latin-1'), ln=True, fill=highlight)
        else:
            words = text.split()
            line = ""
            for word in words:
                if self.get_string_width(line + word) < w:
                    line += word + " "
                else:
                    self.cell(w, h, line.strip().encode('latin-1', 'replace').decode('latin-1'), ln=True, fill=highlight)
                    line = word + " "
            self.cell(w, h, line.strip().encode('latin-1', 'replace').decode('latin-1'), ln=True, fill=highlight)
        if highlight:
            self.set_fill_color(255, 255, 255)  # Reset para branco

def generate_pdf(data, filename, start_index, selected_course, marked_items={}):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do relatório
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Relatório de Vagas", ln=True, align="C")
    pdf.ln(10)

    # Curso selecionado
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(40, 10, txt="Curso de Graduação:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell_with_wrapping(150, 10, selected_course)
    pdf.ln(10)

    # Conteúdo do relatório
    for idx, row in enumerate(data.itertuples(), start=start_index):
        is_marked = marked_items.get(idx, False)  # Verificar se o item está marcado

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt=f"{idx}. Opção nº:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[1]}", highlight=is_marked)

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Área:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[2]}", highlight=is_marked)

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Subárea:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[3]}", highlight=is_marked)

        pdf.ln(5)

        # Adicionar separador (linha horizontal)
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(2)

    pdf.output(filename, dest="F")


def generate_pesquisador_pdf(data, filename, start_index, selected_course, selected_mestrado, marked_items):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do relatório
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Relatório de Vagas para Pesquisador", ln=True, align="C")
    pdf.ln(10)

    # Aviso
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Aviso:", ln=True)
    pdf.set_font("Arial", size=12)
    aviso_text = (
        "Este relatório de vagas foi elaborado com o objetivo de facilitar o processo "
        "de busca de vagas no edital. Recomenda-se, com base nas informações apresentadas, "
        "que os dados sejam verificados cuidadosamente, especialmente no momento da inscrição."
    )
    pdf.cell_with_wrapping(190, 10, aviso_text)
    pdf.ln(10)

    # Curso selecionado
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(40, 10, txt="Curso de Graduação:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell_with_wrapping(150, 10, selected_course)
    pdf.ln(10)

    if selected_mestrado != "Todos":
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(40, 10, txt="Mestrado Selecionado:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(150, 10, selected_mestrado)
        pdf.ln(10)

    # Conteúdo do relatório
    for idx, row in enumerate(data.itertuples(), start=start_index):
        is_marked = marked_items.get(idx, False)

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt=f"{idx}. Opção nº:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[1]}", highlight=is_marked)

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Área:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[2]}", highlight=is_marked)

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Subárea:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[3]}", highlight=is_marked)

        pdf.ln(5)

        # Adicionar separador (linha horizontal)
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(2)

    pdf.output(filename, dest="F")



# Caminho dos arquivos Excel
tecnico_file_path = "tecnico.xlsx"
analista_file_path = "Analista.xlsx"
pesquisador_file_path = "pesquisador.xlsx"

# Adicionar logo na barra lateral
st.sidebar.image(
    "images/logo_embrapa.jpg",  # Substitua pelo caminho correto da imagem
    use_column_width=True
)


# Interface do Streamlit
st.title("Consulta de Áreas e Subáreas por Cargo baseado na sua Formação")
st.markdown("**ATENÇÃO:** Há também as opções **Qualquer área de formação** e também **Qualquer área de formação de nível superior**")

# Carregar dados
tecnico_data = load_data(tecnico_file_path)
analista_data = load_data(analista_file_path)
pesquisador_data = load_data(pesquisador_file_path)

# Processar lista de cursos para ambas as planilhas
tecnico_courses = extract_courses(tecnico_data, "Nível Médio Técnico")
analista_courses = extract_courses(analista_data, "Graduação")
pesquisador_courses = extract_courses(pesquisador_data, "Graduação")
all_courses = sorted(set(analista_courses + pesquisador_courses))

# Extrair lista única de Mestrados
unique_mestrados = extract_unique_mestrados(pesquisador_data, "Mestrado")
st.header("Filtro para Analista")

# Lista suspensa para seleção de curso
selected_course = st.selectbox("Selecione uma formação de graduação:", all_courses)

if selected_course:
    # Filtrar áreas e subáreas para Analista
    analista_areas_subareas = filter_areas_subareas(analista_data, "Graduação", "Área", "Subárea", selected_course)

    marked_analista_items = {}

    with st.expander("Resultados para as vagas de Analista 🔎"):
        if not analista_areas_subareas.empty:
            st.markdown("### Marque as opções que você gostaria de dar destaque no relatório")

            # Criar as checkboxes para marcar os itens
            for idx, row in enumerate(analista_areas_subareas.itertuples(), start=1):
                marked_analista_items[idx] = st.checkbox(
                    f"{idx}. **Opção nº**: {row[1]}, **Área**: {row[2]}, **Subárea**: {row[3]}", value=False
                )
                st.write("---")

            # Botão para gerar o relatório em PDF
            if st.button("Gerar Relatório em PDF para Analista"):
                # Filtrar itens marcados
                filtered_marked_items = {idx: marked_analista_items[idx] for idx in marked_analista_items if
                                         marked_analista_items[idx]}

                # Gerar o PDF com itens destacados
                generate_pdf(
                    analista_areas_subareas,
                    "Relatorio_Analista.pdf",
                    start_index=1,
                    selected_course=selected_course,
                    marked_items=filtered_marked_items
                )
                st.success("Relatório gerado com sucesso! Faça o download abaixo.")
                with open("Relatorio_Analista.pdf", "rb") as pdf_file:
                    st.download_button(
                        label="Baixar Relatório PDF",
                        data=pdf_file,
                        file_name="Relatorio_Analista.pdf",
                        mime="application/pdf",
                    )
        else:
            st.write("Nenhuma área ou subárea encontrada para o curso")

            # Adicionar separador de seção
st.markdown("---")
st.header("Filtro para Pesquisador")

# Lista suspensa para seleção de curso específico para Pesquisador
selected_pesquisador_course = st.selectbox(
    "Selecione uma formação de graduação para Pesquisador:",
    pesquisador_courses
)

# Obter lista única de Mestrados
mestrados_list = pesquisador_data["Mestrado"].dropna().unique()
mestrados_list = sorted(mestrados_list)

# Lista suspensa para seleção de Mestrado
selected_mestrado = st.selectbox(
    "Selecione um Mestrado (opcional):",
    options=["Todos"] + unique_mestrados  # Adiciona "Todos" como opção padrão
)

if selected_pesquisador_course:
    pesquisador_filtered = pesquisador_data[
        pesquisador_data["Graduação"].str.contains(selected_pesquisador_course, na=False, case=False)
    ]
    if selected_mestrado != "Todos":
        pesquisador_filtered = pesquisador_filtered[
            pesquisador_filtered["Mestrado"].str.contains(selected_mestrado, na=False, case=False)
        ]

    pesquisador_areas_subareas = pesquisador_filtered[["Opção nº", "Área", "Subárea"]].drop_duplicates()

    # Dicionário para armazenar os itens marcados
    marked_items = {}

    with st.expander("Resultados para as vagas de Pesquisador 👩‍🔬"):
        if not pesquisador_areas_subareas.empty:
            st.write("**Resultados encontrados:**")
            # Criar as checkboxes e atualizar o estado do dicionário `marked_items`
            for idx, row in enumerate(pesquisador_areas_subareas.itertuples(), start=1):
                marked_items[idx] = st.checkbox(
                    f"{idx}. **Opção nº**: {row[1]}, **Área**: {row[2]}, **Subárea**: {row[3]}", value=False
                )
                st.write("---")

            # Gerar o PDF somente quando o botão for pressionado
            if st.button("Gerar Relatório em PDF para Pesquisador", key="pesquisador_pdf_button"):
                # Filtrar itens marcados
                filtered_marked_items = {
                    idx: marked_items[idx] for idx in marked_items if marked_items[idx]
                }

                # Gerar o PDF
                generate_pesquisador_pdf(
                    pesquisador_areas_subareas,
                    "Relatorio_Pesquisador.pdf",
                    start_index=1,
                    selected_course=selected_pesquisador_course,
                    selected_mestrado=selected_mestrado,
                    marked_items=filtered_marked_items,
                )

                # Exibir botão para download
                st.success("Relatório gerado com sucesso! Faça o download abaixo.")
                with open("Relatorio_Pesquisador.pdf", "rb") as pdf_file:
                    st.download_button(
                        label="Baixar Relatório PDF",
                        data=pdf_file,
                        file_name="Relatorio_Pesquisador.pdf",
                        mime="application/pdf",
                        key="pesquisador_pdf_download_button"
                    )
        else:
            st.write("Nenhum resultado encontrado para os filtros selecionados.")



# Adicionar separador de seção
st.markdown("---")

st.header("Filtro para Nível Médio Técnico")
# Lista suspensa para seleção de curso técnico
selected_tecnico_course = st.selectbox("Selecione uma formação de Nível Médio Técnico:", tecnico_courses)

if selected_tecnico_course:
    # Filtrar áreas e subáreas para Técnico
    tecnico_areas_subareas = filter_areas_subareas(
        tecnico_data,
        "Nível Médio Técnico",
        "Área",
        "Subárea",
        selected_tecnico_course
    )

    # Dicionário para armazenar os itens marcados
    marked_tecnico_items = {}

    with st.expander("Resultados para as vagas de Técnico 🛠️"):
        if not tecnico_areas_subareas.empty:
            st.markdown("### Marque as opções que você gostaria de dar destaque no relatório")

            # Criar as checkboxes para marcar os itens
            for idx, row in enumerate(tecnico_areas_subareas.itertuples(), start=1):
                marked_tecnico_items[idx] = st.checkbox(
                    f"{idx}. **Opção nº**: {row[1]}, **Área**: {row[2]}, **Subárea**: {row[3]}", value=False
                )
                st.write("---")

            # Botão para gerar o relatório em PDF
            if st.button("Gerar Relatório em PDF para Técnico"):
                # Filtrar itens marcados
                filtered_marked_items = {idx: marked_tecnico_items[idx] for idx in marked_tecnico_items if
                                         marked_tecnico_items[idx]}

                # Gerar o PDF com itens destacados
                generate_pdf(
                    tecnico_areas_subareas,
                    "Relatorio_Tecnico.pdf",
                    start_index=1,
                    selected_course=selected_tecnico_course,
                    marked_items=filtered_marked_items
                )
                st.success("Relatório gerado com sucesso! Faça o download abaixo.")
                with open("Relatorio_Tecnico.pdf", "rb") as pdf_file:
                    st.download_button(
                        label="Baixar Relatório PDF",
                        data=pdf_file,
                        file_name="Relatorio_Tecnico.pdf",
                        mime="application/pdf",
                    )
        else:
            st.write("Nenhuma área ou subárea encontrada para a formação técnica selecionada.")

