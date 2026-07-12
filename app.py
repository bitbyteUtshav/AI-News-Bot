import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from google import genai

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI News Bot V2\n\n"
        "কমান্ড:\n"
        "/news - AI দিয়ে আজকের নিউজ"
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ AI নিউজ তৈরি করছে...")

    prompt = """
বাংলায় আজকের ৫টি গুরুত্বপূর্ণ আন্তর্জাতিক, AI, প্রতিরক্ষা ও মহাকাশ বিষয় লিখো।

ফরম্যাট:
📰 শিরোনাম
• ২-৩ লাইনের বর্ণনা
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        await update.message.reply_text(response.text)

    except Exception as e:
        await update.message.reply_text(f"❌ Error:\n{e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))

    print("AI News Bot Started")

    app.run_polling()

if __name__ == "__main__":
    main()
