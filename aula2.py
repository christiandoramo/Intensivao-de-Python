import pandas as pd
import plotly.express as px
# para rodar o grafico.show foi necessario usar o run in interactive window

tabela = pd.read_csv(r"clientes.csv", encoding="latin",
                     sep=";", thousands='.', decimal=',')

# apagando coluna inutil Unnamed: 8 -> NaN, NaN...
# axis = 0 eixo linha; = 1 eixo coluna
tabela = tabela.drop("Unnamed: 8", axis=1)
# transformando salario de object para float
tabela["Salário Anual (R$)"] = pd.to_numeric(
    tabela["Salário Anual (R$)"], errors="coerce")  # coerce força quem não conseguiu virar numero a ser NaN
# apagando os 35 de 2000 profissionais com profissao nula incluindo qualquer linha com pelo menos 1 valor nulo

# print(tabela[tabela["Profissão"].isna()]) vizualizas os dados onde há profissão nula

tabela = tabela.dropna()
# apaga dados duplicados tabela = tabela.drop_duplicates()


print(tabela)
print(tabela.info())  # descreve tipos de dados por coluna
print(tabela.describe())  # descreve estatiticas dos dados porcoluna

# criando e imprimindo gráficos com plotly
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)",
                           histfunc="avg", text_auto=True)
    grafico.show()

#   Analise dos dados - perfi ideal de cliente
# Acima de 15 anos
# Faixa salarial é irrelevante
# Evitar profissionais de construção. Priorizar de entreteriemento e artista
# entre 10 e 15 anos de experiencia
# com familias no maximo de 6 pessoas
#
