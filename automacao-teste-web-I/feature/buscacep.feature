Feature: Como usuario, quero buscar um endereco informando cep, e conseguir visualizar os endereços.

  Background: Pre condicao
    Given Eu acesso a pagina de Busca por CEP

    @example01
    Scenario: Busca de endereco informando cep
      When eu informo o "69005-040" no campo CEP
      And eu clico no botao Buscar
      Then a tela exibe o resultado da busca

    @example02
    Scenario: Busca de endereco informando cep
      When eu informo o "Lojas Bemol" no campo CEP
      And eu clico no botao Buscar
      Then a tela exibe uma mensagem de alerta

    @example03
    Scenario: Busca de endereco informando cep com um digito
      When eu informo o "6" no campo CEP
      And eu clico no botao Buscar
      Then a tela exibe uma mensagem de alerta


