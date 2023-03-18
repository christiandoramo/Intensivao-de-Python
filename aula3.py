# Automação Web
# (Web Scraping)
# Selenium
# Exportar Relatórios
# Pesquisa Automática

from selenium import webdriver
import pandas
import unidecode


navegador = webdriver.Chrome()
tabela = pandas.read_excel("commodities.xlsx")
navegador.get("https://www.google.com/")

for linha in tabela.index:  # tabela.index retorna uma lista com as linhas da tabela
    produto = tabela.loc[linha, "Produto"]
    print(produto)
    produto = unidecode.unidecode(produto.lower())
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    navegador.get(link)
    print(link)
    preco = navegador.find_element(
        'xpath', '/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')
    print(preco)
    preco = preco.replace('.', '').replace(',', '.')
    tabela.loc[linha, "Preço Atual"] = float(preco)

tabela['Comprar'] = tabela['Preço Atual'] <= tabela["Preço Ideal"]
navegador.quit()
tabela.to_excel("commodities_atualizado.xlsx", index=False)
print(tabela)


# print(tabela)
# print(precoMilho)
