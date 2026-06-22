# 📝 02-DERS_MESTRE.md: Especificação Mestre de Requisitos

## 📑 1. Identificação e Controle de Versão

* **Projeto:** Plataforma de Troca de Figurinhas da Copa do Mundo.
* **Versão:** 1.0 (MVP).
* **Responsáveis:** Equipe de Engenharia.
* **Histórico:** Consolidação inicial baseada no North Star.

---

## 🎯 2. Visão Geral e Escopo

* **Objetivo Central:** Permitir que colecionadores acompanhem seu álbum, gerenciem figurinhas repetidas e encontrem oportunidades de troca.
* **Público-Alvo:** Colecionadores iniciantes, casuais e avançados.
* **Fora de Escopo:** Pagamentos, aplicativos nativos, integração com redes sociais e marketplace.

---

## 👥 3. Requisitos de Usuário (RU)

* **RU01:** O usuário deseja registrar quais figurinhas já possui.
* **RU02:** O usuário deseja identificar rapidamente quais figurinhas faltam.
* **RU03:** O usuário deseja cadastrar figurinhas repetidas disponíveis para troca.
* **RU04:** O usuário deseja encontrar pessoas interessadas em trocar figurinhas.
* **RU05:** O usuário deseja marcar local e horário para realizar trocas.

---

## ⚙️ 4. Requisitos de Sistema (RS)

* **RS01:** O sistema deve armazenar usuários em banco SQLite.
* **RS02:** O sistema deve armazenar figurinhas possuídas, faltantes e repetidas.
* **RS03:** O sistema deve permitir o cadastro de propostas de troca.
* **RS04:** O sistema deve registrar local, data e horário das trocas.
* **RS05:** O sistema deve calcular automaticamente o percentual de conclusão do álbum.

---

## ✅ 5. Requisitos Funcionais (RF) e Priorização

| ID   | Descrição do Requisito            | Tipo | Prioridade | Critério de Aceite                |
| ---- | --------------------------------- | ---- | ---------- | --------------------------------- |
| RF01 | Cadastro de usuário.              | RS   | Essencial  | Usuário criado com sucesso.       |
| RF02 | Cadastro de figurinhas possuídas. | RS   | Essencial  | Figurinhas salvas no banco.       |
| RF03 | Cadastro de figurinhas repetidas. | RS   | Essencial  | Repetidas associadas ao usuário.  |
| RF04 | Consulta do progresso do álbum.   | RS   | Essencial  | Exibir percentual concluído.      |
| RF05 | Busca de possíveis trocas.        | RS   | Importante | Encontrar usuários compatíveis.   |
| RF06 | Agendamento de troca.             | RS   | Importante | Local e horário registrados.      |
| RF07 | Histórico de trocas realizadas.   | RS   | Desejável  | Trocas registradas para consulta. |

---

## 📏 6. Regras de Negócio (RN)

| ID   | Descrição da Regra                                                          | Requisito Relacionado |
| ---- | --------------------------------------------------------------------------- | --------------------- |
| RN01 | Uma figurinha só pode existir uma vez na coleção principal do usuário.      | RF02                  |
| RN02 | Figurinhas repetidas devem estar associadas ao proprietário.                | RF03                  |
| RN03 | Uma troca só pode ser concluída quando ambas as partes aceitarem.           | RF06                  |
| RN04 | O percentual do álbum deve ser recalculado automaticamente após alterações. | RF04                  |

---

## 🛡️ 7. Requisitos Não Funcionais (RNF)

| ID    | Nome / Atributo    | Categoria      | Prioridade | Descrição Técnica                 |
| ----- | ------------------ | -------------- | ---------- | --------------------------------- |
| RNF01 | Responsividade     | Usabilidade    | Essencial  | Funcionar em celular e desktop.   |
| RNF02 | Baixa Latência     | Performance    | Essencial  | Respostas em menos de 2 segundos. |
| RNF03 | Persistência Local | Confiabilidade | Essencial  | Utilizar SQLite.                  |
| RNF04 | Interface Moderna  | Usabilidade    | Importante | Visual limpo e intuitivo.         |

---

## ⚖️ 8. Diretrizes Karpathy de Implementação (VEM)

1. Implementar apenas funcionalidades necessárias ao MVP.
2. Priorizar HTML, CSS e JavaScript simples.
3. Evitar dependências desnecessárias.
4. Fazer alterações mínimas e objetivas.
5. Registrar premissas em FINDINGS.md quando houver ambiguidade.

---

## 🔗 9. Matriz de Rastreabilidade Simples

* RU01 → RF02.
* RU02 → RF04.
* RU03 → RF03.
* RU04 → RF05.
* RU05 → RF06.

---

💡 Instrução para a IA: Priorizar sempre a conclusão do álbum e a facilitação das trocas entre colecionadores. Funcionalidades extras devem ser avaliadas segundo a Regra 80/20.
