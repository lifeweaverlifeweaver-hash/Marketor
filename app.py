import streamlit as st
import random

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

st.markdown("### 💡 Въведи само **една дума** и получи пълен бизнес наръчник за всеки бранш!")

# --- ФУНКЦИЯ ЗА ГЕНЕРИРАНЕ НА БИЗНЕС ПАКЕТА ---
def generate_business_package(keyword: str) -> dict:
    clean_keyword = keyword.strip().capitalize()
    
    package = {
        "industry": f"Стратегически бизнес наръчник за ниша: {clean_keyword}",
        
        "executive_summary": (
            f"Този документ представлява пълен и структуриран план за стартиране, позициониране и мащабиране на бизнес в сферата на **{clean_keyword}**. "
            f"Включва точни инструкции, разпределение на бюджета в евро (€), времеви рамки и маркетингови канали за бърза възвращаемост."
        ),
        
        "step_by_step_setup": (
            f"### 🛠️ Етап 1: Техническа и организационна подготовка\n"
            f"1. **Регистрация и правна форма:** Изберете подходяща структура (напр. ЕООД или регистрация като свободна професия), съобразена с българското законодателство.\n"
            f"2. **Банкова сметка и плащания:** Настройте бизнес сметка и интегрирайте готови разплащателни методи (EasyPay, Stripe, банков превод) с фиксирани цени в евро (€).\n"
            f"3. **Оборудване и софтуер:** Осигурете си надежден лаптоп, постоянен интернет достъп и специализиран софтуер за управление на клиенти (CRM) и фактуриране.\n"
            f"4. **Брандинг:** Съберете качествен снимков и видео материал, представящ вашите услуги/продукти за {clean_keyword} в най-добра светлина."
        ),
        
        "buyer_persona": (
            f"### 🎯 Етап 2: Идентифициране на идеалния клиент (Buyer Persona)\n"
            f"• **Профил:** Мъже и жени на възраст 25–50 години, собственици на малък бизнес или крайни потребители, търсещи бързо и надеждно решение за {clean_keyword}.\n"
            f"• **Основни проблеми (боли точки):** Липса на време, несигурност в качеството, високи цени на пазара.\n"
            f"• **Какво ги печели:** Бърза комуникация, ясни цени в евро (€) без скрити такси, гаранция за свършена работа и отлично обслужване."
        ),

        "pricing_and_packages": (
            f"### 💰 Етап 3: Ценообразуване и пакети (в евро €)\n"
            f"За да изградите доверие и да улесните клиентите, разделете услугите/продуктите си на 3 яснии пакета:\n"
            f"1. **Стартов пакет (Базов):** Фокусиран върху основната нужда от {clean_keyword}. *Цена: 49 €.*\n"
            f"2. **Премиум пакет (Най-продаван):** Пълно обслужване с включени допълнителни екстри и бърза реакция. *Цена: 149 €.*\n"
            f"3. **Корпоративен / VIP пакет:** Дългосрочно обслужване или обемни поръчки с персонален мениджър. *Цена: 399 €.*"
        ),

        "marketing_strategy": (
            f"### 📈 Етап 4: Маркетингова стратегия и привличане на клиенти\n"
            f"1. **Социални мрежи (Органично):** Публикувайте ежедневни видеа (Reels/Shorts/TikTok), показващи процеса на работа с {clean_keyword}.\n"
            f"2. **Платена реклама (Meta Ads):** Стартирайте таргетирани реклами във Facebook и Instagram с малък бюджет (напр. 5 € на ден), насочени към местната ви аудитория.\n"
            f"3. **Препоръки от клиенти:** Предложете 10% отстъпка за следваща услуга на всеки клиент, който ви доведе нов човек."
        ),
        
        "social_media_posts": [
            f"🚀 Търсите перфектното решение за {clean_keyword} без компромиси в качеството? Ние предлагаме бързи, сигурни и доказани резултати. Свържете се с нас днес и вземете безплатна консултация!",
            f"💡 Защо да губите време и нерви? Професионалните услуги за {clean_keyword} са създадени да ви улеснят. Прозрачни цени в евро и гарантиран краен резултат. Запазете час сега!"
        ],
        
        "video_script": (
            f"[ВИЗУАЛНО: Динамично видео, показващо резултат от работа с {clean_keyword}]\n\n"
            f"(Уверен и спокоен глас зад кадър):\n"
            f"'Искате ли най-доброто за {clean_keyword} без излишни главоболия, чакане и скрити такси? "
            f"Ние знаем как да свършим работата бързо, чисто и професионално. "
            f"Доверете се на доказаните специалисти. Посетете профила ни или ни пишете на лично съобщение още сега!'"
        ),
        
        "action_plan_30_days": (
            f"### 📅 Етап 5: 30-дневен план за действие\n"
            f"• **Дни 1–5:** Финализиране на брандинга, цените и създаване на профили в социалните мрежи.\n"
            f"• **Дни 6–15:** Създаване на първите 10 информационни и рекламни видеа за {clean_keyword}.\n"
            f"• **Дни 16–25:** Пускане на първите платени кампании и събиране на контакти на заинтересовани клиенти.\n"
            f"• **Дни 26–30:** Анализ на резултатите, затваряне на първите платени сделки и оптимизиране на офертата."
        )
    }
    
    return package

# --- СИСТЕМА ЗА ДОСТУП И УПРАВЛЕНИЕ ---
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
