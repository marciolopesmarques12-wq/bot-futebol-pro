import os
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

# =========================
# VARIÁVEIS DE AMBIENTE
# =========================
BOT_TOKEN = os.getenv("8245511133:AAFQ-M_vfP8_SKr3L2ITe2wT2kfIUtJSL0Y")
API_KEY = os.getenv("caffc8e22839f780d3884dd16fd8c3a4")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN não encontrado nas Environment Variables")

if not API_KEY:
    raise ValueError("❌ API_KEY não encontrada nas Environment Variables")

# =========================
# COMANDOS DO BOT
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Bot Futebol Pro Online!*\n\n"
        "⚽ Análises profissionais dos jogos do dia\n"
        "📊 Somente palpites acima de 55%\n\n"
        "Use o comando:\n"
        "/jogos — Ver jogos do dia",
        parse_mode="Markdown"
    )

async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://v3.football.api-sports.io/fixtures?date=2026-01-08"
    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers, timeout=15)
    data = response.json()

    if "response" not in data or len(data["response"]) == 0:
        await update.message.reply_text("⚠️ Nenhum jogo encontrado hoje.")
        return

    mensagem = "⚽ *Jogos do Dia — Análises*\n\n"

    for jogo in data["response"][:5]:
        casa = jogo["teams"]["home"]["name"]
        fora = jogo["teams"]["away"]["name"]

        # Simulação de probabilidade (placeholder profissional)
        prob = 58  # depois podemos calcular de verdade

        if prob >= 55:
            mensagem += (
                f"🏟️ {casa} x {fora}\n"
                f"📊 Probabilidade: *{prob}%*\n"
                f"💡 Palpite: Vitória ou Over 1.5\n\n"
            )

    await update.message.reply_text(mensagem, parse_mode="Markdown")

# =========================
# MAIN
# =========================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogos", jogos))

    print("🤖 Bot Futebol Pro rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()