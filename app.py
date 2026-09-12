import streamlit as st


# ============================================================
# GRAMVYAPAR AI
# Know Before You Borrow
# ============================================================

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# COLOUR THEME
# ============================================================

PRIMARY = "#526A3A"
SECONDARY = "#7D9A55"
ACCENT = "#C88A3D"
BACKGROUND = "#FAF8F1"
TEXT = "#33352C"
CARD = "#FFFFFF"
LIGHT_TEXT = "#F8F7F0"
MUTED = "#6F7466"
BORDER = "#D9DED1"


# ============================================================
# LANGUAGE SYSTEM
# Backend-ready: UI text can be translated without changing
# business logic, calculations, APIs, or database structures.
# ============================================================

LANGUAGES = {
    "English": "en",
    "മലയാളം": "ml",
}

TEXTS = {
    "en": {
        "tagline": "Know Before You Borrow",
        "step": "Step 1 of 6",
        "intro_title": "Tell us about yourself",
        "intro_description": (
            "This helps us understand which business opportunities "
            "may fit you best."
        ),
        "skills": "Your skills",
        "skills_desc": "Choose the skills you already have.",
        "skills_placeholder": "Select your skills",
        "custom_skill": "Add a custom skill",
        "custom_skill_placeholder": "Example: Mobile repair",
        "experience": "Years of experience",
        "experience_caption": (
            "Enter the number of years you have worked in your main skill."
        ),
        "capital": "Available capital",
        "capital_desc": "How much of your own money can you invest?",
        "capital_caption": (
            "Your own funds available for starting or expanding the business."
        ),
        "interests": "Business interests",
        "interests_desc": (
            "Choose the types of businesses you are interested in."
        ),
        "interests_placeholder": "Select your interests",
        "custom_interest": "Add a custom business interest",
        "custom_interest_placeholder": "Example: Mobile accessories",
        "risk": "Risk preference",
        "risk_desc": (
            "How comfortable are you with uncertainty when starting a business?"
        ),
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "low_description": "Prefer stable and predictable businesses.",
        "medium_description": "Comfortable with some uncertainty.",
        "high_description": "Willing to accept more uncertainty for higher potential.",
        "existing": "Existing business",
        "existing_toggle": "I already have a business",
        "existing_placeholder": "Example: Small tailoring shop",
        "continue": "Continue →",
        "local_dashboard": "Local Dashboard",
        "local_description": (
            "Your Kerala locality will be analyzed using available local evidence."
        ),
        "local_info": (
            "Frame 2 will connect to the Kerala location and local-data engine."
        ),
        "back": "← Back to Profile",
    },

    "ml": {
        "tagline": "വായ്പ എടുക്കും മുമ്പ് അറിയുക",
        "step": "ഘട്ടം 1 / 6",
        "intro_title": "നിങ്ങളെക്കുറിച്ച് പറയൂ",
        "intro_description": (
            "നിങ്ങൾക്ക് അനുയോജ്യമായ ബിസിനസ് അവസരങ്ങൾ കണ്ടെത്താൻ "
            "ഇത് ഞങ്ങളെ സഹായിക്കും."
        ),
        "skills": "നിങ്ങളുടെ കഴിവുകൾ",
        "skills_desc": "നിങ്ങൾക്ക് നിലവിൽ ഉള്ള കഴിവുകൾ തിരഞ്ഞെടുക്കുക.",
        "skills_placeholder": "കഴിവുകൾ തിരഞ്ഞെടുക്കുക",
        "custom_skill": "മറ്റൊരു കഴിവ് ചേർക്കുക",
        "custom_skill_placeholder": "ഉദാ: മൊബൈൽ റിപ്പയർ",
        "experience": "പ്രവൃത്തി പരിചയം",
        "experience_caption": (
            "നിങ്ങളുടെ പ്രധാന കഴിവിൽ എത്ര വർഷത്തെ പരിചയമുണ്ടെന്ന് നൽകുക."
        ),
        "capital": "ലഭ്യമായ മൂലധനം",
        "capital_desc": "നിങ്ങൾക്ക് നിക്ഷേപിക്കാൻ കഴിയുന്ന സ്വന്തം തുക എത്രയാണ്?",
        "capital_caption": (
            "ബിസിനസ് ആരംഭിക്കാനോ വികസിപ്പിക്കാനോ ലഭ്യമായ സ്വന്തം പണം."
        ),
        "interests": "ബിസിനസ് താൽപര്യങ്ങൾ",
        "interests_desc": "നിങ്ങൾക്ക് താൽപര്യമുള്ള ബിസിനസുകൾ തിരഞ്ഞെടുക്കുക.",
        "interests_placeholder": "ബിസിനസുകൾ തിരഞ്ഞെടുക്കുക",
        "custom_interest": "മറ്റൊരു ബിസിനസ് താൽപര്യം ചേർക്കുക",
        "custom_interest_placeholder": "ഉദാ: മൊബൈൽ ആക്സസറീസ്",
        "risk": "അപകടസാധ്യതയോടുള്ള സമീപനം",
        "risk_desc": (
            "ബിസിനസ് ആരംഭിക്കുമ്പോൾ അനിശ്ചിതത്വം സ്വീകരിക്കാൻ നിങ്ങൾ എത്രത്തോളം തയ്യാറാണ്?"
        ),
        "low": "കുറവ്",
        "medium": "മിതമായത്",
        "high": "കൂടുതൽ",
        "low_description": "സ്ഥിരതയും പ്രവചനീയതയും ഉള്ള ബിസിനസുകൾ ഇഷ്ടപ്പെടുന്നു.",
        "medium_description": "ചില അനിശ്ചിതത്വങ്ങൾ സ്വീകരിക്കാൻ തയ്യാറാണ്.",
        "high_description": "കൂടുതൽ സാധ്യതയ്ക്കായി കൂടുതൽ അനിശ്ചിതത്വം സ്വീകരിക്കാൻ തയ്യാറാണ്.",
        "existing": "നിലവിലുള്ള ബിസിനസ്",
        "existing_toggle": "എനിക്ക് ഇതിനകം ഒരു ബിസിനസ് ഉണ്ട്",
        "existing_placeholder": "ഉദാ: ചെറിയ തയ്യൽക്കട",
        "continue": "തുടരുക →",
        "local_dashboard": "പ്രാദേശിക ഡാഷ്ബോർഡ്",
        "local_description": (
            "ലഭ്യമായ പ്രാദേശിക വിവരങ്ങൾ ഉപയോഗിച്ച് നിങ്ങളുടെ കേരള പ്രദേശം വിശകലനം ചെയ്യും."
        ),
        "local_info": (
            "ഘട്ടം 2 കേരള ലൊക്കേഷൻ, പ്രാദേശിക ഡാറ്റാ സംവിധാനവുമായി ബന്ധിപ്പിക്കും."
        ),
        "back": "← പ്രൊഫൈലിലേക്ക് മടങ്ങുക",
    },
}


# ============================================================
# LANGUAGE STATE
# ============================================================

if "language" not in st.session_state:
    st.session_state.language = "en"


def t(key):
    return TEXTS[st.session_state.language][key]


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ==============================
       PAGE
       ============================== */

    .stApp {{
        background-color: {BACKGROUND};
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1180px;
        padding-top: 30px;
        padding-bottom: 60px;
    }}


    /* ==============================
       TEXT
       ============================== */

    h1, h2, h3, h4, h5, h6 {{
        color: {TEXT} !important;
    }}

    p {{
        color: {TEXT};
    }}


    /* ==============================
       BRAND
       ============================== */

    .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 5px;
    }}

    .brand-icon {{
        font-size: 38px;
    }}

    .brand-name {{
        font-size: 32px;
        font-weight: 750;
        color: {PRIMARY};
        letter-spacing: -0.5px;
    }}

    .tagline {{
        color: {MUTED};
        font-size: 16px;
        margin-left: 51px;
        margin-bottom: 25px;
    }}


    /* ==============================
       LANGUAGE SELECTOR
       ============================== */

    .language-label {{
        font-size: 12px;
        font-weight: 700;
        color: {MUTED};
        margin-bottom: 3px;
    }}


    /* ==============================
       PROGRESS
       ============================== */

    .progress-text {{
        text-align: center;
        font-size: 14px;
        font-weight: 600;
        color: {PRIMARY};
        margin-bottom: 6px;
    }}

    [data-testid="stProgress"] > div > div {{
        background-color: {SECONDARY};
    }}


    /* ==============================
       INTRO
       ============================== */

    .intro-title {{
        font-size: 30px;
        font-weight: 750;
        color: {TEXT};
        margin-top: 25px;
        margin-bottom: 6px;
    }}

    .intro-description {{
        font-size: 16px;
        color: {MUTED};
        margin-bottom: 30px;
    }}


    /* ==============================
       FIELD LABELS
       ============================== */

    .field-label {{
        font-size: 17px;
        font-weight: 700;
        color: {TEXT};
        margin-top: 20px;
        margin-bottom: 8px;
    }}

    .field-description {{
        font-size: 13px;
        color: {MUTED};
        margin-bottom: 8px;
    }}


    /* ==============================
       ALL INPUT TEXT
       ============================== */

    label {{
        color: {TEXT} !important;
    }}

    [data-testid="stWidgetLabel"] {{
        color: {TEXT} !important;
    }}

    [data-testid="stWidgetLabel"] p {{
        color: {TEXT} !important;
    }}

    /* Normal text / number inputs */

    input[type="text"],
    input[type="number"] {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
        font-weight: 600 !important;
        caret-color: {PRIMARY} !important;
    }}

    input::placeholder {{
        color: #85897E !important;
        -webkit-text-fill-color: #85897E !important;
        opacity: 1 !important;
    }}

    textarea {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}


    /* ==============================
       NUMBER INPUT
       ============================== */

    [data-testid="stNumberInput"] {{
        background-color: {PRIMARY};
        border-radius: 12px;
        padding: 2px;
    }}

    [data-testid="stNumberInput"] input {{
        background-color: {PRIMARY} !important;
        color: {LIGHT_TEXT} !important;
        -webkit-text-fill-color: {LIGHT_TEXT} !important;
        font-size: 19px !important;
        font-weight: 700 !important;
    }}

    [data-testid="stNumberInput"] button {{
        color: {PRIMARY} !important;
        background-color: #F0F3E9 !important;
    }}


    /* ==============================
       SELECT / MULTISELECT
       ============================== */

    [data-baseweb="select"] {{
        color: {TEXT} !important;
    }}

    [data-baseweb="select"] > div {{
        background-color: {CARD};
        border-radius: 12px;
        border: 1px solid {BORDER};
        min-height: 48px;
    }}

    [data-baseweb="select"] input {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    [data-baseweb="tag"] {{
        background-color: #E8EEDC !important;
        color: {PRIMARY} !important;
        border-radius: 20px !important;
    }}

    [data-baseweb="tag"] span {{
        color: {PRIMARY} !important;
    }}


    /* ==============================
       CUSTOM TEXT INPUTS
       ============================== */

    .custom-input {{
        margin-top: 7px;
        margin-bottom: 5px;
    }}

    .custom-input input {{
        background-color: #EEF2E7 !important;
        border: 1px solid #C7D0BA !important;
        border-radius: 12px !important;
        color: {PRIMARY} !important;
        -webkit-text-fill-color: {PRIMARY} !important;
        font-weight: 600 !important;
    }}


    /* ==============================
       SLIDER
       ============================== */

    [data-testid="stSlider"] {{
        padding-top: 5px;
        padding-bottom: 5px;
    }}


    /* ==============================
       RISK DESCRIPTION
       ============================== */

    .risk-description {{
        background-color: {CARD};
        border: 1px solid #E1E3DB;
        border-radius: 14px;
        padding: 14px 16px;
        margin-top: 10px;
        color: {TEXT} !important;
        font-size: 14px;
    }}

    .risk-description b {{
        color: {PRIMARY} !important;
    }}


    /* ==============================
       CONTINUE BUTTON
       ============================== */

    div.stButton > button {{
        background-color: {PRIMARY};
        color: white;
        border: none;
        border-radius: 12px;
        min-height: 52px;
        font-size: 16px;
        font-weight: 700;
        transition: 0.2s;
    }}

    div.stButton > button:hover {{
        background-color: #43572F;
        color: white;
        border: none;
    }}


    /* ==============================
       DIVIDER
       ============================== */

    hr {{
        border-color: #E4E5DD;
    }}


    /* ==============================
       INFO / WARNING
       ============================== */

    [data-testid="stAlert"] {{
        border-radius: 12px;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "current_screen" not in st.session_state:
    st.session_state.current_screen = "profile"

if "profile" not in st.session_state:
    st.session_state.profile = {}


# ============================================================
# BACKEND-READY PROFILE STORAGE
# ============================================================

def save_profile(profile_data):
    """
    Temporary frontend storage.

    Later this same structured object can be sent to:
    Python backend → API → database → decision engine.
    """
    st.session_state.profile = profile_data


# ============================================================
# FRAME 1 — PROFILE INPUT
# ============================================================

def render_profile():

    # --------------------------------------------------------
    # LANGUAGE SELECTOR
    # --------------------------------------------------------

    language_options = list(LANGUAGES.keys())

    current_language_name = (
        "English"
        if st.session_state.language == "en"
        else "മലയാളം"
    )

    selected_language = st.selectbox(
        "Language",
        language_options,
        index=language_options.index(current_language_name),
        label_visibility="collapsed",
        key="language_selector",
    )

    st.session_state.language = LANGUAGES[selected_language]

    # --------------------------------------------------------
    # BRAND
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🌾</div>
            <div class="brand-name">GramVyapar AI</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="tagline">{t("tagline")}</div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    st.markdown(
        f'<div class="progress-text">{t("step")}</div>',
        unsafe_allow_html=True,
    )

    st.progress(1 / 6)


    # --------------------------------------------------------
    # INTRO
    # --------------------------------------------------------

    st.markdown(
        f'<div class="intro-title">{t("intro_title")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="intro-description">{t("intro_description")}</div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # SKILLS
    # --------------------------------------------------------

    st.markdown(
        f'<div class="field-label">🛠️ {t("skills")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="field-description">{t("skills_desc")}</div>',
        unsafe_allow_html=True,
    )

    skill_options = [
        "Tailoring",
        "Cooking",
        "Carpentry",
        "Farming",
        "Dairy",
        "Poultry",
        "Repair",
        "Food Processing",
        "Other",
    ]

    skills = st.multiselect(
        "Skills",
        skill_options,
        placeholder=t("skills_placeholder"),
        label_visibility="collapsed",
        key="skills_selector",
    )

    st.markdown(
        f'<div class="custom-input">',
        unsafe_allow_html=True,
    )

    custom_skill = st.text_input(
        t("custom_skill"),
        placeholder=t("custom_skill_placeholder"),
        label_visibility="visible",
        key="custom_skill_input",
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # --------------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------------

    st.markdown(
        f'<div class="field-label">🧑‍🔧 {t("experience")}</div>',
        unsafe_allow_html=True,
    )

    experience = st.number_input(
        "Experience",
        min_value=0,
        max_value=50,
        value=0,
        step=1,
        label_visibility="collapsed",
        key="experience_input",
    )

    st.caption(t("experience_caption"))


    # --------------------------------------------------------
    # CAPITAL
    # --------------------------------------------------------

    st.markdown(
        f'<div class="field-label">💰 {t("capital")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="field-description">{t("capital_desc")}</div>',
        unsafe_allow_html=True,
    )

    capital = st.slider(
        "Capital",
        min_value=0,
        max_value=500000,
        value=100000,
        step=5000,
        format="₹%d",
        label_visibility="collapsed",
        key="capital_slider",
    )

    st.markdown(
        f"""
        <div style="
            font-size: 26px;
            font-weight: 750;
            color: {PRIMARY};
            margin-top: -5px;
        ">
            ₹{capital:,.0f}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(t("capital_caption"))


    # --------------------------------------------------------
    # BUSINESS INTERESTS
    # --------------------------------------------------------

    st.markdown(
        f'<div class="field-label">💡 {t("interests")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="field-description">{t("interests_desc")}</div>',
        unsafe_allow_html=True,
    )

    interest_options = [
        "Dairy",
        "Bakery",
        "Tailoring",
        "Grocery",
        "Poultry",
        "Food Processing",
        "Repair Services",
        "Other",
    ]

    interests = st.multiselect(
        "Interests",
        interest_options,
        placeholder=t("interests_placeholder"),
        label_visibility="collapsed",
        key="interests_selector",
    )

    custom_interest = st.text_input(
        t("custom_interest"),
        placeholder=t("custom_interest_placeholder"),
        label_visibility="visible",
        key="custom_interest_input",
    )


    # --------------------------------------------------------
    # RISK PREFERENCE
    # --------------------------------------------------------

    st.markdown(
        f'<div class="field-label">⚖️ {t("risk")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="field-description">{t("risk_desc")}</div>',
        unsafe_allow_html=True,
    )

    risk_options = [
        ("Low", t("low")),
        ("Medium", t("medium")),
        ("High", t("high")),
    ]

    risk_display = st.radio(
        "Risk",
        [item[1] for item in risk_options],
        index=1,
        horizontal=True,
        label_visibility="collapsed",
        key="risk_selector",
    )

    risk_lookup = {
        t("low"): "Low",
        t("medium"): "Medium",
        t("high"): "High",
    }

    risk = risk_lookup[risk_display]

    if risk == "Low":

        st.markdown(
            f"""
            <div class="risk-description">
                🟢 <b>{t("low")}</b> — {t("low_description")}
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif risk == "Medium":

        st.markdown(
            f"""
            <div class="risk-description">
                🟠 <b>{t("medium")}</b> — {t("medium_description")}
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            f"""
            <div class="risk-description">
                🔴 <b>{t("high")}</b> — {t("high_description")}
            </div>
            """,
            unsafe_allow_html=True,
        )


    # --------------------------------------------------------
    # EXISTING BUSINESS
    # --------------------------------------------------------

    st.markdown(
        f'<div class="field-label">🏪 {t("existing")}</div>',
        unsafe_allow_html=True,
    )

    existing_business = st.toggle(
        t("existing_toggle"),
        key="existing_business_toggle",
    )

    existing_details = ""

    if existing_business:

        existing_details = st.text_input(
            "Existing business",
            placeholder=t("existing_placeholder"),
            label_visibility="collapsed",
            key="existing_business_details",
        )


    # --------------------------------------------------------
    # CONTINUE
    # --------------------------------------------------------

    st.divider()

    if st.button(
        t("continue"),
        type="primary",
        use_container_width=True,
    ):

        final_skills = list(skills)

        if custom_skill.strip():
            final_skills.append(custom_skill.strip())

        final_interests = list(interests)

        if custom_interest.strip():
            final_interests.append(custom_interest.strip())

        profile_data = {
            "language": st.session_state.language,
            "skills": final_skills,
            "experience_years": experience,
            "available_capital": capital,
            "business_interests": final_interests,
            "risk_preference": risk,
            "existing_business": existing_business,
            "existing_business_details": existing_details,
        }

        save_profile(profile_data)

        st.session_state.current_screen = "local_dashboard"

        st.rerun()


# ============================================================
# FRAME 2 — TEMPORARY PLACEHOLDER
# ============================================================

def render_local_dashboard():

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🌾</div>
            <div class="brand-name">GramVyapar AI</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="tagline">{t("tagline")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="intro-title">{t("local_dashboard")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="intro-description">{t("local_description")}</div>',
        unsafe_allow_html=True,
    )

    st.info(t("local_info"))

    if st.button(t("back")):

        st.session_state.current_screen = "profile"

        st.rerun()


# ============================================================
# APPLICATION ROUTER
# ============================================================

def main():

    if st.session_state.current_screen == "profile":

        render_profile()

    elif st.session_state.current_screen == "local_dashboard":

        render_local_dashboard()


# ============================================================
# START APPLICATION
# ============================================================

main()
