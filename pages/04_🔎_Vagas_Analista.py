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
    file_path = '../concurso_embrapa/Analista.xlsx'  # Substitua pelo caminho correto
    data = pd.read_excel(file_path)
    return data

data = load_data()

conhecimentos_complementares = {
    "Ciência e Tecnologia de Alimentos": """
    1. Reações químicas durante o processamento e armazenamento dos alimentos.  
    2. Alterações químicas em alimentos devido a fatores ambientais.  
    3. Métodos de conservação de alimentos.  
    4. Efeito dos processos de conservação na qualidade sensorial e nutricional dos alimentos.  
    5. Desenvolvimento e aplicação de novas tecnologias de preservação.  
    6. Desenvolvimento de produtos.  
        6.1. Tecnologia de alimentos.  
        6.2. Bromatologia.  
        6.3. Legislação.  
        6.4. Rotulagem obrigatória e nutricional de alimentos.  
        6.5. Estudos de vida-útil.  
    7. Impacto dos processos tecnológicos na segurança alimentar e na qualidade dos produtos.  
    8. Relação entre transformações físico-químicas e propriedades finais dos alimentos e as técnicas para medir e controlar essas transformações.  
    9. Ingredientes para alimentos.  
        9.1. Macronutrientes.  
        9.2. Ingredientes para substituições.  
        9.3. Aditivos alimentares.  
        9.4. Probióticos.  
        9.5. Prebióticos.  
        9.6. Simbióticos.  
    10. Boas práticas de fabricação de alimentos.  
    11. Elaboração de procedimentos operacionais padrão.  
    12. Gestão de laboratórios, experimentos, instrumentação analítica e operação de equipamentos piloto com foco em ciência e tecnologia de alimentos.  
    13. Etapas e processos importantes para estabelecimento e padronização de protocolos experimentais com foco em ciência e tecnologia de alimentos.  
    14. Tecnologias de processamento de alimentos extrusados.  
    15. Física e química de alimentos: conceitos teóricos e processos analíticos.  
    16. Nutrição e alimentação de espécies aquícolas, engenharia e/ou ciência de alimentos, tecnologia de alimentos, zootecnia.  
    """,
    "Ciências Agrárias": """
    1. Administração rural.  
    2. Agricultura de precisão.  
    3. Economia e Política Agrícola.  
        3.1. Política agrícola brasileira e internacional.  
        3.2. Comercialização de produtos agrícolas.  
        3.3. Análise de custos de produção.  
        3.4. Cooperativismo e associativismo no setor agrícola.  
    4. Experimentação agrícola.  
    5. Entomologia.  
        5.1. Principais pragas de plantas cultivadas.  
        5.2. Métodos de controle de pragas e tecnologia de aplicação de defensivos.  
        5.3. Manejo integrado de pragas.  
    6. Fisiologia vegetal.  
        6.1. Água no sistema solo-planta-atmosfera.  
        6.2. Fotossíntese e respiração.  
        6.3. Absorção e translocação de solutos orgânicos e inorgânicos.  
        6.4. Efeitos da temperatura e da luz na planta.  
        6.5. Reguladores de crescimento.  
    7. Fitopatologia.  
        7.1. Conceitos básicos: histórico, sintomas, agentes fitopatogênicos, patogênese, epidemiologia.  
        7.2. Princípios gerais de controle.  
        7.3. Principais doenças de plantas e métodos de controle.  
        7.4. Fungicidas, nematicidas e bactericidas.  
        7.5. Biopesticidas.  
    8. Geoprocessamento.  
        8.1. Sistemas de sensoriamento remoto.  
        8.2. Sensores e produtos.  
        8.3. Interpretação de imagens.  
        8.4. Tomada, transmissão, armazenamento, processamento e interpretação de dados.  
        8.5. Georreferenciamento.  
        8.6. Aplicações de sensoriamento remoto no planejamento, monitoramento e controle dos recursos naturais e das atividades antrópicas.  
    9. Fisiologia vegetal e nutrição das plantas.  
        9.1. Processos fisiológicos das plantas e seu impacto no crescimento e produtividade.  
        9.2. Nutrientes essenciais e técnicas de fertilização.  
        9.3. Diagnóstico e manejo de deficiências nutricionais.  
    10. Mecanização agrícola.  
    11. Melhoramento genético de plantas.  
        11.1. Noções de melhoramento genético vegetal.  
        11.2. Métodos e técnicas de melhoramento vegetal.  
    12. Mudanças climáticas e agricultura.  
    13. Principais culturas agrícolas brasileiras: grãos, fibras, fruteiras, olerícolas, matérias-primas industriais, aspectos econômicos, características botânicas e agronômicas, exigências edafoclimáticas, técnicas de cultivo, pós-colheita e comercialização.  
    14. Sanidade animal.  
        14.1. Defesa sanitária animal.  
        14.2. Doenças parasitárias dos animais de produção.  
    15. Sistemas de produção agrícola.  
        15.1. Agroecologia.  
        15.2. Produção orgânica.  
        15.3. Agricultura familiar.  
        15.4. Sistemas integrados de produção.  
        15.5. Sistemas agroflorestais.  
    16. Solos.  
        16.1. Gênese, morfologia e classificação dos solos.  
        16.2. Física e química do solo.  
        16.3. Solos e nutrição de plantas.  
        16.4. Práticas de uso e manejo sustentável do solo.  
        16.5. Conservação do solo e água.  
        16.6. Recuperação de áreas degradadas.  
        16.7. Sistemas de cultivo e rotação de culturas.  
        16.8. Biofertilizantes.  
    17. Tecnologia pós-colheita de grãos e sementes: secagem, beneficiamento e armazenagem.  
    18. Zootecnia.  
        18.1. Agrostologia.  
        18.2. Boas práticas de produção agropecuária.  
        18.3. Nutrição e alimentação animal.  
        18.4. Sistemas de produção e manejo de animais.  
        18.5. Reprodução e melhoramento genético animal.  
        18.6. Sistemas de produção aquícola.  
        18.7. Qualidade da água em aquicultura.  
    """,
"Ciências Biológicas": """
1. Biodiversidade e ecologia.  
    1.1. Ecossistemas terrestres e aquáticos.  
    1.2. Conservação da biodiversidade.  
    1.3. Biodiversidade brasileira.  
2. Bioeconomia.  
3. Bioinsumos para agropecuária.  
4. Biologia celular e molecular.  
    4.1. Estrutura e função da célula.  
    4.2. Biologia molecular e genética.  
    4.3. Biotecnologia e engenharia genética.  
5. Engenharia de bioprocessos e biotecnologia.  
6. Ferramentas e métodos de prospecção de genes.  
7. Fisiologia vegetal.  
8. Ecofisiologia vegetal.  
9. Genética.  
    9.1. Genética clássica e molecular.  
    9.2. Genética quantitativa.  
    9.3. Genética de populações.  
    9.4. Genética animal.  
    9.5. Genética de microrganismos.  
    9.6. Genética quantitativa e estatística genética.  
10. Ciências ômicas.  
    10.1. Proteômica.  
    10.2. Transcriptômica.  
    10.3. Metabolômica.  
11. Melhoramento genético de plantas.  
    11.1. Noções de melhoramento genético vegetal.  
    11.2. Métodos e técnicas de melhoramento vegetal.  
12. Microbiologia.  
    12.1. Microbiologia geral e aplicada.  
    12.2. Microbiologia agrícola.  
13. Conhecimentos em gestão de laboratório e metodologias, equipamentos, procedimentos laboratoriais e gestão da qualidade.  
""",
"Ciências Exatas e da Terra": """
1. Agricultura 5.0.  
    1.1. Noções de inteligência artificial, big data, data warehouse, descoberta de conhecimento e mineração de dados, aprendizado de máquina e Internet das coisas (IoT).  
2. Métodos de análise multivariada.  
    2.1. PCA (análise de componentes principais), análise de clusters e análise discriminante.  
3. Técnicas para redução de dimensionalidade e interpretação de dados complexos.  
4. Estrutura de dados: variáveis, registros, banco de dados, estruturas de bancos de dados.  
5. Fundamentos de estatística aplicada.  
    5.1. Conceitos básicos de estatística descritiva: medidas de tendência central, dispersão e distribuição, forma assimétrica e curtose, associação entre variáveis quantitativas e qualitativas.  
    5.2. Métodos de inferência estatística: estimativas, intervalos de confiança e testes de hipótese.  
    5.3. Técnicas de amostragem, planejamento e análise de experimentos.  
6. Métodos estatísticos para dados não-normais e não-paramétricos.  
    6.1. Técnicas para análise de dados que não seguem distribuições normais.  
    6.2. Métodos não-paramétricos: testes de Wilcoxon, Kruskal-Wallis e outros.  
    6.3. Aplicação de técnicas robustas para dados com outliers e distribuições irregulares.  
7. Modelagem estatística e regressão.  
    7.1. Modelos de regressão linear e não linear: aplicação e interpretação.  
    7.2. Regressão múltipla, análise de variância (ANOVA) e técnicas de modelagem avançada.  
    7.3. Avaliação da adequação dos modelos e diagnóstico de problemas.  
8. Processamento e análise de dados.  
9. Agrometeorologia.  
10. Bioclimatologia.  
11. Engenharia de processos.  
12. Geoprocessamento, sensoriamento remoto e geotecnologias.  
""",
"Ciências Sociais Aplicadas": """
1. Administração rural.  
2. Antropologia.  
    2.1. Diversidade cultural e agroecologia.  
    2.2. Relações de gênero e trabalho no campo.  
3. Economia.  
    3.1. Economia agrícola e desenvolvimento rural.  
    3.2. Política econômica e agronegócio.  
4. Geografia.  
    4.1. Geografia rural e agrária.  
    4.2. Uso e ocupação do solo.  
    4.3. Questões ambientais e desenvolvimento regional.  
5. Sistemas de produção agrícola.  
    5.1. Agroecologia.  
    5.2. Produção orgânica.  
    5.3. Agricultura familiar.  
    5.4. Sistemas integrados de produção.  
    5.5. Sistemas agroflorestais.  
6. Sociologia rural.  
    6.1. Relações sociais no campo.  
    6.2. Desenvolvimento rural sustentável.  
    6.3. Movimentos sociais no campo.  
""",
"Direito e Auditoria": """
I. Direito Administrativo.  
    1. Estado, governo e administração pública.  
        1.1. Conceitos.  
        1.2. Elementos.  
    2. Direito administrativo.  
        2.1. Conceito.  
        2.2. Objeto.  
        2.3. Fontes.  
    3. Ato administrativo.  
        3.1. Conceito, requisitos, atributos, classificação e espécies.  
        3.2. Extinção do ato administrativo: cassação, anulação, revogação e convalidação.  
        3.3. Decadência administrativa.  
    4. Agentes públicos.  
        4.1. Cargo, emprego e função pública.  
        4.2. Direitos e deveres.  
        4.3. Responsabilidade.  
        4.4. Processo administrativo disciplinar.  
    5. Poderes da administração pública.  
        5.1. Hierárquico, disciplinar, regulamentar e de polícia.  
        5.2. Uso e abuso do poder.  
    6. Regime jurídico-administrativo.  
    7. Serviços públicos.  
        7.1. Conceito.  
        7.2. Elementos constitutivos.  
        7.3. Princípios.  
    8. Organização administrativa.  
        8.1. Centralização, descentralização, concentração e desconcentração.  
        8.2. Administração direta e indireta.  
        8.3. Autarquias, fundações, empresas públicas e sociedades de economia mista.  

II. Direito Constitucional.  
    1. Constituição da República Federativa do Brasil de 1988.  
        1.1. Princípios fundamentais.  
    2. Aplicabilidade das normas constitucionais.  
        2.1. Normas de eficácia plena, contida e limitada.  
        2.2. Normas programáticas.  
    3. Direitos e garantias fundamentais.  
        3.1. Direitos e deveres individuais e coletivos, direitos sociais, direitos de nacionalidade, direitos políticos, partidos políticos.  
    4. Organização político-administrativa do Estado.  
        4.1. Estado federal brasileiro, União, estados, Distrito Federal, municípios e territórios.  
    5. Administração pública.  
        5.1. Disposições gerais, servidores públicos.  
    6. Poder executivo.  
""",
"Engenharias": """
1. Agricultura de precisão.  
2. Agricultura digital.  
3. Ciência da computação.  
4. Engenharia de sistemas agrícolas.  
    4.1. Sistemas de controle e automação agropecuária.  
    4.2. Sistemas de controle supervisório e aquisição de dados.  
    4.3. Sistemas de sensores e atuadores.  
5. Inteligência artificial.  
6. Mecanização e automação agrícola.  
7. Mecatrônica e robótica.  
    7.1. Noções de mecatrônica.  
    7.2. Integração de sistemas mecânicos, elétricos e de controle.  
    7.3. Tipos e componentes de sistemas robóticos.  
    7.4. Aplicações práticas de robótica em diferentes setores industriais.  
    7.5. Controle e automação de sistemas robóticos.  
""",
"Gestão da Informação": """
1. Administração de sistemas e infraestrutura de TI.  
2. Arquitetura da informação e estruturas de dados.  
3. Arquitetura de rede.  
    3.1. Projeto, configuração e administração de redes de computadores.  
    3.2. Implementação e monitoramento de medidas de segurança como firewalls, VPNs, IDS, IPS.  
4. Base de dados.  
5. Ciclo de vida do software.  
6. Ciência de dados.  
7. Computação em nuvem.  
    7.1. Conceitos.  
    7.2. Serviços.  
    7.3. Plataformas de computação em nuvem: AWS, Azure, Google Cloud.  
8. Frameworks e padrões de arquitetura de software e serviços.  
9. Fundamentos de ciência da informação.  
10. Gerenciamento de servidores Windows e Linux.  
11. Gestão de informações.  
    11.1. Princípios de segurança da informação, classificação e controle de acesso em sistemas computacionais.  
12. Gestão de infraestrutura e redes de computadores.  
13. Gestão de projetos.  
    13.1. Conceitos, escopo, tempo, custos, qualidade, recursos humanos, comunicações, riscos, aquisições, partes interessadas.  
14. Gestão de redes e infraestrutura tecnológica.  
15. Governança de TI.  
16. Inteligência artificial.  
17. Metodologias ágeis de desenvolvimento de software.  
18. Planejamento e gestão estratégica: conceitos, princípios, etapas, níveis, métodos e ferramentas.  
19. Qualidade e testes de software.  
20. Segurança da informação.  
    20.1. Princípios, normas e melhores práticas de segurança da informação como criptografia, autenticação, controle de acesso, backup, auditoria.  
21. Serviços de TI.  
22. Servidores web, rede e comunicações.  
23. Sistemas de informação.  
24. Suporte técnico aos usuários.  
25. Usabilidade e experiência de usuário.  
26. Lei nº 12.527/2011.  
27. Lei nº 13.709/2018.  
""",
"Gestão de Pessoas": """
1. Avaliação de desempenho: objetivos, métodos, vantagens e desvantagens.  
2. Clima e cultura organizacional.  
3. Comportamento organizacional.  
    3.1. Relações indivíduo/organização, liderança, engajamento, desenvolvimento e motivação de colaboradores.  
4. Conceitos de insalubridade e periculosidade, caracterização e controle.  
5. Consolidação das Leis Trabalhistas (CLT).  
6. Equipamentos e métodos de proteção individual e coletiva.  
7. Ficha de informações sobre produtos químicos (FISPQ); ficha com dados de segurança; cuidados com fabricação, preparação, armazenamento, transporte, uso e eliminação de resíduos tóxicos.  
8. Gestão de pessoas nas organizações.  
    8.1. Conceitos, importância, relação com os outros sistemas de organização.  
    8.2. Órgão de gestão de pessoas: atribuições, objetivos, políticas e sistemas de informações gerenciais.  
    8.3. Gestão e administração do capital humano para empresas.  
9. Higiene e segurança no trabalho e saúde ocupacional.  
10. Legislação sobre insalubridade e periculosidade.  
11. Métodos e técnicas de pesquisa organizacional.  
12. Noções de higiene do trabalho e suas relações com o ambiente de trabalho.  
13. Qualidade de vida no trabalho.  
14. Treinamento, capacitação e desenvolvimento de pessoal.  
15. Lei nº 13.467/2017.  
16. Lei nº 13.709/2018.  
17. Lei nº 11.340/2006.  
18. Lei nº 10.741/2003.  
19. Legislação relacionada aos direitos sociais e aos serviços de assistência, fundamentos éticos, ética profissional, código de ética profissional.  
""",
"Gestão Estratégica": """
1. Abordagem para construção de soluções inovadoras.  
    1.1. Design thinking.  
    1.2. UX design.  
    1.3. Economia comportamental.  
    1.4. Canvas.  
2. Avaliação de programas e instituições.  
3. Balanced scorecard (BSC).  
4. Boas práticas em gerenciamento de projetos.  
    4.1. PMBOK.  
    4.2. PRINCE2.  
5. Boas práticas em gerenciamento de riscos corporativos.  
    5.1. Frameworks COSO ERM.  
    5.2. NBR ISO 31000.  
    5.3. Orange Book.  
6. Ciclo de vida do projeto: elaboração, gestão, monitoramento e avaliação de projetos e programas.  
7. Gerenciamento de processos de negócio (business process modeling – BPM).  
8. Gestão da mudança.  
9. Gestão de programas e projetos em ciência, tecnologia e inovação.  
10. Métodos ágeis.  
    10.1. Scrum.  
    10.2. Kanban.  
    10.3. Lean Six Sigma.  
11. Noções de ciência e de método científico.  
12. Noções de gestão da informação e de gestão de riscos institucionais.  
13. Noções de gestão pública e de administração pública federal.  
14. Noções de planejamento estratégico e inteligência estratégica.  
15. Noções de políticas públicas.  
16. Papel da ciência e da agricultura no mundo contemporâneo.  
17. Planejamento e gestão de ciência, tecnologia e inovação.  
""",
"Laboratórios e Campos Experimentais": """
1. Biossegurança em laboratórios.  
    1.1. Esterilização, desinfecção e desinfetantes.  
    1.2. Níveis de biossegurança.  
    1.3. Descarte de material biológico.  
    1.5. Manuseio e transporte de amostras.  
    1.6. Equipamentos de contenção, equipamento de proteção individual e coletivo.  
2. Boas Práticas de Laboratório.  
    2.1. Estocagem de substâncias químicas e biológicas.  
    2.2. Normas de segurança no preparo de soluções, meios de cultura e produtos biológicos ou químicos.  
    2.3. Descarte de substâncias químicas e biológicas.  
    2.4. Informações toxicológicas relevantes.  
    2.5. Coleta, preservação e fixação de material biológico.  
3. Estatística experimental.  
    3.1. Princípios da estatística experimental.  
        3.1.1. Unidade experimental ou parcela.  
        3.1.2. Repetição, casualização e controle local.  
        3.1.3. Experimentação intensiva e extensiva.  
    3.2. Grau de liberdade.  
    3.3. Testes de comparação de médias.  
    3.4. Decomposição da variância.  
    3.5. O modelo matemático.  
        3.5.1. Conceituação, componentes e classificação.  
        3.5.2. Desenvolvimento e restrições do modelo.  
        3.5.3. Contrastes.  
    3.6. Experimentos inteiramente casualizados.  
    3.7. Experimentos em blocos casualizados.  
    3.8. Experimentos em quadrados latinos.  
    3.9. Experimentos fatoriais.  
    3.10. Utilização de informática em estatística experimental.  
4. Gestão da Qualidade de Laboratórios e Áreas Experimentais.  
    4.1. NBR ISO/IEC 17025:2017.  
    4.2. ABNT NBR ISO 9000: sistemas de gestão da qualidade – fundamentos e vocabulários.  
    4.3. ABNT NBR ISO 9001: sistemas de gestão da qualidade – requisitos.  
    4.4. INMETRO: NIT-DICLA-034: aplicação dos princípios de BPL aos estudos de campo.  
    4.5. INMETRO: NIT-DICLA-035: princípios das Boas Práticas de Laboratório – BPL.  
    4.6. INMETRO (Brasil). DOQ-CGCRE-008: orientação sobre validação de métodos analíticos.  
5. Procedimentos analíticos.  
    5.1. Vidrarias e equipamentos utilizados no laboratório para pesagem e volumetria.  
    5.2. Conversões de unidades, abreviaturas e símbolos.  
    5.3. Operação, funcionamento, limpeza e calibração de equipamentos.  
6. Fundamentos das metodologias analíticas.  
    6.1. Colorimetria e espectrofotometria.  
    6.2. Espectrofotometria Infravermelho.  
    6.3. Espectrofluorimetria.  
    6.4. Potenciometria.  
    6.5. Condutimetria.  
    6.6. Cromatografia Líquida de Alta Eficiência.  
    6.7. Cromatografia líquida em camada fina.  
    6.8. Cromatografia gasosa.  
7. Princípios bioquímicos aplicados às principais análises e dosagens de substâncias.  
    7.1. Análise titrimétrica.  
    7.2. Turbidimetria.  
    7.3. Nefelometria.  
    7.4. Eletroforese.  
    7.5. Enzimaimunoensaio (EIA).  
    7.6. Radioimunoensaio (RIA).  
    7.7. Quimioluminescência.  
    7.8. Titulações neutralização.  
    7.9. Oxi-redução.  
    7.10. Precipitação.  
8. Legislações sanitárias.  
    8.1. Lei nº 6.360/1976.  
9. Normas de segurança no trabalho agrícola e uso de Equipamentos de Proteção Individual (EPIs).  
10. Protocolos de segurança para manuseio de defensivos agrícolas e produtos químicos.  
11. Procedimentos para manutenção e conservação de equipamentos e infraestrutura de campo.  
12. Gestão de resíduos e práticas para minimizar impactos ambientais no campo experimental.  
""",
"Métodos Quantitativos Avançados": """
1. Amostragem.  
2. Probabilidade e estatística.  
3. Estatística experimental.  
4. Métodos de análise multivariada.  
    4.1. PCA (análise de componentes principais), análise de clusters e análise discriminante.  
5. Técnicas para redução de dimensionalidade e interpretação de dados complexos.  
6. Estrutura de dados: variáveis, registros, banco de dados, estruturas de bancos de dados.  
7. Fundamentos de estatística aplicada.  
    7.1. Conceitos básicos de estatística descritiva: medidas de tendência central, dispersão e distribuição, forma assimétrica e curtose, associação entre variáveis quantitativas e qualitativas.  
    7.2. Métodos de inferência estatística: estimativas, intervalos de confiança e testes de hipótese.  
    7.3. Técnicas de amostragem, planejamento e análise de experimentos.  
8. Métodos estatísticos para dados não-normais e não-paramétricos.  
    8.1. Técnicas para análise de dados que não seguem distribuições normais.  
    8.2. Métodos não-paramétricos: testes de Wilcoxon, Kruskal-Wallis e outros.  
    8.3. Aplicação de técnicas robustas para dados com outliers e distribuições irregulares.  
9. Modelagem estatística e regressão.  
    9.1. Modelos de regressão linear e não linear: aplicação e interpretação.  
    9.2. Regressão múltipla, análise de variância (ANOVA) e técnicas de modelagem avançada.  
    9.3. Avaliação da adequação dos modelos e diagnóstico de problemas.  
10. Gestão de dados.  
11. Aprendizado de máquina.  
12. Softwares R e Python.  
""",
"Nanotecnologia": """
1. Definição de materiais compósitos, compósitos de matriz: polimérica, metálica e cerâmica.  
2. Compósitos de fibra de carbono, micro e macromecânica dos compósitos, resistência mecânica, fratura e fadiga de compósitos.  
3. Introdução a polímeros: conceituação e classificação, reações de polimerização, técnicas de polimerização.  
4. Síntese e caracterização de polímeros: polimerização em massa, solução, suspensão e emulsão.  
5. Recuperação e purificação de polímeros sintetizados, caracterização de polímeros quanto à estrutura e peso molecular.  
6. Introdução a Nanotecnologia: histórico, conceitos, desafios e fundamentos da Nanotecnologia, morfologia de materiais nanoestruturados.  
7. Nanopartículas (técnicas bottom-up) e Nanopós (técnicas de top-down).  
8. Nanotubos, “nanorods”, nanofios e nanofibras, fulerenos e nanotubos de carbono.  
9. Blocos de construção: nanotubos e nanopartículas.  
10. Técnicas e ferramentas de manipulação molecular e atômica: Nanofabricação “Positional Assembly” e “Self-Replication”.  
11. Nanociência e nanotecnologia com ênfase em Bionanotecnologia.  
""",
"Orçamento e Finanças": """
1. Contabilidade pública.  
    1.1. Conceito, objeto e regime.  
    1.2. Campo de aplicação.  
2. Demonstrações contábeis segundo o MCASP 10ª Edição.  
3. Despesa pública: conceito, etapas, estágios e categorias econômicas.  
4. Execução orçamentária e financeira.  
5. Gestão fiscal e tributária aplicada ao setor público.  
6. Gestão financeira e controladoria.  
    6.1. Princípios de gestão financeira no setor público e na iniciativa privada, com foco no controle de custos e otimização de recursos.  
7. Identificação e classificação de riscos.  
8. Legislação societária.  
9. Legislação tributária.  
10. Noções sobre a Lei nº 4.320/1964 e suas alterações (normas gerais de direito financeiro para elaboração e controle dos orçamentos e balanços da União, dos estados, dos municípios e do Distrito Federal).  
11. Macrofunções da Secretaria do Tesouro Nacional (STN).  
12. Orçamento público no Brasil.  
    12.1. Fundamentos do processo orçamentário no setor público brasileiro.  
    12.2. Normas e diretrizes que regem a execução orçamentária.  
13. Princípios fundamentais de contabilidade aprovados pelo Conselho Federal de Contabilidade pela Resolução CFC nº 750/1993.  
14. Pronunciamentos do Comitê de Pronunciamentos Contábeis (CPC).  
15. Noções de responsabilidade fiscal.  
    15.1. Importância do equilíbrio fiscal para o cumprimento de metas orçamentárias.  
    15.2. Lei de Responsabilidade Fiscal (LRF): Lei complementar nº 101/2000.  
16. Sistema integrado de administração financeira (SIAFI): conceitos básicos, objetivos, características, instrumentos de segurança e principais documentos de entrada.  
17. Lei nº 13.303/2016.  
18. Decreto-lei nº 5.452/1943.  
""",
"Suprimento, Manutenção e Serviços": """
1. Administração de materiais e patrimônio.  
2. Administração financeira e orçamentária.  
3. Contratos, seleção e qualificação de fornecedores.  
4. Ferramentas governamentais para gestão de processos.  
5. Gestão de contratos de terceirização na administração pública.  
6. Gestão de contratos e convênios.  
7. Gestão de infraestrutura e logística.  
8. Gestão de pessoas.  
9. Gestão de Suprimentos.  
    9.1. Princípios e práticas de planejamento, aquisição, armazenamento, movimentação e controle de materiais.  
10. Gestão e fiscalização de contratos.  
11. Gestão e manutenção de infraestruturas prediais e equipamentos.  
12. Lei nº 13.303/2016 e Regulamento de Licitação, Contratos e Convênios da Embrapa  
    (disponível no endereço eletrônico:  
    https://www.embrapa.br/documents/10180/36044282/Regulamento+de+Licita%C3%A7%C3%B5es%2C+Contratos+e+Conv%C3%AAnios/d656d57e-4cd5-1bb6-6d61-4ee3900197e6).  
13. Manutenção e gestão de ativos.  
    13.1. Técnicas de manutenção preventiva e corretiva.  
    13.2. Gestão de ativos físicos, essenciais para garantir a operação contínua e eficiente de equipamentos.  
14. Plano de contratação anual (PCA) na administração pública.  
15. Processos, normas e políticas de gestão patrimonial.  
""",
"Transferência de Tecnologia e Comunicação": """
1. Boas práticas em gerenciamento de projetos.  
2. Comunicação organizacional.  
3. Exploração comercial de ativos tecnológicos.  
4. Ferramentas e métodos da nova economia.  
5. Gestão de crises, comunicação estratégica e relacionamento com stakeholders.  
6. Gestão da inovação e capacidade tecnológica.  
7. Gestão de parcerias e cooperação técnica.  
8. Gestão do conhecimento.  
    8.1. Conceitos de criatividade, inovação, cognição, metacognição, tecnologia, conhecimento.  
    8.2. Noções de gestão do conhecimento e aprendizagem organizacional.  
    8.3. Tecnologia convencional, tecnologia social e tecnologia digital.  
9. Instrumentos de estímulo à inovação nas instituições científica, tecnológica e de inovação (ICTs) e nas empresas.  
10. Marco legal de CT&I (Lei nº 13.243/2016 e Decreto nº 9.283/2018).  
    10.1. Fundamentos e aplicações relacionados a inovação, ambientes promotores de inovação e ecossistemas de inovação.  
11. Marketing digital e mídias sociais.  
12. Marketing e comunicação.  
    12.1. Conceitos de marketing.  
    12.2. Importância do marketing, da comunicação e do planejamento estratégico para as organizações.  
    12.3. Marketing institucional e imagem da marca.  
13. Mecanismos de transferência de tecnologia e propriedade intelectual.  
14. Noções de inovação: conceito, transferência de tecnologia, inovação fechada, market-pull, technology-push, inovação aberta.  
15. Noções de modelos de negócios.  
16. Noções de sociologia rural, princípios e conceitos de transversalidade, interdisciplinaridade, sustentabilidade, história e cultura de povos tradicionais e agricultores familiares.  
17. Propriedade intelectual: proteção, patentes e transferência de conhecimento.  
"""
}

localidades_coordenadas = {
    "EMBRAPA SEMIÁRIDO – Petrolina/PE": (-9.3833, -40.5014),
    "EMBRAPA AMAZÔNIA OCIDENTAL – Manaus/AM": (-3.1190, -60.0217),
    "EMBRAPA COCAIS – São Luís/MA": (-2.5364, -44.3056),
    "EMBRAPA RORAIMA – Boa Vista/RR": (2.8250, -60.6750),
    "EMBRAPA CAPRINOS E OVINOS – Campina Grande/PB": (-7.2172, -35.8811),
    "EMBRAPA CAPRINOS E OVINOS – Sobral/CE": (-3.6886, -40.3520),
    "EMBRAPA SUÍNOS E AVES – Concórdia/SC": (-27.2333, -51.9833),
    "EMBRAPA PECUÁRIA SUL – Bagé/RS": (-31.3289, -54.1019),
    "EMBRAPA GADO DE LEITE – Juiz de Fora/MG": (-21.7667, -43.3500),
    "EMBRAPA HORTALIÇAS – Brasília/DF": (-15.7942, -47.8825),
    "EMBRAPA PANTANAL – Corumbá/MS": (-19.0078, -57.6547),
    "EMBRAPA SOLOS – Rio de Janeiro/RJ": (-22.9068, -43.1729),
    "EMBRAPA AMAZÔNIA ORIENTAL – Belém/PA": (-1.4558, -48.5044),
    "EMBRAPA AGROSSILVIPASTORIL – Sinop/MT": (-11.8639, -55.5167),
    "EMBRAPA AMAPÁ – Macapá/AP": (0.0347, -51.0662),
    "EMBRAPA MEIO AMBIENTE – Jaguariúna/SP": (-22.7042, -47.0042),
    "EMBRAPA TABULEIROS COSTEIROS – Aracaju/SE": (-10.9472, -37.0731),
    "EMBRAPA TABULEIROS COSTEIROS – Rio Largo/AL": (-9.4841, -35.8443),
    "EMBRAPA RONDÔNIA – Ouro Preto do Oeste/RO": (-10.7250, -62.2500),
    "EMBRAPA ALIMENTOS E TERRITÓRIOS – Maceió/AL": (-9.6662, -35.7356),
    "EMBRAPA MILHO E SORGO – Sete Lagoas/MG": (-19.4611, -44.2489),
    "EMBRAPA AGROPECUÁRIA OESTE – Dourados/MS": (-22.2233, -54.8083),
    "EMBRAPA PESCA E AQUICULTURA – Palmas/TO": (-10.1692, -48.3308),
    "EMBRAPA ACRE – Rio Branco/AC": (-9.9753, -67.8106),
    "EMBRAPA MILHO E SORGO – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA TRIGO – Passo Fundo/RS": (-28.2622, -52.4083),
    "EMBRAPA RONDÔNIA – Porto Velho/RO": (-8.7608, -63.9025),
    "EMBRAPA MEIO-NORTE – Teresina/PI": (-5.0892, -42.8019),
    "EMBRAPA RECURSOS GENÉTICOS E BIOTECNOLOGIA – Brasília/DF": (-15.7942, -47.8825),
    "EMBRAPA ARROZ E FEIJÃO – Santo Antônio de Goiás/GO": (-16.4833, -49.3000),
    "EMBRAPA SOJA – Londrina/PR": (-23.3045, -51.1696),
    "EMBRAPA AGROBIOLOGIA – Seropédica/RJ": (-22.7458, -43.7092),
    "EMBRAPA COCAIS – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA MEIO AMBIENTE – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA MANDIOCA E FRUTICULTURA – Cruz das Almas/BA": (-12.6750, -39.1067),
    "EMBRAPA ALGODÃO – Sinop/MT": (-11.8639, -55.5167),
    "EMBRAPA RONDÔNIA – Vilhena/RO": (-12.7417, -60.1433),
    "EMBRAPA SOJA – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA MEIO-NORTE – Parnaíba/PI": (-2.9083, -41.7769),
    "EMBRAPA CLIMA TEMPERADO – Pelotas/RS": (-31.7654, -52.3376),
    "EMBRAPA FLORESTAS – Colombo/PR": (-25.2927, -49.2231),
    "EMBRAPA UVA E VINHO – Bento Gonçalves/RS": (-29.1699, -51.5185),
    "EMBRAPA ALGODÃO – Campina Grande/PB": (-7.2172, -35.8811),
    "EMBRAPA ALGODÃO – Luís Eduardo Magalhães/BA": (-12.0967, -45.7869),
    "EMBRAPA ALGODÃO – Irecê/BA": (-11.3033, -41.8553),
    "EMBRAPA INSTRUMENTAÇÃO – São Carlos/SP": (-22.0064, -47.8972),
    "EMBRAPA PECUÁRIA SUDESTE – São Carlos/SP": (-22.0064, -47.8972),
    "EMBRAPA TERRITORIAL – Campinas/SP": (-22.9099, -47.0626),
    "EMBRAPA ACRE – Cruzeiro do Sul/AC": (-7.6303, -72.6727),
    "EMBRAPA CERRADOS – Planaltina/DF": (-15.6100, -47.6536),
    "EMBRAPA AGROINDÚSTRIA TROPICAL – Fortaleza/CE": (-3.7172, -38.5433),
    "EMBRAPA AGROENERGIA – Brasília/DF": (-15.7942, -47.8825),
    "EMBRAPA AGRICULTURA DIGITAL – Campinas/SP": (-22.9099, -47.0626),
    "EMBRAPA AGROINDÚSTRIA DE ALIMENTOS – Rio de Janeiro/RJ": (-22.9068, -43.1729),
    "EMBRAPA SEDE – Brasília/DF": (-15.7942, -47.8825),
    "EMBRAPA SOLOS – Balsas/MA": (-7.5333, -46.0417),
    "EMBRAPA SOLOS – Recife/PE": (-8.0476, -34.8770),
    "EMBRAPA ARROZ E FEIJÃO – Alegrete/RS": (-29.7883, -55.7949),  # Coordenadas aproximadas
    "EMBRAPA GADO DE LEITE – Coronel Pacheco/MG": (-21.5597, -43.2583),  # Coordenadas aproximadas
    "EMBRAPA CLIMA TEMPERADO – Francisco Beltrão/RS": (-26.0792, -53.0577),  # Coordenadas aproximadas
    "EMBRAPA AMAZÔNIA OCIDENTAL – Itacoatiara/AM": (-3.1386, -58.4442),  # Coordenadas aproximadas
    "EMBRAPA SEMIÁRIDO – Nossa Senhora da Glória/SE": (-10.2158, -37.4217),  # Coordenadas aproximadas
    "EMBRAPA TRIGO – Uberaba/MG": (-19.7472, -47.9312)
}


# Aplicação Streamlit
def main():
    st.title("Vagas para Analista 🔎")
    st.subheader("Salário-base: R$ 10.921,33")

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

            st.write("**Diploma de Graduação:**")
            for graduacao in vaga['Graduação'].split(';'):
                st.write(f"- {graduacao.strip()}")

            st.write("---")
            st.write("**DESCRIÇÃO ESPECÍFICA DAS ATIVIDADES DO CARGO:**")
            st.write(
                f"<p style='text-align: justify;'>{vaga['Descrição específica das atividade do cargo'].capitalize()}</p>",
                unsafe_allow_html=True
            )
            st.write("---")
    st.header("Assuntos cobrados")
    st.header("Conhecimentos Gerais")
    st.subheader("Língua Portuguesa")
    st.markdown("""
        1. Compreensão e interpretação de textos de gêneros variados.  
        2. Reconhecimento de tipos e gêneros textuais.  
        3. Domínio da ortografia oficial.  
        4. Domínio dos mecanismos de coesão textual.  
           - Emprego de elementos de referenciação, substituição e repetição, de conectores e de outros elementos de sequenciação textual.  
           - Emprego de tempos e modos verbais.  
        5. Domínio da estrutura morfossintática do período.  
           - Emprego das classes de palavras.  
           - Relações de coordenação entre orações e entre termos da oração.  
           - Relações de subordinação entre orações e entre termos da oração.  
           - Emprego dos sinais de pontuação.  
           - Concordância verbal e nominal.  
           - Regência verbal e nominal.  
           - Emprego do sinal indicativo de crase.  
           - Colocação dos pronomes átonos.  
        6. Reescrita de frases e parágrafos do texto.  
           - Significação das palavras.  
           - Substituição de palavras ou de trechos de texto.  
           - Reorganização da estrutura de orações e de períodos do texto.  
           - Reescrita de textos de diferentes gêneros e níveis de formalidade.
        """)

    st.subheader("Língua Inglesa")
    st.markdown("""
        1. Compreensão de textos escritos em língua inglesa.  
        2. Itens gramaticais relevantes para compreensão dos conteúdos semânticos.  
        3. Versão do Português para o Inglês: fidelidade ao texto-fonte; respeito à qualidade e ao registro do texto-fonte; correção morfossintática e lexical.  
        4. Tradução do Inglês para o Português: fidelidade ao texto-fonte; respeito à qualidade e ao registro do texto-fonte; correção morfossintática e lexical.
        """)
    st.subheader("Noções de Lógica e Estatística")
    st.markdown("""
    ### Raciocínio Lógico
    1. Estruturas lógicas.  
    2. Lógica de argumentação:  
       - Analogias, inferências, deduções e conclusões.  
    3. Lógica sentencial (ou proposicional):  
       - Proposições simples e compostas.  
       - Tabelas-verdade.  
       - Equivalências.  
       - Leis de Morgan; problemas.  

    ### Noções de Estatística
    1. População e amostra.  
    2. Histogramas e curvas de frequência.  
    3. Medidas de posição:  
       - Média, moda, mediana e separatrizes.  
    4. Medidas de dispersão:  
       - Absoluta e relativa.  
    5. Probabilidade:  
       - Probabilidade condicional e independência.  
    6. Variável aleatória e funções de distribuição.
    """)
    st.subheader("Ética e Legislação")
    st.markdown("""
        1. **Código de Conduta, Ética e Integridade da Embrapa**  
           - Disponível no endereço eletrônico:  
             [Código de Conduta, Ética e Integridade da Embrapa](https://www.embrapa.br/documents/10180/56556577/C%C3%B3digo_Conduta_Etica_Integridade_daEmbrapa.pdfRC207.pdf/caa4d33e-7a5a-d048-0da7-12583d0eaf64).

        2. **Estatuto jurídico da empresa pública, da sociedade de economia mista e de suas subsidiárias**  
           - No âmbito da União, dos estados, do Distrito Federal e dos municípios.  
           - Lei nº 13.303/2016 e Decreto nº 8.945/2016 e alterações.

        3. **Estatuto da Embrapa**  
           - Aprovado em 24/04/2024.  
           - Disponível no endereço eletrônico:  
             [Estatuto da Embrapa](https://www.embrapa.br/documents/10180/36830205/8%C2%AA+AGO+24abr2024+-+Estatuto/f6eadc9b-65aa-36c0-27ee-bfffdbb7358f).

        4. **Lei Geral de Proteção de Dados Pessoais – LGPD**  
           - Lei nº 13.709/2018 e suas alterações.
        """)

    st.subheader("Plano Diretor da Embrapa")
    st.markdown("""
        - Plano Diretor da Embrapa 2024-2030.
        """)

    st.subheader("Atualidades")
    st.markdown("""
        Tópicos relevantes e atuais de diversas áreas, tais como cultura, desenvolvimento sustentável, economia, ecologia, educação, energia, mudanças climáticas, política, relações internacionais, saúde, segurança, sociedade, tecnologia e transportes.
        """)
    # Configurar a página no Streamlit
    st.title("Conhecimentos Complementares")
    st.markdown(conhecimentos_complementares[selected_area])

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
