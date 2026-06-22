# 🧠 05-FINDINGS.md: Memória Técnica e Log de Autocura

## 🎯 1. Propósito e Uso

Este arquivo é o cérebro de recuperação da Plataforma de Troca de Figurinhas da Copa do Mundo.

Sempre que ocorrer um erro de execução, falha visual, inconsistência nas trocas ou problema de persistência, o erro deve ser registrado aqui antes de solicitar correções.

### Protocolo de Autocura

1. Copiar o erro do terminal ou console.
2. Registrar no Log de Incidentes.
3. Solicitar à IA:

"Analise os erros no FINDINGS.md, identifique a causa raiz e aplique uma correção cirúrgica."

---

## 📋 2. Log de Incidentes e Erros

| Data   | Sessão | Descrição do Erro | Causa Raiz | Correção Aplicada |
| ------ | ------ | ----------------- | ---------- | ----------------- |
| [Data] | [ID]   | [Erro registrado] | [Análise]  | [Correção]        |

---

## 🔬 3. Análise de Causa Raiz e Padrões

Espaço para registrar padrões recorrentes encontrados durante o desenvolvimento.

### Exemplo

**Padrão Detectado:**

A IA gerou tabelas divergentes do SCHEMA.md.

**Ação Preventiva:**

Reforçar a regra "JSON is Law".

---

### Exemplo

**Padrão Detectado:**

Trocas sendo registradas sem validação dos usuários envolvidos.

**Ação Preventiva:**

Validar existência dos participantes antes de salvar a troca.

---

## 💡 4. Decisões Técnicas e Trade-offs

### Decisão

Uso de Flask + SQLite.

**Justificativa:**

Simplicidade, facilidade de implantação e aderência ao MVP.

---

### Decisão

Frontend em HTML, CSS e JavaScript Vanilla.

**Justificativa:**

Menor complexidade e manutenção simplificada.

---

### Decisão

Plataforma responsiva para celular e desktop.

**Justificativa:**

Colecionadores utilizam o sistema durante encontros de troca.

---

### Decisão

Cadastro de figurinhas repetidas separado da coleção principal.

**Justificativa:**

Facilitar a identificação de oportunidades de troca.

---

## 🚧 5. Dívida Técnica e Lições Aprendidas

### Lições

1. Não adicionar dependências sem necessidade.
2. Manter o banco compatível com SQLite puro.
3. Garantir que o progresso do álbum seja recalculado automaticamente.

---

### Dívidas Técnicas Futuras

1. Sistema de notificações de novas oportunidades de troca.
2. Sugestões inteligentes de troca utilizando IA.
3. Mapa de pontos de encontro para colecionadores.

---

## 🛂 Instrução para a IA

"Antes de cada correção, consulte as seções 2 e 4 deste arquivo para evitar regressões, respeitar decisões já tomadas e manter a simplicidade do MVP."
