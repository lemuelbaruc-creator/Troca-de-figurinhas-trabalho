// O usuário inicial para simulação (MVP 80/20 sem login complexo)
const USER_ID = 1;

document.addEventListener("DOMContentLoaded", async () => {
    console.log("Inicializando Frontend Lemuel...");
    
    // 1. Criar dados de mock no backend
    await setupMockData();
    
    // 2. Carregar informações
    await loadProgress();
    loadRepeated();
    loadTrades();
});

async function setupMockData() {
    try {
        // Tenta criar o usuário 1
        await fetch('/api/users', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ nome: 'Pedro (Iniciante)', email: 'pedro@email.com' })
        });
        
        // Simular a posse de algumas figurinhas pelo Pedro
        await fetch('/api/stickers', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ user_id: USER_ID, sticker_id: 1 }) // Neymar
        });
        await fetch('/api/stickers', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ user_id: USER_ID, sticker_id: 3 }) // Messi
        });
        
        // Simular repetição
        await fetch('/api/repeated', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ user_id: USER_ID, sticker_id: 2, quantidade: 2 }) // Vinicius Jr repetida
        });
    } catch(e) {
        console.error("Erro no setup (ignorável caso o banco já tenha dados):", e);
    }
}

async function loadProgress() {
    try {
        const response = await fetch(`/api/progress/${USER_ID}`);
        if(!response.ok) return;
        const data = await response.json();
        
        document.getElementById('user-name').innerText = 'Pedro';
        document.getElementById('stat-collected').innerText = data.collected;
        document.getElementById('stat-missing').innerText = data.missing;
        document.getElementById('album-percentage').innerText = data.completion_percentage;
        document.getElementById('header-progress').innerText = `${data.completion_percentage}%`;
        
        document.getElementById('album-progress-bar').style.width = `${data.completion_percentage}%`;
    } catch(e) {
        console.error("Progresso erro:", e);
    }
}

function loadRepeated() {
    // Para simplificar o MVP (Regra 80/20), usando listagem controlada para exibir no layout
    const list = document.getElementById('repeated-list');
    const repetidas = [
        { codigo: '#87', nome: 'Vinicius Jr', qty: 2 }
    ];
    
    list.innerHTML = repetidas.map(r => `
        <li class="sticker-item">
            <span><strong>${r.codigo}</strong> ${r.nome}</span>
            <span class="badge">x${r.qty} disponíveis</span>
        </li>
    `).join('');
}

function loadTrades() {
    const box = document.getElementById('trade-opportunities');
    box.innerHTML = `
        <div class="trade-item">
            <p><strong>Carlos possui:</strong> #88 Mbappé</p>
            <p><strong>Carlos deseja:</strong> #87 Vinicius Jr</p>
            <button class="btn" onclick="proposeTrade()">Propor Troca</button>
        </div>
    `;
}

async function proposeTrade() {
    try {
        const res = await fetch('/api/trades', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                from_user_id: USER_ID,
                to_user_id: 2, // Carlos fake
                offered_sticker_id: 2, // Vinicius
                requested_sticker_id: 4 // Mbappe
            })
        });
        
        if(res.ok) {
            alert('✅ Troca proposta com sucesso!');
        } else {
            alert('Erro ao propor troca.');
        }
    } catch(e) {
        console.error(e);
    }
}
