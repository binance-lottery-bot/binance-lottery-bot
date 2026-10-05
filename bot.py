import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name
    welcome_message = (
        f"Hello {user_name}! Welcome to our 20 Cent (0.20 USDT) Crypto Lottery.\n\n"
        "🎫 To purchase a ticket, please send your payment to the Binance Pay ID below:\n"
        "Binance Pay ID: `532779799`\n\n"
        "After sending the payment, please forward your **Transaction ID (TxID)** and your name to this bot."
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

def main():
    # Bot token obtained from BotFather
    TOKEN = "8602618032:AAH5WB4-nYyV_aRoh1ier8aT3rGj01kIY_o"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running on Render...")
    app.run_polling()

if __name__ == "__main__":
    main()
