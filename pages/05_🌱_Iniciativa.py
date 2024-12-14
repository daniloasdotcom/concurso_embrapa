import streamlit as st

# Configurações da página
st.set_page_config(page_title="Desenvolvido por Danilo Andrade Santos", layout="centered")

# Adicionando Font Awesome para ícones
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)
# Título e subtítulo
st.title("Uma iniciativa")
st.subheader("Questões Agro")

# Adicionar logo na barra lateral
st.sidebar.image(
    "images/logo_embrapa.jpg",  # Substitua pelo caminho correto da imagem
    use_column_width=True
)

# Adicionar imagem no corpo principal entre colunas
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.image(
        "images/QuestoesAgro.png",  # Substitua pelo caminho correto da imagem
        use_column_width=True
    )
with col2:
    st.empty()
with col3:
    st.empty()


# Lista de informações
st.markdown(
    """
    Seu Perfil no Instagram que lhe ensina através de questões!
    """
)

# Ícones com links sutis
st.markdown(
    """
    <a href="https://www.instagram.com/questoesagro/" target="_blank"><i class="fab fa-instagram"></i> Questões Agro</a><br>
    """,
    unsafe_allow_html=True
)

# Adicionar imagem no corpo principal entre colunas
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.image(
        "images/codigo_agro.png",  # Substitua pelo caminho correto da imagem
        use_column_width=True
    )
with col2:
    st.empty()
with col3:
    st.empty()


# Lista de informações
st.markdown(
    """
    Vem conosco!!
    """
)

# Ícones com links sutis
st.markdown(
    """
    <a href="https://www.instagram.com/codigo.agro/" target="_blank"><i class="fab fa-instagram"></i> Código Agro🌱 </a><br>
    """,
    unsafe_allow_html=True
)
