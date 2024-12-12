import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Apoie-se - Concurso Embrapa 2024",
    page_icon="❤",
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

# Título "Apoie-se" centralizado
st.markdown("<h1 class='centered-text'>🌱❤ Apoie esta ferramenta ❤🌱</h1>", unsafe_allow_html=True)

# Mensagem de apoio
st.markdown(
    """
    **Se este site foi útil para você, considere apoiá-lo fazendo um PIX:**
    """
)

# Trecho copiável para o Pix "daniloaa"
pix_info = "danilo_as@live.com"
st.code(pix_info, language="text")

# Adicionar Font Awesome para os ícones
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# Mensagem de apoio
st.markdown(
    """
    <p>Siga-nos no Instagram para mais atualizações e conteúdos exclusivos:</p>
    <a href="https://www.instagram.com/questoesagro/" target="_blank">
        <i class="fab fa-instagram"></i> @questoesagro
    </a>
    """,
    unsafe_allow_html=True
)

# Adicionar rodapé com ícones de redes sociais
st.markdown(
    """
    <div class="footer">
        <p>Uma iniciativa Questões Agro</p>
        <a href="https://www.instagram.com/questoesagro/" target="_blank"><i class="fab fa-instagram"></i></a>
    </div>
    """,
    unsafe_allow_html=True
)
