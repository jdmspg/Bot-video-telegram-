import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot está funcionando correctamente con v22.2")

# Función principal
async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot en línea con python-telegram-bot v22.2")
    await app.run_polling()

# Ejecutar con asyncio
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
