import streamlit as st

def show_rules_page():
    st.title("📚 Граматичний довідник")
    st.write("Оберіть рід та категорію, щоб переглянути правила та закінчення.")

    # 1. Полочки (Вкладки по родах)
    tab_meski, tab_zenski, tab_nijaki = st.tabs([
        "👔 Чоловічий (Męski)", 
        "👗 Жіночий (Żeński)", 
        "👶 Середній (Nijaki)"
    ])

    # === ПОЛОЧКА: ЧОЛОВІЧИЙ РІД ===
    with tab_meski:
        st.subheader("Правила для чоловічого роду")
        
        # Папочка 1: Минулий час
        with st.expander("⏳ Минулий час (Czas przeszły)"):
            st.markdown("""
            **Особливості творення:**
            * **ja** -> *-em* (byłem, robiłem)
            * **ty** -> *-eś* (byłeś, robiłeś)
            * **on** -> *-ił / -ał / -ł* (był, robił)
            """)

        # Папочка 2: Відмінки
        with st.expander("🔄 Відмінки (Deklinacja)"):
            st.markdown("""
            * **Narzędnik (Орудний):** закінчення *-em* (z bratem, z psem).
            * **Biernik (Знахідний):** істоти мають закінчення *-a* (widzę psa), неістоти — як у називному (widzę stół).
            """)

    # === ПОЛОЧКА: ЖІНОЧИЙ РІД ===
    with tab_zenski:
        st.subheader("Правила для жіночого роду")
        
        with st.expander("⏳ Минулий час (Czas przeszły)"):
            st.markdown("""
            * **ja** -> *-am* (byłam, robiłam)
            * **ty** -> *-aś* (byłaś, robiłaś)
            * **ona** -> *-a* (była, robiła)
            """)

        with st.expander("🔄 Відмінки (Deklinacja)"):
            st.markdown("""
            * **Biernik (Знахідний):** майже завжди закінчення *-ę* (widzę mamę, książkę).
            * **Narzędnik (Орудний):** завжди закінчення *-ą* (z mamą, z siostrą).
            """)

    # === ПОЛОЧКА: СЕРЕДНІЙ РІД ===
    with tab_nijaki:
        st.subheader("Правила для середнього роду")
        
        with st.expander("⏳ Минулий час (Czas przeszły)"):
            st.markdown("""
            * **ono** -> *-o* (było, robiło)
            """)