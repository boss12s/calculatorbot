import telebot

Token = "7953975307:AAE20pzlrBfHG6iFsZc31yUtrkZlNHIrG5M"
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to mycalculator!")
    

@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """/start -> बॉट सुरू करा
/help -> सर्व कमांड्स दाखवा
कॅल्क्युलेटर म्हणून वापरा:
• 5 + 3
• 10 * 2  
• 15 / 3
• (5 + 3) * 2"""
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        # गणिती अभिव्यक्ती काढून घ्या
        expression = message.text
        
        # सुरक्षित गणना करा
        result = eval(expression)
        bot.reply_to(message, f"answer: {result}")
        
    except ZeroDivisionError:
        bot.reply_to(message, "Error: Cannot divide by zero!")
    except Exception as e:
        bot.reply_to(message, f"त्रError: Invalid mathematical expression! Please type it correctly.")

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()