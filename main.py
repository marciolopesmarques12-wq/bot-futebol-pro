import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8245511133:AAH6PQWgLITgvLFiW6dWDS4VGHrjcmlYyTQ"

API_FOOTBALL_KEY = "caffc8e22839f780d3884dd16fd8c3a4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖⚽ Bot Profissional de Análises Ativo!\n\n"
        "Use o comando /jogos para receber análises dos jogos do dia."
    )

async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://v3.football.api-sports.io/fixtures?date=TODAY"
    headers = {"x-apisports-key": API_FOOTBALL_KEY}

    response = requests.get(url, headers=headers).json()
    fixtures = response.get("response", [])[:5]

    if not fixtures:
        await update.message.reply_text("Nenhum jogo encontrado hoje.")
        return

    msg = "📊 *Análises do Dia*\n\n"

    for game in fixtures:
        home = game["teams"]["home"]["name"]
        away = game["teams"]["away"]["name"]

        prob_home = 58
        prob_draw = 22
        prob_away = 20

        msg += (
            f"⚽ {home} x {away}\n"
            f"🏠 Casa: {prob_home}%\n"
            f"🤝 Empate: {prob_draw}%\n"
            f"✈️ Fora: {prob_away}%\n"
            f"🎯 Palpite: Casa vence\n\n"
        )

    await update.message.reply_text(msg, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogos", jogos))
    app.run_polling()

if __name__ == "__main__":
    main()