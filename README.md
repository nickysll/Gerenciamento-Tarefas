# Gerenciamento-Tarefas
# Sistema de Gerenciamento de Tarefas

Bem-vindo ao **Sistema de Gerenciamento de Tarefas**! Este aplicativo permite que você adicione, remova, liste e marque suas tarefas como concluídas de forma simples e eficiente.

## Funcionalidades

- **Adicionar Tarefa**: Permite adicionar uma nova tarefa com nome, descrição e status.
- **Remover Tarefa**: Remove uma tarefa existente com base no índice informado.
- **Listar Tarefas**: Exibe todas as tarefas registradas, incluindo seu estado atual.
- **Marcar como Concluída**: Atualiza o status de uma tarefa para "Concluída".
- **Interface Simples**: O menu interativo facilita a navegação e o gerenciamento de tarefas.

## Como Usar

1. **Inicie o aplicativo**: Execute o código e você será recebido com um menu de opções.
2. **Escolha uma ação**: Selecione uma das opções disponíveis:
   - **Adicionar Tarefa**: Informe o nome, descrição e status da tarefa.
   - **Remover Tarefa**: Digite o número da tarefa que deseja remover.
   - **Listar Tarefas**: Visualize todas as suas tarefas e seus estados.
   - **Marcar como Concluída**: Selecione o número da tarefa a ser marcada como concluída.
   - **Sair**: Encerre o aplicativo.
3. **Confirmações**: O aplicativo fornecerá mensagens de sucesso após cada ação.

## Estrutura do Código

- **Função `mostra_menu()`**: Exibe as opções disponíveis para o usuário.
- **Função `escolhe_status()`**: Permite ao usuário selecionar o status da tarefa (Não iniciada, Em andamento, Concluída).
- **Função `adicionar_tarefa()`**: Adiciona uma nova tarefa à lista e exibe as tarefas existentes.
- **Função `remover_tarefa()`**: Remove uma tarefa com base no índice fornecido.
- **Função `tarefa_concluida()`**: Marca uma tarefa como concluída.
- **Loop Principal**: O aplicativo continua executando até que o usuário escolha sair.

## Exemplo de Uso

```python
# Para iniciar o aplicativo, execute o código e siga as instruções do menu.
