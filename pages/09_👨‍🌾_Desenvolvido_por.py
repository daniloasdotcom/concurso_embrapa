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

# Adicionar logo na barra lateral
st.sidebar.image(
    "images/logo_embrapa.jpg",  # Substitua pelo caminho correto da imagem
    use_column_width=True
)

# Título e subtítulo
st.title("Desenvolvido por")
st.subheader("[Danilo Andrade Santos](https://daniloas.com)")

# Lista de informações
st.markdown(
    """
    - **Agrônomo**  
    - **Gestor de IA**  
    - **Problem Solver**  
    - **Professor de Bioquímica**  
    - **Programador Jr. Web/Mobile**  
    - **Pesquisador em Produção Vegetal**  
    - **Cursando Análise e Desenvolvimento de Sistemas**  
    - **Analista de dados (Python, Excel/VBA, R)**  
    - **Cursando Especialização em IA na Agricultura**  
    """
)


# Ícones com links sutis
st.markdown(
    """
    <a href="https://www.instagram.com/daniloas.com_" target="_blank"><i class="fab fa-instagram"></i> Instagram</a><br>
    <a href="https://daniloas.com" target="_blank"><i class="fas fa-globe"></i> Website</a><br>
    <a href="https://www.linkedin.com/in/daniloandradesantos/" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a><br>
    <a href="https://github.com/daniloasdotcom" target="_blank"><i class="fab fa-github"></i> GitHub</a><br>
    <a href="mailto:danilo_as@live.com" target="_blank"><i class="fas fa-envelope"></i> danilo_as@live.com</a><br>
    """,
    unsafe_allow_html=True
)