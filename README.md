
# WhatsApp Messages (Projeto Fullstack)

  

Projeto fullstack para cadastro de contatos, gerenciamento de mensagens e envio automático via WhatsApp (integração com Z-API). Atualmente o backend está em Python com conexão a um banco PostgreSQL hospedado no Supabase. O frontend será React (ainda em decisão).

  

## Visão geral

Tarefa                                          | Status
------------------------------------------------|-------------------------
Backend: Conector para Supabase/Postgres | Concluído
Backend: Conector para Z-API | Concluído
Backend: FastAPI para orquestração das conexões |Em andamento
CLI: Implantar as funções do front para teste | Aguardando início
Frontend: previsto React (ainda não implementado). | Levantamento de requisitos

  

## Pré-requisitos

- Python 3.8+

- Variáveis de ambiente no arquivo `.env`:

-  `SUPABASE_BASE_URL`

-  `SUPABASE_API_KEY`
-  `ZAPI_URL`
-  `ZAPI_CLIENT_TOKEN`

## Instalação (rápida)

Instale dependências essenciais:

```sh

pip  install  python-dotenv  supabase requests pytest

```  

## Configuração

1. Preencha o arquivo [.env](.env) com as chaves do Supabase:

-  `SUPABASE_BASE_URL`
-  `SUPABASE_API_KEY`
-  `ZAPI_URL`
-  `ZAPI_CLIENT_TOKEN`

2. Crie o schema/tabela no Supabase rodando [database/create_contacts.sql](database/create_contacts.sql) no seu DB.

3. (Opcional) Insira dados de exemplo usando [database/insert.sql](database/insert.sql) ou [database/insert_min.sql](database/insert_min.sql).

  

## Como executar

O exemplo atual usa [main.py](main.py) para demonstrar o conector:

```sh

python  main.py

```

O [main.py](main.py) instancia [`api.DatabaseConnector`](api/api_connector.py) e demonstra chamadas a:

```

supabase.insert_contact
supabase.get_contacts()
```
E, dentro de um loop faz o envio para o whatsapp com

```
zapi.send_message()
```
  

## Estrutura do conector

A classe principal do conector do Supabase está em [api/supabase_connector.py](api/supabase_connector.py). Ela encapsula a criação do cliente Supabase e fornece métodos para leitura/inserção de contatos.

Já a classe principal do conector do Z-API está em [api/zapi_connector.py](api/zapi_connector.py). Ela encapsula a criação do cliente ZAPI e fornece métodos para envio de mensagens.
  
 
## Próximos passos / TODOs

- Criar CLI com funções administrativas (Criar contatos, criar mensagens, enviar mensagens, etc..)

- Implementar backend HTTP (FastAPI) para expor endpoints.

- Desenvolver frontend em React para gerenciamento de contatos e mensagens.

- Adicionar testes automatizados e CI.

- Tratar melhor erros e validações na camada de inserção (ex.: evitar duplicidades, validar E.164).

  

## Observações

- Os scripts SQL estão em [database](database/). Veja [database/create_contacts.sql](database/create_contacts.sql) para a definição da tabela.

- Exemplo de payload JSON em [database/test.json](database/test.json).
	 

Contribuições e melhorias são bem-vindas.