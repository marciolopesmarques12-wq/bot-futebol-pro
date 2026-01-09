import os
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

BOT_TOKEN = os.getenv("8245511133:AAFQ-M_vfP8_SKr3L2ITe2wT2kfIUtJSL0Y")
API_KEY = os.getenv("caffc8e22839f780d3884dd16fd8c3a4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Futebol Pro ativo!\n\n"
        "Use /jogos para ver análises do dia ⚽📊"
    )

async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://v3.football.api-sports.io/fixtures?date=2026-01-08"
    headers = {
        "x-apisports-key": API_KEY
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if "response" not in data or len(data["response"]) == 0:
        await update.message.reply_text("Nenhum jogo encontrado hoje.")
        return

    mensagem = "⚽ *Jogos do Dia — Análises*\n\n"

    for jogo in data["response"][:5]:
        casa = jogo["teams"]["home"]["name"]
        fora = jogo["teams"]["away"]["name"]
        mensagem += f"• {casa} x {fora}\n"
        mensagem += "Probabilidade: +55% 📈\n\n"

    await update.message.reply_text(mensagem, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogos", jogos))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()