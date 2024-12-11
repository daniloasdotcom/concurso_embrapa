import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Concurso Embrapa 2024 - Busca de Vagas",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.sidebar.image(
    "images/logo_embrapa.jpg",  # Substitua pelo caminho correto da imagem
    use_column_width=True
)

# Título principal
st.title("🔍 Concurso Embrapa 2024 - Busca de Vagas")

# Subtítulo
st.subheader("Encontre facilmente as vagas disponíveis no concurso da Embrapa.")

# Descrição do concurso
st.markdown(
    """
    **Sobre o Concurso:**
    A Empresa Brasileira de Pesquisa Agropecuária (Embrapa) anunciou a abertura de 1.027 vagas para diversos cargos, incluindo assistente, técnico, analista e pesquisador. As inscrições estarão abertas de 16 de dezembro de 2024 a 7 de janeiro de 2025, e podem ser realizadas no site do Cebraspe.
    """
)

# Link para o edital
st.markdown(
    """
    [Clique aqui para acessar o edital completo](https://www.cebraspe.org.br/concursos/EMBRAPA_24)
    """
)

# Seção de busca de vagas
st.markdown("### Busque por vagas disponíveis")

# Campo de seleção de cargo
cargo = st.selectbox(
    "Selecione o cargo de interesse:",
    ["Assistente", "Técnico", "Analista", "Pesquisador"]
)

# Campo de seleção de região
regiao = st.selectbox(
    "Selecione a região desejada:",
    ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
)

# Botão de busca
if st.button("Buscar Vagas"):
    st.write(f"Exibindo vagas para o cargo de **{cargo}** na região **{regiao}**.")
    # Aqui você pode adicionar a lógica para buscar e exibir as vagas correspondentes

# Mensagem de apoio
st.markdown(
    """
    ---
    **Se este site foi útil para você, considere apoiá-lo fazendo um PIX:**
    """
)
