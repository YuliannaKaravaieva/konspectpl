import streamlit as st
import sqlite3

# 1. Настройка темы оформления (Streamlit сам сделает темный фон, если в системе включена темная тема)
st.set_page_config(page_title="Konspekt.pl", page_icon="🇵🇱", layout="wide")


st.title("Konspekt.pl")
st.caption("Твiй інтерактивний тренажер польсько мови")

# 2. ЗОНА ВВОДА: Строка для ввода слова
word_input = st.text_input("Введiть польське слово:", value="być")

col1, col2, col3 = st.columns(3)

with col1:
    vydminok = st.selectbox("Відмінки", ["Mianownik (Називний)", "Narzędnik (Орудний)", "Miejscownik (Місцевий)"])

with col2:
    rid = st.selectbox("Рід", ["Męski (Чоловічий)", "Żeński (Жіночий)", "Nijaki (Середній)"])

with col3:
    chas = st.selectbox("Часи", ["Przeszły (Минулий)", "Teraźniejszy (Теперішній)", "Przyszły (Майбутній)"])

# 3. БОКОВАЯ ПАНЕЛЬ (Sidebar): Переносим туда настройки, чтобы разгрузить экран
with st.sidebar:
    lang = st.sidebar.selectbox("Mowa / Мова", ["Українська", "Беларуская", "Polski"])
    app_mode = st.selectbox("Режим", ["📚 Довiдник", "Перевiр себе"])
    info_type = st.selectbox(
        "Тип информации",
        ["🔄 Вiдмiнювання", "📖 Грамматичне правило"],
    )

gender = rid


# 4. ЦЕНТРАЛЬНАЯ ЗОНА: Логика переключения экранов через If/Else
if app_mode == "📚 Довiдник":
    st.subheader(f"Анализ слова: {word_input}")

    if info_type == "🔄 Вiдмiнювання":
        st.info(f"Тут ми будемo виводити таблицi форм для родy: {gender}")
        # Сюда мы позже подключим нашу базу данных SQLite

        # Кнопка для вывода правила по требованию (то, о чем ты просила)
        with st.expander("ℹ️ Показати грамматичне правило для цього випадку"):
            st.write(
                "Тут буде текст правила, який ми  виймемо з бази данних для цього слова."
            )

    else:
        st.subheader("📖 Грамматическое справочное правило")
        st.write("Выводим чистое теоретическое правило без таблиц.")

else:
    # РЕЖИМ: Проверить себя
    st.subheader("🧠 Тренажер: Перевір свої знання")
    st.write(f"Давай перевіримо, як ти пам'ятаєш слово **{word_input}**")

    # Имитация задания (пока без базы данных)
    st.write(f"Завдвння: Переведiть i поставте в правильну форму.")
    st.write(f"Контекст: **On ______ (бути) w domu.**")

    # Поле ввода для пользователя
    user_answer = st.text_input("Введи правильне закiнчення або форму слова:")

    # Кнопка проверки
    if st.button("Перевiрити вiдповiдь"):
        if user_answer.lower() == "był":
            st.success("🔥 Генiально! Вiдповiдь вiрна: On był w domu.")
        else:
            st.error("❌  Попробуй ще раз або подивись в Довiдник!")


