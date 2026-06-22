# 📊 SCHEMA.md: Constituição dos Dados e Contratos de API

## 📑 1. Identificação do Modelo

**Projeto:** Plataforma de Troca de Figurinhas da Copa do Mundo
**Arquiteto de Dados:** Lemuel (Backend)
**Revisora:** Maria (Consistência do Sistema)
**Versão:** 1.0

---

## 🏛️ 2. Entidades e Atributos (The Law)

*Define todas as estruturas persistidas no SQLite. Nenhum campo fora deste schema pode ser criado.*

---

### 👤 Tabela: `users`

| Campo        | Tipo     | Restrição    | Descrição                      |
| :----------- | :------- | :----------- | :----------------------------- |
| `id`         | Integer  | Primary Key  | Identificador único do usuário |
| `nome`       | String   | Not Null     | Nome do colecionador           |
| `email`      | String   | Not Null     | E-mail do usuário              |
| `created_at` | DateTime | Default: NOW | Data de criação                |

---

### 📒 Tabela: `stickers`

| Campo    | Tipo    | Restrição   | Descrição                            |
| :------- | :------ | :---------- | :----------------------------------- |
| `id`     | Integer | Primary Key | ID da figurinha                      |
| `codigo` | String  | Not Null    | Código da figurinha (ex: #15 Neymar) |
| `nome`   | String  | Not Null    | Nome do jogador                      |
| `time`   | String  | Not Null    | Seleção do jogador                   |

---

### 📦 Tabela: `user_stickers`

| Campo         | Tipo    | Restrição      | Descrição                      |
| :------------ | :------ | :------------- | :----------------------------- |
| `id`          | Integer | Primary Key    | Registro único                 |
| `user_id`     | Integer | Foreign Key    | Usuário dono da figurinha      |
| `sticker_id`  | Integer | Foreign Key    | Figurinha associada            |
| `quantidade`  | Integer | Default: 1     | Quantidade (permite repetidas) |
| `is_repeated` | Boolean | Default: false | Indica se é repetida           |

---

### 🔁 Tabela: `trades`

| Campo                  | Tipo     | Restrição        | Descrição           |
| :--------------------- | :------- | :--------------- | :------------------ |
| `id`                   | Integer  | Primary Key      | ID da troca         |
| `from_user_id`         | Integer  | Foreign Key      | Usuário que oferece |
| `to_user_id`           | Integer  | Foreign Key      | Usuário que recebe  |
| `offered_sticker_id`   | Integer  | Not Null         | Figurinha oferecida |
| `requested_sticker_id` | Integer  | Not Null         | Figurinha desejada  |
| `status`               | String   | Default: pending | Estado da troca     |
| `created_at`           | DateTime | Default: NOW     | Data da solicitação |

---

## 📜 3. Contrato de API (JSON is Law)

---

### 📥 Usuários (POST /api/users)

```json
{
  "nome": "string",
  "email": "string"
}
```

---

### 📥 Figurinhas (POST /api/stickers)

```json
{
  "user_id": 1,
  "codigo": "#15",
  "nome": "Neymar",
  "time": "Brasil"
}
```

---

### 📥 Repetidas (POST /api/repeated)

```json
{
  "user_id": 1,
  "sticker_id": 15,
  "quantidade": 2
}
```

---

### 📥 Trocas (POST /api/trades)

```json
{
  "from_user_id": 1,
  "to_user_id": 2,
  "offered_sticker_id": 15,
  "requested_sticker_id": 87
}
```

---

### 📤 Progresso (GET /api/progress/:user_id)

```json
{
  "user_id": 1,
  "total_stickers": 670,
  "collected": 520,
  "missing": 150,
  "completion_percentage": 77.6
}
```

---

## 🛡️ 4. Regras de Integridade e Validação

1. **Integridade de Trocas:** Uma troca só pode existir se ambos os usuários existirem.
2. **Consistência de Estoque:** Um usuário não pode oferecer uma figurinha que não possui.
3. **Repetidas:** `is_repeated = true` sempre que `quantidade > 1`.
4. **Offline-First:** Todas as operações devem funcionar sem internet.
5. **JSON is Law:** Nenhuma API pode retornar campos fora deste schema.

---

## 🛂 5. Protocolo de Governança para Agentes

* **Lemuel (Backend):** Deve seguir exatamente os nomes de tabelas e campos aqui definidos.
* **Lemuel (Frontend):** Inputs e requests devem espelhar este schema sem divergências.
* **Maria (Revisora):** Deve bloquear qualquer expansão de escopo fora do MVP de trocas de figurinhas.

---

### ⚽ Por que este arquivo é o núcleo do sistema?

Este schema garante que toda a plataforma — frontend, backend e lógica de trocas — fale exatamente a mesma língua.

Ele substitui qualquer ambiguidade por regras determinísticas, permitindo geração automática de código via `/init` sem deriva de escopo.
