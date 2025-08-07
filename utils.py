import os
import datetime

LOG_DIR = "logs"

def get_today_folder(chat_id=None, date_override=None):
    if date_override is not None:
        folder_date = date_override
    else:
        folder_date = datetime.date.today().isoformat()
    if chat_id is not None:
        folder = os.path.join(LOG_DIR, str(chat_id), folder_date)
    else:
        folder = os.path.join(LOG_DIR, folder_date)
    os.makedirs(folder, exist_ok=True)
    return folder

def save_food(label, text, chat_id=None):
    folder = get_today_folder(chat_id)
    path = os.path.join(folder, "food.txt")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{label}] {text}\n")

def save_water(amount, chat_id=None):
    folder = get_today_folder(chat_id)
    path = os.path.join(folder, "water.txt")
    time = datetime.datetime.now().strftime("%H:%M")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{time} — {amount} мл\n")

def get_water_summary(chat_id=None):
    folder = get_today_folder(chat_id)
    path = os.path.join(folder, "water.txt")
    total = 0
    try:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("—")
                    if len(parts) == 2:
                        amount = parts[1].strip().replace("мл", "").strip()
                        total += int(amount)
    except Exception:
        pass
    return total

def save_reflection(text, chat_id=None):
    folder = get_today_folder(chat_id)
    path = os.path.join(folder, "reflection.txt")
    with open(path, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def get_day_summary(chat_id=None, date_override=None):
    folder = get_today_folder(chat_id, date_override=date_override)
    parts = []

    food_path = os.path.join(folder, "food.txt")
    try:
        if os.path.exists(food_path):
            with open(food_path, encoding="utf-8") as f:
                parts.append("🍽️ Что ты ел сегодня:\n" + f.read())
    except Exception as e:
        parts.append(f"[Ошибка при чтении еды: {e}]")

    try:
        total_water = get_water_summary(chat_id) if date_override is None else get_water_summary_by_date(chat_id, date_override)
        parts.append(f"💧 Воды выпито: {total_water} мл")
    except Exception as e:
        parts.append(f"[Ошибка при подсчёте воды: {e}]")

    reflection_path = os.path.join(folder, "reflection.txt")
    try:
        if os.path.exists(reflection_path):
            with open(reflection_path, encoding="utf-8") as f:
                parts.append("💭 Рефлексия:\n" + f.read())
    except Exception as e:
        parts.append(f"[Ошибка при чтении рефлексии: {e}]")

    return "\n\n".join(parts)

def get_water_summary_by_date(chat_id=None, date_override=None):
    folder = get_today_folder(chat_id, date_override=date_override)
    path = os.path.join(folder, "water.txt")
    total = 0
    try:
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("—")
                    if len(parts) == 2:
                        amount = parts[1].strip().replace("мл", "").strip()
                        total += int(amount)
    except Exception:
        pass
    return total
