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

**[RF001]** - Como **usuário**, eu gostaria de acessar a plataforma através de credenciais como e-mail e senha ou certificado digital, **para que** eu possa utilizar os serviços oferecidos de forma segura e autenticada.

**[RF022]** - Como **usuário**, eu gostaria de recuperar minha senha caso a tenha esquecido, recebendo um link de redefinição no meu e-mail cadastrado, **para que** eu possa acessar a plataforma novamente de forma segura.

**[RF002]** - Como **administrador**, eu gostaria de cadastrar advogados no sistema, registrando os seguintes dados: nome, CPF, OAB, endereço, data de nascimento, telefone e e-mail, **para que** eles possam acessar e utilizar a plataforma.

**[RF021]** - Como **administrador**, eu gostaria de cadastrar funcionários no sistema, registrando os seguintes dados: nome, CPF, endereço, data de nascimento, telefone e e-mail, **para que** eles possam desempenhar suas funções dentro da plataforma.

**[RF003]** - Como **advogado ou funcionário**, eu gostaria de selecionar as UFs (Unidades da Federação) cujas publicações nos diários da justiça desejo monitorar, selecionando uma ou mais UFs e salvando a seleção ao clicar em um botão "Salvar", **para que** eu possa acompanhar as publicações relevantes aos meus casos.

**[RF004]** - Como **advogado ou funcionário**, eu gostaria de registrar meus clientes e seus respectivos processos, armazenando dados pessoais e informações das demandas judiciais, **para que** eu possa gerenciar e acompanhar os casos de forma eficiente.

**[RF005]** - Como **advogado, funcionário ou administrador**, eu gostaria de ter o histórico dos advogados e/ou estagiários que atuaram em cada fase dos processos judiciais dos clientes do escritório, **para que** eu possa rastrear a participação da equipe em cada caso.

**[RF006]** - Como **administrador**, eu gostaria de realizar o backup dos dados dos clientes e seus respectivos processos, **para que** eu possa recuperá-los em caso de falha no sistema.

**[RF007]** - Como **advogado ou funcionário**, eu gostaria de gerenciar minhas audiências de maneira cronológica, **para que** eu possa organizar meu calendário e compromissos judiciais.

**[RF008]** - Como **advogado ou funcionário**, eu gostaria que o sistema fosse capaz de ler automaticamente as intimações no PJe (Processo Judicial Eletrônico) e categorizá-las, **para que** eu possa identificar rapidamente as ações necessárias.

**[RF009]** - Como **administrador**, eu gostaria de definir um horário para que o sistema realize as buscas de publicações para os advogados do escritório nos diários da justiça, **para que** possamos otimizar o fluxo de trabalho e garantir atualizações oportunas.

**[RF010]** - Como **advogado ou funcionário**, eu gostaria de poder visualizar e interagir com as notificações das publicações dos diários da justiça, marcando-as como "concluídas", "em andamento" ou "a serem feitas", **para que** eu possa gerenciar minhas tarefas de forma eficaz.

**[RF011]** - Como **advogado ou funcionário**, eu gostaria de poder excluir as notificações das publicações dos diários da justiça, **para que** eu possa manter minha área de trabalho organizada e relevante.

**[RF012]** - Como **advogado ou funcionário**, eu gostaria de categorizar os processos em "urgentes", "prioritários" ou "sem prioridade", **para que** eu possa estabelecer prioridades no meu trabalho diário.

**[RF013]** - Como **advogado ou funcionário**, eu gostaria de encaminhar para o WhatsApp dos clientes o andamento processual dos seus respectivos processos, **para que** eles estejam sempre informados sobre o status de seus casos.

**[RF014]** - Como **administrador**, eu gostaria de remover funcionários e advogados do sistema, **para que** eu possa manter o controle sobre o acesso e a segurança da plataforma.

**[RF015]** - Como **administrador**, eu gostaria de conceder e revogar as permissões dos funcionários e advogados a qualquer momento, **para que** eu possa controlar quem tem acesso a determinadas funcionalidades do sistema.

**[RF016]** - Como **administrador**, eu gostaria de vincular e desvincular cada funcionário ao seu respectivo advogado, **para que** eu possa organizar a estrutura de trabalho e hierarquia dentro do sistema.

**[RF017]** - Como **administrador**, eu gostaria de abrir chamados diretamente para a equipe de suporte do sistema, **para que** eu possa reportar problemas ou solicitar melhorias.

**[RF018]** - Como **advogado ou funcionário**, eu gostaria de pesquisar jurisprudências e doutrinas dentro do sistema, com base em palavras-chave e categorias, **para que** eu possa fundamentar melhor os processos.

**[RF019]** - Como **administrador**, eu gostaria de acessar um painel que mostre a produtividade dos advogados e funcionários do sistema, **para que** eu possa monitorar o desempenho da equipe.

**[RF020]** - Como **administrador**, eu gostaria de anotar as faltas funcionais dos advogados e funcionários, **para que** eu possa acompanhar a assiduidade e cumprir com as políticas internas.

---

# Requisitos Não-Funcionais

## Disponibilidade
- **[RNF007]** O sistema deverá estar disponível 24 horas por dia, 7 dias por semana, 365 dias por ano.

## Privacidade e Segurança
- **[RNF005]** O sistema deve ser seguro, protegido contra acesso não autorizado, invasões e roubo de dados.

## Usabilidade
- **[RNF006]** O sistema deve ser desenvolvido de forma que seja fácil de usar e de fácil aprendizado, de forma que os usuários não precisem de um treinamento extensivo para utilizá-lo.

## Suportabilidade
- **[RNF002]** O sistema deve ser desenvolvido de forma que possa ser executado nos três principais navegadores da web: Google Chrome, Mozilla Firefox e Microsoft Edge, através de um computador com sistema operacional Windows, Linux ou Mac OS, bem como tablets e smartphones com sistema operacional Android ou iOS.

## Interoperabilidade
- **[RNF001]** O sistema deve ser integrado com o Diário da Justiça para a leitura das intimações.
- **[RNF008]** O sistema deve ser integrado com os sites dos tribunais de justiça para permitir buscas por jurisprudência.

## Manutenibilidade
- **[RNF004]** O sistema deve ser desenvolvido de forma que possa ser escalável, ou seja, deve ser possível aumentar a capacidade de armazenamento de dados e de processamento de requisições sem que haja perda de desempenho.
- **[RNF009]** O sistema deve ser desenvolvido de forma que possa ser facilmente atualizado e mantido, preferencialmente, de maneira automatizada.
- **[RNF010]** O sistema deve ser desenvolvido de forma que possa ser facilmente testado e validado, de forma manual e automatizada.

## Desempenho
- **[RNF003]** O sistema deve ser desenvolvido de forma que possa ser executado em qualquer dispositivo com conexão à internet, com velocidade de conexão de no mínimo 1 Mbps com tempo de resposta de no máximo 5 segundos.

# Matriz de Rastreabilidade

| RF / RNF  | RNF001 | RNF002 | RNF003 | RNF004 | RNF005 | RNF006 | RNF007 | RNF008 | RNF009 | RNF010 |
| :-------: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|  **RF001**|        |        |        |        |   X    |        |        |        |        |        |
|  **RF002**|        |        |        |        |        |        |        |        |        |        |
|  **RF003**|        |        |        |        |        |        |        |        |        |        |
|  **RF004**|        |        |        |        |        |        |        |        |        |        |
|  **RF005**|        |        |        |        |   X    |        |        |        |        |        |
|  **RF006**|        |        |        |        |        |        |        |        |        |        |
|  **RF007**|        |        |        |        |        |        |        |        |        |        |
|  **RF008**|        |        |        |        |        |        |        |        |        |        |
|  **RF009**|   X    |        |        |        |        |        |        |        |        |        |
|  **RF010**|   X    |        |        |        |        |        |        |        |        |        |
|  **RF011**|   X    |        |        |        |        |        |        |        |        |        |
|  **RF012**|        |        |        |        |        |        |        |        |        |        |
|  **RF013**|        |        |        |        |        |        |        |        |        |        |
|  **RF014**|        |        |        |        |        |        |        |        |        |        |
|  **RF015**|        |        |        |        |        |        |        |        |        |        |
|  **RF016**|        |        |        |        |        |        |        |        |        |        |
|  **RF017**|        |        |        |        |        |        |        |        |        |        |
|  **RF018**|        |        |        |        |        |        |        |   X    |        |        |
|  **RF019**|        |        |        |        |        |        |        |        |        |        |
|  **RF020**|        |        |        |        |        |        |        |        |        |        |

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
