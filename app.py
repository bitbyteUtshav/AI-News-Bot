import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI News Bot V1 চালু হয়েছে!\n\n"
        "কমান্ড:\n"
        "/start - Bot চালু\n"
        "/news - আজকের AI নিউজ"
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 আজকের নিউজ সংগ্রহ করছি...\n\n"
        "পরবর্তী ধাপে Gemini AI থেকে লাইভ উত্তর আসবে।"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))

    print("AI News Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
