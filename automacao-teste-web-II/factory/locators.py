from selenium.webdriver.common.by import By

class PesquisaHotel(object):
    DESTINO = (By.CSS_SELECTOR, "#querytext")
    SUGESTAO = (By.CSS_SELECTOR, "#suggestion-56507\/200 .ssg-subtitle")
    BOTAOPESQUISAR = (By.CSS_SELECTOR, ".search-button__label")
    ORDERNAR = (By.ID, "mf-select-sortby")
    NOMEHOTEL = (By.XPATH, "//h3/span")
    ITEMLISTA = (By.XPATH, "//*[@id='js_itemlist']")


