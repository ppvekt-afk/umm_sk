import os
import json
import re
import random
import time
import requests
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

TOKEN = os.environ.get('TELEGRAM_TOKEN')
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
OPENROUTER_MODEL = os.environ.get('OPENROUTER_MODEL', 'openai/gpt-oss-120b:free')
BOT_USERNAME = "iris_personalsmm_bot"

USER_NAME = "Катя"
NAME_VARIANTS = ['Катя', 'Кать', 'Екатерина', 'Катрин']
MIN_GAP = 3
MAX_GAP = 6
SESSION_TIMEOUT = 1800
TASK_CHAT_ID = "-1003972417391"

user_counters = {}
user_histories = {}

IRIS_PERSONALITY = """Ты Айрис — руководитель SMM-отдела, энергичная, чуткая и профессиональная. 
Отвечай как живой человек, без маркдауна, коротко, с эмодзи. 
Если нужно уточнить — задавай вопросы по одному. Всегда предлагай конкретные варианты."""

def load_skill_for_query(user_text):
    """Загружает подходящий навык из папки social-media-skills/skills."""
    skills_dir = "social-media-skills/skills"
    if not os.path.exists(skills_dir):
        return None

    # Сопоставление ключевых слов с навыками
    skill_keywords = {
        "strategy": ["стратеги", "продвижени", "маркетинг", "стратег"],
        "plan": ["план", "календар", "расписани", "планировани"],
        "post": ["пост", "текст", "напиши", "создай пост"],
        "hook": ["заголовок", "крючок", "привлек", "заинтересов"],
        "repurpose": ["передел", "адаптир", "рерайт", "переформатир"],
        "analyze": ["анализ", "метрик", "статистик", "отчет"],
        "trends": ["тренд", "актуальн", "популярн", "новинк"],
        "caption": ["подпись", "caption", "описани"],
        "ai": ["нейросет", "ии", "ai", "чат"],
        "video": ["видео", "ролик", "клип"],
        "image": ["картинк", "изображени", "фото"],
        "voice": ["голос", "озвучк", "аудио"],
        "brand": ["бренд", "аудит", "узнаваемост"],
        "campaign": ["кампани", "акци", "запуск"],
        "canva": ["дизайн", "макет", "canva"],
        "capcut": ["монтаж", "капкат", "редактир"],
        "audience": ["аудитори", "целевой", "портрет"],
        "batch": ["пакетн", "серийн", "массов"],
        "before": ["до", "после", "трансформаци", "изменени"],
        "behind": ["за кулис", "процесс", "истори"],
    }

    best_skill = None
    best_score = 0
    user_lower = user_text.lower()
    for skill, keywords in skill_keywords.items():
        score = sum(1 for kw in keywords if kw in user_lower)
        if score > best_score:
            best_score = score
            best_skill = skill

    if not best_skill:
        return None

    for root, dirs, files in os.walk(skills_dir):
        for file in files:
            if file.endswith(".md") and best_skill in file.lower():
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        return f.read()
                except:
                    pass
    return None

def format_text(text):
    text = re.sub(r'[*_`#]', '', text)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    paragraphs = []
    current = []
    for i, sent in enumerate(sentences):
        if i > 0 and i % 3 == 0:
            paragraphs.append(' '.join(current))
            current = []
        current.append(sent)
    if current:
        paragraphs.append(' '.join(current))
    return '\n\n'.join(paragraphs)

def send_chat_action(chat_id, action):
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendChatAction", json={"chat_id": chat_id, "action": action}, timeout=5)
    except:
        pass

def send_message(chat_id, text, reply_to_message_id=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    formatted = format_text(text)
    payload = {"chat_id": chat_id, "text": formatted[:4096], "parse_mode": ""}
    if reply_to_message_id:
        payload["reply_to_message_id"] = reply_to_message_id
    requests.post(url, json=payload, timeout=10)

def send_task_to_masha(task_description):
    masha_mentions = ["Маша", "Машенька", "Машуля", "@editorinchief_masha_bot"]
    mention = random.choice(masha_mentions)
    message = f"{mention}, привет! ✨ Айрис поставила задачу на текст:\n\n{task_description}\n\nЖду результат!"
    send_message(TASK_CHAT_ID, message)

def get_user_counter(user_id):
    now = time.time()
    if user_id not in user_counters:
        user_counters[user_id] = {"count": 0, "last_reset": now}
    else:
        if now - user_counters[user_id]["last_reset"] > SESSION_TIMEOUT:
            user_counters[user_id]["count"] = 0
            user_counters[user_id]["last_reset"] = now
    return user_counters[user_id]

def should_use_name(user_id):
    counter = get_user_counter(user_id)
    counter["count"] += 1
    gap = random.randint(MIN_GAP, MAX_GAP)
    if counter["count"] >= gap:
        counter["count"] = 0
        counter["last_reset"] = time.time()
        return random.choice(NAME_VARIANTS)
    return None

def is_addressed_to_me(chat_type, text, reply_to_bot_name):
    if chat_type == "private":
        return True
    if not text:
        return False
    if f"@{BOT_USERNAME}" in text:
        return True
    text_lower = text.lower()
    names = ['айрис', 'айриска', 'iris', 'риса', 'айра', 'ая', 'ирис', 'айрис-директор', f'@{BOT_USERNAME}']
    if any(name in text_lower for name in names):
        return True
    if reply_to_bot_name == BOT_USERNAME:
        return True
    return False

def generate_llm_response(prompt, system_prompt=None, temperature=0.85, max_tokens=1500):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    payload = {"model": OPENROUTER_MODEL, "messages": messages, "max_tokens": max_tokens, "temperature": temperature}
    try:
        resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=90)
        if resp.status_code == 200:
            data = resp.json()
            raw = data['choices'][0]['message']['content']
            return re.sub(r'[*_`#]', '', raw).strip()
        else:
            return f"Ошибка API ({resp.status_code}). Попробуй позже."
    except Exception as e:
        print(f"LLM error: {e}")
        return "Ошибка связи. Напиши ещё раз."

def get_history(user_id):
    return user_histories.get(user_id, [])

def update_history(user_id, user_msg, bot_msg):
    if user_id not in user_histories:
        user_histories[user_id] = []
    user_histories[user_id].append({"role": "user", "content": user_msg})
    user_histories[user_id].append({"role": "assistant", "content": bot_msg})
    if len(user_histories[user_id]) > 20:
        user_histories[user_id] = user_histories[user_id][-20:]

def handle_start(chat_id, message_id):
    text = """
👋 Привет, Катя! Я Айрис — твой SMM-директор. 
Я могу помочь с чем угодно: стратегия, план, посты, заголовки, рерайт, анализ, тренды, нейросети, видео, дизайн и многое другое.
Просто напиши, что нужно сделать, и я подберу подходящий навык!
"""
    send_message(chat_id, text, message_id)

def process_update(update):
    try:
        if 'message' not in update:
            return
        msg = update['message']
        chat_id = msg['chat']['id']
        user_id = msg['from']['id']
        user_text = msg.get('text', '')
        chat_type = msg['chat']['type']
        reply_to_bot_name = None
        if 'reply_to_message' in msg and msg['reply_to_message']:
            reply_to = msg['reply_to_message']
            if 'from' in reply_to and reply_to['from'].get('is_bot', False):
                reply_to_bot_name = reply_to['from'].get('username')
        if not is_addressed_to_me(chat_type, user_text, reply_to_bot_name):
            return
        user_text_clean = re.sub(f"@{BOT_USERNAME}", "", user_text, flags=re.IGNORECASE)
        names = ['айрис', 'айриска', 'iris', 'риса', 'айра', 'ая', 'ирис', 'айрис-директор']
        for name in names:
            user_text_clean = re.sub(r'\b' + re.escape(name) + r'\b', "", user_text_clean, flags=re.IGNORECASE)
        user_text_clean = user_text_clean.strip()
        if not user_text_clean:
            send_message(chat_id, "Слушаю тебя. Рассказывай.", msg.get('message_id'))
            return
        lower_text = user_text_clean.lower()
        if lower_text == '/start':
            handle_start(chat_id, msg.get('message_id'))
            return
        if lower_text == '/help':
            send_message(chat_id, "Просто напиши, что нужно сделать. Я подберу подходящий навык.", msg.get('message_id'))
            return
        
        send_chat_action(chat_id, "typing")
        skill_content = load_skill_for_query(user_text_clean)
        if skill_content:
            prompt = f"{skill_content}\n\nПожалуйста, выполни задачу пользователя, используя этот навык.\nЗапрос пользователя: {user_text_clean}"
        else:
            prompt = f"Пожалуйста, помоги с задачей пользователя, используя свои знания SMM.\nЗапрос: {user_text_clean}"
        
        name_to_use = should_use_name(user_id)
        history = get_history(user_id)
        history_text = "\n".join([f"{h['role']}: {h['content']}" for h in history[-10:]]) if history else ""
        system_prompt = f"{IRIS_PERSONALITY}\nПользователя зовут {USER_NAME}. {'Обратись к ней: ' + name_to_use if name_to_use else 'Не используй имя.'}\nИстория диалога:\n{history_text}"
        response = generate_llm_response(prompt, system_prompt, temperature=0.85, max_tokens=1500)
        update_history(user_id, user_text_clean, response)
        send_message(chat_id, response, msg.get('message_id'))
    except Exception as e:
        print(f"Ошибка обработки: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        update = request.get_json()
        print("Получен webhook запрос")
        process_update(update)
        return jsonify({"status": "ok"})
    except Exception as e:
        print(f"Webhook error: {e}")
        return jsonify({"status": "error"}), 500

@app.route('/')
def hello():
    return "Iris SMM bot is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
