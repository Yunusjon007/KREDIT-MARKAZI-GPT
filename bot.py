import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from openai import OpenAI

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=OPENAI_API_KEY)

async def chatgpt_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    completion = client.chat.completions.create(
        model="gpt-4o",   # <-- Diqqat: aynan shu joyda!
        messages=[{"role": "user", "content": user_text}]
    )
    reply = completion.choices[0].message.content
    await update.message.reply_text(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply))
    app.run_polling()
