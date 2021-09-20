from behave import*
from nose.tools import *
from factory.locators import BuscacepLocator
from factory.locators import ResultadoBuscaLocator


@given(u'Eu acesso a pagina de Busca por CEP')
def step_impl(context):
    context.browser.get("https://buscacepinter.correios.com.br/app/cep/index.php")
    assert_true(context.browser.find_element(*BuscacepLocator.TITULO))


@when(u'eu informo o "{cep}" no campo CEP')
def step_impl(context,cep):
    context.browser.find_element(*BuscacepLocator.CAMPOCEP).send_keys(cep)


@when(u'eu clico no botao Buscar')
def step_impl(context):
    context.browser.find_element(*BuscacepLocator.BOTAOBUSCAR).click()



@then(u'a tela exibe o resultado da busca')
def step_impl(context):

    assert_equal("Rua Miranda Leão", context.browser.find_element(*ResultadoBuscaLocator.LOGRADOURONOME).text)
    assert_equal("Centro", context.browser.find_element(*ResultadoBuscaLocator.BAIRRO).text)
    assert_equal("Manaus/AM", context.browser.find_element(*ResultadoBuscaLocator.LOCALIDADE).text)
    assert_equal("69005-040", context.browser.find_element(*ResultadoBuscaLocator.CEP).text)


@then(u'a tela exibe uma mensagem de alerta')
def step_impl(context):
    assert_equal("Informe no mínimo os 5(cinco) primeiros dígitos do CEP! Ex.70001", context.browser.find_element(*BuscacepLocator.ALERTA).text)
