import streamlit as st
from engine import generate_business_package

# Настройка на страницата на Marketor
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

# --- СИСТЕМА ЗА ДОСТУП И УПРАВЛЕНИЕ ---
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

if "is_subscriber" not in st.session_state:
    st.session_state.is_subscriber = False

# Странично меню за управление, абонаменти и EasyPay
st.sidebar.header("🔐 Достъп и Плащане")

# Администраторски вход (за теб - напълно безплатно и неограничено)
admin_pass_input = st.sidebar.text_input("Администраторски код (за теб):", type="password")
# Можеш да смениш тази парола с каквато пожелаеш
if admin_pass_input == "tsvetelina2026": 
    st.session_state.is_admin = True
    st.sidebar.success("✅ Влязъл си като Администратор (Неограничен безплатен достъп)!")

if not st.session_state.is_admin:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💳 Плащане през EasyPay")
    st.sidebar.info(
        "**Как да получиш достъп:**\n"
        "1. Направи превод по твоето EasyPay.\n"
        "2. Получи своя уникален код за достъп.\n"
        "3. Въведи го по-долу:"
    )
    
    # Поле за въвеждане на код от клиент
    client_code = st.sidebar.text_input("Въведи код за достъп:")
    
    # Тук можеш да зададеш валидни кодове или да ги проверяваш
    valid_codes = ["MARKETOR2026", "VIP-CLIENT", "EASYPAY-100"] 
    
    if st.sidebar.button("Активирай код"):
        if client_code in valid_codes:
            st.session_state.is_subscriber = True
            st.sidebar.success("✅ Успешен абонамент! Добре дошъл!")
        else:
            st.sidebar.error("❌ Невалиден код за достъп.")

# Проверка дали потребителят има права да ползва софтуера
has_access = st.session_state.is_admin or st.session_state.is_subscriber

if not has_access:
    st.warning("🔒 **Този софтуер е достъпен само за активни абонати или клиенти на нашата платформа.** Моля, въведи код за достъп от лявото меню или се свържи с нас за плащане през EasyPay.")
else:
    if st.session_state.is_admin:
        st.info("👑 Работиш в администраторски режим (Неограничени безплатни генерации).")
    
    # Основно поле за въвеждане на думата
    keyword_input = st.text_input("Въведи дума (напр. Палачинки, Ремонти, Адвокат...):", placeholder="напр. Ремонти")

    if st.button("✨ Създай всичко с едно докосване"):
        if not keyword_input:
            st.warning("Моля, въведи поне една дума!")
        else:
            with st.spinner("Marketor анализира и генерира твоя пакет... Моля, изчакай секунда."):
                result = generate_business_package(keyword_input)
                
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
