import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Dados dos estados brasileiros e Distrito Federal com coordenadas centrais
estados_coordenadas = {
    "BR": [-14.2350, -53.9253],
    "AC": [-9.0238, -70.8111],
    "AL": [-9.5713, -36.7819],
    "AP": [0.9020, -52.0030],
    "AM": [-3.4168, -65.8561],
    "BA": [-12.5797, -41.7007],
    "CE": [-5.2030, -39.2845],
    "DF": [-15.8267, -47.9218],
    "ES": [-19.1834, -40.3089],
    "GO": [-15.8270, -49.8362],
    "MA": [-5.4186, -45.0732],
    "MT": [-12.6819, -56.9211],
    "MS": [-20.7722, -54.7852],
    "MG": [-18.5122, -44.5550],
    "PA": [-4.7407, -52.1835],
    "PB": [-7.2399, -36.7813],
    "PR": [-25.2521, -52.0216],
    "PE": [-8.8137, -36.9541],
    "PI": [-7.7183, -42.7289],
    "RJ": [-22.9068, -43.1729],
    "RN": [-5.4026, -36.9541],
    "RS": [-30.0346, -51.2177],
    "RO": [-10.9436, -62.8278],
    "RR": [2.7376, -61.3072],
    "SC": [-27.2423, -50.2189],
    "SP": [-23.5505, -46.6333],
    "SE": [-10.5741, -37.3857],
    "TO": [-10.1753, -48.2982]
}

# Dados das cidades e suas coordenadas
localidades_coordenadas = {
    "Aracaju/SE": (-10.9472, -37.0731),
    "Bagé/RS": (-31.3289, -54.1019),
    "Belo Horizonte/MG": (-19.9167, -43.9345),
    "Belém/PA": (-1.4558, -48.5044),
    "Bento Gonçalves/RS": (-29.1699, -51.5185),
    "Boa Vista/RR": (2.8235, -60.6758),
    "Brasília/DF": (-15.7942, -47.8825),
    "Campina Grande/PB": (-7.2306, -35.8811),
    "Campinas/SP": (-22.9099, -47.0626),
    "Campo Grande/MS": (-20.4697, -54.6201),
    "Colombo/PR": (-25.2927, -49.2231),
    "Concórdia/SC": (-27.2333, -51.9833),
    "Corumbá/MS": (-19.0078, -57.6547),
    "Cruz das Almas/BA": (-12.6750, -39.1067),
    "Cuiabá/MT": (-15.6014, -56.0979),
    "Curitiba/PR": (-25.4296, -49.2713),
    "Dourados/MS": (-22.2233, -54.8083),
    "Florianópolis/SC": (-27.5954, -48.5480),
    "Fortaleza/CE": (-3.7172, -38.5433),
    "Goiânia/GO": (-16.6869, -49.2648),
    "Jaguariúna/SP": (-22.7033, -46.9858),
    "João Pessoa/PB": (-7.1195, -34.8450),
    "Juiz de Fora/MG": (-21.7612, -43.3496),
    "Londrina/PR": (-23.3045, -51.1696),
    "Macapá/AP": (0.0349, -51.0694),
    "Maceió/AL": (-9.6498, -35.7089),
    "Manaus/AM": (-3.1190, -60.0217),
    "Natal/RN": (-5.7945, -35.2110),
    "Palmas/TO": (-10.2406, -48.3558),
    "Passo Fundo/RS": (-28.2622, -52.4083),
    "Pelotas/RS": (-31.7649, -52.3371),
    "Petrolina/PE": (-9.3891, -40.5033),
    "Porto Alegre/RS": (-30.0346, -51.2177),
    "Porto Velho/RO": (-8.7608, -63.9025),
    "Recife/PE": (-8.0476, -34.8770),
    "Rio Branco/AC": (-9.9753, -67.8241),
    "Rio de Janeiro/RJ": (-22.9068, -43.1729),
    "Salvador/BA": (-12.9714, -38.5014),
    "Santo Antônio de Goiás/GO": (-16.4847, -49.3153),
    "Seropédica/RJ": (-22.7443, -43.7156),
    "Sete Lagoas/MG": (-19.4566, -44.2414),
    "Sinop/MT": (-11.8642, -55.5039),
    "Sobral/CE": (-3.6894, -40.3482),
    "São Carlos/SP": (-22.0074, -47.8972),
    "São Luís/MA": (-2.5307, -44.3068),
    "São Paulo/SP": (-23.5505, -46.6333),
    "Teresina/PI": (-5.0892, -42.8019),
    "Vitória/ES": (-20.3155, -40.3128)
}

# Dados dos locais de aplicação da prova prática
locais_prova_pratica = {
    "Embrapa Acre": {
        "endereco": "Rodovia BR-364, Km 14 (Rio Branco/Porto Velho), CEP: 69900-970 - Rio Branco – AC",
        "geolocalizacao": [-9.9753, -67.8241],
    },
    "Embrapa Amazônia Oriental": {
        "endereco": "Travessa Dr. Enéas Pinheiro s/n, Bairro do Marco, CEP: 66095-903 - Belém – PA",
        "geolocalizacao": [-1.4558, -48.5044],
    },
    "Embrapa Cerrados": {
        "endereco": "CTZL - Rod. DF 180 S/N, KM 64 - CEP: 72668-900 Recanto das Emas – DF",
        "geolocalizacao": [-15.7942, -47.8825],
    },
    "Embrapa Cocais": {
        "endereco": "São Luís MA - End. Rua dos Cúrios S/N IFMA Campus São Luís Maracanã",
        "geolocalizacao": [-2.5307, -44.3068],
    },
    "Embrapa Gado de Leite": {
        "endereco": "Campo Experimental José Henrique Bruschi - ROD MG 133, S/N, KM 42, CEP: 36.155-000, Zona Rural, Coronel Pacheco - MG",
        "geolocalizacao": [-21.7612, -43.3496],
    },
    "Embrapa Milho e Sorgo": {
        "endereco": "Rodovia MG 424, Km 45 - CEP: 35.702-098 - Sete Lagoas - Área Rural, MG",
        "geolocalizacao": [-19.4566, -44.2414],
    },
    "Embrapa Pantanal": {
        "endereco": "Rua 21 de Setembro, 1880, Bairro Nossa Senhora de Fátima, CEP 79320-900 Corumbá, MS",
        "geolocalizacao": [-19.0078, -57.6547],
    },
    "Embrapa Pecuária Sul": {
        "endereco": "Rodovia BR-153, Km 632,9 Vila Industrial, Zona Rural, Caixa Postal 242, CEP: 96401-970, Bagé, RS",
        "geolocalizacao": [-31.3289, -54.1019],
    },
    "Embrapa Recursos Genéticos": {
        "endereco": "Campo Experimental Fazenda Sucupira, Quadra QC 06, etapa 2A, conjunto 28, final, Fazenda Sucupira, Riacho Fundo 2, CEP 71882-277",
        "geolocalizacao": [-15.8270, -49.8362],
    },
    "Embrapa Rondônia": {
        "endereco": "Rodovia BR 364 Km 55 Zona Rural C.P 127 - 76815-800 Porto Velho, Rondônia",
        "geolocalizacao": [-8.7608, -63.9025],
    },
    "Embrapa Semiárido": {
        "endereco": "Rodovia BR 428, Km 152, Zona Rural. Petrolina-PE",
        "geolocalizacao": [-9.3891, -40.5033],
    },
    "Embrapa Suíno e Aves": {
        "endereco": "Rodovia BR-153, Km 110, Distrito de Tamanduá - Concórdia – SC",
        "geolocalizacao": [-27.2333, -51.9833],
    },
    "Embrapa Tabuleiros Costeiros": {
        "endereco": "Av. Gov. Paulo Barreto de Menezes, nº 3.250 - Jardins, Aracaju - SE, 49025-040",
        "geolocalizacao": [-10.9472, -37.0731],
    },
}

# Dados dos locais de aplicação da prova prática
locais_prova_pratica_40001925 = {
    "Embrapa Acre": {
        "endereco": "Rodovia BR-364, Km 14 (Rio Branco/Porto Velho), CEP: 69900-970 - Rio Branco – AC",
        "geolocalizacao": [-9.9753, -67.8241],
    },
    "Embrapa Amazônia Oriental": {
        "endereco": "Travessa Dr. Enéas Pinheiro s/n, Bairro do Marco, CEP: 66095-903 - Belém – PA",
        "geolocalizacao": [-1.4558, -48.5044],
    },
    "Embrapa Roraima": {
        "endereco": "Campo Experimental do Confiança - Vila Central - Vicinal 03 - Confiança 3 - Cantá - RR CEP: 69390-000",
        "geolocalizacao": [2.249166, -60.6783],
    },
}

# Dados dos locais de aplicação da prova prática para OPÇÃO 40000007
locais_prova_pratica_40000007 = {
    "Embrapa Acre": {
        "endereco": "Rodovia BR-364, Km 14 (Rio Branco/Porto Velho), CEP: 69900-970 - Rio Branco – AC",
        "geolocalizacao": [-9.9753, -67.8241],
        "link_mapa": "https://maps.app.goo.gl/i8Ee49xvpj18W6RU8",
    },
    "Embrapa Amazônia Oriental": {
        "endereco": "Travessa Dr. Enéas Pinheiro s/n, Bairro do Marco, CEP: 66095-903 - Belém – PA",
        "geolocalizacao": [-1.4558, -48.5044],
        "link_mapa": "https://maps.app.goo.gl/k9XCCABiAoegeE3j8",
    },
    "Embrapa Caprinos e Ovinos": {
        "endereco": "Rodovia Moésio Loiola de Melo Júnior, km 4, Fazenda Três Lagoas/Salgado dos Machados CEP 62103-905 - Sobral, CE",
        "geolocalizacao": [-3.6892, -40.3497],
        "link_mapa": "https://maps.app.goo.gl/xdsb39hx8pZGZXAeA",
    },
    "Embrapa Cerrados": {
        "endereco": "CTZL - Rod. DF 180 S/N, KM 64 - CEP: 72668-900 Recanto das Emas – DF",
        "geolocalizacao": [-15.6044, -47.7399],
        "link_mapa": "https://maps.app.goo.gl/NeCxHS2giZrUR4dm6",
    },
    "Embrapa Clima Temperado": {
        "endereco": "Estação Experimental de Terras Baixas – ETB, Campos Universitário, Capão Leão – RS, CEP 96160-000",
        "geolocalizacao": [-31.8002, -52.4842],
        "link_mapa": "https://maps.app.goo.gl/KsNXCPiXhFuj3J4m8",
    },
    "Embrapa Gado de Corte": {
        "endereco": "Avenida Radio Maia, 830 - Vila Popular - CEP 79.106-550; Telefone (67) 3368-2000 Campo Grande, MS",
        "geolocalizacao": [-20.4697, -54.6458],
        "link_mapa": "https://maps.app.goo.gl/YG8Wa4uZYmE4939C9",
    },
    "Embrapa Gado de Leite": {
        "endereco": "Campo Experimental José Henrique Bruschi - ROD MG 133, S/N, KM 42, CEP: 36.155-000, Zona Rural, Coronel Pacheco - MG",
        "geolocalizacao": [-21.5292, -43.2583],
        "link_mapa": "https://maps.app.goo.gl/yB1g3wXC1xqVKrgXA",
    },
    "Embrapa Milho e Sorgo": {
        "endereco": "Rodovia MG 424, km 65, Zona Rural, CEP 35.701-970, Sete Lagoas, MG",
        "geolocalizacao": [-19.4564, -44.2267],
        "link_mapa": "https://maps.app.goo.gl/mhMYL83FqriCmqYU7",
    },
    "Embrapa Pantanal": {
        "endereco": "Rua 21 de Setembro, 1880, Bairro Nossa Senhora de Fátima, CEP 79320-900 Corumbá, MS",
        "geolocalizacao": [-19.0091, -57.6523],
        "link_mapa": "https://maps.app.goo.gl/rCLk72fKyREP3mWi8",
    },
    "Embrapa Pecuária Sudeste": {
        "endereco": "Rodovia Washingtom Luiz, km 234, CP339, CEP 13.560-970, São Carlos, SP. Portaria Estr. Mun. Guilherme Scatena, km 3,5 - Água Vermelha, Zona Rural, São Carlos - SP",
        "geolocalizacao": [-22.0167, -47.8906],
        "link_mapa": "https://maps.app.goo.gl/Fsxg1Uov5j3voRx4A",
    },
    "Embrapa Semiárido": {
        "endereco": "Rodovia BR 428, Km 152, Zona Rural, Petrolina-PE",
        "geolocalizacao": [-9.3891, -40.5026],
        "link_mapa": "https://maps.app.goo.gl/E2HxjDfNg2pApPL69",
    },
    "Embrapa Suínos e Aves": {
        "endereco": "Rodovia BR-153, Km 110, Distrito de Tamanduá - Concórdia – SC",
        "geolocalizacao": [-27.2346, -52.0222],
        "link_mapa": "https://maps.app.goo.gl/cQy2ZsQYpA51D5vb6",
    },
    "Embrapa Tabuleiros Costeiros": {
        "endereco": "Av. Gov. Paulo Barreto de Menezes, nº 3250 - Jardins, Aracaju - SE, 49025-040",
        "geolocalizacao": [-10.9472, -37.0731],
        "link_mapa": "https://maps.app.goo.gl/TBLkskVjAJKeVWrU9",
    },
}

# Título e instrução
st.title("Locais de provas")

# Inicializando o estado da sessão
if "estado_selecionado" not in st.session_state:
    st.session_state.estado_selecionado = "BR"
    st.session_state.centro_mapa = estados_coordenadas["BR"]
    st.session_state.zoom_mapa = 4

# Expander para Locais de Provas Objetivas
with st.expander("Locais de Provas Objetivas"):
    st.title("Locais de provas")
    st.markdown("**LOCAIS DE PROVAS OBJETIVAS E DISCURSIVA, BEM COMO DA AVALIAÇÃO BIOPSICOSSOCIAL E DO PROCEDIMENTO DE HETEROIDENTIFICAÇÃO**")

    # Botões organizados em colunas
    colunas = st.columns(10)
    for i, estado in enumerate(estados_coordenadas.keys()):
        if colunas[i % 10].button(estado, key=f"botao_{estado}"):
            st.session_state.estado_selecionado = estado
            st.session_state.centro_mapa = estados_coordenadas[estado]
            st.session_state.zoom_mapa = 4 if estado == "BR" else 6

    # Configurando o mapa
    mapa = folium.Map(location=st.session_state.centro_mapa, zoom_start=st.session_state.zoom_mapa)

    # Adicionando os marcadores de todas as cidades
    for cidade, (lat, lon) in localidades_coordenadas.items():
        folium.Marker(
            location=[lat, lon],
            popup=cidade,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(mapa)

    # Renderizando o mapa no Streamlit
    st_folium(mapa, width=800, height=600, key="mapa_locais_provas")


# Expander para Prova Prática: Manejo Animal
with st.expander("Locais de Aplicação da Prova Prática - Manejo Animal"):
    st.title("Locais de Aplicação da Prova Prática")
    st.markdown("**OPÇÃO:** 40000007: **TÉCNICO**")
    st.markdown("**ÁREA:** LABORATÓRIO E CAMPOS EXPERIMENTAIS")
    st.markdown("**SUBÁREA:** MANEJO ANIMAL")
    st.markdown("**Confira os locais de aplicação da prova prática com seus endereços e geolocalizações.**")

    # Configurando o mapa
    mapa = folium.Map(location=st.session_state.centro_mapa, zoom_start=st.session_state.zoom_mapa)

    # Adicionando os marcadores dos locais
    for local, dados in locais_prova_pratica_40000007.items():
        endereco = dados["endereco"]
        lat, lon = dados["geolocalizacao"]
        folium.Marker(
            location=[lat, lon],
            popup=f"<b>{local}</b><br>{endereco}",
            icon=folium.Icon(color="green", icon="info-sign")
        ).add_to(mapa)

    # Renderizando o mapa no Streamlit
    st_folium(mapa, width=800, height=600, key="mapa_manejo_animal")


# Expander para Prova Prática: Manejo Florestal
with st.expander("Locais de Aplicação da Prova Prática - Manejo Florestal"):
    st.title("Locais de Aplicação da Prova Prática")
    st.markdown("**OPÇÃO:** 40001925: **TÉCNICO**")
    st.markdown("**ÁREA:** LABORATÓRIO E CAMPOS EXPERIMENTAIS")
    st.markdown("**SUBÁREA:** MANEJO FLORESTAL")
    st.markdown("**Confira os locais de aplicação da prova prática com seus endereços e geolocalizações.**")

    # Configurando o mapa
    mapa = folium.Map(location=st.session_state.centro_mapa, zoom_start=st.session_state.zoom_mapa)

    # Adicionando os marcadores dos locais
    for local, dados in locais_prova_pratica_40001925.items():
        endereco = dados["endereco"]
        lat, lon = dados["geolocalizacao"]
        folium.Marker(
            location=[lat, lon],
            popup=f"<b>{local}</b><br>{endereco}",
            icon=folium.Icon(color="green", icon="info-sign")
        ).add_to(mapa)

    # Renderizando o mapa no Streamlit
    st_folium(mapa, width=800, height=600, key="mapa_manejo_florestal")




