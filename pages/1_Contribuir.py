import streamlit as st
import json
import os
from datetime import datetime

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

DARK = st.session_state.dark_mode

if DARK:
    BG          = "#0f1117"
    BG2         = "#1a1d27"
    TEXT        = "#f0f2f8"
    TEXT_MUTED  = "#b0b4cc"
    BORDER      = "#2e3044"
else:
    BG          = "#ffffff"
    BG2         = "#f8f9fa"
    TEXT        = "#1a1a1a"
    TEXT_MUTED  = "#555555"
    BORDER      = "#e0e0e0"

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
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div,
        .stMultiSelect > div > div,
        [data-baseweb="select"] > div,
        [data-baseweb="popover"],
        [data-baseweb="menu"],
        [data-baseweb="option"] {{
            background-color: {BG2} !important;
            color: {TEXT} !important;
            border-color: {BORDER} !important;
        }}
        [data-baseweb="option"]:hover {{
            background-color: {BORDER} !important;
        }}
        hr {{
            border-color: {BORDER} !important;
        }}
        #MainMenu {{ visibility: hidden; }}
                header[data-testid="stHeader"] {{
            background-color: {BG} !important;
        }}
        div[data-testid="stToolbar"] {{
            background-color: {BG} !important;
        }}
        header[data-testid="stHeader"] * {{
            color: {TEXT} !important;
        }}
        div[data-testid="stToolbar"] * {{
            color: {TEXT} !important;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.set_page_config(
    page_title="Contribuir — EduBenefits",
    page_icon="🎓",
    layout="centered",
)

st.title("🤝 Contribuir")
st.write(
    "Conhece uma universidade ou serviço que deveria estar na lista? "
    "Preencha o formulário abaixo. Sua sugestão será salva e revisada."
)

st.divider()

CONTRIB_FILE = "contributions.json"


def load_contributions():
    if os.path.exists(CONTRIB_FILE):
        with open(CONTRIB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_contribution(entry: dict):
    data = load_contributions()
    data.append(entry)
    with open(CONTRIB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


tab_domain, tab_service = st.tabs(["🏫 Sugerir domínio de instituição", "🛠️ Sugerir novo serviço"])

# --- Tab 1: Sugerir domínio ---
with tab_domain:
    st.subheader("Adicionar domínio de instituição")
    st.caption("Use quando sua universidade ou instituto não for detectada automaticamente.")

    with st.form("form_domain"):
        inst_name = st.text_input("Nome da instituição", placeholder="Universidade Federal do Exemplo")
        inst_domain = st.text_input(
            "Domínio do email institucional",
            placeholder="ufexemplo.br",
            help="Apenas o domínio, sem o @. Ex: uerj.br",
        )
        inst_type = st.selectbox(
            "Tipo",
            ["Universidade Federal", "Universidade Estadual", "Instituto Federal",
             "Universidade Privada", "Escola Técnica", "Outro"],
        )
        inst_country = st.text_input("País", value="Brasil")
        inst_note = st.text_area(
            "Observações (opcional)",
            placeholder="Ex: domínio confirmado via portal do aluno",
            max_chars=300,
        )
        submitted_domain = st.form_submit_button("Enviar sugestão", type="primary")

        if submitted_domain:
            if not inst_name or not inst_domain:
                st.error("Preencha pelo menos o nome e o domínio.")
            elif "@" in inst_domain or " " in inst_domain:
                st.error("Insira apenas o domínio, sem @ ou espaços. Ex: uerj.br")
            else:
                entry = {
                    "type": "domain",
                    "name": inst_name,
                    "domain": inst_domain.lower().strip(),
                    "inst_type": inst_type,
                    "country": inst_country,
                    "note": inst_note,
                    "created_at": datetime.now().isoformat(),
                }
                save_contribution(entry)
                st.success(f"✅ Obrigado! O domínio `{inst_domain}` foi registrado para revisão.")

# --- Tab 2: Sugerir serviço ---
with tab_service:
    st.subheader("Adicionar novo serviço ou benefício")
    st.caption("Conhece um software, plataforma ou serviço que oferece plano grátis/desconto institucional?")

    with st.form("form_service"):
        svc_name = st.text_input("Nome do serviço", placeholder="Ex: Zoom for Education")
        svc_link = st.text_input(
            "Link da página de benefício",
            placeholder="https://zoom.us/education",
        )
        svc_desc = st.text_area(
            "Descrição do benefício",
            placeholder="Ex: Plano gratuito com reuniões ilimitadas para instituições de ensino.",
            max_chars=400,
        )
        svc_cats = st.multiselect(
            "Categorias",
            ["Acadêmico", "Startup", "Dev / Cloud", "Design", "Produtividade"],
        )
        svc_eligible = st.multiselect(
            "Quem é elegível?",
            ["Estudantes universitários", "Professores / Docentes", "Startups", "ONGs", "Governo"],
        )
        svc_note = st.text_area("Observações (opcional)", max_chars=300)
        submitted_service = st.form_submit_button("Enviar sugestão", type="primary")

        if submitted_service:
            if not svc_name or not svc_link:
                st.error("Preencha pelo menos o nome e o link do serviço.")
            else:
                entry = {
                    "type": "service",
                    "name": svc_name,
                    "link": svc_link,
                    "desc": svc_desc,
                    "cats": svc_cats,
                    "eligible": svc_eligible,
                    "note": svc_note,
                    "created_at": datetime.now().isoformat(),
                }
                save_contribution(entry)
                st.success(f"✅ Obrigado! O serviço **{svc_name}** foi registrado para revisão.")

st.divider()

# --- Visualizar contribuições recentes (opcional, pode remover) ---
with st.expander("📋 Ver contribuições enviadas"):
    contribs = load_contributions()
    if not contribs:
        st.caption("Nenhuma contribuição ainda.")
    else:
        for c in reversed(contribs[-20:]):
            if c["type"] == "domain":
                st.markdown(f"🏫 **{c['name']}** — `{c['domain']}` ({c['inst_type']}) — {c['created_at'][:10]}")
            else:
                st.markdown(f"🛠️ **{c['name']}** — [{c['link']}]({c['link']}) — {c['created_at'][:10]}")
