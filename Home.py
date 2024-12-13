import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Concurso Embrapa 2024 - Busca de Vagas",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .rounded-image {
        border-radius: 15px;
    }
    .centered-text {
        text-align: center;
    }
    .icon-link {
        display: flex;
        align-items: center;
        text-decoration: none;
        color: inherit;
    }
    .icon-link i {
        margin-right: 8px;
    }
    .stButton>button {
        border: 2px solid blue; /* Adicionar borda azul */
        font-size: 14px; /* Diminuir o tamanho da fonte */
    }
    .stButton>button:focus, .stButton>button:hover {
        background-color: #90EE90; /* Verde mais claro */
        color: black; /* Garantir que a cor da fonte permaneça preta */
        border: 2px solid blue; /* Manter a borda azul */
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #eff2f6; /* Cor da barra lateral */
        color: black;
        text-align: center;
        padding: 10px;
    }
    .footer a {
        margin: 0 10px;
        color: inherit;
        text-decoration: none;
    }
    .footer a:hover {
        color: #007BFF;
    }
    /* Estilização da barra lateral */
    .css-1d391kg {
        background-color: #eff2f6; /* Cor da barra lateral */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título "Filtro de Vagas" centralizado
st.markdown("<h1 class='centered-text'>🔎 Filtro de Vagas</h1>", unsafe_allow_html=True)

# Criar duas colunas para centralizar a imagem
col1, col2, col3 = st.columns([1, 2, 1])

# Adicionar a imagem na coluna do meio
with col2:
    st.markdown("<h2 class='centered-text'>Concurso</h2>", unsafe_allow_html=True)
    st.image("images/logo_home.jpg", use_column_width=True)

# Subtítulo
st.markdown("<h3 class='centered-text'>Acesse as opções da barra lateral para encontrar as vagas disponíveis no concurso da Embrapa.</h3>", unsafe_allow_html=True)

# Descrição do concurso
st.markdown(
    """
    **Sobre o Concurso:**
    """
)

# Descrição do concurso
st.markdown(
    """
    A Empresa Brasileira de Pesquisa Agropecuária (Embrapa) anunciou a abertura de 1.027 vagas para diversos cargos, incluindo assistente, técnico, analista e pesquisador. As inscrições estarão abertas de 16 de dezembro de 2024 a 7 de janeiro de 2025, e podem ser realizadas no site do Cebraspe.
    """
)

# Título "Concurso Embrapa"
st.markdown("### Links úteis")

# Link para o edital
st.markdown(
    """
    [Acesse a página do concurso na Cebraspe](https://www.cebraspe.org.br/concursos/EMBRAPA_24)

    [Saiba mais sobre o concurso no site da Embrapa](https://www.embrapa.br/concurso-2024)
    """
)

# Mensagem de apoio
st.markdown(
    """
    ---
    """
)

# Título "Apoie esta ferramenta" com ícone
st.markdown(
    """
        <h3>🌱❤ Apoie esta ferramenta ❤🌱</h3>
    """,
    unsafe_allow_html=True
)

# Mensagem de apoio
st.markdown(
    """
    **Se este site foi útil para você, considere apoiá-lo fazendo um PIX:**
    """
)

# Trecho copiável para o Pix "daniloaa"
pix_info = "questoesagro@gmail.com"
st.code(pix_info, language="text")

# Adicionar Font Awesome para os ícones
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """,
    unsafe_allow_html=True
)

