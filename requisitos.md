# Requisitos de Software

<h2>Sistema de Gestão de Processos Judiciais (SGPJ)</h2>

<small>Versão 1.0</small>

---

## Histórico de revisões

|    Data    | Versão |           Descrição           |      Autor       |
| :--------: | :----: | :---------------------------: | :--------------: |
| 10/09/2024 |  1.0   |    Criação do documento        | Equipe 4         |

---

## Sumário

- [Capa](#capa)
  - [Histórico de revisões](#histórico-de-revisões)
  - [Sumário](#sumário)
- [Introdução](#introdução)
  - [Definições, Acrônimos e Abreviações](#definições-acrônimos-e-abreviações)
- [Usuários Identificados](#usuários-identificados)
- [Requisitos Funcionais](#requisitos-funcionais)
- [Requisitos Não-Funcionais](#requisitos-não-funcionais)
  - [Disponibilidade](#disponibilidade)
  - [Privacidade e Segurança](#privacidade-e-segurança)
  - [Usabilidade](#usabilidade)
  - [Suportabilidade](#suportabilidade)
  - [Interoperabilidade](#interoperabilidade)
  - [Manutenibilidade](#manutenibilidade)
  - [Desempenho](#desempenho)
  - [Implantação](#implantação)

---

# Introdução

Este documento apresenta os requisitos de software para o **Sistema de Gestão de Processos Judiciais (SGPJ)**, que será utilizado por advogados, funcionários administrativos e administradores para facilitar o gerenciamento de processos judiciais, intimações, prazos e audiências.

## Definições, Acrônimos e Abreviações

Esta subseção fornece as definições de todos os termos, acrônimos e abreviações necessárias à adequada interpretação do Documento de Requisitos.

- Identificação dos requisitos: por convenção, a referência a requisitos é feita através do identificador de requisitos, de acordo como descrito abaixo:

  `[IDENTIFICADOR DO TIPO DE REQUISITOSidentificador do requisito]`

  O identificador do tipo de requisitos é conforme abaixo:

  - RF – Requisito Funcional
  - RNF – Requisito Não-Funcional
  - NR – Não-Requisito

  O identificador do requisito será uma sequência numérica. Esse número sequencial será único para todo o conjunto de tipos de requisitos.

  **Exemplo**: RF0001, RF1234, RNF1234, NR1212

---

# Usuários Identificados

Os seguintes usuários foram identificados para o **SGPJ**:

- **Advogados**: Utilizam o sistema para gerenciar seus processos, intimações e prazos.
- **Funcionários Administrativos**: Auxiliam na gestão dos processos e no suporte administrativo aos advogados.
- **Administradores**: Gerenciam o sistema, controlando o cadastro de usuários e os backups de dados.

---

# Requisitos Funcionais

- **[RF001]** Como usuário, gostaria de acessar a plataforma através de credenciais como email e senha ou certificado digital.
- **[RF002]** Como administrador, gostaria de cadastrar advogados e funcionários.
- **[RF003]** Como advogado ou funcionário, gostaria de selecionar as UFs cujas publicações nos diários da justiça desejo monitorar.
- **[RF004]** Como advogado ou funcionário, gostaria de registrar meus clientes e seus respectivos processos, armazenando dados pessoais e informações das demandas judiciais.
- **[RF005]** Como advogado, funcionário ou administrador, gostaria de ter o histórico dos advogados e/ou estagiários que atuaram em cada fase dos processos judiciais dos clientes.
- **[RF006]** Como administrador, gostaria de realizar o backup dos dados dos clientes e seus respectivos processos, para poder recuperá-los em caso de falha.
- **[RF007]** Como advogado ou funcionário, gostaria de gerenciar minhas audiências de maneira cronológica.
- **[RF008]** Como advogado ou funcionário, gostaria que o sistema fosse capaz de ler automaticamente as intimações no PJe e categorizá-las.
- **[RF009]** Como administrador, gostaria de definir um horário para que o sistema realizasse as buscas de publicações para os advogados do escritório nos diários da justiça.
- **[RF010]** Como advogado ou funcionário, gostaria de poder visualizar e interagir com as notificações das publicações dos diários da justiça, marcando-as como concluídas, em andamento ou a serem feitas.
- **[RF011]** Como advogado ou funcionário, gostaria de poder excluir as notificações das publicações dos diários da justiça.
- **[RF012]** Como advogado ou funcionário, gostaria de categorizar os processos em **URGENTES**, **PRIORITÁRIOS** ou **SEM PRIORIDADE**.
- **[RF013]** Como advogado ou funcionário, gostaria de encaminhar para o WhatsApp dos clientes o andamento processual dos seus respectivos processos.
- **[RF014]** Como administrador, gostaria de remover os funcionários e advogados do sistema.
- **[RF015]** Como administrador, gostaria de conceder e revogar as permissões dos funcionários e advogados a qualquer momento.
- **[RF016]** Como administrador, gostaria de vincular e desvincular cada funcionário a seu respectivo advogado.
- **[RF017]** Como administrador, gostaria de abrir chamados diretamente para a equipe de suporte do sistema.
- **[RF018]** Como advogado ou funcionário, gostaria de pesquisar jurisprudências e doutrinas dentro do sistema, com base em palavras-chave e categorias.
- **[RF019]** Como administrador, gostaria de acessar um painel que mostrasse a produtividade dos advogados e funcionários do sistema.
- **[RF020]** Como administrador, gostaria de anotar as faltas funcionais dos advogados e funcionários.

---

# Requisitos Não-Funcionais

## Disponibilidade
- **[RNF001]** O sistema deverá estar disponível 24 horas por dia, 7 dias por semana, 365 dias por ano.

## Privacidade e Segurança
- **[RNF002]** O sistema deve ser integrado com o Diário da Justiça para a leitura das intimações.
- **[RNF005]** O sistema deve ser seguro, protegido contra acesso não autorizado, invasões e roubo de dados.

## Usabilidade
- **[RNF006]** O sistema deve ser fácil de usar, sem exigir treinamento extenso para advogados e funcionários.

## Suportabilidade
- **[RNF007]** O sistema deve ser compatível com os navegadores Google Chrome, Mozilla Firefox e Microsoft Edge.

## Interoperabilidade
- **[RNF008]** O sistema deve ser integrado com os sites dos tribunais de justiça para permitir buscas por jurisprudência.

## Manutenibilidade
- **[RNF009]** O sistema deve ser escalável, permitindo a expansão de sua capacidade sem perda de desempenho.

## Desempenho
- **[RNF010]** O tempo de resposta do sistema deve ser de no máximo 5 segundos com uma conexão de 1 Mbps.

## Implantação
- **[RNF011]** O sistema deve ser executado em qualquer dispositivo com conexão à internet, incluindo desktops, tablets e smartphones.

# Matriz de Rastreabilidade

| RF / RNF  | RNF001 | RNF002 | RNF003 | RNF004 | RNF005 | RNF006 | RNF007 | RNF008 | RNF009 | RNF010 | RNF011 |
| :-------: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|  **RF001**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF002**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF003**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF004**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF005**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF006**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF007**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF008**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF009**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF010**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF011**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF012**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF013**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF014**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF015**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF016**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF017**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF018**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF019**|        |        |        |        |        |        |        |        |        |        |        |
|  **RF020**|        |        |        |        |        |        |        |        |        |        |        |

---

Data: 10 de setembro de 2024

**Validado por:**

<address>
<a href="mailto:equipe4@equipe4.com.br">Equipe 4</a> | Desenvolvimento de Software<br>
equipe4@equipe4.com.br<br>
equipe4.com<br>
Av. Epitácio Pessoa, S/N, João Pessoa(PB)<br>
BRA
</address>

---

Criado em Setembro de 2024 por Equipe 4

---
