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
    file_path = '../concurso_embrapa/pesquisador.xlsx'  # Substitua pelo caminho correto
    data = pd.read_excel(file_path)
    return data

data = load_data()
conhecimentos_complementares = {
        "Ciência e Tecnologia de Alimentos": """
        1. Análise e controle de qualidade de alimentos de origem vegetal e animal.  
        2. Bioengenharia de alimentos.  
        3. Controle de qualidade de alimentos: ferramentas e programas.  
        4. Ciência de alimentos aplicada à segurança alimentar.  
        5. Desenvolvimento de novos produtos alimentícios.  
        6. Matérias-primas alimentares e não alimentares na agroindústria.  
        7. Métodos e técnicas de preservação de alimentos e bebidas.  
        8. Microbiologia dos alimentos.  
        9. Principais tendências tecnológicas relativas à agroindústria.
        """,
        "Ciências Agrárias": """
        1. Agrometeorologia.  
           1.1 Meteorologia básica.  
           1.2 Climatologia aplicada à agricultura.  
        2. Entomologia.  
           2.1 Biologia e ecologia dos insetos e princípios de sistemática.  
           2.2 Principais pragas de plantas cultivadas.  
           2.3 Métodos de controle de pragas e tecnologia de aplicação de defensivos.  
           2.4 Inseticidas.  
           2.5 Manejo integrado de pragas.  
        3. Fisiologia vegetal.  
           3.1 Água no sistema solo-planta-atmosfera.  
           3.2 Fotossíntese e respiração.  
           3.3 Absorção e translocação de solutos orgânicos e inorgânicos.  
           3.4 Efeitos da temperatura e da luz na planta.  
           3.5 Reguladores de crescimento.  
           3.6 Germinação e dormência de sementes.  
           3.7 Fisiologia de pós-colheita.  
           3.8 Ecofisiologia vegetal.  
        4. Fitopatologia.  
           4.1 Conceitos básicos: histórico, sintomas, agentes fitopatogênicos, patogênese, epidemiologia.  
           4.2 Princípios gerais de controle.  
           4.3 Principais doenças de plantas e métodos de controle.  
           4.4 Fungicidas, nematicidas e bactericidas.  
        5. Geoprocessamento.  
           5.1 Princípios físicos e elementos de interpretação.  
           5.2 Sistemas de sensoriamento remoto.  
           5.3 Sensores e produtos.  
           5.4 Interpretação de imagens.  
           5.5 Fotointerpretação e fotogrametria.  
           5.6 Restituição.  
           5.7 Tomada, transmissão, armazenamento, processamento e interpretação de dados.  
           5.8 Georreferenciamento.  
           5.9 Aplicações de sensoriamento remoto no planejamento, monitoramento e controle dos recursos naturais e das atividades antrópicas.  
        6. Irrigação e drenagem.  
           6.1 Métodos de irrigação.  
           6.2 Projetos de irrigação e drenagem.  
           6.3 Manejo da irrigação.  
        7. Melhoramento genético de plantas.  
           7.1 Noções de melhoramento genético vegetal.  
           7.2 Métodos e técnicas de melhoramento vegetal.  
           7.3 Engenharia genética: legislação sobre organismos geneticamente modificados e aplicações na agricultura.  
           7.4 Biotecnologia aplicada ao melhoramento genético de plantas.  
        8. Plantas daninhas.  
           8.1 Biologia das plantas daninhas.  
           8.2 Métodos de controle.  
           8.3 Herbicidas.  
           8.4 Tecnologia de aplicação de herbicidas.  
        9. Preservação, conservação e manejo de recursos naturais renováveis.  
           9.1 Noções de ecologia.  
           9.2 Poluição em agroecossistemas.  
           9.3 Recuperação de áreas degradadas.  
        10. Principais culturas agrícolas brasileiras.  
            10.1 Grãos, fibras, fruteiras, olerícolas, matérias primas industriais.  
            10.2 Aspectos econômicos, características botânicas e agronômicas, exigências edafoclimáticas, técnicas de cultivo, pós-colheita e comercialização.  
        11. Relações entre solo, organismos e plantas.  
            11.1 Morfologia, fisiologia, genética e taxonomia de microrganismos de importância agrícola.  
            11.2 Transformações bioquímicas envolvendo microrganismos do solo.  
            11.3 Associações simbióticas entre microrganismos do solo e plantas.  
            11.4 Microflora, micro e mesofauna do solo.  
        12. Silvicultura.  
            12.1 Princípios.  
            12.2 Fisiologia de espécies florestais.  
            12.3 Serviços ambientais e ecossistêmicos.  
        13. Tecnologia pós-colheita de grãos e sementes.  
            13.1 Secagem, beneficiamento e armazenagem.  
        14. Sanidade animal.  
            14.1 Defesa sanitária animal.  
            14.2 Doenças parasitárias dos animais de produção.  
        15. Sistemas de produção agrícola.  
            15.1 Agroecologia.  
            15.2 Produção orgânica.  
            15.3 Agricultura familiar.  
            15.4 Sistemas integrados de produção.  
            15.5 Sistemas agroflorestais.  
        16. Solos.  
            16.1 Química e fertilidade do solo.  
            16.2 Física do solo.  
            16.3 Gênese e morfologia do solo.  
            16.4 Sistema brasileiro de classificação de solos.  
            16.5 Principais domínios pedológicos brasileiros.  
            16.6 Capacidade de uso, manejo e conservação de solos.  
        17. Zootecnia.  
            17.1 Agrostologia.  
            17.2 Bromatologia.  
            17.3 Boas práticas de produção agropecuária.  
            17.4 Nutrição e alimentação animal.  
            17.5 Sistemas de produção e manejo de animais.  
            17.6 Reprodução e melhoramento genético animal.  
            17.7 Sistemas de produção aquícola.  
            17.8 Qualidade da água em aquicultura.  
            17.9 Apicultura e meliponicultura:  
                 17.9.1 Noções de apicultura e meliponicultura, biologia e evolução de abelhas.  
                 17.9.2 Interação abelhas e ambiente.  
        """,
        "Ciências Ambientais": """
        1. Geoprocessamento e sensoriamento remoto.  
           1.1 Conceitos básicos de Sistemas de Informação Geográfica (SIG).  
           1.2 Sistemas de coordenadas e georreferenciamento.  
           1.3 Sistemas de imageamento.  
               1.3.1 Principais sistemas sensores, conceitos de pixel, resolução espacial, temporal e radiométrica.  
           1.4 Imagens de radar, multiespectrais e multitemporais.  
           1.5 Aplicações de sensoriamento remoto no planejamento, monitoramento e controle dos recursos naturais e das atividades antrópicas.  
        2. Ecologia geral e aplicada.  
           2.1 Ecossistemas brasileiros.  
           2.2 Cadeia alimentar.  
           2.3 Sucessões ecológicas.  
        3. Recursos hídricos.  
           3.1 Noções de meteorologia e climatologia.  
           3.2 Noções de hidrologia.  
               3.2.1 Ciclo hidrológico, balanço hídrico, bacias hidrográficas, transporte de sedimentos.  
           3.3 Noções de hidráulica.  
        4. Controle de poluição ambiental.  
           4.1 Qualidade da água.  
           4.2 Poluição hídrica.  
           4.3 Tecnologias de tratamento de água.  
           4.4 Tecnologias de tratamento de efluentes sanitários.  
           4.5 Tecnologias de tratamento de resíduos sólidos.  
        5. Saneamento ambiental.  
           5.1 Sistema de abastecimento de água.  
           5.2 Rede de esgotamento sanitário.  
           5.3 Gerenciamento de resíduos sólidos.  
               5.3.1 Acondicionamento, coleta, transporte, tratamento e destinação final.  
           5.4 Drenagem urbana (micro e macro).  
        6. Planejamento e gestão ambiental.  
           6.1 Avaliação de impactos ambientais.  
           6.2 Riscos ambientais.  
           6.3 Valoração de danos ambientais.  
           6.4 Sistema Nacional de Unidades de Conservação (SNUC).  
        7. Planejamento territorial.  
           7.1 Instrumentos de controle do uso e ocupação do solo.  
           7.2 Estatuto das Cidades.  
           7.3 Planos diretores de ordenamento do território.  
        8. Defesa civil.  
           8.1 Sistema Nacional de Defesa Civil.  
           8.2 Gerenciamento de desastres, ameaças e riscos.  
           8.3 Política de combate a calamidades.  
        9. Legislação ambiental.  
           9.1 Lei nº 9.605/1998 e alterações e Decreto nº 6.514/2008 (Lei dos Crimes Ambientais).  
           9.2 Lei nº 12.651/2012 e alterações.  
           9.3 Lei nº 9.795/1999 e Decreto nº 4.281/2002 (Educação Ambiental).  
           9.4 Lei nº 12.305/2010 (Política Nacional de Resíduos Sólidos).  
           9.5 Lei nº 7.802/1989 e alterações (Lei de Agrotóxicos).  
           9.6 Lei nº 9.433/1997 e alterações (Política Nacional de Recursos Hídricos).  
           9.7 Lei nº 6.938/1981 e alterações (Política Nacional do Meio Ambiente).  
           9.8 Lei nº 9.985/2000 e alterações (Sistema Nacional de Unidades de Conservação da Natureza).  
           9.9 Decretos nº 875/1993 e nº 4.581/2003 (Convenção de Basileia).  
           9.10 Decreto nº 5.472/2005 (Convenção de Estocolmo).  
           9.11 Decreto nº 5.360/2005 (Convenção de Roterdã).  
           9.12 Decreto nº 5.445/2005 (Protocolo de Quioto).  
           9.13 Decreto nº 2.699/1998 (Protocolo de Montreal).  
           9.14 Lei nº 9.966/2000 e Decreto nº 4.136/2002 (Lançamento de óleo e outras substâncias nocivas).  
           9.15 Resoluções do CONAMA atinentes ao tema gestão, proteção e controle da qualidade ambiental:  
                - nº 1/1986 e alterações; nº 18/1986 e alterações; nº 5/1989 e alterações; nº 2/1990; nº 2/1991; nº 6/1991; nº 5/1993 e alterações; nº 24/1994; nº 23/1996 e alterações; nº 237/1997; nº 267/2000 e alterações; nº 275/2001; nº 302/2002; nº 303/2002; nº 307/2002 e alterações; nº 313/2002; nº 316/2002 e suas alterações; nº 357/2005 e alterações; nº 358/2005; nº 362/2005 e suas alterações; nº 369/2006; nº 371/2006; nº 375/2006 e suas alterações; nº 377/2006; nº 380/2006; nº 396/2008; nº 401/2008 e alterações; nº 403/2008; nº 404/2008; nº 410/2009; nº 412/2009; nº 413/2009; nº 414/2009; nº 415/2009 e alterações; nº 416/2009; nº 418/2009 e alterações; nº 420/2009; nº 422/2010; nº 424/2010; nº 2/2012.  
        10. NBR ISO.  
            10.1 NBR ISO nº 14001:2015 (sistemas de gestão ambiental: requisitos e normas para uso).  
            10.2 NBR ISO nº 14004:2018 (sistemas de gestão ambiental: diretrizes e princípios gerais de uso).  
            10.3 NBR ISO nº 19011:2018 (diretrizes para auditoria de sistema de gestão).
        """,
        "Ciências Biológicas": """
        1. Biodiversidade e ecologia.  
           1.1 Ecossistemas terrestres e aquáticos.  
           1.2 Biodiversidade brasileira.  
           1.3 Conservação da biodiversidade.  
        2. Bioeconomia.  
        3. Bioinformática.  
        4. Biologia celular e desenvolvimento.  
           4.1 Mecanismos moleculares e celulares no desenvolvimento e diferenciação celular.  
           4.2 Tecnologias para a visualização e análise de processos celulares em tempo real.  
        5. Biologia celular e molecular.  
           5.1 Estrutura e função da célula.  
           5.2 Biologia molecular e genética.  
           5.3 Biotecnologia e engenharia genética.  
           5.4 Aplicações de biologia molecular em pesquisa agrícola e farmacológica.  
        6. Biologia sintética.  
        7. Desenvolvimento de produtos e processos agroindustriais e controle biológico.  
        8. Ecofisiologia vegetal.  
        9. Engenharia de bioprocessos e biotecnologia.  
        10. Genética.  
            10.1 Genética clássica e molecular.  
            10.2 Genética de populações.  
        11. Genômica funcional e estrutural.  
            11.1 Análise funcional de genomas.  
            11.2 Tecnologias para mapeamento genômico e análise estrutural de genomas.  
        12. Insumos biológicos para a produção animal e vegetal.  
        13. Melhoramento genético vegetal e animal.  
        14. Microbiologia.  
            14.1 Microbiologia geral e aplicada.  
            14.2 Microbiologia agrícola.  
                14.2.1 Fundamentos em controle microbiológico microbiano.  
                14.2.2 Fundamentos em promoção de crescimento de plantas por microrganismos.  
                14.2.3 Processos de produção e formulação de microrganismos benéficos.  
        15. Fisiologia vegetal.  
        16. Nutrição e crescimento de plantas.  
        17. Ômicas.  
            17.1 Genômica.  
            17.2 Proteômica.  
            17.3 Metabolômica.  
        18. Tecnologia de processos fermentativos.  
        """,
        "Ciências da Saúde": """
        1. Nutrição básica.  
           1.1 Nutrientes: conceito, classificação, funções, requerimentos, recomendações e fontes alimentares.  
           1.2 Aspectos clínicos da carência e do excesso.  
           1.3 Dietas não convencionais.  
           1.4 Aspectos antropométricos, clínicos e bioquímicos da avaliação nutricional.  
           1.5 Nutrição e fibras.  
           1.6 Utilização de tabelas de alimentos.  
           1.7 Alimentação nas diferentes fases e momentos biológicos.  
        2. Educação nutricional.  
           2.1 Conceito, importância, princípios e objetivos da educação nutricional.  
           2.2 Papel da educação nutricional nos hábitos alimentares.  
           2.3 Aplicação de meios e técnicas do processo educativo.  
           2.4 Desenvolvimento e avaliação de atividades educativas em nutrição.  
        3. Avaliação nutricional.  
           3.1 Métodos diretos e indiretos de avaliação nutricional.  
           3.2 Técnicas de medição.  
           3.3 Avaliação do estado e situação nutricional da população.  
        4. Técnica dietética.  
           4.1 Alimentos: conceito, classificação, características, grupos de alimentos, valor nutritivo, caracteres organolépticos.  
           4.2 Seleção e preparo dos alimentos.  
           4.3 Planejamento, execução e avaliação de cardápios.  
        5. Higiene de alimentos.  
           5.1 Análise microbiológica e toxicológica dos alimentos.  
           5.2 Fontes de contaminação.  
           5.3 Fatores extrínsecos e intrínsecos que condicionam o desenvolvimento de microrganismos no alimento.  
           5.4 Modificações físicas, químicas e biológicas dos alimentos.  
           5.5 Enfermidades transmitidas pelos alimentos.  
        6. Nutrição e dietética.  
           6.1 Recomendações nutricionais.  
           6.2 Função social dos alimentos.  
           6.3 Atividade física e alimentação.  
           6.4 Alimentação vegetariana e suas implicações nutricionais.  
        7. Tecnologia de alimentos.  
           7.1 Operações unitárias.  
           7.2 Conservação de alimentos.  
           7.3 Embalagem em alimentos.  
           7.4 Processamento tecnológico de produtos de origem vegetal e animal.  
           7.5 Análise sensorial.  
        8. Nutrição em saúde pública.  
           8.1 Análise dos distúrbios nutricionais como problemas de saúde pública.  
           8.2 Problemas nutricionais em populações em desenvolvimento.  
        9. Dietoterapia.  
           9.1 Abordagem ao paciente hospitalizado.  
           9.2 Generalidades, fisiopatologia e tratamento das diversas enfermidades.  
           9.3 Exames laboratoriais: importância e interpretação.  
           9.4 Suporte nutricional enteral e parenteral.  
        10. Bromatologia.  
            10.1 Aditivos alimentares.  
            10.2 Condimentos.  
            10.3 Pigmentos.  
            10.4 Estudo químico-bromatológico dos alimentos: proteínas, lipídios e carboidratos.  
            10.5 Vitaminas.  
            10.6 Minerais.  
            10.7 Bebidas.  
        """,
        "Ciências Exatas e da Terra": """
        1. Agricultura digital.  
           1.1 Legislação e compliance.  
        2. Agrometeorologia.  
        3. Bioclimatologia.  
        4. Computação numérica.  
           4.1 Sistemas de equações numéricas.  
           4.2 Otimização baseada em gradientes.  
        5. Engenharia de software.  
        6. Engenharia de produção e otimização de processos.  
           6.1 Métodos de otimização e análise de processos produtivos.  
           6.2 Ferramentas e técnicas de controle de qualidade e melhoria contínua.  
           6.3 Modelagem e simulação de processos industriais e logísticos.  
        7. Fundamentos de álgebra linear.  
           7.1 Vetores, matrizes, determinantes, autovalores, autovetores.  
        8. Gestão de recursos naturais e sustentabilidade.  
           8.1 Estratégias para a gestão sustentável dos recursos hídricos e do solo.  
           8.2 Práticas para a conservação da biodiversidade e dos habitats naturais em áreas agrícolas.  
           8.3 Métodos de avaliação e monitoramento da sustentabilidade em sistemas agrícolas.  
        9. Inovações em tecnologias de sensoriamento e geotecnologias.  
        10. Integração de sistemas energéticos e agricultura.  
            10.1 Aplicações de energias renováveis em sistemas agrícolas: bioenergia e sistemas fotovoltaicos.  
            10.2 Estratégias para o uso eficiente de recursos energéticos na agricultura.  
            10.3 Modelagem de sistemas integrados de produção de energia e cultivo agrícola.  
        11. Inteligência artificial para o reconhecimento automático de padrões de imagens de satélite.  
        12. Mapeamento de uso e cobertura das terras.  
        13. Otimização de tráfego para diferentes modais de transportes.  
        14. Políticas e economia da agricultura sustentável.  
            14.1 Políticas públicas e regulamentações para promover práticas agrícolas sustentáveis.  
            14.2 Avaliação econômica da adoção de práticas sustentáveis e incentivos financeiros.  
            14.3 Programas de certificação e rotulagem para produtos sustentáveis.  
        15. Princípios e práticas de agricultura sustentável.  
            15.1 Conceitos e princípios fundamentais da agricultura sustentável.  
            15.2 Técnicas de manejo sustentável: rotação de culturas, cultivo mínimo e agroecologia.  
            15.3 Estratégias para melhorar a saúde do solo e a biodiversidade nas práticas agrícolas.  
        16. Probabilidade e estatística.  
            16.1 Distribuição de probabilidade.  
            16.2 Probabilidade condicional, esperança.  
            16.3 Variância e covariância.  
            16.4 Regra de Bayes.  
            16.5 Entropia de Shannon.  
            16.6 Divergência de Kullback-Leibler.  
        17. Rastreabilidade e certificação de produtos agrícolas.  
        18. Sistema de produção integrada e agroecologia.  
            18.1 Métodos de produção integrada e sistemas agroecológicos.  
            18.2 Desenvolvimento de sistemas agroflorestais e policulturas como alternativas sustentáveis.  
            18.3 Benefícios e desafios da integração de produção vegetal e animal.  
        19. Tecnologias e inovações em agricultura sustentável.  
            19.1 Tecnologias emergentes para a agricultura sustentável: sensores, drones e tecnologias de precisão.  
            19.2 Inovações em sistemas de irrigação e manejo de água para redução do consumo e eficiência.  
            19.3 Aplicações de tecnologias digitais na gestão sustentável de culturas.  
        20. Tecnologias e inovações em produção de energia.  
            20.1 Tecnologias convencionais e renováveis para a geração de energia: características e aplicações.  
            20.2 Inovações recentes em produção de energia: impacto econômico e ambiental.  
            20.3 Viabilidade e otimização de sistemas de produção de energia.  
        21. Zoneamentos agrícolas.  
        """,
        "Ciências Sociais Aplicadas": """
        1. Antropologia.  
           1.1 Diversidade cultural e agroecologia.  
           1.2 Relações de gênero e trabalho no campo.  
        2. Economia rural.  
           2.1 Economia agrícola e desenvolvimento rural.  
           2.2 Competitividade, mercados e cadeias agroindustriais.  
           2.3 Política econômica e agronegócio.  
           2.4 Políticas agrícolas.  
        3. Geografia.  
           3.1 Geografia rural e agrária.  
           3.2 Uso e ocupação do solo.  
           3.3 Questões ambientais e desenvolvimento regional.  
        4. Gestão estratégica do agronegócio.  
           4.1 Estudo das cadeias de valor agrícolas.  
           4.2 Agregação de valor aos produtos locais.  
           4.3 Promoção da comercialização sustentável e melhoria da distribuição e acesso aos mercados.  
           4.4 Sistemas de produção agropecuária.  
        5. Sociologia rural.  
           5.1 Relações sociais no campo.  
           5.2 Desenvolvimento rural sustentável.  
           5.3 Movimentos sociais no campo.  
        """,
        "Engenharias": """
        1. Agricultura de precisão.  
        2. Agricultura digital.  
        3. Engenharia de controle.  
           3.1 Inteligência computacional.  
               3.1.1 Comando.  
               3.1.2 Monitoração.  
               3.1.3 Alarme.  
               3.1.4 Intertravamento.  
               3.1.5 Registro e comunicação de sinais.  
        4. Engenharia Agrícola.  
           4.1 Máquinas e implementos agrícolas.  
           4.2 Manejo de recursos hídricos e tecnologias de irrigação.  
        5. Engenharia de sistemas agrícolas.  
           5.1 Sistemas de controle e automação agropecuária.  
           5.2 Sistemas de controle supervisório e aquisição de dados.  
           5.3 Sistemas de sensores e atuadores.  
        6. Engenharia de software.  
           6.1 Modelos de ciclo de vida de software.  
           6.2 Metodologias de desenvolvimento de software (Scrum, Lean, Kanban).  
           6.3 Arquitetura de software.  
           6.4 Processos e práticas de desenvolvimento de software.  
           6.5 Gestão de backlog.  
           6.6 Produto mínimo viável (MVP).  
           6.7 Práticas ágeis de desenvolvimento de software.  
           6.8 Desenvolvimento guiado por testes (TDD).  
           6.9 Notação BPMN.  
           6.10 Low-code e no-code software development.  
           6.11 Conceitos e ferramentas de DevOps.  
           6.12 Técnicas de integração e implantação contínua de código (CI/CD).  
        7. Fundamentos de Mecatrônica e Robótica.  
           7.1 Princípios básicos de mecatrônica.  
           7.2 Integração de sistemas mecânicos, elétricos e de controle.  
           7.3 Tipos e componentes de sistemas robóticos.  
               7.3.1 Atuadores.  
               7.3.2 Sensores.  
               7.3.3 Sistemas de controle.  
           7.4 Aplicações práticas de robótica em diferentes setores industriais.  
           7.5 Controle e automação de sistemas robóticos.  
        8. Inteligência artificial.  
        9. Mecanização e automação agrícola.  
        10. Métodos de controle para robótica.  
            10.1 Controle PID, controle adaptativo e controle baseado em modelos.  
            10.2 Técnicas de programação de robôs.  
                10.2.1 Linguagens de programação e frameworks.  
            10.3 Sistemas de visão computacional e integração de sensores para controle preciso.  
        11. Projeto e desenvolvimento de sistemas mecatrônicos.  
            11.1 Projeto de sistemas mecatrônicos.  
                11.1.1 Modelagem.  
                11.1.2 Simulação.  
                11.1.3 Prototipagem.  
            11.2 Integração de componentes mecânicos e eletrônicos em sistemas automatizados.  
            11.3 Análise de desempenho e otimização de sistemas mecatrônicos.  
        12. Robótica.  
            12.1 Robótica colaborativa e sistemas de robôs autônomos.  
                12.1.1 Conceitos e aplicações.  
            12.2 Tecnologias emergentes em robótica.  
                12.2.1 Inteligência artificial.  
                12.2.2 Aprendizado de máquina e redes neurais.  
            12.3 Aplicações inovadoras de robótica em áreas como saúde, agricultura e manufatura.  
        13. Segurança e manutenção de sistemas robóticos.  
            13.1 Protocolos de segurança e práticas para garantir a operação segura de robôs industriais.  
            13.2 Estratégias de manutenção preventiva e corretiva para sistemas robóticos.  
            13.3 Análise de falhas e desenvolvimento de sistemas de diagnóstico para robótica.  
        """,
        "Espectroscopia Aplicada": """
        1. Conceitos básicos da interação da radiação eletromagnética com a matéria e processos de interação da luz com sistemas biológicos.  
        2. Conceitos básicos de óptica.  
           2.1 Espectroscopia.  
           2.2 Eletrônica.  
           2.3 Mecânica quântica.  
           2.4 Termodinâmica.  
        3. Espectroscopia de absorção de luz UV-visível.  
        4. Espectroscopia de fluorescência.  
           4.1 Espectroscopia de fluorescência resolvida no tempo.  
        5. Espectroscopia de emissão por plasma induzido por laser (LIBS).  
        6. Espectroscopia de infravermelho próximo (NIR).  
        7. Espectroscopia de infravermelho com transformada de Fourier (FTIR) e espectroscopia Raman.  
        8. Imagens de fluorescência.  
        9. Imagens térmicas.  
        10. Imagens multi e hiperespectrais.  
        11. Noções de estatística:  
            11.1 Modelos univariados e multivariados.  
        12. Tratamento e análise de sinais espectroscópicos e processamento de imagens.  
        """


        # Adicione mais áreas conforme necessário
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
    "EMBRAPA SOLOS – Recife/PE": (-8.0476, -34.8770)
}


# Aplicação Streamlit
def main():
    st.title("Vagas para Pesquisador 👩‍🔬")
    st.subheader("Salário-base: R$ 12.814,61")

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
            st.write("**Diploma de Mestrado:**")
            for mestrado in vaga['Mestrado'].split(';'):
                st.write(f"- {mestrado.strip()}")

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

    st.subheader("Metodologia de Pesquisa")
    st.markdown("""
    1. Conhecimento científico e outras classes de conhecimento.  
    2. Ciências formais e factuais.  
       - Ciências físicas e sociais.  
       - Ciências básicas e aplicadas.  
       - Abordagens mecanicistas e holísticas.  
    3. Problemas de construção do conhecimento científico.  
       - Teoria e empiria.  
       - Lógica e evidência.  
       - Razão e intuição.  
       - Causalidade, objetividade, neutralidade, linearidade, observação e sentidos.  
       - Especificidade e generalidade do conhecimento, falsificabilidade, predição e controle.  
       - Paradigmas e mudanças, realismo e relativismo.  
    4. Abrangências da explicação científica:  
       - Descrições, correlações, teorias, modelos, sistemas, emergentismo, reducionismo, holismo.  
    5. O modelo clássico da pesquisa:  
       - O problema e a sua identificação.  
       - Conceitos, fundamentação teórica, indução, dedução, hipóteses e plano de prova.  
       - Suporte bibliográfico, delineamento da pesquisa, princípios do planejamento de ensaios experimentais.  
       - Métodos e técnicas, variáveis e constantes, evidências e interpretação, resultados e redação de relatórios.  
    6. O papel dos ensaios comparativos.  
    7. Tendências recentes de concepção da pesquisa:  
       - Pesquisa-ação, pesquisa participativa, pesquisa sistêmica, holismo, paradigma ecológico, feminismo, perspectivas emergentes.  
    8. O projeto de pesquisa no Sistema Nacional de Pesquisa Agropecuária:  
       - Finalidade, justificativa, objetivos, metas, procedimentos, cronograma e recursos, evidências e resultados.  
    9. Lógica dos procedimentos da pesquisa:  
       - Uso de dados secundários, experimentação, amostragem, observação naturalista.  
       - Qualidade, quantidade, mensuração, escalas, uso de estatística.  
    10. Casualização e controle de erro.  
    11. Problemas especiais da pesquisa aplicada:  
       - Identificação de problemas de pesquisa, escolhas de prioridades, o papel da teoria e da criatividade.  
       - Fidedignidade e validez, recursos, protótipos e tecnologias, uso dos resultados.  
    12. Relatório, protótipos, meios de disseminação dos resultados.  
       - Usos de meios eletrônicos para coleta, documentação e difusão de informações na pesquisa científica.
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

    ### Estatística Experimental
    1. Princípios básicos da experimentação:  
       - Unidade experimental, repetição, casualização e controle local.  
    2. Análise de variância.  
    3. Delineamentos estatísticos:  
       - Inteiramente casualizado, blocos ao acaso, quadrado latino, parcelas subdivididas.  
    4. Testes de comparação de médias e contrastes ortogonais.  
    5. Correlação e regressão simples ou múltipla e análise de covariância.
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
