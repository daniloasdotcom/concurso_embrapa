import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import LocateControl

# Configuração da página
st.set_page_config(page_title="Vagas por Subárea", page_icon="📋")

# Adicionar logo na barra lateral
st.sidebar.image(
    "images/logo_embrapa.jpg",  # Substitua pelo caminho correto da imagem
    use_column_width=True
)

# Carregar o dataset
def load_data():
    file_path = '../concurso_embrapa/assistente.xlsx'  # Substitua pelo caminho correto
    data = pd.read_excel(file_path)
    return data

data = load_data()

localidades_coordenadas = {
    "EMBRAPA AGROBIOLOGIA – Seropédica/RJ": (-22.7458, -43.7092),
    "EMBRAPA AGROENERGIA – Brasília/DF": (-15.7942, -47.8825),
    "EMBRAPA AGROINDÚSTRIA DE ALIMENTOS – Rio de Janeiro/RJ": (-22.9068, -43.1729),
    "EMBRAPA AGROINDÚSTRIA TROPICAL – Fortaleza/CE": (-3.7172, -38.5433),
    "EMBRAPA AGROPECUÁRIA OESTE – Dourados/MS": (-22.2233, -54.8083),
    "EMBRAPA AGROSSILVIPASTORIL – Sinop/MT": (-11.8639, -55.5167),
    "EMBRAPA AGRICULTURA DIGITAL – Campinas/SP": (-22.9099, -47.0626),
    "EMBRAPA ALIMENTOS E TERRITÓRIOS – Maceió/AL": (-9.6662, -35.7356),
    "EMBRAPA ALGODÃO – Barbalha/CE": (-7.3655, -39.2883),
    "EMBRAPA ALGODÃO – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA ALGODÃO – Campina Grande/PB": (-7.2172, -35.8811),
    "EMBRAPA ALGODÃO – Irecê/BA": (-11.3033, -41.8553),
    "EMBRAPA ALGODÃO – Luis Eduardo Magalhães/BA": (-12.0967, -45.7869),
    "EMBRAPA ALGODÃO – Palmas/TO": (-10.1692, -48.3308),
    "EMBRAPA ALGODÃO – Sinop/MT": (-11.8639, -55.5167),
    "EMBRAPA ALGODÃO – Santo Antônio de Goiás": (-16.4833, -49.3000),
    "EMBRAPA AMAZÔNIA OCIDENTAL – Iranduba/AM": (-3.1025, -59.4558),
    "EMBRAPA AMAZÔNIA OCIDENTAL – Manaus/AM": (-3.1190, -60.0217),
    "EMBRAPA AMAZÔNIA OCIDENTAL – Maués/AM": (-3.3400, -57.6989),
    "EMBRAPA AMAZÔNIA OCIDENTAL – Parintins/AM": (-2.5681, -56.7236),
    "EMBRAPA AMAZÔNIA OCIDENTAL – Rio Preto da Eva/AM": (-3.1442, -59.1192),
    "EMBRAPA AMAZÔNIA ORIENTAL – Belém/PA": (-1.4558, -48.5044),
    "EMBRAPA ACRE – Cruzeiro do Sul/AC": (-7.6303, -72.6727),
    "EMBRAPA ACRE – Rio Branco/AC": (-9.9753, -67.8106),
    "EMBRAPA ARROZ E FEIJÃO – Palmas/TO": (-10.1692, -48.3308),
    "EMBRAPA ARROZ E FEIJÃO – Santo Antônio de Goiás/GO": (-16.4833, -49.3000),
    "EMBRAPA ARROZ E FEIJÃO – Sinop/MT": (-11.8639, -55.5167),
    "EMBRAPA CLIMA TEMPERADO – Pelotas/RS": (-31.7654, -52.3376),
    "EMBRAPA CERRADOS – Planaltina/DF": (-15.6100, -47.6536),
    "EMBRAPA COCAIS – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA COCAIS – São Luís/MA": (-2.5364, -44.3056),
    "EMBRAPA FLORESTAS – Colombo/PR": (-25.2927, -49.2231),
    "EMBRAPA GADO DE CORTE – Campo Grande/MS": (-20.4412, -54.6128),
    "EMBRAPA GADO DE LEITE – Juiz de Fora/MG": (-21.7667, -43.3500),
    "EMBRAPA HORTALIÇAS – Brasília/DF": (-15.7942, -47.8825),
    "EMBRAPA INSTRUMENTAÇÃO – São Carlos/SP": (-22.0064, -47.8972),
    "EMBRAPA MANDIOCA E FRUTICULTURA – Cruz das Almas/BA": (-12.6750, -39.1067),
    "EMBRAPA MEIO AMBIENTE – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA MEIO AMBIENTE – Jaguariúna/SP": (-22.7042, -47.0042),
    "EMBRAPA MEIO-NORTE – Parnaíba/PI": (-2.9083, -41.7769),
    "EMBRAPA MEIO-NORTE – Teresina/PI": (-5.0892, -42.8019),
    "EMBRAPA MILHO E SORGO – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA MILHO E SORGO – Nova Porteirinha/MG": (-19.4611, -44.2489),
    "EMBRAPA MILHO E SORGO – Sete Lagoas/MG": (-19.4611, -44.2489),
    "EMBRAPA PANTANAL – Corumbá/MS": (-19.0078, -57.6547),
    "EMBRAPA PECUÁRIA SUL – Bagé/RS": (-31.3289, -54.1019),
    "EMBRAPA PECUÁRIA SUDESTE – São Carlos/SP": (-22.0064, -47.8972),
    "EMBRAPA PESCAS E AQUICULTURA – Palmas/TO": (-10.1692, -48.3308),
    "EMBRAPA RONDÔNIA – Ouro Preto d´Oeste/RO": (-10.7250, -62.2500),
    "EMBRAPA RONDÔNIA – Porto Velho/RO": (-8.7608, -63.9025),
    "EMBRAPA RONDÔNIA – Vilhena/RO": (-12.7417, -60.1433),
    "EMBRAPA RORAIMA – Boa Vista/RR": (2.8250, -60.6750),
    "EMBRAPA SOJA – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA SOJA – Goiânia/GO": (-16.6833, -49.2536),
    "EMBRAPA SOJA – Londrina/PR": (-23.3045, -51.1696),
    "EMBRAPA SOJA – Ponta Grossa/PR": (-25.0045, -50.0187),
    "EMBRAPA SOLOS – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA SOLOS – Recife/PE": (-8.0476, -34.8770),
    "EMBRAPA SOLOS – Rio de Janeiro/RJ": (-22.9068, -43.1729),
    "EMBRAPA SUÍNOS E AVES – Concórdia/SC": (-27.2333, -51.9833),
    "EMBRAPA TABULEIROS COSTEIROS – Aracaju/SE": (-10.9472, -37.0731),
    "EMBRAPA TABULEIROS COSTEIROS – Rio Largo/AL": (-9.4841, -35.8443),
    "EMBRAPA TRIGO – Passo Fundo/RS": (-28.2622, -52.4083),
    "EMBRAPA UVA E VINHO – Bento Gonçalves/RS": (-29.1699, -51.5185),
    "EMBRAPA SEDE – Brasília/DF": (-15.7942, -47.8825),
    "EMBRAPA ARROZ E FEIJÃO – Alegrete/RS": (-29.7883, -55.7949),  # Coordenadas aproximadas
    "EMBRAPA GADO DE LEITE – Coronel Pacheco/MG": (-21.5597, -43.2583),  # Coordenadas aproximadas
    "EMBRAPA CLIMA TEMPERADO – Francisco Beltrão/RS": (-26.0792, -53.0577),  # Coordenadas aproximadas
    "EMBRAPA AMAZÔNIA OCIDENTAL – Itacoatiara/AM": (-3.1386, -58.4442),  # Coordenadas aproximadas
    "EMBRAPA AMAPÁ – Macapá/AP": (0.0342, -51.0694),  # Coordenadas aproximadas
    "EMBRAPA SEMIÁRIDO – Nossa Senhora da Glória/SE": (-10.2158, -37.4217),  # Coordenadas aproximadas
    "EMBRAPA SEMIÁRIDO – Petrolina/PE": (-9.3891, -40.5027),  # Coordenadas aproximadas
    "EMBRAPA CAPRINOS E OVINOS – Sobral/CE": (-3.6942, -40.3496),  # Coordenadas aproximadas
    "EMBRAPA TRIGO – Uberaba/MG": (-19.7472, -47.9312)
}

# Aplicação Streamlit
def main():
    st.title("Vagas para Assistente 🔎")
    st.subheader("Salário-base: R$ 2.186,19")

    # Filtro de áreas
    area_options = data['Área'].dropna().unique()
    selected_area = st.selectbox("Selecione a Área", options=["Selecionar Área"] + list(area_options))

    if selected_area == "Selecionar Área":
        st.write("Por favor, selecione uma Área para visualizar as Subáreas.")
        return

    # Botões de subárea
    subarea_options = data[data['Área'] == selected_area]['Subárea'].dropna().unique()
    st.write("**Subáreas Disponíveis:**")
    selected_subarea = None

    cols = st.columns(4)
    for i, subarea in enumerate(subarea_options):
        col = cols[i % len(cols)]
        if col.button(subarea):
            selected_subarea = subarea

    if not selected_subarea:
        st.write("Por favor, clique em uma Subárea para visualizar as informações.")
        return

    # Filtro de dados baseado nas seleções
    filtered_data = data[(data['Área'] == selected_area) & (data['Subárea'] == selected_subarea)]

    # Adicionar âncora HTML para a seção "Resultados Filtrados"
    st.markdown(
        """
        <a id="resultados-filtrados"></a>
        """,
        unsafe_allow_html=True
    )

    # Script de rolagem automática
    scroll_script = """
    <script>
        document.getElementById("resultados-filtrados").scrollIntoView({ behavior: 'smooth' });
    </script>
    """
    st.markdown(scroll_script, unsafe_allow_html=True)

    # Exibição dos resultados
    st.header("Resultados Filtrados")
    if filtered_data.empty:
        st.write("Nenhuma vaga encontrada para os filtros selecionados.")
    else:
        for _, vaga in filtered_data.iterrows():
            st.write(f"**Opção:** {vaga['Opção nº']}")
        st.write(f"**Área:** {selected_area}")
        st.write(f"**Subárea:** {selected_subarea}")
        st.write("---")

        localidades_series = filtered_data['Localidade'].dropna().str.split(';')
        localidades = [loc.strip() for sublist in localidades_series for loc in sublist]
        localidades = list(set(localidades))

        st.write("**LOCALIDADES:**")
        for localidade in localidades:
            st.write(f"- {localidade}")

        # Criar mapa com Folium
        m = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

        for localidade in localidades:
            if localidade in localidades_coordenadas:
                lat, lon = localidades_coordenadas[localidade]
                folium.Marker([lat, lon], popup=localidade).add_to(m)

        folium_static(m)
        st.write(
            "**A localização no mapa não indica o local exato de trabalho, apenas a cidade indicada no edital.**"
        )

        st.write("---")
        st.write("**VAGAS:**")
        for _, vaga in filtered_data.iterrows():
            st.write(f"- AC: {vaga['AC']}")
            st.write(f"- PcD: {vaga['PcD']}")
            st.write(f"- PPP: {vaga['PPP']}")
            st.write(f"- Total de Vagas: {vaga['Total de Vagas']}")

            # Verifica se há "*" em AC, PcD ou PPP e exibe a mensagem
            if "*" in str(vaga['AC']) or "*" in str(vaga['PcD']) or "*" in str(vaga['PPP']):
                st.write(
                    "*Devido ao quantitativo total de vagas, não haverá reserva para provimento imediato, mantendo-se, portanto, o cadastro de reserva.")
            st.write("---")

        st.write("**REQUISITOS**")
        for _, vaga in filtered_data.iterrows():

            st.write("**Assistente:**")
            for nivel_tecnico in vaga['Requisitos'].split(';'):
                st.write(f"- {nivel_tecnico.strip()}")

            st.write("---")
            st.write("**DESCRIÇÃO ESPECÍFICA DAS ATIVIDADES DO CARGO:**")
            st.write(
                f"<p style='text-align: justify;'>{vaga['Descrição específica das atividade do cargo'].capitalize()}</p>",
                unsafe_allow_html=True
            )
            st.write("---")

    st.header("Assuntos cobrados")
    st.subheader("Em breve descreveremos aqui")
    st.markdown("""
        1.Em breve descreveremos aqui
        """)

# Adicionar CSS personalizado
st.markdown(
    """
    <style>
    .stButton>button {
        border: 2px solid blue;
    }
    .stButton>button:focus, .stButton>button:hover {
        background-color: #90EE90;
        color: black;
        border: 2px solid blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
