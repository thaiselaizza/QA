Feature: Como usuario, quero pesquisar hotéis por avaliação e sugestões, e visualizar as opções disponiveis

  Background: Pre condicao
    Given Eu acesso a pagina da Trivago

    @example01
    Scenario: Pesquisa de hoteis por avaliacao e sugestoes
      When eu informo "Manaus"
      And eu clico no botao Pesquisar
      And escolho ordernar por "Avaliações e sugestões"
      Then a tela exibe o resultado da pesquisa