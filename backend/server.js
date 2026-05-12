const express = require('express');
const app = express();

app.use(express.json());

// =======================
// ROTA DA YARI
// =======================
app.post('/instance/chat', (req, res) => {
    const { message, user } = req.body;

    console.log("📩 Mensagem recebida:", message);

    // 🛡️ proteção contra erro
    if (!message || typeof message !== "string") {
        return res.json({
            reply: "⚠️ Mensagem inválida recebida"
        });
    }

    const text = message.toLowerCase();

    let reply = "🤖 Não entendi sua mensagem";

    if (text.includes("glpi")) {
        reply = "📌 O GLPI é um sistema de chamados. Quer ajuda com tickets?";
    } 
    else if (text.includes("internet")) {
        reply = "🌐 Verifique o cabo de rede ou reinicie o roteador.";
    } 
    else if (text.includes("oi") || text.includes("olá")) {
        reply = "👋 Olá! Como posso te ajudar?";
    } 
    else {
        reply = `🤖 Yari: recebi sua mensagem -> "${message}"`;
    }

    return res.json({
        reply
    });
});

// =======================
// START SERVER
// =======================
app.listen(8080, () => {
    console.log("🚀 Yari API rodando em http://localhost:8080");
});