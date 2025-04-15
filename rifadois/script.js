// Dados iniciais da rifa
let pontos = Array.from({ length: 100 }, (_, i) => ({
    numero: i + 1,
    status: "livre",
    comprador: ""
}));

// Função para renderizar os pontos na tabela
function renderTable() {
    const rifaBody = document.getElementById("rifa-body");
    rifaBody.innerHTML = ""; // Limpa o corpo da tabela

    pontos.forEach((ponto) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${ponto.numero}</td>
            <td>${ponto.status}</td>
            <td>
                <input type="text" value="${ponto.comprador}" 
                       onchange="atualizarNome(${ponto.numero}, this.value)">
            </td>
            <td>
                <button class="livre" onclick="atualizarStatus(${ponto.numero}, 'livre')">Livre</button>
                <button class="reservado" onclick="atualizarStatus(${ponto.numero}, 'reservado')">Reservar</button>
            </td>
        `;
        rifaBody.appendChild(row);
    });
}

// Função para atualizar o status de um ponto
function atualizarStatus(numero, status) {
    const ponto = pontos.find((p) => p.numero === numero);
    if (ponto) {
        ponto.status = status;
        if (status === "livre") {
            ponto.comprador = ""; // Limpa o nome se o status for "livre"
        }
        salvarDados(); // Salva os dados após a atualização
        renderTable(); // Atualiza a tabela
    }
}

// Função para atualizar o nome do comprador
function atualizarNome(numero, nome) {
    const ponto = pontos.find((p) => p.numero === numero);
    if (ponto) {
        ponto.comprador = nome;
        salvarDados(); // Salva os dados após a atualização
    }
}

// Função para salvar os dados no Local Storage
function salvarDados() {
    localStorage.setItem("pontos", JSON.stringify(pontos));
}

// Função para carregar os dados do Local Storage
function carregarDados() {
    const dadosSalvos = localStorage.getItem("pontos");
    if (dadosSalvos) {
        pontos = JSON.parse(dadosSalvos);
    }
}

// Carrega os dados ao iniciar a aplicação
carregarDados();
renderTable();