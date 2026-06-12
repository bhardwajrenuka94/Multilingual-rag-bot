import streamlit as st
from rag_chain import get_chain

# ── UI text translations ──────────────────────────────────────────────────────
UI_TEXT = {
    "English":    {
        "title":       "💬 Customer Support Bot",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "Hello! I am your customer support assistant. Ask me about orders, refunds, payments, or account issues!",
        "placeholder": "Type your question here...",
        "spinner":     "Searching knowledge base...",
        "lang_label":  "🌐 Language",
    },
    "Hindi":      {
        "title":       "💬 ग्राहक सहायता बॉट",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "नमस्ते! मैं आपका ग्राहक सहायता सहायक हूँ। ऑर्डर, रिफंड, भुगतान या खाता संबंधी समस्याओं के बारे में पूछें!",
        "placeholder": "यहाँ अपना प्रश्न लिखें...",
        "spinner":     "ज्ञान आधार खोज रहा है...",
        "lang_label":  "🌐 भाषा",
    },
    "Spanish":    {
        "title":       "💬 Bot de Soporte al Cliente",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "¡Hola! Soy tu asistente de soporte al cliente. ¡Pregúntame sobre pedidos, reembolsos, pagos o problemas de cuenta!",
        "placeholder": "Escribe tu pregunta aquí...",
        "spinner":     "Buscando en la base de conocimiento...",
        "lang_label":  "🌐 Idioma",
    },
    "French":     {
        "title":       "💬 Bot de Support Client",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "Bonjour ! Je suis votre assistant support client. Posez-moi des questions sur les commandes, remboursements, paiements ou comptes !",
        "placeholder": "Tapez votre question ici...",
        "spinner":     "Recherche dans la base de connaissances...",
        "lang_label":  "🌐 Langue",
    },
    "German":     {
        "title":       "💬 Kundensupport-Bot",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "Hallo! Ich bin Ihr Kundensupport-Assistent. Fragen Sie mich zu Bestellungen, Rückerstattungen, Zahlungen oder Kontoproblemen!",
        "placeholder": "Geben Sie Ihre Frage hier ein...",
        "spinner":     "Wissensdatenbank wird durchsucht...",
        "lang_label":  "🌐 Sprache",
    },
    "Arabic":     {
        "title":       "💬 بوت دعم العملاء",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "مرحباً! أنا مساعد دعم العملاء. اسألني عن الطلبات والمبالغ المستردة والمدفوعات ومشاكل الحساب!",
        "placeholder": "اكتب سؤالك هنا...",
        "spinner":     "جاري البحث في قاعدة المعرفة...",
        "lang_label":  "🌐 اللغة",
    },
    "Bengali":    {
        "title":       "💬 গ্রাহক সহায়তা বট",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "নমস্কার! আমি আপনার গ্রাহক সহায়তা সহকারী। অর্ডার, রিফান্ড, পেমেন্ট বা অ্যাকাউন্ট সমস্যা সম্পর্কে জিজ্ঞাসা করুন!",
        "placeholder": "এখানে আপনার প্রশ্ন টাইপ করুন...",
        "spinner":     "জ্ঞানভাণ্ডার অনুসন্ধান করা হচ্ছে...",
        "lang_label":  "🌐 ভাষা",
    },
    "Tamil":      {
        "title":       "💬 வாடிக்கையாளர் ஆதரவு போட்",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "வணக்கம்! நான் உங்கள் வாடிக்கையாளர் ஆதரவு உதவியாளர். ஆர்டர், திரும்பப் பெறுதல், கட்டணம் அல்லது கணக்கு சிக்கல்களைப் பற்றி கேளுங்கள்!",
        "placeholder": "உங்கள் கேள்வியை இங்கே தட்டச்சு செய்யுங்கள்...",
        "spinner":     "அறிவுத் தளத்தில் தேடுகிறது...",
        "lang_label":  "🌐 மொழி",
    },
    "Telugu":     {
        "title":       "💬 కస్టమర్ సపోర్ట్ బాట్",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "నమస్కారం! నేను మీ కస్టమర్ సపోర్ట్ అసిస్టెంట్‌ని. ఆర్డర్లు, రీఫండ్లు, చెల్లింపులు లేదా ఖాతా సమస్యల గురించి అడగండి!",
        "placeholder": "మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి...",
        "spinner":     "నాలెడ్జ్ బేస్ శోధిస్తోంది...",
        "lang_label":  "🌐 భాష",
    },
    "Chinese":    {
        "title":       "💬 客户支持机器人",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "您好！我是您的客户支持助手。请询问有关订单、退款、付款或账户问题！",
        "placeholder": "在此输入您的问题...",
        "spinner":     "正在搜索知识库...",
        "lang_label":  "🌐 语言",
    },
    "Japanese":   {
        "title":       "💬 カスタマーサポートボット",
        "caption":     "RAG · LangChain · ChromaDB · Groq · HuggingFace",
        "greeting":    "こんにちは！カスタマーサポートアシスタントです。注文、返金、支払い、アカウントの問題についてお気軽にどうぞ！",
        "placeholder": "ご質問をここに入力してください...",
        "spinner":     "ナレッジベースを検索中...",
        "lang_label":  "🌐 言語",
    },
}

LANGUAGES = list(UI_TEXT.keys())

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Support Bot",
    page_icon="💬",
    layout="centered"
)

# ── Language selector (sidebar) ───────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")
    selected_lang = st.selectbox(
        "🌐 Interface Language",
        options=LANGUAGES,
        index=0,
        key="selected_language"
    )
    st.info(
        "The bot will automatically detect the language of your question "
        "and reply in the **same language**, regardless of the interface language chosen above."
    )
    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

txt = UI_TEXT[selected_lang]

# ── Title & caption ───────────────────────────────────────────────────────────
st.title(txt["title"])
st.caption(txt["caption"])
st.divider()

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show greeting only when chat is empty
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(txt["greeting"])

# ── Chat history ──────────────────────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Input ─────────────────────────────────────────────────────────────────────
user_question = st.chat_input(txt["placeholder"])

if user_question:
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})

    # Build a language-aware chain on each call (cheap — just builds prompt)
    chain = get_chain(selected_lang)

    with st.chat_message("assistant"):
        with st.spinner(txt["spinner"]):
            answer = chain.invoke(user_question)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})