const qrcode = require('qrcode-terminal');
const { Client, LocalAuth } = require('whatsapp-web.js');
const axios = require('axios');


const client = new Client({
    authStrategy: new LocalAuth({
        dataPath: "./session"
    }),
    puppeteer: {
        headless: true,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ]
    }
});


client.on('message', msg => {
    console.log(`📩 FROM: ${msg.from} | MSG: ${msg.body}`);
});

client.on('qr', qr => {
    console.log('📲 Escaneie o QR Code:');
    qrcode.generate(qr, { small: true });
});


client.on('ready', () => {
    console.log('🤖 Yari ONLINE e recebendo mensagens!');
});


client.on('disconnected', (reason) => {
    console.log('⚠️ Desconectado:', reason);
    client.initialize();
});


const userContext = {};

function setContext(userId, context) {
    userContext[userId] = {
        context,
        time: Date.now()
    };
}

function getContext(userId) {
    return userContext[userId]?.context || null;
}


async function askYari(message, userId) {
    try {
        const res = await axios.post('http://localhost:8080/message/sendText/{instanceName}', {
            message: message,
            user: userId,
            context: getContext(userId),
            apikey: "YARI123"
        });

        return res.data?.reply || "Não consegui responder agora 😕";

    } catch (err) {
        console.error("Erro Yari:", err.message);
        return "Erro ao conectar com a IA 🤖";
    }
}


const delay = ms => new Promise(res => setTimeout(res, ms));

// =======================
// LIMPEZA CONTEXTO
// =======================
setInterval(() => {
    const now = Date.now();
    for (const id in userContext) {
        if (now - userContext[id].time > 30 * 60 * 1000) {
            delete userContext[id];
        }
    }
}, 5 * 60 * 1000);


client.on('message', async msg => {

    try {

        if (!msg.body) return;
        if (msg.isGroup) return;

        const from = msg.from;
        const text = msg.body;

        const chat = await msg.getChat();
        const contact = await msg.getContact();
        const name = contact.pushname || "aluno";

        // MENU
        if (/oi|olá|ola|bom dia|boa tarde|boa noite|menu/i.test(text.toLowerCase())) {

            setContext(from, 'menu');

            await delay(800);
            await chat.sendStateTyping();
            await delay(1000);

            await msg.reply(
`📚 Olá ${name}!

Sou a Yari 🤖

Posso te ajudar com:

📌 GLPI
📌 Problemas de equipamentos
📌 Sistema escolar
📌 Dúvidas técnicas

Me envie sua dúvida 👇`
            );

            return;
        }

        // CONTEXTO
        setContext(from, 'suporte');

        await delay(600);
        await chat.sendStateTyping();
        await delay(1000);

        // IA
        const resposta = await askYari(text, from);

        await msg.reply(resposta);

    } catch (err) {
        console.error("Erro geral:", err.message);
    }
});

// =======================
// START
// =======================
client.initialize();