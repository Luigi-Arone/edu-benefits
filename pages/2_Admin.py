import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="Admin — EduBenefits",
    page_icon="🎓",
    layout="wide",
)

# --- Tema ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

DARK = st.session_state.dark_mode

if DARK:
    BG         = "#0f1117"
    BG2        = "#1a1d27"
    TEXT       = "#ffffff"
    TEXT_MUTED = "#e0e0e6"
    BORDER     = "#2e3044"
else:
    BG         = "#ffffff"
    BG2        = "#f8f9fa"
    TEXT       = "#000000"
    TEXT_MUTED = "#242424"
    BORDER     = "#e0e0e0"

st.markdown(
    f"""
    <style>
        .stApp, .stApp > div, .block-container {{
            background-color: {BG} !important;
            color: {TEXT} !important;
        }}
        section[data-testid="stSidebar"],
        section[data-testid="stSidebar"] > div {{
            background-color: {BG2} !important;
        }}
        p, span, div, li, label {{
            color: {TEXT} !important;
        }}
        h1, h2, h3, h4 {{
            color: {TEXT} !important;
        }}
        .stCaption, small,
        [data-testid="stCaptionContainer"] p {{
            color: {TEXT_MUTED} !important;
        }}
        .stTextInput > div > div > input {{
            background-color: {BG2} !important;
            color: {TEXT} !important;
            border-color: {BORDER} !important;
        }}
        .stButton > button {{
            background-color: #1D9E75 !important;
            color: white !important;
            border: none !important;
        }}
        hr, [data-testid="stDivider"] {{
            border-color: {BORDER} !important;
        }}
        header[data-testid="stHeader"] {{
            background-color: {BG} !important;
        }}
        div[data-testid="stToolbar"] {{
            background-color: {BG} !important;
        }}
        #MainMenu {{ visibility: hidden; }}
        /* Tabela */
        [data-testid="stDataFrame"] {{
            background-color: {BG2} !important;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Autenticação ---
if "admin_auth" not in st.session_state:
    st.session_state.admin_auth = False

if not st.session_state.admin_auth:
    st.title("🔒 Admin")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar", type="primary"):
        if senha == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.admin_auth = True
            st.rerun()
        else:
            st.error("Senha incorreta.")
    st.stop()

# --- Dashboard ---
@st.cache_resource
def get_supabase():
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

def load_contributions():
    db = get_supabase()
    res = db.table("contributions").select("*").order("created_at", desc=True).execute()
    return res.data or []

def delete_contribution(id: int):
    db = get_supabase()
    db.table("contributions").delete().eq("id", id).execute()

col_title, col_logout = st.columns([8, 1])
with col_title:
    st.title("🛠️ Admin — Contribuições")
with col_logout:
    st.write("")
    st.write("")
    if st.button("Sair", use_container_width=True):
        st.session_state.admin_auth = False
        st.rerun()

st.divider()

contribs = load_contributions()

if not contribs:
    st.info("Nenhuma contribuição ainda.")
else:
    dominios = [c for c in contribs if c["type"] == "domain"]
    servicos = [c for c in contribs if c["type"] == "service"]

    m1, m2 = st.columns(2)
    m1.metric("Domínios sugeridos", len(dominios))
    m2.metric("Serviços sugeridos", len(servicos))

    st.write("")

    tab_dom, tab_svc = st.tabs([f"🏫 Domínios ({len(dominios)})", f"🛠️ Serviços ({len(servicos)})"])

    with tab_dom:
        for c in dominios:
            with st.container():
                col_info, col_del = st.columns([9, 1])
                with col_info:
                    st.markdown(
                        f"**{c['name']}** — `{c.get('domain', '')}` — "
                        f"{c.get('inst_type', '')} — {c.get('country', '')} — "
                        f"{c['created_at'][:10]}"
                    )
                    if c.get("note"):
                        st.caption(c["note"])
                with col_del:
                    if st.button("🗑️", key=f"del_{c['id']}"):
                        delete_contribution(c["id"])
                        st.cache_resource.clear()
                        st.rerun()
                st.divider()

    with tab_svc:
        for c in servicos:
            with st.container():
                col_info, col_del = st.columns([9, 1])
                with col_info:
                    st.markdown(
                        f"**{c['name']}** — [{c.get('link', '')}]({c.get('link', '')}) — "
                        f"{c['created_at'][:10]}"
                    )
                    if c.get("description"):
                        st.caption(c["description"])
                    if c.get("cats"):
                        st.caption(f"Categorias: {', '.join(c['cats'])}")
                    if c.get("eligible"):
                        st.caption(f"Elegíveis: {', '.join(c['eligible'])}")
                    if c.get("note"):
                        st.caption(c["note"])
                with col_del:
                    if st.button("🗑️", key=f"del_{c['id']}"):
                        delete_contribution(c["id"])
                        st.cache_resource.clear()
                        st.rerun()
                st.divider()