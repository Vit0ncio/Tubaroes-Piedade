# Instruções

Esse arquivo contém as tarefas que deverão ser executadas por cada membro do grupo.  

Cada pessoa será responsável por um arquivo, sendo eles:
* **main.py** (Arthur)
* **crm.py** (Carlos)
* **motor_solar.py** (Vitor)
* **catalogo_poo.py** (Antônio)
* **proposta.py** (Juan)

O workflow será da seguinte forma:

```
  Vitor─┐
        ├─Carlos──Arthur
Antonio─┘            │
                Juan─┘
```

## 1. main.py (Arthur)
Vai juntar tudo no `main.py`, vai pegar as funções de outros arquivos e chamar eles na ordem certa.

### Tarefas:
1. Chama crm para coletar todos os dados do cliente
2. Mostra o catálogo feito no `catalogo_poo` (Antônio) e deixa o usuário escolher o painel
3. Chama as funções do `motor_solar` (Vitor) com os dados coletados
4. Se for Off-Grid, chama também o cálculo de baterias
5. Calcula custo total e payback
6. Chama proposta para imprimit o ticket final

## 2. crm.py (Carlos)
Vai criar o formulário com as perguntas pro usuário responder.

### Tarefas:
1. Pede o nome do cliente
2. Pede o consumo dos 12 meses um por um (usando `for`) e não aceita número negativo
3. Calcula a média dos 12 meses automaticamente
4. Pede o HSP da cidade do cliente
5. Pergunta se o sistema é On-Grid ou Off-Grid
6. Se for Off-Grid, pede a autonomia em dias e a tensão do sistema

## 3. motor_solar.py (Vitor)
Vai criar todas as funções de cálculo do sistema.

### Tarefas:
1. Função que calcula o consumo diário (`consumo mensal/30`)
2. Função que calcula o kWp (`consumo diário / (HSP * 0.80)`)
3. Função que calcula a quantidade de painéis e arredonda pra cima sem usar bibliotecas
4. Função que calcula o banco de baterias em Ah (só usada se for Off-Grid)

## 4. catalogo_poo.py (Antônio)
Vai criar os produtos que o cliente pode escolher

### Tarefas:
1. Criar a classe PainelSolar com modelo, potência e peso
2. Criar a classe Inversor com modelo, potência e preço
3. Criar a classe Bateria com modelo, capacidade e tensão
4. Cirar listas com 2 ou 3 objetod de cada classe pra o usuário escolher pelo número

## 5. proposta.py (Juan):
Vai pegar todos os resultados e imprimir o recibo final no terminal.

### Tarefas:
1. Recebe todos os dados calculados como parâmetro
2. Imprime o nome do cliente e tipo do sistema
3. Imprime quantidade de painéis e kWp
4. Imprime o custo total de cada item separado e o total geral
5. Imprime a economia mensal e o payback em meses
