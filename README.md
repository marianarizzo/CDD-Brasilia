# Sistema de Etiquetas A4 - CDD Brasília

Sistema web interno para solicitar, organizar e imprimir folhas A4 no padrão operacional do CDD Brasília.

## O que ele faz

- permite lançar solicitações no **celular** ou no **computador**
- guarda **rua** e **endereço** apenas para controle interno
- gera a **quantidade correta de folhas** para impressão
- organiza as solicitações por **rua/endereço**
- permite que outra pessoa abra no computador e apenas **imprima**
- marca registros como **impresso** e permite **reabrir** quando necessário

## Importante sobre uso em várias máquinas

Este sistema **não salva nada no celular ou no computador do usuário**.

Ele precisa ficar rodando em **um servidor central** da operação:

- pode ser um computador da área rodando como servidor interno
- pode ser um mini PC / servidor local
- pode ser um servidor na nuvem

Todos os celulares e computadores acessam o **mesmo endereço** do sistema, então os dados ficam centralizados.

## Tecnologias

- FastAPI
- Jinja2
- SQLite (já incluso, bom para começar)

## Recomendação para produção

Para começar, o SQLite atende bem se o sistema estiver rodando em um único servidor.

Se quiser crescer com mais volume e concorrência, vale migrar depois para **PostgreSQL**.

## Como rodar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Inicie o sistema

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. Acesse

No próprio servidor:

```text
http://localhost:8000
```

Em outras máquinas da mesma rede:

```text
http://IP_DO_SERVIDOR:8000
```

Exemplo:

```text
http://192.168.0.25:8000
```

## Estrutura das telas

### Painel
- mostra os grupos por rua/endereço
- permite ver pendentes, impressos ou todos
- abre detalhes do grupo
- gera impressão do grupo

### Nova solicitação
Campos:
- código
- origem
- produto
- recebimento
- conferente
- vencimento
- quantidade de folhas
- rua
- endereço
- observação opcional

### Impressão
- abre todas as páginas A4 prontas
- botão para imprimir
- botão para marcar como impresso

## Banco de dados

O arquivo padrão fica em:

```text
/data/app.db
```

Você pode trocar isso com variável de ambiente:

```bash
CDD_DB_PATH=/caminho/compartilhado/app.db
```

## Ajustes fáceis

No arquivo `main.py`, você pode mudar o nome do cabeçalho:

```python
CDD_NAME = os.getenv("CDD_NAME", "CDD BRASÍLIA")
```

Ou via ambiente:

```bash
CDD_NAME="CDD BRASILIA"
```

## Próximo passo ideal

Para uso real na operação, o melhor cenário é:

- deixar esse sistema em um servidor da rede interna
- colocar um atalho no celular e no computador
- conectar a impressora no computador da área de impressão



## Deploy pronto para nuvem

O projeto já vai com:

- `render.yaml` para subir no **Render**
- `Procfile` para compatibilidade simples de deploy
- banco em disco persistente (`/var/data/app.db`) no Render
- botão de **Imprimir tudo da rua** no painel

### Subir no Render

1. Coloque essa pasta em um repositório GitHub.
2. No Render, crie um novo **Blueprint** apontando para esse repositório.
3. O Render vai ler o `render.yaml` e criar o serviço web com disco persistente.
4. Depois é só abrir a URL pública do sistema no celular e no computador.

### Importante

Eu consigo deixar o projeto pronto para deploy, mas a publicação em uma conta de nuvem precisa ser feita em uma conta sua ou da empresa.
