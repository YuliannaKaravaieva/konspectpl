import streamlit as st
import sqlite3
from rules import show_rules_page  # 🚀 ПРИШИВАЕМ ТВОЙ НОВЫЙ МОДУЛЬ С ПРАВИЛАМИ

# 1. Настройка темы оформления (Streamlit сам сделает темный фон, если в системе включена темная тема)
st.set_page_config(page_title="Konspekt.pl", page_icon="🇵🇱", layout="wide")

st.title("Konspekt.pl")
st.caption("Твiй інтерактивний тренажер польської мови")

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
    
    if info_type == "🔄 Вiдмiнювання":
        # Этот блок показывается ТОЛЬКО когда выбрано "Відмінювання"
        st.subheader(f"Аналіз слова: {word_input}")
        st.info(f"Тут ми будемо виводити таблиці форм для роду: {gender}")
        # Сюда мы позже подключим нашу базу данных

        # Кнопка для вывода правила по требованию 
        with st.expander("ℹ️ Показати граматичне правило для цього випадку"):
            st.write(
                "Тут буде текст правила, який ми витягнемо з бази даних для цього слова."
            )

    else:
        # 🚀 А ВОТ ТУТ СРАБАТЫВАЕТ МАГИЯ!
        # Если юзер выбрал "Грамматичне правило", мы вызываем функцию из rules.py
        show_rules_page()

else:
    # РЕЖИМ: Проверить себя
    st.subheader("🧠 Тренажер: Перевір свої знання")
    st.write(f"Давай перевіримо, як ти пам'ятаєш слово **{word_input}**")

    # Имитация задания (пока без базы данных)
    st.write("Завдання: Перекладіть і поставте в правильну форму.")
    st.write("Контекст: **On ______ (бути) w domu.**")

    # Поле ввода для пользователя
    user_answer = st.text_input("Введи правильне закінчення або форму слова:")

    # Кнопка проверки
    if st.button("Перевірити відповідь"):
        if user_answer.lower() == "był":
            st.success("🔥 Геніально! Відповідь вірна: On był w domu.")
        else:
            st.error("❌ Спробуй ще раз або подивись у Довідник!")