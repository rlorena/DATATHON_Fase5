from __future__ import print_function
import os
import streamlit as st
import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from plotly.subplots import make_subplots
from PIL import Image






# Configuração da página
st.set_page_config(layout="wide", page_title="Passos Mágicos - DATATHON 2024", page_icon=":bar_chart:")

# Imagem (logo)
st.image("passos_magicos 2024-08-10 173732.png", width=200)

# Configuração de estilo

st.markdown('<style>h1{color: #191970;}</style>', unsafe_allow_html=True)  # MidnightBlue
st.markdown('<style>h2{color: #000080;}</style>', unsafe_allow_html=True)  # Navy
st.markdown('<style>h3{color: #191970;}</style>', unsafe_allow_html=True)  # DodgerBlue
st.markdown('<style>h4{color: #A9A9A9;}</style>', unsafe_allow_html=True)  # DarkGray
st.markdown('<style>h5{color: #696969;}</style>', unsafe_allow_html=True)  # DimGray
st.markdown('<style>h6{color: #708090;}</style>', unsafe_allow_html=True)  # SlateGray
st.markdown('<style>p{color: #000000;}</style>', unsafe_allow_html=True)   # Black

# Título 
st.title('Passos Mágicos- DATATHON 2024')

# Subtítulo
st.subheader('Análise de indicadores Passos Mágicos', divider='rainbow')

# Barra de menus
tab0, tab1, tab2, tab3 = st.tabs(['###### Análises', '###### Predições', '###### Dados Externos', '###### Códigos Utilizados'])

with tab0:
    st.markdown ('## ⭐ Jovens Atendidos: 1348', unsafe_allow_html=True,)


# Importação da base
df = pd.read_csv("PEDE_PASSOS_DATASET_FIAP.csv", sep=";", encoding="Utf-8", thousands='.', decimal=',')

# Substituindo valores nulos por 0
df = df.fillna(0)

# Criando uma função para verificar se um valor é incorreto. Exemplo(V202 e D108)
def verificar(valor):
    return isinstance(valor, str) and re.match(r'^[A-Za-z]\d+', valor)

# Identificando os índices das linhas que contêm valores incorretos em qualquer coluna
indices_para_remover = df.applymap(verificar).any(axis=1)

# Removendo as linhas identificadas
df = df[~indices_para_remover]

# Separando as colunas que serão utilizadas para a análise
df_selecionadas = df[['NOME',
       'ANOS_PM_2020','FASE_TURMA_2020', 'INDE_2020','PEDRA_2020', 
       'IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 
       'FASE_2021', 'INDE_2021', 'PEDRA_2021',
       'IAA_2021','IEG_2021', 'IPS_2021', 'IDA_2021',
       'IPP_2021', 'IPV_2021', 'IAN_2021', 
       'NIVEL_IDEAL_2021',
       'FASE_2022','INDE_2022','PEDRA_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022',
       'IPP_2022', 'IPV_2022', 'IAN_2022',
       'NIVEL_IDEAL_2022']]

# ##### Alterado as colunas Objetc para Float

# Extrai apenas a parte numérica de cada entrada na coluna "FASE_TURMA_2020"
df_selecionadas["FASE_TURMA_2020"] = df_selecionadas["FASE_TURMA_2020"].astype(str).str.extract(r'(\d+)')

# Converte a coluna de volta para numérico.
df_selecionadas["FASE_TURMA_2020"] = pd.to_numeric(df_selecionadas["FASE_TURMA_2020"]).astype("float")

#df_selecionadas.select_dtypes(include='float64').columns

#df_selecionadas.select_dtypes(include='object').columns

#Transformar em float as colunas que são object
colunas_transf_float= df_selecionadas[
    ['ANOS_PM_2020', 'INDE_2020', 'IAA_2020','IEG_2020', 'IPS_2020', 'IDA_2020', 'IPP_2020', 'IPV_2020', 'IAN_2020',
     'INDE_2021', 'INDE_2022', 'IAA_2022', 'IEG_2022', 'IDA_2022', 'IPP_2022',
     'IPV_2022']]

for coluna in colunas_transf_float:
    # Verifica se a coluna é do tipo objeto, o que geralmente indica uma string no pandas
    if df_selecionadas[coluna].dtype == 'object':
        df_selecionadas[coluna] = df_selecionadas[coluna].str.replace(".","").astype(float, errors='ignore')
    else:
        # Se a coluna já for numérica, apenas converte para float sem usar o acessor .str
        df_selecionadas[coluna] = df_selecionadas[coluna].astype(float, errors='ignore')

df_selecionadas["INDE_2021"] = pd.to_numeric(df_selecionadas["INDE_2021"], errors='coerce')


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]].astype(str).applymap(lambda x: x[:2])


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]].replace('na', np.nan)


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]].astype(float)


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
       'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
       'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
       'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
       'IAN_2022',      
]]/10

df_INDES = df_selecionadas[["INDE_2020", "INDE_2021", "INDE_2022"]]
#df_INDES

# #### Renomeando coluna

df_selecionadas.rename(columns={"FASE_TURMA_2020": "FASE_2020"}, inplace=True)

# ### Gráficos Iniciais***********************

# #### Boxplot #############################################################################################################
with tab0:
    # Container 1
    with st.container(border=True):
        col1, col2, col3 =st.columns([1,1,1])
        col4, col5, col6 =st.columns([1,1,1])
        with col3:
            df_INDES = df_INDES[~df_INDES[["INDE_2020", "INDE_2021", "INDE_2022"]].isin([0, '#Nulo'])]  # Remove valores nulos e 0

            # Unpivot the DataFrame para que possamos usar plotly.express
            df_melted = df_INDES.melt(value_vars=["INDE_2020", "INDE_2021", "INDE_2022"], var_name="Ano", value_name="INDE")

            # Construir o boxplot com plotly.express
            fig = px.box(df_melted, x="Ano", y="INDE", title="Distribuição das notas INDE 2020, 2021 e 2022")

            # Ajustar o layout para melhorar a visualização
            fig.update_layout(
                yaxis=dict(title="Nota INDE"),
                xaxis=dict(title="Ano"),font=dict(size=14, color='black', family='Arial'),
                width=800, 
                height=600,
                template='plotly_white'
            )

            fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

            # Mostrar o gráfico
            st.plotly_chart(fig, use_container_width=True)
        
        with col6:
            texto = """
            ### Distribuição das notas INDE 2020, 2021 e 2022:
            O gráfico de boxplot acima mostra a distribuição das notas INDE dos alunos da Passos Mágicos nos anos de 2020, 2021 e 2022.
            - Através dos boxplots, podemos observar a distribuição das notas INDE em cada ano. Os boxplots mostram a mediana, os quartis e os valores extremos (outliers) das notas.
            - Em geral, as notas INDE parecem estar distribuídas de forma semelhante nos três anos, com algumas diferenças nas medianas e nos quartis.
            - O ano de 2021 parece ter uma distribuição ligeiramente mais alta do que os outros anos, com uma mediana mais alta e uma caixa (box) mais alta.
            - Os outliers (valores extremos) são mais comuns nos anos de 2021 e 2022, indicando que algumas notas estão significativamente acima ou abaixo da maioria dos alunos.
            """

            

            # Exibir o texto em Markdown
            st.markdown(texto)


# #### Histograma ##############################################################################################################

# Supondo que df_INDES já esteja carregado

        with col2:
            df_INDES = df_INDES[~df_INDES[["INDE_2020", "INDE_2021", "INDE_2022"]].isin([0, '#Nulo'])]  # Remove valores nulos e 0

            # Unpivot the DataFrame para que possamos usar plotly.express
            df_melted = df_INDES.melt(value_vars=["INDE_2020", "INDE_2021", "INDE_2022"], var_name="Ano", value_name="INDE")

            # Construir o histograma com plotly.express
            fig = px.histogram(df_melted, x="INDE", color="Ano", barmode="overlay", nbins=20, 
                            title="Histograma dos INDEs",
                            labels={"INDE": "Nota INDE", "Ano": "Ano"})

            # Ajustar o layout para melhorar a visualização
            fig.update_layout(
                yaxis=dict(range=[0, 180], title="Contagem"),
                xaxis=dict(title="Nota INDE"),font=dict(size=14, color='black', family='Arial'),    
                legend_title_text='Ano',
                width=800, 
                height=600,
                template='plotly_white'
            )

            # Melhorar a paleta de cores
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

            # Mostrar o gráfico
            st.plotly_chart(fig, use_container_width=True)

        with col5:
            texto = """
            ### Histograma das notas INDE 2020, 2021 e 2022:
            O histograma acima mostra a concentração das notas INDE dos alunos da Passos Mágicos nos anos de 2020, 2021 e 2022.
            - Através do histograma, podemos observar a distribuição das notas INDE em cada ano. As barras representam a contagem de notas em intervalos específicos.
            - Em geral, as notas INDE parecem estar distribuídas de forma semelhante nos três anos, com algumas diferenças nas contagens em cada intervalo.
            - O acúmulo de notas parece estar mais concentrado entre 6 e 8, em todos os anos.
            """
            st.markdown(texto)
# Transformar os dados para formato longo

        with col1:
            df_long = df_selecionadas[["PEDRA_2020", "PEDRA_2021", "PEDRA_2022"]].melt(var_name='Ano', value_name='Nota')

            # Filtrar os dados para excluir 0 e #Nulo
            df_long = df_long[~df_long['Nota'].isin([0, '#NULO!'])]

            # Criar a figura com Plotly Express
            fig = px.histogram(df_long, x='Nota', color='Ano', barmode='group', title="PEDRAS 2020, 2021 e 2022") 

            fig.update_layout(plot_bgcolor='white', font=dict(size=14, color='black', family='Arial'),
                            width=800, height=600, xaxis_title="Nota", yaxis_title="Contagem")
            #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))  

            # Mostrar o gráfico
            st.plotly_chart(fig, use_container_width=True)

        with col4:
            texto = """
            ### PEDRAS 2020, 2021 e 2022:
            O gráfico de histograma acima mostra a distribuição das notas PEDRA dos alunos da Passos Mágicos nos anos de 2020, 2021 e 2022.
            - Através do histograma, podemos observar a distribuição das notas PEDRA em cada ano. As barras representam a contagem de notas em intervalos específicos.
            - Podemos constatar que a classificação que mais se repete ao longo dos anos é a Ametista, seguida pela pedra Ágata.
            """
            st.markdown(texto)


# #### Correlação

# Colunas que serão utilizadas para a análise de correlação
df_correlacao=df_selecionadas[[
    'INDE_2021', 'IAA_2021', 'IEG_2021', 'IPS_2021', 
    'IDA_2021', 'IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
    'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022', 'IPP_2022', 'IPV_2022', 
    'IAN_2022']]


# Calcular a matriz de correlação
df_correlacao = df_correlacao.corr()

# Plotando Gráfico de correlação #########################################################################################################

with tab0:
    # Container 2
    with st.container(border=True):
        col4, col5 = st.columns([2, 1])
        with col4:
            fig = px.imshow(df_correlacao, 
                            labels=dict(color="Correlação"), 
                            x=df_correlacao.columns, 
                            y=df_correlacao.index, 
                            color_continuous_scale='RdBu',  # Usar uma escala de cores válida
                            zmin=-1, zmax=1)
            fig.update_layout(
                title="Correlação entre as variáveis",
                width=1000,
                height=600
            )
            
            st.plotly_chart(fig, use_container_width=True)



with col5:
# Texto em Markdown
    texto = """
    ### Correlação entre as variáveis:
    O gráfico de correlação apresentado mostra a relação entre as variáveis de desempenho dos alunos da Passos Mágicos nos anos de 2021 e 2022. Vamos analisar as correlações mais relevantes:

    ### Correlações Fortes:
    **INDE**: O INDE (Índice de Desenvolvimento Educacional) apresenta uma correlação forte e positiva com a maioria das outras variáveis, especialmente com os indicadores do mesmo ano. Isso indica que o INDE é um bom indicador geral do desempenho dos alunos, refletindo as notas e os indicadores de engajamento, autoavaliação e psicossocial.

    **Indicadores do mesmo ano**: As variáveis do mesmo ano (2021 ou 2022) tendem a ter uma correlação mais forte entre si. Por exemplo, o INDE_2021 tem uma correlação forte com IAA_2021, IEG_2021, IPS_2021 e IDA_2021. Isso é esperado, pois os indicadores do mesmo ano provavelmente se influenciam mutuamente.

    ### Correlações Fracas:
    **Indicadores de anos diferentes**: As variáveis de 2021 e 2022 apresentam correlações mais fracas entre si. Isso sugere que o desempenho dos alunos em um ano não é necessariamente um forte preditor do desempenho no ano seguinte.

    **IPV**: O IPV (Indicador do Ponto de Virada) apresenta correlações mais fracas com as outras variáveis, especialmente com os indicadores de 2021. Isso pode indicar que o IPV é um indicador mais independente, talvez refletindo fatores menos relacionados ao desempenho acadêmico tradicional.
    """

    # Exibir o texto em Markdown
    st.markdown(texto)

# #### Indicadores dos 10 Melhores Alunos

# Filtrando os 20 melhores alunos, conforme nota INDE.
df_melhores = df_selecionadas[["NOME", "INDE_2020","INDE_2021","INDE_2022"]].sort_values(by="INDE_2022", ascending=False).head(10)

# Transformar o DataFrame para o formato longo (long format) necessário para plotly express

df_long = pd.melt(df_melhores, id_vars=['NOME'], value_vars=['INDE_2020', 'INDE_2021', 'INDE_2022'],
                  var_name='Ano', value_name='Indicador')


# #### Médias INDEs(todosos anos) por Aluno
        
# Calcular a média dos indicadores
df_selecionadas['Média_INDE'] = df_selecionadas.apply(lambda x: (x["INDE_2020"] + x["INDE_2021"] + x["INDE_2022"]) / 3, axis=1)

# Ordenar o DataFrame com base na média calculada em ordem decrescente
df_selecionadas = df_selecionadas.sort_values(by='Média_INDE', ascending=False)


# Calcular a média dos indicadores
df_selecionadas['Média_INDE'] = df_selecionadas.apply(lambda x: (x["INDE_2020"] + x["INDE_2021"] + x["INDE_2022"]) / 3, axis=1)

# Ordenar o DataFrame com base na média calculada em ordem decrescente
df_selecionadas = df_selecionadas.sort_values(by='Média_INDE', ascending=False)

# Selecionar as 10 primeiras linhas do DataFrame ordenado
top_10 = df_selecionadas.head(10)

# Criar o gráfico de barras agrupadas  ###################################################################################################

with tab0:
    # Container 3
    with st.container(border=True):
        col6, col7, col8 = st.columns([1,1,1])
        col14, col15 = st.columns([2,1])
# Construir o gráfico de barras com Plotly Express ######################################################################################################

        with col8:
                
            fig = px.bar(top_10, x='NOME', y='Média_INDE', title='Top 10 Médias INDE', labels={'NOME': 'Nome', 'Média_INDE': 'Média INDE'}, color='NOME')

            # Ajustar o layout para melhorar a visualização
            fig.update_layout(xaxis_tickangle=-45, width=600, height=500, font=dict(size=14, color='black', family='Arial'),plot_bgcolor='white')

            #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            # Mostrar o gráfico
            st.plotly_chart(fig, use_container_width=True)

# #### Função para o cálculo do INDE 

# Função para calcular o INDE com base nas notas e critérios de cada fase
def calcular_INDE_fases_2020(row):
    if row["FASE_2020"] <= 7:
        INDE = (row["IAN_2020"] * 0.1 + row["IDA_2020"] * 0.2 + row["IEG_2020"] * 0.2 +
                row["IAA_2020"] * 0.1 + row["IPS_2020"] * 0.1 + row["IPP_2020"] * 0.1 + row["IPV_2020"] * 0.2)
    else:
        INDE = (row["IAN_2020"] * 0.1 + row["IDA_2020"] * 0.4 + row["IEG_2020"] * 0.2 +
                row["IAA_2020"] * 0.1 + row["IPS_2020"] * 0.2)
    return INDE

def calcular_INDE_fases_2021(row):
    if row["FASE_2021"] <= 7:
        INDE = (row["IAN_2021"] * 0.1 + row["IDA_2021"] * 0.2 + row["IEG_2021"] * 0.2 +
                row["IAA_2021"] * 0.1 + row["IPS_2021"] * 0.1 + row["IPP_2021"] * 0.1 + row["IPV_2021"] * 0.2)
    else:
        INDE = (row["IAN_2021"] * 0.1 + row["IDA_2021"] * 0.4 + row["IEG_2021"] * 0.2 +
                row["IAA_2021"] * 0.1 + row["IPS_2021"] * 0.2)
    return INDE

def calcular_INDE_fases_2022(row):
    if row["FASE_2022"] <= 7:
        INDE = (row["IAN_2022"] * 0.1 + row["IDA_2022"] * 0.2 + row["IEG_2022"] * 0.2 +
                row["IAA_2022"] * 0.1 + row["IPS_2022"] * 0.1 + row["IPP_2022"] * 0.1 + row["IPV_2022"] * 0.2)
    else:
        INDE = (row["IAN_2022"] * 0.1 + row["IDA_2022"] * 0.4 + row["IEG_2022"] * 0.2 +
                row["IAA_2022"] * 0.1 + row["IPS_2022"] * 0.2)
    return INDE

df_selecionadas['INDE_2020Novo'] = df_selecionadas.apply(calcular_INDE_fases_2020, axis=1)
df_selecionadas['INDE_2021Novo'] = df_selecionadas.apply(calcular_INDE_fases_2021, axis=1)
df_selecionadas['INDE_2022Novo'] = df_selecionadas.apply(calcular_INDE_fases_2022, axis=1)

# #### GroupBy 

# Agrupa os dados por INDE_2020 e calcula a média de FASE_TURMA_2020
df_agrupado_fase20 = df_selecionadas["INDE_2020"].groupby(df_selecionadas["FASE_2020"]).mean()

# Exibe o DataFrame resultante
pd.DataFrame(df_agrupado_fase20)


# Agrupa os dados por INDE_2020 e calcula a média de FASE_TURMA_2020
df_agrupado_fase21 = df_selecionadas["INDE_2021"].groupby(df_selecionadas["FASE_2021"]).mean()

# Exibe o DataFrame resultante
df_agrupado_fase21 = pd.DataFrame(df_agrupado_fase21)


# Agrupa os dados por INDE_2020 e calcula a média de FASE_TURMA_2020
df_agrupado_fase22 = df_selecionadas["INDE_2022"].groupby(df_selecionadas["FASE_2022"]).mean()

# Exibe o DataFrame resultante
df_agrupado_fase22 = pd.DataFrame(df_agrupado_fase22)


# #### Média dos INDEs por fase

# Agrupar por 'FASE_2020' e calcular a média dos INDEs de 2020, 2021 e 2022
df_agrupado_INDES = df_selecionadas.groupby("FASE_2020")[["INDE_2020", "INDE_2021", "INDE_2022"]].mean()

# Converter o resultado em um DataFrame
df_agrupado_INDES = pd.DataFrame(df_agrupado_INDES)


fig = px.line(df_agrupado_INDES, x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2020"], title="Média das notas INDE por Fase de Turma")
# Removido para usar add_scatter e adicionar um nome à primeira série de dados também

# Adicionando a primeira série de dados com um nome
fig.add_scatter(x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2020"], mode='lines', name='INDE 2020')

# Continuação com as outras séries de dados
fig.add_scatter(x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2021"], mode='lines', name='INDE 2021')
fig.add_scatter(x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2022"], mode='lines', name='INDE 2022')

# Atualizando o layout do gráfico
fig.update_layout(
    xaxis_title="Fase de Turma",
    yaxis_title="Média das Notas INDE",
    plot_bgcolor='white',
    font=dict(size=14, color='black', family='Arial')
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

#fig.show()

df_agrupado_INDESNovos= df_selecionadas[["FASE_2020", "INDE_2020Novo","INDE_2021Novo", "INDE_2022Novo"]]
df_agrupado_INDESNovos.set_index("FASE_2020", inplace=True)
#df_agrupado_INDESNovos


# #### "Comparação das notas INDE 2020, 2021 e 2022"


df_INDES_todos = df_selecionadas[["FASE_2020","INDE_2020", "INDE_2020Novo","INDE_2021","INDE_2021Novo","INDE_2022","INDE_2022Novo"]]
df_INDES_todos.rename(columns={"FASE_2020": "FASE"}, inplace=True)


# Criando subplots com 3 colunas (uma para cada ano) ############################################################################
with tab0:
    # Container 4
    with st.container(border=True):
        st.subheader("Comparação dos resultados INDE 2020, 2021 e 2022 (Cálculo Passos x Cálculo Novo)")
        col9, col10 = st.columns([2, 1])
        col11, col12, col13 = st.columns([1, 1, 1])
        

        with col9:

            fig = make_subplots(rows=1, cols=3, subplot_titles=("2020", "2021", "2022"))

            # Calculando as médias
            media_2020 = df_INDES_todos["INDE_2020"].mean()
            media_2020_novo = df_INDES_todos["INDE_2020Novo"].mean()
            media_2021 = df_INDES_todos["INDE_2021"].mean()
            media_2021_novo = df_INDES_todos["INDE_2021Novo"].mean()
            media_2022 = df_INDES_todos["INDE_2022"].mean()
            media_2022_novo = df_INDES_todos["INDE_2022Novo"].mean()

            # Adicionando os histogramas para 2020
            fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2020] * len(df_INDES_todos["FASE"]), name="INDE 2020", opacity=1, marker_color='blue'), row=1, col=1)
            fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2020_novo] * len(df_INDES_todos["FASE"]), name="INDE 2020 Novo", opacity=1, marker_color='lightblue'), row=1, col=1)

            # Adicionando os histogramas para 2021
            fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2021] * len(df_INDES_todos["FASE"]), name="INDE 2021", opacity=1, marker_color='green'), row=1, col=2)
            fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2021_novo] * len(df_INDES_todos["FASE"]), name="INDE 2021 Novo", opacity=1, marker_color='lightgreen'), row=1, col=2)

            # Adicionando os histogramas para 2022
            fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2022] * len(df_INDES_todos["FASE"]), name="INDE 2022", opacity=1, marker_color='red'), row=1, col=3)
            fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2022_novo] * len(df_INDES_todos["FASE"]), name="INDE 2022 Novo", opacity=1, marker_color='lightcoral'), row=1, col=3)

            # Atualizando o layout do gráfico
            fig.update_layout(
                title_text="Comparação das notas INDE 2020, 2021 e 2022 (Cálculo Passos x Cálculo Novo)",
                xaxis_title="Fases",
                yaxis_title="Notas INDE",
                barmode='group', plot_bgcolor='white',font=dict(size=14, color='black', family='Arial')
            )

            #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

            st.plotly_chart(fig, use_container_width=True)


## Calculando a média por fase
media_por_fase = df_INDES_todos.groupby('FASE')[['INDE_2020', 'INDE_2020Novo', 'INDE_2021', 'INDE_2021Novo', 'INDE_2022', 'INDE_2022Novo']].mean()

# #### Média das Notas do INDEs de cada ano

df_INDES_todos.describe()

# Dados das médias
labels = ['INDE_2020', 'INDE_2020Novo', 'INDE_2021', 'INDE_2021Novo', 'INDE_2022', 'INDE_2022Novo']
means = [6.709491, 5.530289, 6.837427, 2.960015, 4.463205, 4.065504]

# Criando um DataFrame com os dados
df_medias_inde = pd.DataFrame({
    'Ano': labels,
    'Média': means
})
# #### Pedras por Ano

# Remover valores sem classificação (nulos)
df_selecionadas = df_selecionadas.dropna(subset=["PEDRA_2020", "PEDRA_2021", "PEDRA_2022"])

# Contando os valores e resetando o índice para transformar em DataFrame
contagem_pedra_2020 = df_selecionadas["PEDRA_2020"].value_counts().reset_index()
contagem_pedra_2020.columns = ['PEDRA_2020', 'count']
contagem_pedra_2020 = contagem_pedra_2020[(contagem_pedra_2020['PEDRA_2020'] != 0) & (contagem_pedra_2020['PEDRA_2020'] != '#NULO!')]  # Remover zeros e #NULO!

contagem_pedra_2021 = df_selecionadas["PEDRA_2021"].value_counts().reset_index()
contagem_pedra_2021.columns = ['PEDRA_2021', 'count']
contagem_pedra_2021 = contagem_pedra_2021[(contagem_pedra_2021['PEDRA_2021'] != 0) & (contagem_pedra_2021['PEDRA_2021'] != '#NULO!')]  # Remover zeros e #NULO!

contagem_pedra_2022 = df_selecionadas["PEDRA_2022"].value_counts().reset_index()
contagem_pedra_2022.columns = ['PEDRA_2022', 'count']
contagem_pedra_2022 = contagem_pedra_2022[(contagem_pedra_2022['PEDRA_2022'] != 0) & (contagem_pedra_2022['PEDRA_2022'] != '#NULO!')]  # Remover zeros e #NULO!

# Criando o gráfico de barras com plotly.graph_objects ###########################################################################################
with tab0:
  
        with col10:
            fig = go.Figure()

            # Adicionando as barras
            fig.add_trace(go.Bar(
                x=df_medias_inde['Ano'],
                y=df_medias_inde['Média'],
                marker_color=['#1f77b4', '#aec7e8', '#1f77b4', '#aec7e8', '#1f77b4', '#aec7e8']  # Azul escuro e azul claro
            ))

            # Rotacionando as labels do eixo x e aplicando cores diferentes
            fig.update_layout(
                xaxis_tickangle=-45,
                title_text="Médias das Notas INDE por Ano (Cálculo Passos x Cálculo Novo)",
                xaxis_title="INDE por Ano (Cálculo Passos x Cálculo Novo)",
                yaxis_title="Média INDE", font=dict(size=14, color='black', family='Arial'),
                plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
                paper_bgcolor='rgba(0,0,0,0)'  # Fundo transparente
            )
            #fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            # Exibindo o gráfico
            st.plotly_chart(fig, use_container_width=True)

            with col11:
                st.image("Calculo_INDE.png")
                # Texto em Markdown
                texto = """
                ### Cálculo Novo:
                Nos gráficos acima podemos perceber o impacto gerado com os resultados obtidos pelo novo cálculo, para chegar aos valores apresentados, foi necessário realizar uma análise detalhada dos dados e ajustar os cálculos conforme as regras estabelecidas pela Passos Mágicos, conforme apresentado na imagem acima "Composição do Índice de Desenvolvimento Educacional (INDE)".
                """
               
                # Exibir o texto em Markdown
                st.markdown(texto)  

            with col12:
                # Texto em Markdown
                texto = """
                ### Considerações:
                Considerando os resultados do novo cálculo, podemos constatar que existe uma diferença significativa entre os valores obtidos, essa diferença pode ser explicada pela forma como os dados foram tratados e analisados, porém, é importante ressaltar que foi realizado consoante as regras estabelecidas pela Passos Mágicos.
                - O processo foi muito desafiador, ao longo da análise foi necessário realizar diversos ajustes e correções, muitos dados foram tratados e ajustados para garantir a qualidade das análises realizadas.
                """

                # Exibir o texto em Markdown
                st.markdown(texto) 
            
            with col13:
                st.image("Tabela_Passos_2.png")
                # Texto em Markdown
                texto = """
                ### PONTOS DE ATENÇÃO:
                Acima temos um recorte da tabela disponibilizada pela Passos Mágicos, onde de forma clara é possível identificar alguns pontos de atenção:
                
                
                - A importância de padronizar a entrada de dados para evitar inconsistências.
                - Tratar os dados de forma adequada para garantir a qualidade das análises realizadas.
                - Classificar corretamente os tipos de dados, definindo se são numéricos ou categóricos, para evitar erros de interpretação.
                - Realizar a limpeza dos dados, removendo valores nulos e tratando possíveis outliers.
                - Documentar o processo de análise de dados, registrando as etapas realizadas e os resultados obtidos.
                
                
                """


                # Exibir o texto em Markdown
                st.markdown(texto) 


# #### Quantidade de Alunos em Atividade

# Total de Alunos cadastrados na Base de Dados
contagem_total_alunos = df_selecionadas["NOME"].nunique()

# Imprimir o resultado
print("Contagem total de alunos:")
print(contagem_total_alunos)

# Contar a quantidade de alunos AVALIADOS por cada ano do INDE
contagem_inde_2020_unicos = df_selecionadas.loc[df_selecionadas["INDE_2020"] > 0, "NOME"].nunique()
contagem_inde_2021_unicos = df_selecionadas.loc[df_selecionadas["INDE_2021"] > 0, "NOME"].nunique()
contagem_inde_2022_unicos = df_selecionadas.loc[df_selecionadas["INDE_2022"] > 0, "NOME"].nunique()

# Imprimir os resultados
print("Contagem de alunos únicos em 2020:")
print(contagem_inde_2020_unicos)
print("\nContagem de alunos únicos em 2021:")
print(contagem_inde_2021_unicos)
print("\nContagem de alunos únicos em 2022:")
print(contagem_inde_2022_unicos)

df_evolucao = df_selecionadas[['NOME', 'INDE_2020', 'INDE_2021', 'INDE_2022']]

# Remover linhas com valores NaN
df_evolucao = df_evolucao.dropna()

# Calcular a média do INDE para cada aluno
df_evolucao['INDE_MEDIA'] = df_evolucao[['INDE_2020', 'INDE_2021', 'INDE_2022']].mean(axis=1)


# Selecionar os 10 melhores alunos com base na média do INDE
df_melhores_alunos = df_evolucao.nlargest(10, 'INDE_MEDIA')

# Transformar os dados para o formato longo
df_melhores_alunos_long = df_melhores_alunos.melt(id_vars=['NOME'], value_vars=['INDE_2020', 'INDE_2021', 'INDE_2022'], 
                                                var_name='Ano', value_name='INDE')

#TABELA Evolução ###############################################################################################################################
with tab0:
    
        with col6:
            st.subheader("Evolução dos Alunos")

            st.markdown(""" ###### **Tabela com a evolução dos alunos(ordenada pela média dos INDEs).** """)

            st.markdown(
                """
                <style>
                .center-table {
                    display: flex;
                    justify-content: center;
                }
                </style>
                """,
                unsafe_allow_html=True)
            st.markdown('<div class="center-table">', unsafe_allow_html=True)
            st.dataframe(df_evolucao.head(10), width=600, height=400)


# Plotar a evolução do INDE para os melhores alunos ##############################################################################################

with tab0:
    # Container 3
    with st.container(border=True):
            
        with col14:
            
            fig = px.line(df_melhores_alunos_long, x='Ano', y='INDE', color='NOME', markers=True, 
                        title='Evolução do INDE dos 10 Melhores Alunos')

            fig.update_layout(xaxis_title='Ano', yaxis_title='INDE', legend_title_text='Aluno', width=1000, height=600, plot_bgcolor='white', font=dict(size=14, color='black', family='Arial'))
            fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
            st.plotly_chart(fig, use_container_width=True)

        with col15:
            # Texto em Markdown
            texto = """
            ### Melhores Alunos:
            Os gráficos demonstram a evolução do INDE (Índice de Desenvolvimento Educacional) dos 10 melhores alunos ao longo dos anos de 2020, 2021 e 2022. Podemos observar que a maioria dos alunos apresentou um crescimento consistente em seus indicadores, refletindo um bom desempenho acadêmico ao longo do tempo.
            
                        """

            # Exibir o texto em Markdown
            st.markdown(texto)
                
# #### Ponto de Virada  ## 

df_selecionadas1 = df_selecionadas.merge(df[["NOME", "PONTO_VIRADA_2020", "PONTO_VIRADA_2021", "PONTO_VIRADA_2022"]], on="NOME", how="left")

# #### Transformar as colunas "PONTO_VIRADA_2020 , 2121 E 2022" com LabelEncoder

df_selecionadas1["PONTO_VIRADA_2020"] = df_selecionadas1["PONTO_VIRADA_2020"].astype(str)
df_selecionadas1["PONTO_VIRADA_2021"] = df_selecionadas1["PONTO_VIRADA_2021"].astype(str)
df_selecionadas1["PONTO_VIRADA_2022"] = df_selecionadas1["PONTO_VIRADA_2022"].astype(str)

from sklearn.preprocessing import LabelEncoder

# Inicializar o LabelEncoder
label_encoder = LabelEncoder()

# Função para aplicar o LabelEncoder apenas nos valores diferentes de zero ou nulo
def encode_non_zero_null(df, column):
    mask = (df[column] != 0) & (df[column].notnull()) & (df[column] != '#NULO!')
    df.loc[mask, f"{column}_encoded"] = label_encoder.fit_transform(df.loc[mask, column])

# Aplicar a função para cada coluna
encode_non_zero_null(df_selecionadas1, "PONTO_VIRADA_2020")
encode_non_zero_null(df_selecionadas1, "PONTO_VIRADA_2021")
encode_non_zero_null(df_selecionadas1, "PONTO_VIRADA_2022")

print(df_selecionadas1[["PONTO_VIRADA_2020_encoded", "PONTO_VIRADA_2021_encoded", "PONTO_VIRADA_2022_encoded"]].head())

# ### MODELO DE PREDIÇÃO #######################################################################################################################


## Fazendo o Balenceamento das Classes 
df_modelo = df_selecionadas1.copy()

#Dropando as colunas encoded
df_modelo.drop(columns=["PONTO_VIRADA_2020_encoded", "PONTO_VIRADA_2021_encoded", "PONTO_VIRADA_2022_encoded"], inplace=True)

df_modelo_limpo = df_modelo
# Remover valores nulos
df_modelo_limpo = df_modelo_limpo.dropna(subset=["PONTO_VIRADA_2022"])

# Removendo valores "0"
df_modelo_limpo = df_modelo_limpo[df_modelo_limpo["PONTO_VIRADA_2022"] != "0"]

# convertendo os valores SIM e NÃO para 1 e 0	
df_modelo_limpo[["PONTO_VIRADA_2020_encoding"]] = df_modelo_limpo[["PONTO_VIRADA_2020"]].replace({"Sim": 1, "Não": 0}).astype(int)
df_modelo_limpo[["PONTO_VIRADA_2021_encoding"]] = df_modelo_limpo[["PONTO_VIRADA_2021"]].replace({"Sim": 1, "Não": 0}).astype(int)
df_modelo_limpo[["PONTO_VIRADA_2022_encoding"]] = df_modelo_limpo[["PONTO_VIRADA_2022"]].replace({"Sim": 1, "Não": 0}).astype(int)



## Aplicando o SMOTE para balancear as classes################################
# Importar as bibliotecas necessárias
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


X = df_modelo_limpo[['IPV_2020', 'IPV_2021', 'IPV_2022']]
y = df_modelo_limpo['PONTO_VIRADA_2022_encoding']


# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Aplicar a imputação de valores faltantes nos dados de treino
imputer = SimpleImputer(strategy='mean')  # ou 'median', 'most_frequent', etc.
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Aplicar o SMOTE para balancear as classes nos dados de treino
smote = SMOTE(random_state=42, sampling_strategy="minority")
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_imputed, y_train)

# Verificar o balanceamento das classes
print(y_train_resampled.value_counts())


#  Contar a frequência de cada classe
contagem_classes = df_modelo_limpo["PONTO_VIRADA_2022_encoding"].value_counts()

# Contagem das classes
class_counts = y_train_resampled.value_counts().reset_index()
class_counts.columns = ['Classe', 'Contagem']

# Gráfico de barras com Plotly Express
fig = px.bar(class_counts, x='Classe', y='Contagem', title='Contagem das Classes em y_train_resampled', 
             labels={'Classe': 'Classe', 'Contagem': 'Contagem'}, 
             color='Classe', 
             color_continuous_scale='viridis', 
             template='plotly_white')

# Configurar o layout do gráfico
fig.update_layout(
    xaxis_title='Classe',
    yaxis_title='Contagem',
    template='plotly_white'
)

# Mostrar o gráfico no Streamlit
with tab1:
    with st.container(border=True):
        st.subheader("Balanceamento das Classes")
        st.write("O gráfico de barras abaixo mostra o balanceamento das classes após a aplicação do SMOTE. Podemos observar que as classes estão balanceadas, o que é importante para o treinamento de modelos de aprendizado de máquina.")
        st.plotly_chart(fig)



# #### MODELO ESCOLHIDO - ÁRVORE DE DECISÃO ############################################
#### Treinando o MODELO ###############################################################
from sklearn.tree import DecisionTreeClassifier


# Tratar dados nulos e zeros
features3 = df_modelo_limpo[['IPV_2020', 'IPV_2021', 'IPV_2022']].fillna(0)
labels3 = df_modelo_limpo["PONTO_VIRADA_2022_encoding"]


# Inicializar o imputer para substituir valores NaN pela média
imputer = SimpleImputer(strategy='mean')

# Aplicar o imputer aos dados de treino e teste
X_train_imputed = imputer.fit_transform(X_train_resampled)
X_test_imputed = imputer.transform(X_test)

# Inicializar o modelo de Árvore de Decisão
dt_model = DecisionTreeClassifier(random_state=42)  # pode ajustar parâmetros como 'max_depth', 'min_samples_split', etc.

# Treinar o modelo
dt_model.fit(X_train_imputed, y_train_resampled)

# Fazer previsões nos dados de teste
y_pred = dt_model.predict(X_test_imputed)

# Criar uma cópia do DataFrame 
X_test_copy = X_test.copy()

# Adicionar as predições ao DataFrame de teste
X_test_copy['PREDITO'] = y_pred

# Adicionar os valores reais ao DataFrame de teste
X_test_copy['REAL'] = y_test.values

# Mapear os valores preditos e reais de 1 para "SIM" e 0 para "NÃO"
mapping = {1: "SIM", 0: "NÃO"}
X_test_copy['PREDITO'] = X_test_copy['PREDITO'].map(mapping)
X_test_copy['REAL'] = X_test_copy['REAL'].map(mapping)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Acurácia: {accuracy}')
report_df_modelo_limpo = pd.DataFrame(report).transpose()  # Converter para DataFrame
print(report_df_modelo_limpo)

# Exibir os valores reais e previstos
print(X_test_copy[['REAL', 'PREDITO']])


# Plotar a matriz de confusão #######################################################################################
with tab1:
    st.subheader("Modelo para predizer se o aluno atingiu o ponto de virada")
    st.write("O modelo de Árvore de Decisão foi treinado para prever se um aluno atingiu o ponto de virada com base nos indicadores IPV de 2020, 2021 e 2022. O modelo foi avaliado com base na acurácia, no relatório de classificação e na matriz de confusão.") 
with tab1:
    with st.container(border=True):
        col15, col16 = st.columns([1, 1])
        with col16: 
            plt.figure(figsize=(4, 2))
            sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=dt_model.classes_, yticklabels=dt_model.classes_)
            plt.xlabel('Predito')
            plt.ylabel('Verdadeiro')
            plt.title('Matriz de Confusão')
            st.pyplot(plt)

# Avaliação do Modelo 

# Avaliar o modelo
with tab1:
    with st.container(border=True):
        col17, col18, col19= st.columns([1, 1, 1])
        with col18:
            st.subheader("Avaliação do Modelo")
            
            st.write('Relatório de Classificação:')
            st.dataframe(report_df_modelo_limpo, width=400)

        with col17:
            st.write('Valores Reais e Previstos:')
            st.dataframe(X_test_copy[['REAL', 'PREDITO']], width=400, height=750)

        with col18:
            st.write('''
            #### Sobre os Resultados do Modelo:
            O modelo escolhido para prever se um aluno atingiu o ponto de virada é uma Árvore de Decisão. Ele foi treinado com base nos indicadores IPV de 2020, 2021 e 2022.

            Como podemos observar, o modelo apresentado demonstra um desempenho ótimo na tarefa de prever se um aluno atingiu o ponto de virada.

            ➡️ Alta Acurácia: O modelo apresenta uma acurácia de 0.9942, o que indica um alto nível de precisão nas previsões. Isso sugere que o modelo está aprendendo bem os padrões dos dados e conseguindo prever com sucesso se um aluno atingiu o ponto de virada.

            ➡️ A matriz de confusão mostra que o modelo está classificando corretamente a maioria dos alunos que não atingiram o ponto de virada (153 casos) e também está acertando a maioria dos alunos que atingiram o ponto de virada (19 casos).

            ➡️ Poucos Erros: O modelo comete poucos erros, principalmente na identificação de alunos que não atingiram o ponto de virada (1 caso).
         ''' )

        with col19:   
            st.write('''
            #### Benefícios de utilizar um modelo de predição:
                    
            * **Identificação do Ponto de Virada:** O modelo permite identificar alunos em risco de não atingir o ponto de virada precocemente, antes que eles abandonem o programa.
            * **Identificação Precoce de abandono:** Pode ser utilizado para identificar alunos em risco de abandono precocemente, antes que eles abandonem o programa.
            * **Intervenção Direcionada:** A Passos Mágicos pode usar as previsões do modelo para direcionar ações de apoio e acompanhamento para os alunos em risco, como:
            * **Mentoria:**  Oferecer mentoria individualizada para ajudar os alunos a superar as dificuldades.
            * **Acompanhamento:**  Monitorar o progresso dos alunos de forma mais próxima.
            * **Recursos:**  Fornecer recursos adicionais, como materiais de estudo ou apoio psicológico.
            * **Eficiência:**  O modelo pode ajudar a Passos Mágicos a otimizar seus recursos, direcionando o apoio para os alunos que mais precisam.
        ''')

            st.subheader("Conclusão")
            st.write('''
            
            O modelo de Árvore de Decisão apresentado demonstra um desempenho excelente na tarefa de prever se um aluno atingiu o ponto de virada. Sua alta acurácia, poucos erros e interpretabilidade o tornam uma ferramenta valiosa para a Passos Mágicos. No entanto, é importante ter cuidado com o desequilíbrio de classes e realizar uma análise contextual dos erros. 
            
            A Passos Mágicos pode continuar a melhorar o modelo, realizando a validação cruzada, incluindo novos indicadores e investigando as causas dos erros.
        ''')

# ## Tabela #########################################################################################################
# Verificar se X_test e y_test são DataFrames ou Series
if isinstance(X_test, (pd.DataFrame, pd.Series)) and isinstance(y_test, (pd.DataFrame, pd.Series)):
    # Concatenar X_test e y_test ao longo do eixo das colunas
    resultado = pd.concat([X_test, y_test], axis=1)
    
    # Alterar o nome da coluna
    resultado.rename(columns={'PONTO_VIRADA_2022_encoding': 'PONTO_VIRADA_2022_Previsto'}, inplace=True)
    
    # Aplicar o mapeamento na nova coluna
    resultado['PONTO_VIRADA_2022_Previsto'] = resultado['PONTO_VIRADA_2022_Previsto'].map({1: "SIM", 0: "NÃO"})
    print(pd.DataFrame(resultado))

else:
    print("X_test e y_test devem ser DataFrame ou Series do pandas.")

with tab1:
        with col15:
            st.write("Resultado da Predição")
            st.dataframe(resultado, width=600, height=400)




#############################################################################################################################

# IDEB - Índice de Desenvolvimento da Educação Básica
df_IDEB = pd.read_csv("educacao_ideb_mun.csv", sep=";", encoding="latin1")
df_IDEB_mogi_guacu = df_IDEB[df_IDEB["Localidade"] == "Mogi Guaçu"]


with tab2:
    with st.container(border=True):
        st.subheader("Dados do IDEB de Mogi Guaçu")
        st.write("O IDEB é um indicador de qualidade educacional que combina informações sobre o rendimento escolar e o fluxo escolar dos alunos. Ele é calculado com base nas notas das avaliações de Matemática e Língua Portuguesa e na taxa de aprovação dos estudantes.")
        st.write("A tabela abaixo mostra os dados do IDEB de Mogi Guaçu, incluindo as médias de Matemática e Língua Portuguesa, as notas do IDEB e as metas projetadas para os anos de 2017 a 2021.")
        st.write("Os dados são provenientes do INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira) e podem ser encontrados no portal do INEP.")
        st.write("*SAEB: Sistema de Avaliação da Educação Básica.")
        st.write("*IDEB: Índice de Desenvolvimento da Educação Básica.")
        st.write("*Prova Brasil: Avaliação do SAEB aplicada a cada dois anos para alunos do 5º e 9º ano do Ensino Fundamental.")
        st.write("*IDEB projetado: Meta estabelecida para o IDEB de cada escola com base nos resultados anteriores.")
        st.write("*Nota: As médias de Matemática e Língua Portuguesa são calculadas a partir das notas dos alunos na Prova Brasil.")
        st.write("*Metas projetadas: Notas que as escolas deveriam atingir para alcançar as metas do IDEB.")
        st.write("*Nota IDEB: Nota final do IDEB, calculada com base nas médias de Matemática e Língua Portuguesa e na taxa de aprovação dos alunos.")
        st.write("*Taxa de Aprovação: Percentual de alunos aprovados em relação ao total de alunos avaliados.")
        st.write("fonte: https://www.gov.br/inep/pt-br")
        st.dataframe(df_IDEB_mogi_guacu)

# Matrículas por Município, Ano, Nível de ensino e Rede de atendimento
df_MATRICULAS =pd.read_csv("Matrículas por Município, Ano, Nível de ensino e Rede de atendimento.csv", sep=";", encoding="latin1")

#MATRICULAS EM MOGI GUAÇU
df_matriculas_mogi_guacu = df_MATRICULAS.loc[df_MATRICULAS['cod_ibge'] == 3515103]
# Substituir o código do município pelo nome
df_matriculas_mogi_guacu["cod_ibge"] = df_matriculas_mogi_guacu["cod_ibge"].apply(lambda x: "Mogi Guaçu" if x == 3515103 else x)
# Remover vírgulas dos valores numéricos
df_matriculas_mogi_guacu["ano"] = df_matriculas_mogi_guacu["ano"].apply(lambda x: str(x).replace(",", "") if isinstance(x, int) else x)

with tab2:
    with st.container(border=True):
        st.subheader("Matrículas por Município, Ano, Nível de Ensino e Rede de Atendimento")
        st.write("A tabela abaixo mostra o número de matrículas por município, ano, nível de ensino e rede de atendimento. Os dados são provenientes do Censo Escolar, realizado anualmente pelo INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira).")
        st.write("O Censo Escolar é a principal pesquisa estatística educacional brasileira. Ele coleta informações sobre as escolas, turmas, alunos e profissionais da educação básica no país.")
        st.write("Os dados podem ser encontrados no portal do INEP.")
        st.write("fonte: https://www.gov.br/inep/pt-br")
        st.dataframe(df_matriculas_mogi_guacu)

# População em idade escolar por Município, Ano e Nível de ensino

df_idade_escolar = pd.read_csv("pop_idade_escolar_2000a2050_esp.csv", sep=";", encoding="latin1")

#POPULAÇÃO EM IDADE ESCOLAR EM MOGI GUAÇU
df_idade_escolar_mogi_guacu = df_idade_escolar.loc[df_idade_escolar['cod_ibge'] == 3515103]
# Substituir o código do município pelo nome
df_idade_escolar_mogi_guacu["cod_ibge"] = df_idade_escolar_mogi_guacu["cod_ibge"].apply(lambda x: "Mogi Guaçu" if x == 3515103 else x)
df_idade_escolar_mogi_guacu["ano"] = df_idade_escolar_mogi_guacu["ano"].apply(lambda x: str(x).replace(",","") if isinstance(x, int) else x)
pd.DataFrame(df_idade_escolar_mogi_guacu)

with tab2:
    with st.container(border=True):
        st.subheader("População em Idade Escolar por Município, Ano e Nível de Ensino")
        st.write("A tabela abaixo mostra a população em idade escolar por município, ano e nível de ensino. Os dados são provenientes do IBGE (Instituto Brasileiro de Geografia e Estatística) e do IPEA (Instituto de Pesquisa Econômica Aplicada).")
        st.write("As informações são fundamentais para o planejamento e a gestão da educação, pois permitem estimar a demanda por vagas nas escolas e identificar possíveis desafios e oportunidades na área da educação.")
        st.write("Os dados podem ser encontrados nos portais do IBGE e do IPEA.")
        st.write("fonte: https://www.ibge.gov.br/ e https://www.ipea.gov.br/")
        st.dataframe(df_idade_escolar_mogi_guacu)

df_evolucao = pd.DataFrame(df_evolucao)

# Ordenar os valores da coluna INDE_2022 em ordem crescente
melhores_INDE_2022 = df_evolucao.sort_values(by="INDE_2022", ascending=False)

# Exibir o DataFrame ordenado
melhores_INDE_2022 = melhores_INDE_2022.head(10)


# Supondo que df_evolucao já seja um DataFrame
df_evolucao = pd.DataFrame(df_evolucao)

# Ordenar os valores da coluna INDE_2022 em ordem decrescente e selecionar os 10 melhores
melhores_INDE_2022 = df_evolucao.sort_values(by="INDE_2022", ascending=False).head(10)

# Transformar o DataFrame para o formato longo
melhores_INDE_2022_long = melhores_INDE_2022.melt(id_vars=['NOME'], value_vars=['INDE_2020', 'INDE_2021', 'INDE_2022'],
                                                  var_name='Ano', value_name='INDE')


with tab0:
    # Container 3
    with col7:
        # Construir o gráfico de barras agrupadas com Plotly Express
        fig = px.bar(melhores_INDE_2022_long, x='NOME', y='INDE', color='Ano', barmode='group',
                     title="Histórico dos alunos com melhores INDEs em 2022",
                     labels={'NOME': 'Nome', 'INDE': 'Indicador'})

        # Ajustar o layout para melhorar a visualização
        fig.update_layout(xaxis_tickangle=-45, width=800, height=500, font=dict(size=14, color='black', family='Arial'), plot_bgcolor='white', bargap=0.15)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
        fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

        # Mostrar o gráfico
        st.plotly_chart(fig, use_container_width=True)




        #####################################################################################################################
        ##### APRESENTAÇÃO DO CÓDIGO NA PÁGINA STREAMLIT #####################################################################

codigo ='''
from __future__ import print_function
import os
import streamlit as st
import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from plotly.subplots import make_subplots
from PIL import Image






# Configuração da página
st.set_page_config(layout="wide", page_title="Passos Mágicos - DATATHON 2024", page_icon=":bar_chart:")

# Imagem (logo)
st.image("passos_magicos 2024-08-10 173732.png", width=200)

# Configuração de estilo

st.markdown('<style>h1{color: #191970;}</style>', unsafe_allow_html=True)  # MidnightBlue
st.markdown('<style>h2{color: #000080;}</style>', unsafe_allow_html=True)  # Navy
st.markdown('<style>h3{color: #191970;}</style>', unsafe_allow_html=True)  # DodgerBlue
st.markdown('<style>h4{color: #A9A9A9;}</style>', unsafe_allow_html=True)  # DarkGray
st.markdown('<style>h5{color: #696969;}</style>', unsafe_allow_html=True)  # DimGray
st.markdown('<style>h6{color: #708090;}</style>', unsafe_allow_html=True)  # SlateGray
st.markdown('<style>p{color: #000000;}</style>', unsafe_allow_html=True)   # Black

# Título 
st.title('Passos Mágicos- DATATHON 2024')

# Subtítulo
st.subheader('Análise de indicadores Passos Mágicos', divider='rainbow')

# Barra de menus
tab0, tab1, tab2, tab3 = st.tabs(['###### Análises', '###### Predições', '###### Dados Externos', '###### Comentários'])

with tab0:
st.markdown ('## ⭐ Jovens Atendidos: 1348', unsafe_allow_html=True,)


# Importação da base
df = pd.read_csv("PEDE_PASSOS_DATASET_FIAP.csv", sep=";", encoding="Utf-8", thousands='.', decimal=',')

# Substituindo valores nulos por 0
df = df.fillna(0)

# Criando uma função para verificar se um valor é incorreto. Exemplo(V202 e D108)
def verificar(valor):
return isinstance(valor, str) and re.match(r'^[A-Za-z]\d+', valor)

# Identificando os índices das linhas que contêm valores incorretos em qualquer coluna
indices_para_remover = df.applymap(verificar).any(axis=1)

# Removendo as linhas identificadas
df = df[~indices_para_remover]

# Separando as colunas que serão utilizadas para a análise
df_selecionadas = df[['NOME',
'ANOS_PM_2020','FASE_TURMA_2020', 'INDE_2020','PEDRA_2020', 
'IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 
'FASE_2021', 'INDE_2021', 'PEDRA_2021',
'IAA_2021','IEG_2021', 'IPS_2021', 'IDA_2021',
'IPP_2021', 'IPV_2021', 'IAN_2021', 
'NIVEL_IDEAL_2021',
'FASE_2022','INDE_2022','PEDRA_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022',
'IPP_2022', 'IPV_2022', 'IAN_2022',
'NIVEL_IDEAL_2022']]

# ##### Alterado as colunas Objetc para Float

# Extrai apenas a parte numérica de cada entrada na coluna "FASE_TURMA_2020"
df_selecionadas["FASE_TURMA_2020"] = df_selecionadas["FASE_TURMA_2020"].astype(str).str.extract(r'(\d+)')

# Converte a coluna de volta para numérico.
df_selecionadas["FASE_TURMA_2020"] = pd.to_numeric(df_selecionadas["FASE_TURMA_2020"]).astype("float")

#df_selecionadas.select_dtypes(include='float64').columns

#df_selecionadas.select_dtypes(include='object').columns

#Transformar em float as colunas que são object
colunas_transf_float= df_selecionadas[
['ANOS_PM_2020', 'INDE_2020', 'IAA_2020','IEG_2020', 'IPS_2020', 'IDA_2020', 'IPP_2020', 'IPV_2020', 'IAN_2020',
'INDE_2021', 'INDE_2022', 'IAA_2022', 'IEG_2022', 'IDA_2022', 'IPP_2022',
'IPV_2022']]

for coluna in colunas_transf_float:
# Verifica se a coluna é do tipo objeto, o que geralmente indica uma string no pandas
if df_selecionadas[coluna].dtype == 'object':
df_selecionadas[coluna] = df_selecionadas[coluna].str.replace(".","").astype(float, errors='ignore')
else:
# Se a coluna já for numérica, apenas converte para float sem usar o acessor .str
df_selecionadas[coluna] = df_selecionadas[coluna].astype(float, errors='ignore')

df_selecionadas["INDE_2021"] = pd.to_numeric(df_selecionadas["INDE_2021"], errors='coerce')


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]].astype(str).applymap(lambda x: x[:2])


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]].replace('na', np.nan)


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]].astype(float)


df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]] = df_selecionadas[['INDE_2020','IAA_2020', 'IEG_2020','IPS_2020', 'IDA_2020',
'IPP_2020', 'IPV_2020', 'IAN_2020', 'INDE_2021','IAA_2021','IEG_2021', 
'IPS_2021', 'IDA_2021','IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022','IPP_2022', 'IPV_2022', 
'IAN_2022',      
]]/10

df_INDES = df_selecionadas[["INDE_2020", "INDE_2021", "INDE_2022"]]
#df_INDES

# #### Renomeando coluna

df_selecionadas.rename(columns={"FASE_TURMA_2020": "FASE_2020"}, inplace=True)

# ### Gráficos Iniciais***********************

# #### Boxplot #############################################################################################################
with tab0:
# Container 1
with st.container(border=True):
col1, col2, col3 =st.columns([1,1,1])
col4, col5, col6 =st.columns([1,1,1])
with col3:
df_INDES = df_INDES[~df_INDES[["INDE_2020", "INDE_2021", "INDE_2022"]].isin([0, '#Nulo'])]  # Remove valores nulos e 0

# Unpivot the DataFrame para que possamos usar plotly.express
df_melted = df_INDES.melt(value_vars=["INDE_2020", "INDE_2021", "INDE_2022"], var_name="Ano", value_name="INDE")

# Construir o boxplot com plotly.express
fig = px.box(df_melted, x="Ano", y="INDE", title="Distribuição das notas INDE 2020, 2021 e 2022")

# Ajustar o layout para melhorar a visualização
fig.update_layout(
yaxis=dict(title="Nota INDE"),
xaxis=dict(title="Ano"),font=dict(size=14, color='black', family='Arial'),
width=800, 
height=600,
template='plotly_white'
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

# Mostrar o gráfico
st.plotly_chart(fig, use_container_width=True)

with col6:
texto = """
### Distribuição das notas INDE 2020, 2021 e 2022:
O gráfico de boxplot acima mostra a distribuição das notas INDE dos alunos da Passos Mágicos nos anos de 2020, 2021 e 2022.
- Através dos boxplots, podemos observar a distribuição das notas INDE em cada ano. Os boxplots mostram a mediana, os quartis e os valores extremos (outliers) das notas.
- Em geral, as notas INDE parecem estar distribuídas de forma semelhante nos três anos, com algumas diferenças nas medianas e nos quartis.
- O ano de 2021 parece ter uma distribuição ligeiramente mais alta do que os outros anos, com uma mediana mais alta e uma caixa (box) mais alta.
- Os outliers (valores extremos) são mais comuns nos anos de 2021 e 2022, indicando que algumas notas estão significativamente acima ou abaixo da maioria dos alunos.
"""



# Exibir o texto em Markdown
st.markdown(texto)


# #### Histograma ##############################################################################################################

# Supondo que df_INDES já esteja carregado

with col2:
df_INDES = df_INDES[~df_INDES[["INDE_2020", "INDE_2021", "INDE_2022"]].isin([0, '#Nulo'])]  # Remove valores nulos e 0

# Unpivot the DataFrame para que possamos usar plotly.express
df_melted = df_INDES.melt(value_vars=["INDE_2020", "INDE_2021", "INDE_2022"], var_name="Ano", value_name="INDE")

# Construir o histograma com plotly.express
fig = px.histogram(df_melted, x="INDE", color="Ano", barmode="overlay", nbins=20, 
title="Histograma dos INDEs",
labels={"INDE": "Nota INDE", "Ano": "Ano"})

# Ajustar o layout para melhorar a visualização
fig.update_layout(
yaxis=dict(range=[0, 180], title="Contagem"),
xaxis=dict(title="Nota INDE"),font=dict(size=14, color='black', family='Arial'),    
legend_title_text='Ano',
width=800, 
height=600,
template='plotly_white'
)

# Melhorar a paleta de cores
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

# Mostrar o gráfico
st.plotly_chart(fig, use_container_width=True)

with col5:
texto = """
### Histograma das notas INDE 2020, 2021 e 2022:
O histograma acima mostra a concentração das notas INDE dos alunos da Passos Mágicos nos anos de 2020, 2021 e 2022.
- Através do histograma, podemos observar a distribuição das notas INDE em cada ano. As barras representam a contagem de notas em intervalos específicos.
- Em geral, as notas INDE parecem estar distribuídas de forma semelhante nos três anos, com algumas diferenças nas contagens em cada intervalo.
- O acúmulo de notas parece estar mais concentrado entre 6 e 8, em todos os anos.
"""
st.markdown(texto)
# Transformar os dados para formato longo

with col1:
df_long = df_selecionadas[["PEDRA_2020", "PEDRA_2021", "PEDRA_2022"]].melt(var_name='Ano', value_name='Nota')

# Filtrar os dados para excluir 0 e #Nulo
df_long = df_long[~df_long['Nota'].isin([0, '#NULO!'])]

# Criar a figura com Plotly Express
fig = px.histogram(df_long, x='Nota', color='Ano', barmode='group', title="PEDRAS 2020, 2021 e 2022") 

fig.update_layout(plot_bgcolor='white', font=dict(size=14, color='black', family='Arial'),
width=800, height=600, xaxis_title="Nota", yaxis_title="Contagem")
#fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))  

# Mostrar o gráfico
st.plotly_chart(fig, use_container_width=True)

with col4:
texto = """
### PEDRAS 2020, 2021 e 2022:
O gráfico de histograma acima mostra a distribuição das notas PEDRA dos alunos da Passos Mágicos nos anos de 2020, 2021 e 2022.
- Através do histograma, podemos observar a distribuição das notas PEDRA em cada ano. As barras representam a contagem de notas em intervalos específicos.
- Podemos constatar que a classificação que mais se repete ao longo dos anos é a Ametista, seguida pela pedra Ágata.
"""
st.markdown(texto)


# #### Correlação

# Colunas que serão utilizadas para a análise de correlação
df_correlacao=df_selecionadas[[
'INDE_2021', 'IAA_2021', 'IEG_2021', 'IPS_2021', 
'IDA_2021', 'IPP_2021', 'IPV_2021', 'IAN_2021', 'INDE_2022', 
'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022', 'IPP_2022', 'IPV_2022', 
'IAN_2022']]


# Calcular a matriz de correlação
df_correlacao = df_correlacao.corr()

# Plotando Gráfico de correlação #########################################################################################################

with tab0:
# Container 2
with st.container(border=True):
col4, col5 = st.columns([2, 1])
with col4:
fig = px.imshow(df_correlacao, 
labels=dict(color="Correlação"), 
x=df_correlacao.columns, 
y=df_correlacao.index, 
color_continuous_scale='RdBu',  # Usar uma escala de cores válida
zmin=-1, zmax=1)
fig.update_layout(
title="Correlação entre as variáveis",
width=1000,
height=600
)

st.plotly_chart(fig, use_container_width=True)



with col5:
# Texto em Markdown
texto = """
### Correlação entre as variáveis:
O gráfico de correlação apresentado mostra a relação entre as variáveis de desempenho dos alunos da Passos Mágicos nos anos de 2021 e 2022. Vamos analisar as correlações mais relevantes:

### Correlações Fortes:
**INDE**: O INDE (Índice de Desenvolvimento Educacional) apresenta uma correlação forte e positiva com a maioria das outras variáveis, especialmente com os indicadores do mesmo ano. Isso indica que o INDE é um bom indicador geral do desempenho dos alunos, refletindo as notas e os indicadores de engajamento, autoavaliação e psicossocial.

**Indicadores do mesmo ano**: As variáveis do mesmo ano (2021 ou 2022) tendem a ter uma correlação mais forte entre si. Por exemplo, o INDE_2021 tem uma correlação forte com IAA_2021, IEG_2021, IPS_2021 e IDA_2021. Isso é esperado, pois os indicadores do mesmo ano provavelmente se influenciam mutuamente.

### Correlações Fracas:
**Indicadores de anos diferentes**: As variáveis de 2021 e 2022 apresentam correlações mais fracas entre si. Isso sugere que o desempenho dos alunos em um ano não é necessariamente um forte preditor do desempenho no ano seguinte.

**IPV**: O IPV (Indicador do Ponto de Virada) apresenta correlações mais fracas com as outras variáveis, especialmente com os indicadores de 2021. Isso pode indicar que o IPV é um indicador mais independente, talvez refletindo fatores menos relacionados ao desempenho acadêmico tradicional.
"""

# Exibir o texto em Markdown
st.markdown(texto)

# #### Indicadores dos 10 Melhores Alunos

# Filtrando os 20 melhores alunos, conforme nota INDE.
df_melhores = df_selecionadas[["NOME", "INDE_2020","INDE_2021","INDE_2022"]].sort_values(by="INDE_2022", ascending=False).head(10)

# Transformar o DataFrame para o formato longo (long format) necessário para plotly express

df_long = pd.melt(df_melhores, id_vars=['NOME'], value_vars=['INDE_2020', 'INDE_2021', 'INDE_2022'],
var_name='Ano', value_name='Indicador')


# #### Médias INDEs(todosos anos) por Aluno

# Calcular a média dos indicadores
df_selecionadas['Média_INDE'] = df_selecionadas.apply(lambda x: (x["INDE_2020"] + x["INDE_2021"] + x["INDE_2022"]) / 3, axis=1)

# Ordenar o DataFrame com base na média calculada em ordem decrescente
df_selecionadas = df_selecionadas.sort_values(by='Média_INDE', ascending=False)


# Calcular a média dos indicadores
df_selecionadas['Média_INDE'] = df_selecionadas.apply(lambda x: (x["INDE_2020"] + x["INDE_2021"] + x["INDE_2022"]) / 3, axis=1)

# Ordenar o DataFrame com base na média calculada em ordem decrescente
df_selecionadas = df_selecionadas.sort_values(by='Média_INDE', ascending=False)

# Selecionar as 10 primeiras linhas do DataFrame ordenado
top_10 = df_selecionadas.head(10)

# Criar o gráfico de barras agrupadas  ###################################################################################################

with tab0:
# Container 3
with st.container(border=True):
col6, col7, col8 = st.columns([1,1,1])
col14, col15 = st.columns([2,1])
# Construir o gráfico de barras com Plotly Express ######################################################################################################

with col8:

fig = px.bar(top_10, x='NOME', y='Média_INDE', title='Top 10 Médias INDE', labels={'NOME': 'Nome', 'Média_INDE': 'Média INDE'}, color='NOME')

# Ajustar o layout para melhorar a visualização
fig.update_layout(xaxis_tickangle=-45, width=600, height=500, font=dict(size=14, color='black', family='Arial'),plot_bgcolor='white')

#fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
# Mostrar o gráfico
st.plotly_chart(fig, use_container_width=True)

# #### Função para o cálculo do INDE 

# Função para calcular o INDE com base nas notas e critérios de cada fase
def calcular_INDE_fases_2020(row):
if row["FASE_2020"] <= 7:
INDE = (row["IAN_2020"] * 0.1 + row["IDA_2020"] * 0.2 + row["IEG_2020"] * 0.2 +
row["IAA_2020"] * 0.1 + row["IPS_2020"] * 0.1 + row["IPP_2020"] * 0.1 + row["IPV_2020"] * 0.2)
else:
INDE = (row["IAN_2020"] * 0.1 + row["IDA_2020"] * 0.4 + row["IEG_2020"] * 0.2 +
row["IAA_2020"] * 0.1 + row["IPS_2020"] * 0.2)
return INDE

def calcular_INDE_fases_2021(row):
if row["FASE_2021"] <= 7:
INDE = (row["IAN_2021"] * 0.1 + row["IDA_2021"] * 0.2 + row["IEG_2021"] * 0.2 +
row["IAA_2021"] * 0.1 + row["IPS_2021"] * 0.1 + row["IPP_2021"] * 0.1 + row["IPV_2021"] * 0.2)
else:
INDE = (row["IAN_2021"] * 0.1 + row["IDA_2021"] * 0.4 + row["IEG_2021"] * 0.2 +
row["IAA_2021"] * 0.1 + row["IPS_2021"] * 0.2)
return INDE

def calcular_INDE_fases_2022(row):
if row["FASE_2022"] <= 7:
INDE = (row["IAN_2022"] * 0.1 + row["IDA_2022"] * 0.2 + row["IEG_2022"] * 0.2 +
row["IAA_2022"] * 0.1 + row["IPS_2022"] * 0.1 + row["IPP_2022"] * 0.1 + row["IPV_2022"] * 0.2)
else:
INDE = (row["IAN_2022"] * 0.1 + row["IDA_2022"] * 0.4 + row["IEG_2022"] * 0.2 +
row["IAA_2022"] * 0.1 + row["IPS_2022"] * 0.2)
return INDE

df_selecionadas['INDE_2020Novo'] = df_selecionadas.apply(calcular_INDE_fases_2020, axis=1)
df_selecionadas['INDE_2021Novo'] = df_selecionadas.apply(calcular_INDE_fases_2021, axis=1)
df_selecionadas['INDE_2022Novo'] = df_selecionadas.apply(calcular_INDE_fases_2022, axis=1)

# #### GroupBy 

# Agrupa os dados por INDE_2020 e calcula a média de FASE_TURMA_2020
df_agrupado_fase20 = df_selecionadas["INDE_2020"].groupby(df_selecionadas["FASE_2020"]).mean()

# Exibe o DataFrame resultante
pd.DataFrame(df_agrupado_fase20)


# Agrupa os dados por INDE_2020 e calcula a média de FASE_TURMA_2020
df_agrupado_fase21 = df_selecionadas["INDE_2021"].groupby(df_selecionadas["FASE_2021"]).mean()

# Exibe o DataFrame resultante
df_agrupado_fase21 = pd.DataFrame(df_agrupado_fase21)


# Agrupa os dados por INDE_2020 e calcula a média de FASE_TURMA_2020
df_agrupado_fase22 = df_selecionadas["INDE_2022"].groupby(df_selecionadas["FASE_2022"]).mean()

# Exibe o DataFrame resultante
df_agrupado_fase22 = pd.DataFrame(df_agrupado_fase22)


# #### Média dos INDEs por fase

# Agrupar por 'FASE_2020' e calcular a média dos INDEs de 2020, 2021 e 2022
df_agrupado_INDES = df_selecionadas.groupby("FASE_2020")[["INDE_2020", "INDE_2021", "INDE_2022"]].mean()

# Converter o resultado em um DataFrame
df_agrupado_INDES = pd.DataFrame(df_agrupado_INDES)


fig = px.line(df_agrupado_INDES, x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2020"], title="Média das notas INDE por Fase de Turma")
# Removido para usar add_scatter e adicionar um nome à primeira série de dados também

# Adicionando a primeira série de dados com um nome
fig.add_scatter(x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2020"], mode='lines', name='INDE 2020')

# Continuação com as outras séries de dados
fig.add_scatter(x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2021"], mode='lines', name='INDE 2021')
fig.add_scatter(x=df_agrupado_INDES.index, y=df_agrupado_INDES["INDE_2022"], mode='lines', name='INDE 2022')

# Atualizando o layout do gráfico
fig.update_layout(
xaxis_title="Fase de Turma",
yaxis_title="Média das Notas INDE",
plot_bgcolor='white',
font=dict(size=14, color='black', family='Arial')
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

#fig.show()

df_agrupado_INDESNovos= df_selecionadas[["FASE_2020", "INDE_2020Novo","INDE_2021Novo", "INDE_2022Novo"]]
df_agrupado_INDESNovos.set_index("FASE_2020", inplace=True)
#df_agrupado_INDESNovos


# #### "Comparação das notas INDE 2020, 2021 e 2022"


df_INDES_todos = df_selecionadas[["FASE_2020","INDE_2020", "INDE_2020Novo","INDE_2021","INDE_2021Novo","INDE_2022","INDE_2022Novo"]]
df_INDES_todos.rename(columns={"FASE_2020": "FASE"}, inplace=True)


# Criando subplots com 3 colunas (uma para cada ano) ############################################################################
with tab0:
# Container 4
with st.container(border=True):
st.subheader("Comparação dos resultados INDE 2020, 2021 e 2022 (Cálculo Passos x Cálculo Novo)")
col9, col10 = st.columns([2, 1])
col11, col12, col13 = st.columns([1, 1, 1])


with col9:

fig = make_subplots(rows=1, cols=3, subplot_titles=("2020", "2021", "2022"))

# Calculando as médias
media_2020 = df_INDES_todos["INDE_2020"].mean()
media_2020_novo = df_INDES_todos["INDE_2020Novo"].mean()
media_2021 = df_INDES_todos["INDE_2021"].mean()
media_2021_novo = df_INDES_todos["INDE_2021Novo"].mean()
media_2022 = df_INDES_todos["INDE_2022"].mean()
media_2022_novo = df_INDES_todos["INDE_2022Novo"].mean()

# Adicionando os histogramas para 2020
fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2020] * len(df_INDES_todos["FASE"]), name="INDE 2020", opacity=1, marker_color='blue'), row=1, col=1)
fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2020_novo] * len(df_INDES_todos["FASE"]), name="INDE 2020 Novo", opacity=1, marker_color='lightblue'), row=1, col=1)

# Adicionando os histogramas para 2021
fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2021] * len(df_INDES_todos["FASE"]), name="INDE 2021", opacity=1, marker_color='green'), row=1, col=2)
fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2021_novo] * len(df_INDES_todos["FASE"]), name="INDE 2021 Novo", opacity=1, marker_color='lightgreen'), row=1, col=2)

# Adicionando os histogramas para 2022
fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2022] * len(df_INDES_todos["FASE"]), name="INDE 2022", opacity=1, marker_color='red'), row=1, col=3)
fig.add_trace(go.Bar(x=df_INDES_todos["FASE"], y=[media_2022_novo] * len(df_INDES_todos["FASE"]), name="INDE 2022 Novo", opacity=1, marker_color='lightcoral'), row=1, col=3)

# Atualizando o layout do gráfico
fig.update_layout(
title_text="Comparação das notas INDE 2020, 2021 e 2022 (Cálculo Passos x Cálculo Novo)",
xaxis_title="Fases",
yaxis_title="Notas INDE",
barmode='group', plot_bgcolor='white',font=dict(size=14, color='black', family='Arial')
)

#fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

st.plotly_chart(fig, use_container_width=True)


## Calculando a média por fase
media_por_fase = df_INDES_todos.groupby('FASE')[['INDE_2020', 'INDE_2020Novo', 'INDE_2021', 'INDE_2021Novo', 'INDE_2022', 'INDE_2022Novo']].mean()

# #### Média das Notas do INDEs de cada ano

df_INDES_todos.describe()

# Dados das médias
labels = ['INDE_2020', 'INDE_2020Novo', 'INDE_2021', 'INDE_2021Novo', 'INDE_2022', 'INDE_2022Novo']
means = [6.709491, 5.530289, 6.837427, 2.960015, 4.463205, 4.065504]

# Criando um DataFrame com os dados
df_medias_inde = pd.DataFrame({
'Ano': labels,
'Média': means
})
# #### Pedras por Ano

# Remover valores sem classificação (nulos)
df_selecionadas = df_selecionadas.dropna(subset=["PEDRA_2020", "PEDRA_2021", "PEDRA_2022"])

# Contando os valores e resetando o índice para transformar em DataFrame
contagem_pedra_2020 = df_selecionadas["PEDRA_2020"].value_counts().reset_index()
contagem_pedra_2020.columns = ['PEDRA_2020', 'count']
contagem_pedra_2020 = contagem_pedra_2020[(contagem_pedra_2020['PEDRA_2020'] != 0) & (contagem_pedra_2020['PEDRA_2020'] != '#NULO!')]  # Remover zeros e #NULO!

contagem_pedra_2021 = df_selecionadas["PEDRA_2021"].value_counts().reset_index()
contagem_pedra_2021.columns = ['PEDRA_2021', 'count']
contagem_pedra_2021 = contagem_pedra_2021[(contagem_pedra_2021['PEDRA_2021'] != 0) & (contagem_pedra_2021['PEDRA_2021'] != '#NULO!')]  # Remover zeros e #NULO!

contagem_pedra_2022 = df_selecionadas["PEDRA_2022"].value_counts().reset_index()
contagem_pedra_2022.columns = ['PEDRA_2022', 'count']
contagem_pedra_2022 = contagem_pedra_2022[(contagem_pedra_2022['PEDRA_2022'] != 0) & (contagem_pedra_2022['PEDRA_2022'] != '#NULO!')]  # Remover zeros e #NULO!

# Criando o gráfico de barras com plotly.graph_objects ###########################################################################################
with tab0:

with col10:
fig = go.Figure()

# Adicionando as barras
fig.add_trace(go.Bar(
x=df_medias_inde['Ano'],
y=df_medias_inde['Média'],
marker_color=['#1f77b4', '#aec7e8', '#1f77b4', '#aec7e8', '#1f77b4', '#aec7e8']  # Azul escuro e azul claro
))

# Rotacionando as labels do eixo x e aplicando cores diferentes
fig.update_layout(
xaxis_tickangle=-45,
title_text="Médias das Notas INDE por Ano (Cálculo Passos x Cálculo Novo)",
xaxis_title="INDE por Ano (Cálculo Passos x Cálculo Novo)",
yaxis_title="Média INDE", font=dict(size=14, color='black', family='Arial'),
plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
paper_bgcolor='rgba(0,0,0,0)'  # Fundo transparente
)
#fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
# Exibindo o gráfico
st.plotly_chart(fig, use_container_width=True)

with col11:
st.image("Calculo_INDE.png")
# Texto em Markdown
texto = """
### Cálculo Novo:
Nos gráficos acima podemos perceber o impacto gerado com os resultados obtidos pelo novo cálculo, para chegar aos valores apresentados, foi necessário realizar uma análise detalhada dos dados e ajustar os cálculos conforme as regras estabelecidas pela Passos Mágicos, conforme apresentado na imagem acima "Composição do Índice de Desenvolvimento Educacional (INDE)".
"""

# Exibir o texto em Markdown
st.markdown(texto)  

with col12:
# Texto em Markdown
texto = """
### Considerações:
Considerando os resultados do novo cálculo, podemos constatar que existe uma diferença significativa entre os valores obtidos, essa diferença pode ser explicada pela forma como os dados foram tratados e analisados, porém, é importante ressaltar que foi realizado consoante as regras estabelecidas pela Passos Mágicos.
- O processo foi muito desafiador, ao longo da análise foi necessário realizar diversos ajustes e correções, muitos dados foram tratados e ajustados para garantir a qualidade das análises realizadas.
"""

# Exibir o texto em Markdown
st.markdown(texto) 

with col13:
st.image("Tabela_Passos_2.png")
# Texto em Markdown
texto = """
### PONTOS DE ATENÇÃO:
Acima temos um recorte da tabela disponibilizada pela Passos Mágicos, onde de forma clara é possível identificar alguns pontos de atenção:


- A importância de padronizar a entrada de dados para evitar inconsistências.
- Tratar os dados de forma adequada para garantir a qualidade das análises realizadas.
- Classificar corretamente os tipos de dados, definindo se são numéricos ou categóricos, para evitar erros de interpretação.
- Realizar a limpeza dos dados, removendo valores nulos e tratando possíveis outliers.
- Documentar o processo de análise de dados, registrando as etapas realizadas e os resultados obtidos.


"""


# Exibir o texto em Markdown
st.markdown(texto) 


# #### Quantidade de Alunos em Atividade

# Total de Alunos cadastrados na Base de Dados
contagem_total_alunos = df_selecionadas["NOME"].nunique()

# Imprimir o resultado
print("Contagem total de alunos:")
print(contagem_total_alunos)

# Contar a quantidade de alunos AVALIADOS por cada ano do INDE
contagem_inde_2020_unicos = df_selecionadas.loc[df_selecionadas["INDE_2020"] > 0, "NOME"].nunique()
contagem_inde_2021_unicos = df_selecionadas.loc[df_selecionadas["INDE_2021"] > 0, "NOME"].nunique()
contagem_inde_2022_unicos = df_selecionadas.loc[df_selecionadas["INDE_2022"] > 0, "NOME"].nunique()

# Imprimir os resultados
print("Contagem de alunos únicos em 2020:")
print(contagem_inde_2020_unicos)
print("\nContagem de alunos únicos em 2021:")
print(contagem_inde_2021_unicos)
print("\nContagem de alunos únicos em 2022:")
print(contagem_inde_2022_unicos)

df_evolucao = df_selecionadas[['NOME', 'INDE_2020', 'INDE_2021', 'INDE_2022']]

# Remover linhas com valores NaN
df_evolucao = df_evolucao.dropna()

# Calcular a média do INDE para cada aluno
df_evolucao['INDE_MEDIA'] = df_evolucao[['INDE_2020', 'INDE_2021', 'INDE_2022']].mean(axis=1)


# Selecionar os 10 melhores alunos com base na média do INDE
df_melhores_alunos = df_evolucao.nlargest(10, 'INDE_MEDIA')

# Transformar os dados para o formato longo
df_melhores_alunos_long = df_melhores_alunos.melt(id_vars=['NOME'], value_vars=['INDE_2020', 'INDE_2021', 'INDE_2022'], 
var_name='Ano', value_name='INDE')

#TABELA Evolução ###############################################################################################################################
with tab0:

with col6:
st.subheader("Evolução dos Alunos")

st.markdown(""" ###### **Tabela com a evolução dos alunos(ordenada pela média dos INDEs).** """)

st.markdown(
"""
<style>
.center-table {
display: flex;
justify-content: center;
}
</style>
""",
unsafe_allow_html=True)
st.markdown('<div class="center-table">', unsafe_allow_html=True)
st.dataframe(df_evolucao.head(10), width=600, height=400)


# Plotar a evolução do INDE para os melhores alunos ##############################################################################################

with tab0:
# Container 3
with st.container(border=True):

with col14:

fig = px.line(df_melhores_alunos_long, x='Ano', y='INDE', color='NOME', markers=True, 
title='Evolução do INDE dos 10 Melhores Alunos')

fig.update_layout(xaxis_title='Ano', yaxis_title='INDE', legend_title_text='Aluno', width=1000, height=600, plot_bgcolor='white', font=dict(size=14, color='black', family='Arial'))
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
st.plotly_chart(fig, use_container_width=True)

with col15:
# Texto em Markdown
texto = """
### Melhores Alunos:
Os gráficos demonstram a evolução do INDE (Índice de Desenvolvimento Educacional) dos 10 melhores alunos ao longo dos anos de 2020, 2021 e 2022. Podemos observar que a maioria dos alunos apresentou um crescimento consistente em seus indicadores, refletindo um bom desempenho acadêmico ao longo do tempo.

"""

# Exibir o texto em Markdown
st.markdown(texto)

# #### Ponto de Virada  ## 

df_selecionadas1 = df_selecionadas.merge(df[["NOME", "PONTO_VIRADA_2020", "PONTO_VIRADA_2021", "PONTO_VIRADA_2022"]], on="NOME", how="left")

# #### Transformar as colunas "PONTO_VIRADA_2020 , 2121 E 2022" com LabelEncoder

df_selecionadas1["PONTO_VIRADA_2020"] = df_selecionadas1["PONTO_VIRADA_2020"].astype(str)
df_selecionadas1["PONTO_VIRADA_2021"] = df_selecionadas1["PONTO_VIRADA_2021"].astype(str)
df_selecionadas1["PONTO_VIRADA_2022"] = df_selecionadas1["PONTO_VIRADA_2022"].astype(str)

from sklearn.preprocessing import LabelEncoder

# Inicializar o LabelEncoder
label_encoder = LabelEncoder()

# Função para aplicar o LabelEncoder apenas nos valores diferentes de zero ou nulo
def encode_non_zero_null(df, column):
mask = (df[column] != 0) & (df[column].notnull()) & (df[column] != '#NULO!')
df.loc[mask, f"{column}_encoded"] = label_encoder.fit_transform(df.loc[mask, column])

# Aplicar a função para cada coluna
encode_non_zero_null(df_selecionadas1, "PONTO_VIRADA_2020")
encode_non_zero_null(df_selecionadas1, "PONTO_VIRADA_2021")
encode_non_zero_null(df_selecionadas1, "PONTO_VIRADA_2022")

print(df_selecionadas1[["PONTO_VIRADA_2020_encoded", "PONTO_VIRADA_2021_encoded", "PONTO_VIRADA_2022_encoded"]].head())

# ### MODELO DE PREDIÇÃO #######################################################################################################################


## Fazendo o Balenceamento das Classes 
df_modelo = df_selecionadas1.copy()

#Dropando as colunas encoded
df_modelo.drop(columns=["PONTO_VIRADA_2020_encoded", "PONTO_VIRADA_2021_encoded", "PONTO_VIRADA_2022_encoded"], inplace=True)

df_modelo_limpo = df_modelo
# Remover valores nulos
df_modelo_limpo = df_modelo_limpo.dropna(subset=["PONTO_VIRADA_2022"])

# Removendo valores "0"
df_modelo_limpo = df_modelo_limpo[df_modelo_limpo["PONTO_VIRADA_2022"] != "0"]

# convertendo os valores SIM e NÃO para 1 e 0	
df_modelo_limpo[["PONTO_VIRADA_2020_encoding"]] = df_modelo_limpo[["PONTO_VIRADA_2020"]].replace({"Sim": 1, "Não": 0}).astype(int)
df_modelo_limpo[["PONTO_VIRADA_2021_encoding"]] = df_modelo_limpo[["PONTO_VIRADA_2021"]].replace({"Sim": 1, "Não": 0}).astype(int)
df_modelo_limpo[["PONTO_VIRADA_2022_encoding"]] = df_modelo_limpo[["PONTO_VIRADA_2022"]].replace({"Sim": 1, "Não": 0}).astype(int)



## Aplicando o SMOTE para balancear as classes################################
# Importar as bibliotecas necessárias
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


X = df_modelo_limpo[['IPV_2020', 'IPV_2021', 'IPV_2022']]
y = df_modelo_limpo['PONTO_VIRADA_2022_encoding']


# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Aplicar a imputação de valores faltantes nos dados de treino
imputer = SimpleImputer(strategy='mean')  # ou 'median', 'most_frequent', etc.
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Aplicar o SMOTE para balancear as classes nos dados de treino
smote = SMOTE(random_state=42, sampling_strategy="minority")
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_imputed, y_train)

# Verificar o balanceamento das classes
print(y_train_resampled.value_counts())


#  Contar a frequência de cada classe
contagem_classes = df_modelo_limpo["PONTO_VIRADA_2022_encoding"].value_counts()

# Contagem das classes
class_counts = y_train_resampled.value_counts().reset_index()
class_counts.columns = ['Classe', 'Contagem']

# Gráfico de barras com Plotly Express
fig = px.bar(class_counts, x='Classe', y='Contagem', title='Contagem das Classes em y_train_resampled', 
labels={'Classe': 'Classe', 'Contagem': 'Contagem'}, 
color='Classe', 
color_continuous_scale='viridis', 
template='plotly_white')

# Configurar o layout do gráfico
fig.update_layout(
xaxis_title='Classe',
yaxis_title='Contagem',
template='plotly_white'
)

# Mostrar o gráfico no Streamlit
with tab1:
with st.container(border=True):
st.subheader("Balanceamento das Classes")
st.write("O gráfico de barras abaixo mostra o balanceamento das classes após a aplicação do SMOTE. Podemos observar que as classes estão balanceadas, o que é importante para o treinamento de modelos de aprendizado de máquina.")
st.plotly_chart(fig)



# #### MODELO ESCOLHIDO - ÁRVORE DE DECISÃO ############################################
#### Treinando o MODELO ###############################################################
from sklearn.tree import DecisionTreeClassifier


# Tratar dados nulos e zeros
features3 = df_modelo_limpo[['IPV_2020', 'IPV_2021', 'IPV_2022']].fillna(0)
labels3 = df_modelo_limpo["PONTO_VIRADA_2022_encoding"]


# Inicializar o imputer para substituir valores NaN pela média
imputer = SimpleImputer(strategy='mean')

# Aplicar o imputer aos dados de treino e teste
X_train_imputed = imputer.fit_transform(X_train_resampled)
X_test_imputed = imputer.transform(X_test)

# Inicializar o modelo de Árvore de Decisão
dt_model = DecisionTreeClassifier(random_state=42)  # pode ajustar parâmetros como 'max_depth', 'min_samples_split', etc.

# Treinar o modelo
dt_model.fit(X_train_imputed, y_train_resampled)

# Fazer previsões nos dados de teste
y_pred = dt_model.predict(X_test_imputed)

# Criar uma cópia do DataFrame 
X_test_copy = X_test.copy()

# Adicionar as predições ao DataFrame de teste
X_test_copy['PREDITO'] = y_pred

# Adicionar os valores reais ao DataFrame de teste
X_test_copy['REAL'] = y_test.values

# Mapear os valores preditos e reais de 1 para "SIM" e 0 para "NÃO"
mapping = {1: "SIM", 0: "NÃO"}
X_test_copy['PREDITO'] = X_test_copy['PREDITO'].map(mapping)
X_test_copy['REAL'] = X_test_copy['REAL'].map(mapping)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Acurácia: {accuracy}')
report_df_modelo_limpo = pd.DataFrame(report).transpose()  # Converter para DataFrame
print(report_df_modelo_limpo)

# Exibir os valores reais e previstos
print(X_test_copy[['REAL', 'PREDITO']])


# Plotar a matriz de confusão #######################################################################################
with tab1:
st.subheader("Modelo para predizer se o aluno atingiu o ponto de virada")
st.write("O modelo de Árvore de Decisão foi treinado para prever se um aluno atingiu o ponto de virada com base nos indicadores IPV de 2020, 2021 e 2022. O modelo foi avaliado com base na acurácia, no relatório de classificação e na matriz de confusão.") 
with tab1:
with st.container(border=True):
col15, col16 = st.columns([1, 1])
with col16: 
plt.figure(figsize=(4, 2))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=dt_model.classes_, yticklabels=dt_model.classes_)
plt.xlabel('Predito')
plt.ylabel('Verdadeiro')
plt.title('Matriz de Confusão')
st.pyplot(plt)

# Avaliação do Modelo 

# Avaliar o modelo
with tab1:
with st.container(border=True):
col17, col18, col19= st.columns([1, 1, 1])
with col18:
st.subheader("Avaliação do Modelo")

st.write('Relatório de Classificação:')
st.dataframe(report_df_modelo_limpo, width=400)

with col17:
st.write('Valores Reais e Previstos:')
st.dataframe(X_test_copy[['REAL', 'PREDITO']], width=400, height=750)

with col18:
st.write('Sobre os Resultados do Modelo: O modelo escolhido para prever se um aluno atingiu o ponto de virada é uma Árvore de Decisão. Ele foi treinado com base nos indicadores IPV de 2020, 2021 e 2022.')    
Como podemos observar, o modelo apresentado demonstra um desempenho ótimo na tarefa de prever se um aluno atingiu o ponto de virada.
Alta Acurácia: O modelo apresenta uma acurácia de 0.9942, o que indica um alto nível de precisão nas previsões. Isso sugere que o modelo está aprendendo bem os padrões dos dados e conseguindo prever com sucesso se um aluno atingiu o ponto de virada.
A matriz de confusão mostra que o modelo está classificando corretamente a maioria dos alunos que não atingiram o ponto de virada (153 casos) e também está acertando a maioria dos alunos que atingiram o ponto de virada (19 casos).
Poucos Erros: O modelo comete poucos erros, principalmente na identificação de alunos que não atingiram o ponto de virada (1 caso).


with col19:   
st.write('#### Benefícios de utilizar um modelo de predição:')

* **Identificação do Ponto de Virada:** O modelo permite identificar alunos em risco de não atingir o ponto de virada precocemente, antes que eles abandonem o programa.
* **Identificação Precoce de abandono:** Pode ser utilizado para identificar alunos em risco de abandono precocemente, antes que eles abandonem o programa.
* **Intervenção Direcionada:** A Passos Mágicos pode usar as previsões do modelo para direcionar ações de apoio e acompanhamento para os alunos em risco, como:
* **Mentoria:**  Oferecer mentoria individualizada para ajudar os alunos a superar as dificuldades.
* **Acompanhamento:**  Monitorar o progresso dos alunos de forma mais próxima.
* **Recursos:**  Fornecer recursos adicionais, como materiais de estudo ou apoio psicológico.
* **Eficiência:**  O modelo pode ajudar a Passos Mágicos a otimizar seus recursos, direcionando o apoio para os alunos que mais precisam.


st.subheader("Conclusão")
st.write('#O modelo de Árvore de Decisão apresentado demonstra um desempenho excelente na tarefa de prever se um aluno atingiu o ponto de virada. Sua alta acurácia, poucos erros e interpretabilidade o tornam uma ferramenta valiosa para a Passos Mágicos. No entanto, é importante ter cuidado com o desequilíbrio de classes e realizar uma análise contextual dos erros. 
            ')
st.write('#A Passos Mágicos pode continuar a melhorar o modelo, realizando a validação cruzada, incluindo novos indicadores e investigando as causas dos erros.')
')

# ## Tabela #########################################################################################################
# Verificar se X_test e y_test são DataFrames ou Series
if isinstance(X_test, (pd.DataFrame, pd.Series)) and isinstance(y_test, (pd.DataFrame, pd.Series)):
# Concatenar X_test e y_test ao longo do eixo das colunas
resultado = pd.concat([X_test, y_test], axis=1)

# Alterar o nome da coluna
resultado.rename(columns={'PONTO_VIRADA_2022_encoding': 'PONTO_VIRADA_2022_Previsto'}, inplace=True)

# Aplicar o mapeamento na nova coluna
resultado['PONTO_VIRADA_2022_Previsto'] = resultado['PONTO_VIRADA_2022_Previsto'].map({1: "SIM", 0: "NÃO"})
print(pd.DataFrame(resultado))

else:
print("X_test e y_test devem ser DataFrame ou Series do pandas.")

with tab1:
with col15:
st.write("Resultado da Predição")
st.dataframe(resultado, width=600, height=400)




#############################################################################################################################

# IDEB - Índice de Desenvolvimento da Educação Básica
df_IDEB = pd.read_csv("educacao_ideb_mun.csv", sep=";", encoding="latin1")
df_IDEB_mogi_guacu = df_IDEB[df_IDEB["Localidade"] == "Mogi Guaçu"]


with tab2:
with st.container(border=True):
st.subheader("Dados do IDEB de Mogi Guaçu")
st.write("O IDEB é um indicador de qualidade educacional que combina informações sobre o rendimento escolar e o fluxo escolar dos alunos. Ele é calculado com base nas notas das avaliações de Matemática e Língua Portuguesa e na taxa de aprovação dos estudantes.")
st.write("A tabela abaixo mostra os dados do IDEB de Mogi Guaçu, incluindo as médias de Matemática e Língua Portuguesa, as notas do IDEB e as metas projetadas para os anos de 2017 a 2021.")
st.write("Os dados são provenientes do INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira) e podem ser encontrados no portal do INEP.")
st.write("*SAEB: Sistema de Avaliação da Educação Básica.")
st.write("*IDEB: Índice de Desenvolvimento da Educação Básica.")
st.write("*Prova Brasil: Avaliação do SAEB aplicada a cada dois anos para alunos do 5º e 9º ano do Ensino Fundamental.")
st.write("*IDEB projetado: Meta estabelecida para o IDEB de cada escola com base nos resultados anteriores.")
st.write("*Nota: As médias de Matemática e Língua Portuguesa são calculadas a partir das notas dos alunos na Prova Brasil.")
st.write("*Metas projetadas: Notas que as escolas deveriam atingir para alcançar as metas do IDEB.")
st.write("*Nota IDEB: Nota final do IDEB, calculada com base nas médias de Matemática e Língua Portuguesa e na taxa de aprovação dos alunos.")
st.write("*Taxa de Aprovação: Percentual de alunos aprovados em relação ao total de alunos avaliados.")
st.write("fonte: https://www.gov.br/inep/pt-br")
st.dataframe(df_IDEB_mogi_guacu)

# Matrículas por Município, Ano, Nível de ensino e Rede de atendimento
df_MATRICULAS =pd.read_csv("Matrículas por Município, Ano, Nível de ensino e Rede de atendimento.csv", sep=";", encoding="latin1")

#MATRICULAS EM MOGI GUAÇU
df_matriculas_mogi_guacu = df_MATRICULAS.loc[df_MATRICULAS['cod_ibge'] == 3515103]
# Substituir o código do município pelo nome
df_matriculas_mogi_guacu["cod_ibge"] = df_matriculas_mogi_guacu["cod_ibge"].apply(lambda x: "Mogi Guaçu" if x == 3515103 else x)
# Remover vírgulas dos valores numéricos
df_matriculas_mogi_guacu["ano"] = df_matriculas_mogi_guacu["ano"].apply(lambda x: str(x).replace(",", "") if isinstance(x, int) else x)

with tab2:
with st.container(border=True):
st.subheader("Matrículas por Município, Ano, Nível de Ensino e Rede de Atendimento")
st.write("A tabela abaixo mostra o número de matrículas por município, ano, nível de ensino e rede de atendimento. Os dados são provenientes do Censo Escolar, realizado anualmente pelo INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira).")
st.write("O Censo Escolar é a principal pesquisa estatística educacional brasileira. Ele coleta informações sobre as escolas, turmas, alunos e profissionais da educação básica no país.")
st.write("Os dados podem ser encontrados no portal do INEP.")
st.write("fonte: https://www.gov.br/inep/pt-br")
st.dataframe(df_matriculas_mogi_guacu)

# População em idade escolar por Município, Ano e Nível de ensino

df_idade_escolar = pd.read_csv("pop_idade_escolar_2000a2050_esp.csv", sep=";", encoding="latin1")

#POPULAÇÃO EM IDADE ESCOLAR EM MOGI GUAÇU
df_idade_escolar_mogi_guacu = df_idade_escolar.loc[df_idade_escolar['cod_ibge'] == 3515103]
# Substituir o código do município pelo nome
df_idade_escolar_mogi_guacu["cod_ibge"] = df_idade_escolar_mogi_guacu["cod_ibge"].apply(lambda x: "Mogi Guaçu" if x == 3515103 else x)
df_idade_escolar_mogi_guacu["ano"] = df_idade_escolar_mogi_guacu["ano"].apply(lambda x: str(x).replace(",","") if isinstance(x, int) else x)
pd.DataFrame(df_idade_escolar_mogi_guacu)

with tab2:
with st.container(border=True):
st.subheader("População em Idade Escolar por Município, Ano e Nível de Ensino")
st.write("A tabela abaixo mostra a população em idade escolar por município, ano e nível de ensino. Os dados são provenientes do IBGE (Instituto Brasileiro de Geografia e Estatística) e do IPEA (Instituto de Pesquisa Econômica Aplicada).")
st.write("As informações são fundamentais para o planejamento e a gestão da educação, pois permitem estimar a demanda por vagas nas escolas e identificar possíveis desafios e oportunidades na área da educação.")
st.write("Os dados podem ser encontrados nos portais do IBGE e do IPEA.")
st.write("fonte: https://www.ibge.gov.br/ e https://www.ipea.gov.br/")
st.dataframe(df_idade_escolar_mogi_guacu)

df_evolucao = pd.DataFrame(df_evolucao)

# Ordenar os valores da coluna INDE_2022 em ordem crescente
melhores_INDE_2022 = df_evolucao.sort_values(by="INDE_2022", ascending=False)

# Exibir o DataFrame ordenado
melhores_INDE_2022 = melhores_INDE_2022.head(10)


# Supondo que df_evolucao já seja um DataFrame
df_evolucao = pd.DataFrame(df_evolucao)

# Ordenar os valores da coluna INDE_2022 em ordem decrescente e selecionar os 10 melhores
melhores_INDE_2022 = df_evolucao.sort_values(by="INDE_2022", ascending=False).head(10)

# Transformar o DataFrame para o formato longo
melhores_INDE_2022_long = melhores_INDE_2022.melt(id_vars=['NOME'], value_vars=['INDE_2020', 'INDE_2021', 'INDE_2022'],
var_name='Ano', value_name='INDE')


with tab0:
Container 3
with col7:
Construir o gráfico de barras agrupadas com Plotly Express
fig = px.bar(melhores_INDE_2022_long, x='NOME', y='INDE', color='Ano', barmode='group',
title="Histórico dos alunos com melhores INDEs em 2022",
labels={'NOME': 'Nome', 'INDE': 'Indicador'})

# Ajustar o layout para melhorar a visualização
fig.update_layout(xaxis_tickangle=-45, width=800, height=500, font=dict(size=14, color='black', family='Arial'), plot_bgcolor='white', bargap=0.15)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

#Mostrar o gráfico
st.plotly_chart(fig, use_container_width=True)
'''
# Exibir o código no Streamlit
with tab3:
     
    st.code(codigo, language='python')
