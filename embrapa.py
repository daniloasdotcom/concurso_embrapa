import streamlit as st
import pandas as pd
import pydeck as pdk

# Dados das capitais brasileiras
capitais = {
    "Cidade": [
        "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", "Vitória", "Goiânia", "São Luís",
        "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro",
        "Natal", "Porto Alegre", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"
    ],
    "Latitude": [
        -9.974, -9.648, 0.034, -3.119, -12.971, -3.717, -15.793, -20.315, -16.686, -2.538,
        -15.601, -20.448, -19.917, -1.455, -7.115, -25.428, -8.047, -5.091, -22.906,
        -5.794, -30.031, 2.823, -27.595, -23.550, -10.916, -10.184
    ],
    "Longitude": [
        -67.809, -35.713, -51.070, -60.021, -38.501, -38.542, -47.882, -40.337, -49.264, -44.282,
        -56.097, -54.629, -43.935, -48.504, -34.863, -49.267, -34.878, -42.801, -43.172,
        -35.211, -51.227, -60.675, -48.548, -46.633, -37.062, -48.327
    ]
}

# Converter para DataFrame
df = pd.DataFrame(capitais)

# Configuração do Streamlit
st.set_page_config(page_title="Mapa das Capitais do Brasil", layout="wide")

# Título
st.title("Mapa Interativo das Capitais do Brasil")

# Exibir o mapa
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v10",
        initial_view_state=pdk.ViewState(
            latitude=-14.235,  # Latitude média do Brasil
            longitude=-51.925, # Longitude média do Brasil
            zoom=4
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position="[Longitude, Latitude]",
                get_color="[200, 30, 0, 160]",
                get_radius=100000,
            )
        ]
    )
)

# Tabela de dados
st.subheader("Tabela de Capitais")
st.dataframe(df)
