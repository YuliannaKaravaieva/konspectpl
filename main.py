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
        st.info(f"Здесь мы будем выводить таблицы форм для рода: {gender}")
        # Сюда мы позже подключим нашу базу данных SQLite

        # Кнопка для вывода правила по требованию (то, о чем ты просила)
        with st.expander("ℹ️ Показать грамматичне правило для цього випадку"):
            st.write(
                "Тут буде текст правила, який ми  виймемо з бази данних для цього слова."
            )

    else:
        st.subheader("📖 Грамматическое справочное правило")
        st.write("Выводим чистое теоретическое правило без таблиц.")

else:
    # РЕЖИМ: Проверить себя
    st.subheader("🧠 Тренажер: Проверь свои знания")
    st.write(f"Давай проверим, как ты помнишь слово **{word_input}**")

    # Имитация задания (пока без базы данных)
    st.write(f"Задание: Переведите и поставьте в правильную форму.")
    st.write(f"Контекст: **On ______ (быть) w domu.**")

    # Поле ввода для пользователя
    user_answer = st.text_input("Введи правильное окончание или форму слова:")

    # Кнопка проверки
    if st.button("Проверить ответ"):
        if user_answer.lower() == "był":
            st.success("🔥 Гениально! Ответ правильный: On był w domu.")
        else:
            st.error("❌ Мимо. Попробуй еще раз или загляни в Справочник!")


