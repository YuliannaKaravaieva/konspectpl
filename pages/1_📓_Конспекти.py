import streamlit as st

st.set_page_config(page_title="Конспекти", page_icon="📓", layout="wide")

st.title("📚 Граматичний довідник")
st.caption("Статичні конспекти та правила польської мови")

# Полочки (Вкладки).
tab_meski, tab_zenski, tab_nijaki, tab_ogolne = st.tabs([
    "👔 Чоловічий (Męski)", 
    "👗 Жіночий (Żeński)", 
    "👶 Середній (Nijaki)",
    "📌 Загальні правила"
])

with tab_meski:
    st.subheader("Чоловічий рід (Męski)")
    with st.expander("⏳ Минулий час (Czas przeszły)"):
        st.markdown("""
        * **ja** -> *-em* (byłem, robiłem)
        * **ty** -> *-eś* (byłeś, robiłeś)
        * **on** -> *-ił / -ał / -ł* (był, robił)
        """)

    with st.expander("🔄 Відмінки (Deklinacja)"):
        st.markdown("""
        * **Narzędnik (Орудний):** закінчення *-em* (z bratem).
        * **Biernik (Знахідний):** істоти *-a* (widzę brata), неістоти — як у називному.
        """)

with tab_zenski:
    st.subheader("Жіночий рід (Żeński)")
    with st.expander("⏳ Минулий час (Czas przeszły)"):
        st.markdown("""
        * **ja** -> *-am* (byłam, robiłam)
        * **ty** -> *-aś* (byłaś, robiłaś)
        * **ona** -> *-a* (była, robiła)
        """)

with tab_nijaki:
    st.subheader("Середній рід (Nijaki)")
    with st.expander("⏳ Минулий час (Czas przeszły)"):
        st.markdown("""
        * **ono** -> *-o* (było, robiło)
        """)

with tab_ogolne:
    st.subheader("Загальні винятки та правила")
    with st.expander("⚠️ Чергування звуків"):
        st.markdown("""
        * **k -> c**
        * **r -> rz**
        """)