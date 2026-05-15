// tema.js
function aplicar() {
    const tema = localStorage.getItem('tema');
    if (tema === 'dark') {
        document.body.classList.add('dark-mode');
    } else {
        document.body.classList.remove('dark-mode');
    }
}

// Roda assim que o HTML carregar
document.addEventListener("DOMContentLoaded", aplicar);

// Função para o botão clicar
function alternarTema() {
    document.body.classList.toggle('dark-mode');
    const modo = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('tema', modo);
}