import streamlit as st
from data import SERVICES, classify_domain, get_matches, CAT_LABELS

st.set_page_config(
    page_title="EduBenefits — Verifique seus benefícios institucionais",
    page_icon="🎓",
    layout="wide",
)

# --- Tema ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

DARK = st.session_state.dark_mode

if DARK:
    BG          = "#0f1117"
    BG2         = "#1a1d27"
    TEXT        = "#ffffff"
    TEXT_MUTED  = "#e0e0e6"
    BORDER      = "#2e3044"
    BORDER_MATCH= "#1D9E75"
    CARD_MATCH  = "#0d2b22"
    CAT_BG      = "#23263a"
    CAT_FG      = "#9da3be"
    BADGE_BG    = "#0d2b22"
    BADGE_FG    = "#4ecb9e"
    LINK_COLOR  = "#5ba4f5"
    ICON_LABEL  = "☀️ Modo claro"
else:
    BG          = "#ffffff"
    BG2         = "#f8f9fa"
    TEXT        = "#000000"
    TEXT_MUTED  = "#242424"
    BORDER      = "#e0e0e0"
    BORDER_MATCH= "#1D9E75"
    CARD_MATCH  = "#f0faf6"
    CAT_BG      = "#f0f0f0"
    CAT_FG      = "#555555"
    BADGE_BG    = "#E1F5EE"
    BADGE_FG    = "#085041"
    LINK_COLOR  = "#1a73e8"
    ICON_LABEL  = "🌙 Modo escuro"

st.markdown(
    f"""
    <style>
        .stApp, .stApp > div, .block-container {{
            background-color: {BG} !important;
            color: {TEXT} !important;
        }}
        section[data-testid="stSidebar"], section[data-testid="stSidebar"] > div {{
            background-color: {BG2} !important;
        }}
        .stTextInput > div > div > input {{
            background-color: {BG2} !important;
            color: {TEXT} !important;
            border-color: {BORDER} !important;
        }}
        label, p, span, .stRadio label, .stCaption,
        [data-testid="stText"], [data-testid="stMarkdownContainer"] p {{
            color: {TEXT_MUTED} !important;
        }}
        h1, h2, h3 {{
            color: {TEXT} !important;
        }}
        .stButton > button {{
            background-color: #1D9E75 !important;
            color: white !important;
            border: none !important;
        }}
        .stButton > button:hover {{
            background-color: #178a64 !important;
        }}
        div[data-testid="metric-container"] {{
            background-color: {BG2} !important;
            border: 1px solid {BORDER} !important;
            border-radius: 10px !important;
            padding: 12px 16px !important;
        }}
        div[data-testid="metric-container"] label,
        div[data-testid="metric-container"] div {{
            color: {TEXT} !important;
        }}
        hr, [data-testid="stDivider"] {{
            border-color: {BORDER} !important;
        }}
        .stAlert {{
            background-color: {BG2} !important;
        }}
        /* Radio buttons */
        .stRadio > div {{
            background-color: transparent !important;
        }}
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
        #MainMenu {{
            visibility: hidden;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
header_col, toggle_col = st.columns([8, 1])
with header_col:
    st.title("🎓 EduBenefits")
    st.caption("Descubra quais softwares e serviços oferecem planos gratuitos ou descontos para o seu email institucional.")
with toggle_col:
    st.write("")
    st.write("")
    st.button(ICON_LABEL, on_click=toggle_theme, use_container_width=True)

st.divider()

# --- Input ---
email = st.text_input(
    "Seu email institucional",
    placeholder="voce@uerj.br",
    help="Funciona com emails de universidades, institutos federais e startups.",
)

col_btn, col_space = st.columns([1, 5])
with col_btn:
    st.button("Verificar", type="primary", use_container_width=True, key="btn_verificar")

# --- Filtro de categorias ---
st.write("")
cats = ["Todos"] + list(CAT_LABELS.values())
selected_cat = st.radio(
    "Filtrar por categoria",
    cats,
    horizontal=True,
    label_visibility="collapsed",
)

st.divider()

# --- Lógica principal ---
if email:
    if "@" not in email:
        st.warning("Por favor, insira um email válido com @.")
    else:
        domain = email.strip().lower().split("@")[-1]
        domain_type = classify_domain(domain)
        matched = get_matches(domain_type)
        matched_names = {s["name"] for s in matched}

        if domain_type == "academic":
            st.success(f"**Domínio acadêmico detectado:** `@{domain}`")
        elif domain_type == "startup":
            st.warning(f"**Domínio de startup detectado:** `@{domain}`")
        else:
            st.info(
                f"`@{domain}` não foi identificado automaticamente. "
                "Se sua instituição deveria aparecer, considere [contribuir com um novo domínio](/Contribuir)."
            )

        m1, m2, m3 = st.columns(3)
        m1.metric("Serviços verificados", len(SERVICES))
        m2.metric("Provável elegibilidade", len(matched))
        m3.metric("Domínio", f"@{domain}")

        st.write("")

        def cat_key(label):
            for k, v in CAT_LABELS.items():
                if v == label:
                    return k
            return None

        selected_key = cat_key(selected_cat)
        display = [s for s in SERVICES if selected_key in s["cats"]] if selected_key else list(SERVICES)
        display.sort(key=lambda s: (0 if s["name"] in matched_names else 1))

        vis_matched = [s for s in display if s["name"] in matched_names]
        st.caption(
            f"{len(display)} serviços na categoria selecionada — "
            f"**{len(vis_matched)}** com provável elegibilidade"
        )

        cols_per_row = 3
        for i in range(0, len(display), cols_per_row):
            row = display[i : i + cols_per_row]
            cols = st.columns(cols_per_row)
            for col, service in zip(cols, row):
                is_match = service["name"] in matched_names
                with col:
                    border  = BORDER_MATCH if is_match else BORDER
                    card_bg = CARD_MATCH if is_match else BG2
                    opacity = "1" if is_match else "0.45"

                    badge = (
                        f'<span style="background:{BADGE_BG};color:{BADGE_FG};'
                        f'font-size:11px;padding:2px 8px;border-radius:20px;'
                        f'margin-left:6px;">✓ Elegível</span>'
                        if is_match else ""
                    )
                    cat_badges = " ".join(
                        f'<span style="background:{CAT_BG};color:{CAT_FG};'
                        f'font-size:11px;padding:2px 8px;border-radius:20px;">'
                        f'{CAT_LABELS.get(c, c)}</span>'
                        for c in service["cats"]
                    )
                    link_html = (
                        f'<a href="{service["link"]}" target="_blank" '
                        f'style="font-size:12px;color:{LINK_COLOR};text-decoration:none;">'
                        f'Verificar no site oficial →</a>'
                        if is_match else ""
                    )
                    st.markdown(
                        f"""
                        <div style="
                            background-color: {card_bg};
                            border: 1.5px solid {border};
                            border-radius: 12px;
                            padding: 16px;
                            margin-bottom: 12px;
                            opacity: {opacity};
                            min-height: 160px;
                        ">
                            <div style="font-size:15px;font-weight:600;margin-bottom:6px;color:{TEXT};">
                                {service['logo']} {service['name']}{badge}
                            </div>
                            <div style="font-size:13px;color:{TEXT_MUTED};margin-bottom:10px;line-height:1.5;">
                                {service['desc']}
                            </div>
                            <div style="margin-bottom:8px;">{cat_badges}</div>
                            {link_html}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
else:
    st.markdown(
        f'<div style="color:{TEXT_MUTED};font-size:14px;padding:1rem 0;">'
        f'Digite seu email institucional acima para verificar os benefícios disponíveis.</div>',
        unsafe_allow_html=True,
    )

st.divider()
st.caption(
    "⚠️ Este verificador é uma referência — a elegibilidade real é sempre confirmada pelo próprio serviço. "
    "Quer sugerir um domínio ou serviço? Acesse a página **Contribuir** no menu lateral."
)