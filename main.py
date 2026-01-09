from telegram.ext import ApplicationBuilder, CommandHandler
import asyncio
import os

async def start(update, context):
    await update.message.reply_text("OK")

async def main():
    print("🚀 BOT INICIADO")
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
