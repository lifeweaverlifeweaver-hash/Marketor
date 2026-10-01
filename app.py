import streamlit as st
from engine import generate_business_package

# Настройка на страницата с новото лого/иконка
st.set_page_config(
    page_title="Marketor – AI Business Hub", 
    page_icon="🚀", 
    layout="centered"
)

# Визуално лого в горната част на приложението
st.markdown(
    """
    <div style="text-align: center; padding: 10px 0;">
        <h1 style="color: #2E86C1; font-size: 2.8rem; margin-bottom: 0;">🚀 M A R K E T O R</h1>
        <p style="color: #7F8C8D; font-size: 1.1rem; letter-spacing: 2px; margin-top: 5px;">AI BUSINESS HUB</p>
    </div>
    <hr style="border: 0; height: 1px; background: #E5E7E9; margin-bottom: 25px;">
    """, 
    unsafe_allow_html=True
)

st.markdown("### 💡 Въведи само **една дума** и получи готов бизнес пакет за всеки бранш!")

# Управление на кредитите в сесията
if "credits" not in st.session_state:
    st.session_state.credits = 1 # Стартов безплатен кредит

# Странично меню за абонамент и EasyPay плащания
st.sidebar.header("💳 Абонамент и Плащане")
st.sidebar.markdown("Зареди кредити през **EasyPay**, за да ползваш Marketor неограничено!")
st.sidebar.info(
    "**Как да заредиш:**\n"
    "1. Направи превод в евро (€) по твоето EasyPay.\n"
    "2. Изпрати ми код или квитанция.\n"
    "3. Получи код за достъп тук!"
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Налични кредити:** {st.session_state.credits}")

# Основно поле за въвеждане на думата
keyword_input = st.text_input("Въведи дума (напр. Палачинки, Ремонти, Адвокат...):", placeholder="напр. Ремонти")

if st.button("✨ Създай всичко с едно докосване"):
    if not keyword_input:
        st.warning("Моля, въведи поне една дума!")
    elif st.session_state.credits <= 0:
        st.error("Нямаш налични кредити! Моля, зареди през EasyPay в страничното меню.")
    else:
        with st.spinner("Marketor анализира и генерира твоя пакет... Моля, изчакай секунда."):
            result = generate_business_package(keyword_input)
            
            st.session_state.credits -= 1 # Взимаме 1 кредит при успешна генерация
            
            st.success("Готово! Ето Вашият All-in-One пакет:")
            
            st.subheader("📌 Описание на продукта / услугата")
            st.write(result["product_description"])
            
            st.subheader("📱 Рекламни публикации за социални мрежи")
            for post in result["social_media_posts"]:
                st.info(post)
                
            st.subheader("🎬 Сценарий за видео (Reels / TikTok)")
            st.text(result["video_script"])
            
            st.subheader("🎯 Маркетинг стратегия")
            st.write(result["marketing_strategy"])
