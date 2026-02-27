import telebot

# بياناتك الرسمية
TOKEN = '8298735900:AAHx5bCmkiZ1tcyvtK7wt_CSBhDAT43MoVQ'
ADMIN_ID = 7430164282

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_msg = "🛡️ أهلاً بك في نظام التواصل المشفر.\n\nأرسل طلبك (استرجاع، تأمين، بتكوين...) وسأقوم بالرد عليك هنا في أسرع وقت ممكن."
    bot.reply_to(message, welcome_msg)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.chat.id != ADMIN_ID:
        # توجيه رسالة الزبون إليك
        client_name = message.from_user.first_name or "مجهول"
        client_user = f"@{message.from_user.username}" if message.from_user.username else "بدون يوزر"
        
        forward_msg = f"📩 **رسالة جديدة من الموقع:**\n\n👤 الاسم: {client_name}\n🔗 اليوزر: {client_user}\n🆔 الآيدي: `{message.chat.id}`\n\n📝 النص:\n{message.text}"
        
        bot.send_message(ADMIN_ID, forward_msg, parse_mode='Markdown')
        bot.send_message(ADMIN_ID, f"للرد عليه، انسخ هذا الأمر:\n`/reply {message.chat.id} نص الرد`", parse_mode='Markdown')
    else:
        # نظام الرد المخفي الخاص بك
        if message.text.startswith('/reply'):
            try:
                parts = message.text.split(' ', 2)
                target_id = parts[1]
                reply_text = parts[2]
                bot.send_message(target_id, f"📥 **رد من الإدارة:**\n\n{reply_text}", parse_mode='Markdown')
                bot.send_message(ADMIN_ID, "✅ تم إرسال ردك للزبون بنجاح.")
            except Exception as e:
                bot.send_message(ADMIN_ID, "❌ خطأ في الصيغة! استخدم:\n/reply ID نص_الرد")

print("--- [ النظام متصل الآن.. هويتك مخفية ] ---")
bot.polling()
