import telebot
from google import genai
from google.genai import types

# ==========================================
# 1. إعداد مفاتيح الربط (API Keys)
# ==========================================
TELEGRAM_TOKEN = "8777919348:AAGH2qkj5b3DsfSiR_1n3VJDuWGCsjPD-ZE"
GEMINI_API_KEY = "AIzaSyA4GcgZOL0JGpKq95UQgCUm4ROmITS8jv8"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

# ==========================================
# 2. إعداد التعليمات الأساسية (System Prompt)
# ==========================================
SYSTEM_PROMPT = """
أنت عالم متخصص وخبير في علم الفرائض والمواريث الإسلامية.
تلقى المسائل المكتوبة باللغة العربية وحلها بدقة متناهية.

عند الإجابة اتبع التنسيق التالي:
1. تحليل الورثة.
2. نصيب كل وارث مع ذكر السبب (مثلاً: الزوجة لها الثمن لوجود الفرع الوارث).
3. ذكر من حجب من الورثة إن وجد.
4. أصل المسألة (إن أمكن).

استخدم الرموز التعبيرية (Emojis) لتنظيم الإجابة.
"""

config = types.GenerateContentConfig(
    system_instruction=SYSTEM_PROMPT,
    temperature=0.1, 
)

user_sessions = {}

# ==========================================
# 3. دوال التعامل مع رسائل تيليجرام
# ==========================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = "⚖️ حاسبة المواريث الذكية جاهزة.\nاكتب مسألتك الآن (مثال: مات وترك زوجة وأم وابن)..."
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_faraid_query(message):
    chat_id = message.chat.id
    user_text = message.text

    if chat_id not in user_sessions:
        # تم التغيير لـ gemini-1.5-flash لضمان السرعة وعدم التهنيج
        user_sessions[chat_id] = client.chats.create(model="gemini-1.5-flash", config=config)
    
    chat_session = user_sessions[chat_id]

    try:
        bot.send_chat_action(chat_id, 'typing')
        response = chat_session.send_message(user_text)
        bot.reply_to(message, response.text)
        
    except Exception as e:
        # تنظيف الجلسة في حال حدوث خطأ لمحاولة الاتصال من جديد
        if chat_id in user_sessions: del user_sessions[chat_id]
        bot.reply_to(message, "⚠️ السيرفر مشغول حالياً، يرجى إعادة إرسال المسألة مرة أخرى.")
        print(f"Error Details: {e}")

if __name__ == "__main__":
    print("🚀 البوت انطلق بنسخة Flash السريعة... جرب الآن!")
    bot.infinity_polling()