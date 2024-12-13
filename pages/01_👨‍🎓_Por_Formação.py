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

# Função para filtrar áreas e subáreas por curso
def filter_areas_subareas(df, course_column, area_column, subarea_column, selected_course):
    filtered_df = df[df[course_column].str.contains(selected_course, na=False, case=False)]
    areas_subareas = filtered_df[["Opção nº", area_column, subarea_column]].drop_duplicates()
    return areas_subareas

# Função para gerar relatório em PDF
class PDF(FPDF):
    def cell_with_wrapping(self, w, h, text):
        # Adiciona células que respeitam as margens automaticamente quebrando linhas
        if self.get_string_width(text) < w:
            self.cell(w, h, text.encode('latin-1', 'replace').decode('latin-1'), ln=True)
        else:
            words = text.split()
            line = ""
            for word in words:
                if self.get_string_width(line + word) < w:
                    line += word + " "
                else:
                    self.cell(w, h, line.strip().encode('latin-1', 'replace').decode('latin-1'), ln=True)
                    line = word + " "
            self.cell(w, h, line.strip().encode('latin-1', 'replace').decode('latin-1'), ln=True)

def generate_pdf(data, filename, start_index, selected_course):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do relatório
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Relatório de Vagas para Analista", ln=True, align="C")
    pdf.ln(10)

    # Curso selecionado
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(40, 10, txt="Curso de Graduação:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell_with_wrapping(150, 10, selected_course)
    pdf.ln(10)

    # Conteúdo do relatório
    for idx, row in enumerate(data.itertuples(), start=start_index):
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt=f"{idx}. Opção nº:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[1]}")

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Área:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[2]}")

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Subárea:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[3]}")

        pdf.ln(5)

        # Adicionar separador (linha horizontal)
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Desenha uma linha horizontal
        pdf.ln(2)  # Espaço após a linha

    pdf.output(filename, dest="F")


# Função para gerar relatório em PDF para Pesquisador com separador
def generate_pesquisador_pdf(data, filename, start_index, selected_course):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Título do relatório
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Relatório de Vagas para Pesquisador", ln=True, align="C")
    pdf.ln(10)

    # Curso selecionado
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(40, 10, txt="Curso de Graduação:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell_with_wrapping(150, 10, selected_course)
    pdf.ln(10)

    # Conteúdo do relatório
    areas_subareas = data[["Opção nº", "Área", "Subárea"]].drop_duplicates()

    for idx, row in enumerate(areas_subareas.itertuples(), start=start_index):
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt=f"{idx}. Opção nº:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[1]}")

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Área:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[2]}")

        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(30, 10, txt="Subárea:", ln=False)
        pdf.set_font("Arial", size=12)
        pdf.cell_with_wrapping(160, 10, f"{row[3]}")

        # Adicionar informações de mestrados aceitos
        mestrados = data[
            (data["Área"] == row[2]) & (data["Subárea"] == row[3])
        ]["Mestrado"].dropna().unique()

        if mestrados.size > 0:
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(30, 10, txt="Mestrados:", ln=True)
            pdf.set_font("Arial", size=12)
            mestrados_list = "; ".join(mestrados)
            pdf.cell_with_wrapping(160, 10, mestrados_list)

        pdf.ln(5)

        # Adicionar separador (linha horizontal)
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Desenha uma linha horizontal
        pdf.ln(2)  # Espaço após a linha

    pdf.output(filename, dest="F")


# Caminho dos arquivos Excel
analista_file_path = "Analista.xlsx"
pesquisador_file_path = "Pesquisador.xlsx"

# Interface do Streamlit
st.title("Consulta de Áreas e Subáreas por Curso de Graduação")

# Carregar dados
analista_data = load_data(analista_file_path)
pesquisador_data = load_data(pesquisador_file_path)

# Processar lista de cursos para ambas as planilhas
analista_courses = extract_courses(analista_data, "Graduação")
pesquisador_courses = extract_courses(pesquisador_data, "Graduação")
all_courses = sorted(set(analista_courses + pesquisador_courses))

# Lista suspensa para seleção de curso
selected_course = st.selectbox("Selecione um curso de graduação:", all_courses)

if selected_course:
    # Filtrar áreas e subáreas para Analista
    analista_areas_subareas = filter_areas_subareas(analista_data, "Graduação", "Área", "Subárea", selected_course)

    with st.expander("Resultados para as vagas de Analista 🔎"):
        # Botão para gerar o relatório em PDF
        if st.button("Gerar Relatório em PDF"):
            generate_pdf(analista_areas_subareas, "Relatorio_Analista.pdf", start_index=1,
                         selected_course=selected_course)
            st.success("Relatório gerado com sucesso! Faça o download abaixo.")
            with open("Relatorio_Analista.pdf", "rb") as pdf_file:
                st.download_button(
                    label="Baixar Relatório PDF",
                    data=pdf_file,
                    file_name="Relatorio_Analista.pdf",
                    mime="application/pdf",
                )

        if not analista_areas_subareas.empty:
            st.write(
                f"Seu curso de graduação permite que você pleiteie cargos de **ANALISTA** nas seguintes áreas e subáreas:")
            for idx, row in enumerate(analista_areas_subareas.itertuples(), start=1):
                st.write(f"{idx}. **Opção nº**: {row[1]}, **Área**: {row[2]}, **Subárea**: {row[3]}")
                st.write("---")
        else:
            st.write("Nenhuma área ou subárea encontrada para o curso selecionado na vaga de Analista.")

    # Filtrar áreas, subáreas e mestrados para Pesquisador
    pesquisador_filtered = pesquisador_data[pesquisador_data["Graduação"].str.contains(selected_course, na=False, case=False)]
    pesquisador_areas_subareas = pesquisador_filtered[["Opção nº", "Área", "Subárea"]].drop_duplicates()

    # Expander para resultados de Pesquisador
    with st.expander("Resultados para as vagas de Pesquisador 👩‍🔬"):
        if not pesquisador_areas_subareas.empty:
            # Botão para gerar o relatório em PDF
            if st.button("Gerar Relatório em PDF para Pesquisador"):
                generate_pesquisador_pdf(pesquisador_filtered, "Relatorio_Pesquisador.pdf", start_index=1, selected_course=selected_course)

                st.success("Relatório de Pesquisador gerado com sucesso! Faça o download abaixo.")
                with open("Relatorio_Pesquisador.pdf", "rb") as pdf_file:
                    st.download_button(
                        label="Baixar Relatório PDF",
                        data=pdf_file,
                        file_name="Relatorio_Pesquisador.pdf",
                        mime="application/pdf",
                    )

            st.write(
                f"Seu curso de graduação permite que você pleiteie cargos de **PESQUISADOR** nas seguintes áreas e subáreas:")
            for idx, row in enumerate(pesquisador_areas_subareas.itertuples(), start=1):
                st.write(f"{idx}. **Opção nº**: {row[1]}, **Área**: {row[2]}, **Subárea**: {row[3]}")
                mestrados = pesquisador_filtered[
                    (pesquisador_filtered["Área"] == row[2]) & (pesquisador_filtered["Subárea"] == row[3])
                    ]["Mestrado"].dropna().unique()
                if mestrados.size > 0:
                    mestrados_list = "; ".join(mestrados)
                    st.write(f"   **Mestrados aceitos para o cargo:** {mestrados_list}")
                st.write("---")
        else:
            st.write("Nenhuma área, subárea ou mestrado encontrado para o curso selecionado na vaga de Pesquisador.")

