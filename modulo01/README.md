# 🚘 Primus Motors - Sistema de Agendamento e Vendas

> **Projeto Indústria de Automóveis**  
> **Desenvolvedores:** Isaque e Gabriel

---

## 📌 Sobre o Projeto

O **Primus Motors** é um sistema em Python desenvolvido para automatizar e otimizar o atendimento ao cliente, agendamento de horários, test-drives, personalização de veículos e suporte pós-venda para uma concessionária de veículos. 

O objetivo é proporcionar uma experiência simples, prática e ágil tanto para o cliente quanto para a equipe de vendas.

---

## 👥 Visão dos Envolvidos (User Stories & Requirements)

- **PO (Product Owner):** Quero um sistema simples, prático e funcional de agendamento de horários para venda de carros.
- **QA (Quality Assurance):** Quero um sistema de agendamento ágil e intuitivo que facilite a realização do sonho do cliente ao comprar seu carro.
- **Tech Lead:** Quero um código limpo, organizado, fácil de manter e de simples execução.
- **Dev:** Quero implementar um sistema autônomo interativo que facilite a comunicação e os agendamentos.
- **UX Designer:** Quero uma interface acessível, responsiva, com navegação fluida e identidade marcante.
- **IA / Analista de Dados:** Quero coleta estruturada de dados para análise inteligente e identificação de padrões de vendas.

---

## 🚀 Funcionalidades do Sistema

1. **Cadastrar Veículo por Marca:** Permite registrar até 3 veículos no sistema com nome, descrição e marca.
2. **Escolher Cor e Modificações:** Personalização do veículo (cor, modelo do aro e aerofólio).
3. **Escolher Horário:** Agendamento prévio do horário de atendimento.
4. **Finalizar Agendamento de Horário:** Confirmação da data (dia e mês) para a compra.
5. **Agendar Test-Drive:** Seleção de horário para realização de test-drive.
6. **Finalizar Agendamento de Test-Drive:** Confirmação da data do test-drive.
7. **Atendimento / Chat Humanizado:** Coleta de dados (nome, e-mail e telefone) para transferência para um atendente.
8. **Escolher Loja Física:** Seleção e definição do endereço da unidade física para conclusão do negócio.
9. **Feedback e Reclamações:** Canal aberto para avaliação da experiência e envio de sugestões ou reclamações.
10. **Sair:** Encerramento seguro da sessão do sistema.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Estruturas de Dados:** Variáveis simples, condicionais (`if`, `elif`, `else`) e laços de repetição (`while`).
- **Entrada e Saída:** Manipulação no console via `input()` e `print()`.

---

## 📂 Código Fonte Atualizado (`main.py`)

Abaixo está o código-fonte corrigido com todos os ajustes de sintaxe, laço de repetição e variáveis:

```python
'''
Projeto Indústria de Automóveis: Isaque e Gabriel
Sistema de Agendamento - Primus Motors
'''

# Inicialização de variáveis globais
veiculo_1 = ""
veiculo_2 = ""
veiculo_3 = ""

print("Olá, Mundo!")

while True:
    print('\n' + '〰' * 50 + '\n')
    print('Bem-vindo ao sistema de agendamento de horários - Primus Motors')
    print('1 - Cadastrar veículo, por marcas')
    print('2 - Escolhendo a cor e modificações')
    print('3 - Escolhendo o horário')
    print('4 - Finalizar agendamento do horário')
    print('5 - Agendar test-drive')        
    print('6 - Finalizar agendamento do test-drive')
    print('7 - Encaminhar para um chat com um atendente')
    print('8 - Escolher loja física onde finalizar compra')
    print('9 - Enviar feedback/Enviar Reclamação')
    print('0 - Sair')
    print('\n' + '〰' * 50 + '\n')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1': 
        print('\n1 - Cadastrar veículo, por marcas...')
        if veiculo_1 == "":             
            veiculo_1 = input('Digite o Nome do Veículo: ')
            descricao_veiculo = input('Digite a Descrição do Produto: ')
            marca_veiculo = input('Digite a Marca do Veículo: ')
            print('✅ Veículo 1 cadastrado com sucesso!')
        elif veiculo_2 == "":   
            veiculo_2 = input('Digite o Nome do Veículo: ')
            descricao_veiculo = input('Digite a Descrição do Produto: ')
            marca_veiculo = input('Digite a Marca do Veículo: ')
            print('✅ Veículo 2 cadastrado com sucesso!')
        elif veiculo_3 == "":  
            veiculo_3 = input('Digite o Nome do Veículo: ')
            descricao_veiculo = input('Digite a Descrição do Produto: ')
            marca_veiculo = input('Digite a Marca do Veículo: ')
            print('✅ Veículo 3 cadastrado com sucesso!')
        else:
            print('❌ Sistema cheio! Limite de 3 itens atingido.')    

    elif opcao == '2':
        print('\n2 - Escolhendo cor e modificações...')
        cor_veiculo = input('Digite a cor que deseja: ')
        modelo_aro_veiculo = input('Digite o modelo do aro que deseja: ')
        aerofolio_veiculo = input('Digite o modelo de aerofólio que deseja: ')

    elif opcao == '3':
        print('\n3 - Escolhendo horário...')
        agendar_horario = input('Selecione o horário: ')

    elif opcao == '4':
        print('\n4 - Finalizar agendamento do horário...')
        escolher_data = input('Digite o dia e o mês que deseja realizar a compra: ')

    elif opcao == '5':
        print('\n5 - Agendar Test-Drive...')
        agendar_horario = input('Selecione o horário: ')

    elif opcao == '6':
        print('\n6 - Finalizar Agendamento do Test-Drive...')
        escolher_data = input('Digite o dia e o mês que deseja realizar o test-drive: ')

    elif opcao == '7':
        print('\n7 - Encaminhar para um chat com um atendente...')
        seu_nome = input('Digite seu nome: ')
        seu_email = input('Digite seu e-mail: ')
        seu_numero = input('Digite seu número de telefone: ')

    elif opcao == '8':
        print('\n8 - Escolher loja física onde finalizar compra...')
        localizacao_lojafisica = input('Digite o endereço da loja física: ')

    elif opcao == '9':
        print('\n9 - Enviar feedback/Enviar Reclamação...')
        feed_back = input('Digite aqui sua experiência: ')
        reclame_aqui = input('Conte-nos o porquê sua experiência foi ruim: ')

    elif opcao == '0':
        print('\nSaindo do sistema... Primus Motors agradece!')
        break

    else:
        print('\n❌ Opção Inválida! Tente novamente.')
```

---

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto e execute:
   ```bash
   python main.py
   ```
