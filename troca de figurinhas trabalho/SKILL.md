# 🧠 SKILL.md: Base de Conhecimento e Padrões Técnicos

## 🏛️ 1. Engenharia de Requisitos (Taxonomia VEM)

Os requisitos da Plataforma de Troca de Figurinhas da Copa do Mundo devem seguir esta classificação rigorosa para evitar ambiguidades e garantir consistência entre frontend, backend e banco de dados.

* **RU (Requisitos de Usuário):** Necessidades abstratas dos colecionadores (ex: controlar álbum, encontrar trocas, acompanhar progresso).
* **RS (Requisitos de Sistema):** Detalhes técnicos de implementação (APIs Flask, SQLite, estrutura de endpoints e persistência local).
* **RF (Requisitos Funcionais):** Funções diretas do sistema (registrar figurinhas, calcular progresso, propor trocas).
* **RN (Regras de Negócio):** Restrições do domínio da coleção (ex: uma figurinha só pode ser marcada como repetida se `quantidade > 1`).
* **RNF (Requisitos Não Funcionais):** Qualidade do sistema (offline-first, performance, usabilidade mobile-first).

---

## ⚖️ 2. Categorias de Prioridade

Essenciais para aplicação da Regra 80/20 no sistema de figurinhas.

1. **Essencial:** Funcionalidades críticas do MVP:

   * Cadastro de usuários
   * Registro de figurinhas
   * Controle de repetidas
   * Sistema de trocas
   * Cálculo de progresso do álbum

2. **Importante:** Melhorias operacionais:

   * Ranking de colecionadores
   * Histórico de trocas
   * Painel administrativo

3. **Desejável:** Expansões futuras:

   * Sugestão inteligente de trocas
   * Mapa de encontros de colecionadores
   * Gamificação avançada

---

## ♿ 3. Acessibilidade Digital (Padrão WCAG)

Toda interface deve seguir os princípios **POUR**, adaptados ao contexto mobile-first da plataforma.

* **Perceptível:** Interface clara para visualizar progresso do álbum e figurinhas.
* **Operável:** Uso fácil em celular durante eventos de troca.
* **Compreensível:** Fluxos simples de cadastro e troca.
* **Robusto:** Compatível com navegadores leves e offline.

---

## 🧪 4. Padrões de Teste (Modelo AAA)

Aplicável a todas as rotas da API de figurinhas.

* **Arrange (Organizar):** Preparar usuários, figurinhas e banco SQLite.
* **Act (Agir):** Executar ações como registrar figurinha ou criar troca.
* **Assert (Verificar):** Confirmar integridade dos dados e resposta correta da API.

Exemplos de testes:

* Cadastro de usuário
* Registro de figurinha
* Adição de repetidas
* Criação de troca
* Cálculo de progresso

---

## 🤖 5. Spec-Driven Development (SDD)

A plataforma deve ser construída estritamente baseada em especificação.

* **Escopo fechado:** Nenhuma funcionalidade fora do SCHEMA.md.
* **Zero ambiguidade:** Campos sempre explícitos (ex: `user_id`, `sticker_id`).
* **Persistência de contexto:** Tudo documentado em arquivos .md (nunca só no código).
* **Mudanças cirúrgicas:** Alterar apenas o necessário, sem refatoração desnecessária.

---

## 🗺️ 6. Modelagem e Arquitetura (UML)

A IA deve gerar e interpretar diagramas Mermaid para validar o sistema antes da implementação.

### Casos de uso:

* Usuário cadastra coleção
* Usuário adiciona figurinhas
* Usuário marca repetidas
* Usuário propõe troca
* Sistema calcula progresso

### Sequência típica:

Usuário → Frontend → Flask API → SQLite → resposta

---

## ⚽ Contexto do Sistema

A plataforma é um sistema de troca de figurinhas da Copa do Mundo com foco em:

* Colecionadores iniciantes e avançados
* Controle de álbum completo
* Gestão de repetidas
* Sistema de trocas entre usuários
* Progresso automático da coleção

---

### 💡 Instrução Final

Este arquivo é a base de raciocínio técnico do sistema. Sempre que houver dúvida de:

* prioridade
* validação
* teste
* estrutura de dados

👉 Este documento deve ser considerado autoridade máxima junto com o SCHEMA.md.
