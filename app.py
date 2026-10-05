import streamlit as st
import random
from engine import generate_business_package

st.set_page_config(
    page_title="Marketor – AI Business Hub", 
    page_icon="🚀", 
    layout="centered"
)

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

st.markdown("### 💡 Въведи само **една дума** и получи пълен бизнес наръчник за всеки бранш!")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

if "is_subscriber" not in st.session_state:
    st.session_state.is_subscriber = False

if "active_codes" not in st.session_state:
    st.session_state.active_codes = ["MARKETOR2026"]

st.sidebar.header("🔐 Достъп и Управление")

admin_pass_input = st.sidebar.text_input("Администраторски код (за теб):", type="password")
if admin_pass_input == "tsvetelina2026": 
    st.session_state.is_admin = True

if st.session_state.is_admin:
    st.sidebar.success("✅ Влязъл си като Администратор!")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ⚙️ Автоматично генериране на кодове")
    
    if st.sidebar.button("Генерирай нов код за клиент"):
        new_code = f"MKT-{random.randint(1000, 9999)}"
        if new_code not in st.session_state.active_codes:
            st.session_state.active_codes.append(new_code)
        st.sidebar.success(f"Създаден код: **{new_code}**")
        
    st.sidebar.write("Активни кодове:")
    st.sidebar.write(st.session_state.active_codes)
    
else:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💳 Плащане през EasyPay")
    st.sidebar.info(
        "**Как да получиш достъп:**\n"
        "1. Направи превод в евро (€) по EasyPay.\n"
        "2. Получи своя уникален код от нас.\n"
        "3. Въведи го по-долу:"
    )
    
    client_code = st.sidebar.text_input("Въведи клиентски код:")
    
    if st.sidebar.button("Активирай код"):
        if client_code in st.session_state.active_codes:
            st.session_state.is_subscriber = True
            st.sidebar.success("✅ Успешен абонамент!")
        else:
            st.sidebar.error("❌ Невалиден код за достъп.")

has_access = st.session_state.is_admin or st.session_state.is_subscriber

if not has_access:
    st.warning("🔒 **Този софтуер е достъпен само за активни абонати или клиенти на нашата платформа.** Моля, въведи код за достъп от лявото меню след направено плащане през EasyPay.")
else:
    if st.session_state.is_admin:
        st.info("👑 Работиш в администраторски режим (Неограничени безплатни генерации).")
    
    keyword_input = st.text_input("Въведи дума (напр. Палачинки, Ремонти, Адвокат...):", placeholder="напр. Ремонти")

    if st.button("✨ Създай изчерпателен бизнес наръчник"):
        if not keyword_input:
            st.warning("Моля, въведи поне една дума!")
        else:
            with st.spinner("Marketor анализира нишата и изготвя пълния стратегически наръчник... Моля, изчакай секунда."):
                result = generate_business_package(keyword_input)
                
                st.success("Готово! Ето Вашият пълен и детайлен бизнес пакет:")
                
                st.subheader("📊 Стратегическо обобщение")
                st.write(result["executive_summary"])
                
                st.markdown(result["step_by_step_setup"])
                st.markdown(result["buyer_persona"])
                st.markdown(result["pricing_and_packages"])
                st.markdown(result["marketing_strategy"])
                
                st.subheader("📱 Готови публикации за социални мрежи")
                for post in result["social_media_posts"]:
                    st.info(post)
                    
                st.subheader("🎬 Сценарий за видео реклама (Reels / TikTok)")
                st.text(result["video_script"])
                
                st.markdown(result["action_plan_30_days"])
