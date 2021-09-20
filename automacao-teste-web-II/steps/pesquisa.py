import time

from behave import*
from nose.tools import*
from factory.locators import PesquisaHotel
from selenium.webdriver.support.ui import Select


@given(u'Eu acesso a pagina da Trivago')
def step_impl(context):
    context.browser.get("http://www.trivago.com.br")


@when(u'eu informo "{destino}"')
def step_impl(context, destino):
    context.browser.find_element(*PesquisaHotel.DESTINO).send_keys(destino)
    context.browser.find_element(*PesquisaHotel.SUGESTAO).click()


@when(u'eu clico no botao Pesquisar')
def step_impl(context):
    context.browser.find_element(*PesquisaHotel.BOTAOPESQUISAR).click()



@when(u'escolho ordernar por "Avaliações e sugestões"')
def step_impl(context):
    context.browser.set_page_load_timeout(10)
    context.browser.find_element(*PesquisaHotel.ORDERNAR).click()
    selecionado = Select(context.browser.find_element_by_id("mf-select-sortby"))
    selecionado.select_by_visible_text("Avaliação e sugestões")





@then(u'a tela exibe o resultado da pesquisa')
def step_impl(context):
    time.sleep(10)

    ol_hoteis = context.browser.find_element_by_xpath("//*[@id='js_itemlist']")
    hoteis = ol_hoteis.find_elements_by_tag_name("li")
    primeiro = hoteis[0]

    # Traz uma string com várias informações
    # divide a string e converte para uma lista
    primeiro_data = list(primeiro.text.split("\n"))
    print(primeiro_data)
    print("Nome do hotel: " + primeiro_data[2])
    print("Avaliação: " + primeiro_data[5] + " " + primeiro_data[6])
    print("Valor: " + primeiro_data[13])






