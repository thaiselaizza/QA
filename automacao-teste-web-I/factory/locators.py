from selenium.webdriver.common.by import By

class BuscacepLocator(object):
    TITULO = (By.CSS_SELECTOR, "#titulo_tela > h3")
    CAMPOCEP = (By.CSS_SELECTOR, "#cep")
    BOTAOBUSCAR = (By.XPATH, "//button[@id='btn_pesquisar']")
    ALERTA = (By.CSS_SELECTOR, "#alerta")

class ResultadoBuscaLocator(object):
    LOGRADOURONOME = (By.CSS_SELECTOR, "td:nth-child(1)")
    BAIRRO = (By.CSS_SELECTOR, "td:nth-child(2)")
    LOCALIDADE = (By.CSS_SELECTOR, "td:nth-child(3)")
    CEP = (By.CSS_SELECTOR, "td:nth-child(4)")
