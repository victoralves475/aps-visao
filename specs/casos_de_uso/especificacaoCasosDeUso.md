## Caso de Uso UC1 - Acessar plataforma

**Objetivo**: Permitir que o usuário acesse a plataforma de forma segura utilizando credenciais como e-mail e senha ou certificado digital.

**Requisitos**: RF001

**Atores**: Usuário

**Condição de entrada**: O usuário deseja acessar a plataforma e está na tela de login.

**Fluxo principal**:

1. O usuário acessa a página de login da plataforma.
2. O usuário escolhe o método de autenticação: e-mail e senha ou certificado digital.
3. **Se escolher e-mail e senha**:
   - 3.1. O usuário insere seu e-mail e senha nos campos correspondentes.
4. **Se escolher certificado digital**:
   - 4.1. O usuário conecta o dispositivo do certificado digital ao computador.
   - 4.2. O sistema detecta o certificado digital.
5. O usuário clica no botão "Entrar".
6. O sistema valida as credenciais fornecidas. **RN1**
7. O sistema verifica se o usuário possui permissão de acesso.
8. O sistema redireciona o usuário para o dashboard correspondente ao seu perfil.

**Fluxos alternativos**:

- **FA1 - Esqueci minha senha**:
  - 1. O usuário clica no link "Esqueci minha senha".
  - 2. O sistema inicia o caso de uso **UC2 - Recuperar senha**.

**Fluxos de exceção**:

- **RN1 - Validação de credenciais**:
  - **E1**: Se as credenciais forem inválidas, o sistema exibe a mensagem **MSG01** e retorna à tela de login.
  - **E2**: Se o certificado digital não for reconhecido, o sistema exibe a mensagem **MSG02**.

---

## Caso de Uso UC2 - Recuperar senha

**Objetivo**: Permitir que o usuário recupere sua senha caso a tenha esquecido.

**Requisitos**: RF019, RF020

**Atores**: Usuário

**Condição de entrada**: O usuário selecionou "Esqueci minha senha" na tela de login.

**Fluxo principal**:

1. O sistema exibe a tela de recuperação de senha solicitando o e-mail cadastrado.
2. O usuário insere seu e-mail e clica em "Enviar".
3. O sistema verifica se o e-mail está cadastrado. **RN2**
4. O sistema envia um e-mail com um link de redefinição de senha. **MSG03**
5. O usuário acessa o e-mail e clica no link fornecido.
6. O sistema exibe a tela de redefinição de senha.
7. O usuário insere a nova senha e confirma.
8. O sistema valida a força da senha. **RN3**
9. O sistema atualiza a senha e exibe a mensagem de sucesso. **MSG04**

**Fluxos alternativos**:

- **FA1 - E-mail não cadastrado**:
  - 1. Se o e-mail não estiver cadastrado, o sistema exibe a mensagem **MSG05**.

**Fluxos de exceção**:

- **RN2 - Verificação de e-mail**:
  - Todas as informações são obrigatórias.
- **RN3 - Validação de senha**:
  - A senha deve atender aos critérios de segurança (mínimo de 8 caracteres, incluindo letras e números).

---

## Caso de Uso UC3 - Cadastrar advogados

**Objetivo**: Permitir que o administrador cadastre novos advogados no sistema.

**Requisitos**: RF002

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e seleciona a opção "Cadastrar Advogado" no menu de administração.

**Fluxo principal**:

1. O sistema exibe o formulário de cadastro de advogados com os campos: nome, CPF, OAB, endereço, data de nascimento, telefone e e-mail.
2. O administrador preenche todos os campos obrigatórios.
3. O administrador clica em "Salvar".
4. O sistema valida as informações inseridas. **RN4**
5. O sistema registra o novo advogado no banco de dados.
6. O sistema exibe a mensagem de sucesso. **MSG06**

**Fluxos alternativos**:

- **FA1 - Cadastro duplicado**:
  - 1. Se o CPF ou OAB já estiver cadastrado, o sistema exibe a mensagem **MSG07**.

**Fluxos de exceção**:

- **RN4 - Validação de dados**:
  - Todos os campos marcados como obrigatórios devem ser preenchidos.
  - O CPF e OAB devem ser únicos no sistema.

---

## Caso de Uso UC4 - Cadastrar funcionários

**Objetivo**: Permitir que o administrador cadastre novos funcionários no sistema.

**Requisitos**: RF021

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e seleciona a opção "Cadastrar Funcionário" no menu de administração.

**Fluxo principal**:

1. O sistema exibe o formulário de cadastro de funcionários com os campos: nome, CPF, endereço, data de nascimento, telefone e e-mail.
2. O administrador preenche todos os campos obrigatórios.
3. O administrador clica em "Salvar".
4. O sistema valida as informações inseridas. **RN5**
5. O sistema registra o novo funcionário no banco de dados.
6. O sistema exibe a mensagem de sucesso. **MSG06**

**Fluxos alternativos**:

- **FA1 - Cadastro duplicado**:
  - 1. Se o CPF já estiver cadastrado, o sistema exibe a mensagem **MSG07**.

**Fluxos de exceção**:

- **RN5 - Validação de dados**:
  - Todos os campos marcados como obrigatórios devem ser preenchidos.
  - O CPF deve ser único no sistema.

---

## Caso de Uso UC5 - Selecionar UFs para monitorar publicações

**Objetivo**: Permitir que o advogado ou funcionário selecione as unidades federativas (UFs) cujas publicações deseja monitorar nos diários da justiça.

**Requisitos**: RF003

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e acessa a opção "Configurar Monitoramento" no menu.

**Fluxo principal**:

1. O sistema exibe a lista de todas as UFs disponíveis para monitoramento.
2. O usuário seleciona uma ou mais UFs marcando as caixas correspondentes.
3. O usuário clica no botão "Salvar".
4. O sistema registra as UFs selecionadas para o usuário.
5. O sistema exibe a mensagem de sucesso. **MSG08**

**Fluxos alternativos**:

- **FA1 - Nenhuma UF selecionada**:
  - 1. Se o usuário não selecionar nenhuma UF, o sistema exibe a mensagem **MSG09** solicitando a seleção de pelo menos uma UF.

**Fluxos de exceção**:

- **RN6 - Seleção mínima**:
  - Pelo menos uma UF deve ser selecionada para o monitoramento.

---

## Caso de Uso UC6 - Registrar clientes e processos

**Objetivo**: Permitir que o advogado ou funcionário registre clientes e seus respectivos processos, armazenando dados pessoais e informações das demandas judiciais.

**Requisitos**: RF004

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e acessa a opção "Cadastrar Cliente/Processo" no menu.

**Fluxo principal**:

1. O sistema exibe o formulário de cadastro com campos para dados pessoais do cliente (nome, CPF, endereço, telefone, e-mail) e informações do processo (número do processo, vara, comarca, assunto, descrição).
2. O usuário preenche todos os campos obrigatórios.
3. O usuário clica em "Salvar".
4. O sistema valida as informações inseridas. **RN7**
5. O sistema registra o cliente e o processo no banco de dados.
6. O sistema exibe a mensagem de sucesso. **MSG06**

**Fluxos alternativos**:

- **FA1 - Cliente já cadastrado**:
  - 1. Se o CPF do cliente já estiver cadastrado, o sistema pergunta se deseja vincular o novo processo ao cliente existente.

**Fluxos de exceção**:

- **RN7 - Validação de dados**:
  - Todos os campos obrigatórios devem ser preenchidos.
  - O CPF do cliente deve ser válido.

---

## Caso de Uso UC7 - Visualizar histórico de atuação em processos

**Objetivo**: Permitir que o advogado ou funcionário visualize o histórico de profissionais que atuaram em cada fase dos processos judiciais dos clientes.

**Requisitos**: RF005

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e acessa a opção "Histórico de Atuação" em um processo específico.

**Fluxo principal**:

1. O sistema exibe a lista de fases do processo selecionado.
2. Para cada fase, o sistema mostra os advogados e estagiários que atuaram.
3. O usuário pode filtrar o histórico por data, profissional ou fase do processo.
4. O usuário visualiza os detalhes conforme necessário.

**Fluxos alternativos**:

- **FA1 - Nenhum histórico disponível**:
  - 1. Se não houver registros de atuação, o sistema exibe a mensagem **MSG10** informando a ausência de histórico.

**Fluxos de exceção**:

- **RN8 - Permissões de acesso**:
  - O usuário deve ter permissão para visualizar o processo.

---

## Caso de Uso UC8 - Gerenciar audiências cronologicamente

**Objetivo**: Permitir que o advogado ou funcionário gerencie suas audiências de forma cronológica.

**Requisitos**: RF007

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e acessa a opção "Agenda de Audiências".

**Fluxo principal**:

1. O sistema exibe um calendário com as audiências agendadas.
2. O usuário pode visualizar audiências passadas e futuras.
3. O usuário pode adicionar, editar ou remover audiências.
4. O sistema permite a inclusão de detalhes como data, hora, local, processo relacionado e observações.
5. O sistema salva as alterações e atualiza o calendário.

**Fluxos alternativos**:

- **FA1 - Conflito de horários**:
  - 1. Se o usuário tenta agendar uma audiência em um horário já ocupado, o sistema exibe a mensagem **MSG11**.

**Fluxos de exceção**:

- **RN9 - Validação de datas**:
  - A data e hora da audiência devem ser futuras ao momento atual.

---

## Caso de Uso UC9 - Ler e categorizar intimações do PJe

**Objetivo**: Permitir que o sistema leia automaticamente as intimações no PJe e as categorize para o advogado ou funcionário.

**Requisitos**: RF008

**Atores**: Sistema (processo automatizado), Advogado, Funcionário

**Condição de entrada**: O sistema está programado para realizar a leitura das intimações.

**Fluxo principal**:

1. O sistema acessa o PJe utilizando as credenciais dos usuários configurados.
2. O sistema verifica novas intimações disponíveis.
3. O sistema baixa as intimações e as associa aos processos correspondentes.
4. O sistema categoriza as intimações com base em critérios predefinidos (urgência, assunto, prazo).
5. O sistema notifica o advogado ou funcionário sobre as novas intimações.

**Fluxos alternativos**:

- **FA1 - Falha na conexão**:
  - 1. Se o sistema não conseguir acessar o PJe, registra o erro e notifica o administrador.

**Fluxos de exceção**:

- **RN10 - Segurança e privacidade**:
  - As credenciais devem ser armazenadas de forma segura.
  - O acesso ao PJe deve estar em conformidade com as políticas de uso.

---

## Caso de Uso UC10 - Interagir com notificações das publicações

**Objetivo**: Permitir que o advogado ou funcionário visualize e gerencie as notificações das publicações dos diários da justiça.

**Requisitos**: RF010

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e acessa a seção "Notificações".

**Fluxo principal**:

1. O sistema exibe a lista de notificações com status "A serem feitas", "Em andamento" ou "Concluídas".
2. O usuário seleciona uma notificação para visualizar os detalhes.
3. O usuário pode alterar o status da notificação conforme o progresso da tarefa.
4. O sistema atualiza o status e registra a data e hora da alteração.

**Fluxos alternativos**:

- **FA1 - Filtrar notificações**:
  - 1. O usuário aplica filtros por status, data ou tipo de publicação para facilitar a busca.

**Fluxos de exceção**:

- **RN11 - Permissões de edição**:
  - Apenas o responsável pela notificação ou seu superior pode alterar o status.

---

## Caso de Uso UC11 - Excluir notificações das publicações

**Objetivo**: Permitir que o advogado ou funcionário exclua notificações irrelevantes ou duplicadas.

**Requisitos**: RF011

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e na lista de notificações.

**Fluxo principal**:

1. O usuário seleciona a notificação que deseja excluir.
2. O usuário clica no botão "Excluir".
3. O sistema solicita confirmação da exclusão.
4. O usuário confirma a ação.
5. O sistema remove a notificação da lista e atualiza o banco de dados.
6. O sistema exibe a mensagem de sucesso. **MSG12**

**Fluxos alternativos**:

- **FA1 - Cancelar exclusão**:
  - 1. Se o usuário cancelar a ação, o sistema não realiza nenhuma alteração.

**Fluxos de exceção**:

- **RN12 - Registro de atividades**:
  - O sistema deve manter um registro da exclusão para fins de auditoria.

---

## Caso de Uso UC12 - Categorizar processos

**Objetivo**: Permitir que o advogado ou funcionário categorize os processos em "Urgentes", "Prioritários" ou "Sem Prioridade".

**Requisitos**: RF012

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e acessa a lista de processos.

**Fluxo principal**:

1. O sistema exibe a lista de processos do usuário.
2. O usuário seleciona um processo para categorizar.
3. O usuário escolhe a categoria desejada.
4. O sistema atualiza a categoria do processo.
5. O sistema exibe a mensagem de sucesso. **MSG13**

**Fluxos alternativos**:

- **FA1 - Alteração em massa**:
  - 1. O usuário seleciona múltiplos processos e aplica a mesma categoria a todos.

**Fluxos de exceção**:

- **RN13 - Permissões de edição**:
  - O usuário deve ter permissão para editar o processo.

---

## Caso de Uso UC13 - Enviar andamento processual via WhatsApp

**Objetivo**: Permitir que o advogado ou funcionário encaminhe atualizações do andamento processual aos clientes via WhatsApp.

**Requisitos**: RF013

**Atores**: Advogado, Funcionário

**Condição de entrada**: O usuário está autenticado e acessa o processo de um cliente.

**Fluxo principal**:

1. O sistema exibe os detalhes do processo selecionado.
2. O usuário clica na opção "Enviar via WhatsApp".
3. O sistema gera uma mensagem padrão com as informações do andamento processual.
4. O sistema abre o aplicativo do WhatsApp ou web com a mensagem pronta e o contato do cliente.
5. O usuário confirma o envio no WhatsApp.

**Fluxos alternativos**:

- **FA1 - Editar mensagem**:
  - 1. O usuário edita a mensagem antes de enviar.

**Fluxos de exceção**:

- **RN14 - Consentimento do cliente**:
  - O cliente deve ter autorizado o recebimento de mensagens via WhatsApp.

---

## Caso de Uso UC14 - Remover advogados e funcionários

**Objetivo**: Permitir que o administrador remova advogados e funcionários do sistema.

**Requisitos**: RF014

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e acessa a lista de usuários.

**Fluxo principal**:

1. O sistema exibe a lista de advogados e funcionários cadastrados.
2. O administrador seleciona o usuário que deseja remover.
3. O administrador clica em "Remover".
4. O sistema solicita confirmação da ação.
5. O administrador confirma a remoção.
6. O sistema desativa o usuário e impede futuros acessos.
7. O sistema exibe a mensagem de sucesso. **MSG14**

**Fluxos alternativos**:

- **FA1 - Cancelar remoção**:
  - 1. Se o administrador cancelar a ação, o sistema não realiza nenhuma alteração.

**Fluxos de exceção**:

- **RN15 - Registro de atividades**:
  - O sistema deve manter um registro da remoção para fins de auditoria.

---

## Caso de Uso UC15 - Conceder e revogar permissões

**Objetivo**: Permitir que o administrador gerencie as permissões dos advogados e funcionários a qualquer momento.

**Requisitos**: RF015

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e acessa o perfil de um usuário.

**Fluxo principal**:

1. O sistema exibe as informações do usuário selecionado, incluindo as permissões atuais.
2. O administrador marca ou desmarca as permissões que deseja conceder ou revogar.
3. O administrador clica em "Salvar".
4. O sistema atualiza as permissões do usuário.
5. O sistema exibe a mensagem de sucesso. **MSG15**

**Fluxos alternativos**:

- **FA1 - Visualizar histórico de permissões**:
  - 1. O administrador pode visualizar as alterações de permissões realizadas anteriormente.

**Fluxos de exceção**:

- **RN16 - Restrições de permissões**:
  - Não é possível conceder permissões de administrador a si mesmo.

---

## Caso de Uso UC16 - Vincular funcionários a advogados

**Objetivo**: Permitir que o administrador vincule ou desvincule funcionários aos seus respectivos advogados.

**Requisitos**: RF016

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e acessa a opção "Gerenciar Equipes".

**Fluxo principal**:

1. O sistema exibe a lista de advogados e funcionários disponíveis.
2. O administrador seleciona um advogado e visualiza os funcionários associados.
3. O administrador adiciona ou remove funcionários da equipe do advogado.
4. O sistema atualiza as associações no banco de dados.
5. O sistema exibe a mensagem de sucesso. **MSG16**

**Fluxos alternativos**:

- **FA1 - Transferência de funcionários**:
  - 1. O administrador pode transferir um funcionário de um advogado para outro.

**Fluxos de exceção**:

- **RN17 - Limite de funcionários por advogado**:
  - Pode existir um limite máximo de funcionários por advogado definido pelo sistema.

---

## Caso de Uso UC17 - Abrir chamados para suporte

**Objetivo**: Permitir que o administrador abra chamados diretamente para a equipe de suporte do sistema.

**Requisitos**: RF017

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e acessa a opção "Suporte".

**Fluxo principal**:

1. O sistema exibe o formulário para abertura de chamados com campos para descrição do problema, prioridade e anexos.
2. O administrador preenche os detalhes do chamado.
3. O administrador clica em "Enviar".
4. O sistema registra o chamado e gera um número de protocolo.
5. O sistema exibe a mensagem de confirmação com o número do chamado. **MSG17**

**Fluxos alternativos**:

- **FA1 - Consultar chamados abertos**:
  - 1. O administrador pode visualizar o status de chamados anteriores.

**Fluxos de exceção**:

- **RN18 - Campos obrigatórios**:
  - A descrição do problema e a prioridade são campos obrigatórios.

---

## Caso de Uso UC18 - Acessar painel de produtividade

**Objetivo**: Permitir que o administrador acesse um painel que mostre a produtividade dos advogados e funcionários do sistema.

**Requisitos**: RF019

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e seleciona a opção "Painel de Produtividade".

**Fluxo principal**:

1. O sistema exibe gráficos e relatórios com indicadores de desempenho.
2. O administrador pode filtrar as informações por período, equipe ou usuário específico.
3. O administrador analisa os dados para tomada de decisões.

**Fluxos alternativos**:

- **FA1 - Exportar dados**:
  - 1. O administrador pode exportar os relatórios em formatos como PDF ou Excel.

**Fluxos de exceção**:

- **RN19 - Atualização de dados**:
  - Os dados devem ser atualizados em tempo real ou em intervalos definidos.

---

## Caso de Uso UC19 - Anotar faltas funcionais

**Objetivo**: Permitir que o administrador registre as faltas funcionais dos advogados e funcionários.

**Requisitos**: RF020

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e acessa o perfil do usuário.

**Fluxo principal**:

1. O sistema exibe o histórico de faltas do usuário.
2. O administrador clica em "Registrar Falta".
3. O administrador insere a data, motivo e observações.
4. O sistema salva o registro da falta.
5. O sistema exibe a mensagem de sucesso. **MSG18**

**Fluxos alternativos**:

- **FA1 - Editar registro de falta**:
  - 1. O administrador pode editar ou remover registros anteriores.

**Fluxos de exceção**:

- **RN20 - Notificação ao funcionário**:
  - O sistema deve notificar o funcionário sobre o registro da falta.

---

## Caso de Uso UC20 - Realizar backup dos dados

**Objetivo**: Permitir que o administrador realize backups dos dados dos clientes e seus respectivos processos.

**Requisitos**: RF006

**Atores**: Administrador

**Condição de entrada**: O administrador está autenticado e acessa a opção "Backup do Sistema".

**Fluxo principal**:

1. O sistema exibe as opções de backup (completo, incremental, agendado).
2. O administrador seleciona o tipo de backup desejado.
3. O administrador clica em "Iniciar Backup".
4. O sistema realiza o backup dos dados conforme a opção escolhida.
5. O sistema exibe a mensagem de sucesso. **MSG19**

**Fluxos alternativos**:

- **FA1 - Agendar backup**:
  - 1. O administrador define data e hora para backups automáticos.

**Fluxos de exceção**:

- **RN21 - Espaço de armazenamento**:
  - O sistema verifica se há espaço suficiente para o backup.

---

**Notas Finais**:

- **Mensagens**:
  - **MSG01**: "Credenciais inválidas. Por favor, tente novamente."
  - **MSG02**: "Certificado digital não reconhecido. Verifique seu dispositivo."
  - **MSG03**: "Um e-mail de recuperação foi enviado para o seu endereço."
  - **MSG04**: "Senha redefinida com sucesso."
  - **MSG05**: "E-mail não cadastrado no sistema."
  - **MSG06**: "Cadastro realizado com sucesso."
  - **MSG07**: "Usuário já cadastrado com este CPF/OAB."
  - **MSG08**: "Configurações salvas com sucesso."
  - **MSG09**: "Selecione pelo menos uma UF para monitoramento."
  - **MSG10**: "Nenhum histórico de atuação disponível."
  - **MSG11**: "Conflito de horário. Verifique sua agenda."
  - **MSG12**: "Notificação excluída com sucesso."
  - **MSG13**: "Categoria atualizada com sucesso."
  - **MSG14**: "Usuário removido com sucesso."
  - **MSG15**: "Permissões atualizadas com sucesso."
  - **MSG16**: "Equipe atualizada com sucesso."
  - **MSG17**: "Chamado aberto com sucesso. Protocolo nº XXXX."
  - **MSG18**: "Falta registrada com sucesso."
  - **MSG19**: "Backup realizado com sucesso."

- **Regras de Negócio**:
  - **RN1 a RN21**: Correspondem às validações e restrições mencionadas nos fluxos de exceção.
