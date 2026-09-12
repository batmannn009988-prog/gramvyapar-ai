import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# COLOR PALETTE
# =========================================================

PRIMARY = "#526A3A"
SECONDARY = "#7D9A55"
ACCENT = "#C88A3D"
BACKGROUND = "#FAF8F1"
TEXT = "#33352C"
WHITE = "#FFFFFF"

# =========================================================
# LANGUAGE
# =========================================================

LANGUAGES = {
    "English": "en",
    "മലയാളം": "ml",
}

TEXTS = {
    "en": {
        "brand": "GramVyapar AI",
        "tagline": "Know Before You Borrow",
        "step": "Step 1 of 10",
        "title": "Tell us about yourself",
        "subtitle": "Help us understand your skills, capital and business interests.",
        "skills": "Skills",
        "select_skills": "Select your skills",
        "custom_skill": "Add a custom skill",
        "custom_skill_placeholder": "Example: Mobile repair",
        "experience": "Years of experience",
        "capital": "Available capital",
        "interests": "Business interests",
        "select_interests": "Select your interests",
        "custom_interest": "Add a custom business interest",
        "custom_interest_placeholder": "Example: Fresh juice shop",
        "risk": "Risk preference",
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "low_desc": "Prefer safer and more predictable businesses",
        "medium_desc": "Comfortable with moderate uncertainty",
        "high_desc": "Open to higher risk for higher potential",
        "existing": "I already have a business",
        "existing_placeholder": "Example: Small tailoring shop",
        "continue": "Continue",
        "profile_saved": "Profile saved successfully.",
        "dashboard": "Local Dashboard",
        "dashboard_subtitle": "Your local business intelligence will appear here.",
    },

    "ml": {
        "brand": "ഗ്രാംവ്യാപാർ AI",
        "tagline": "വായ്പ എടുക്കുന്നതിന് മുമ്പ് അറിയുക",
        "step": "ഘട്ടം 1 / 10",
        "title": "നിങ്ങളെക്കുറിച്ച് പറയൂ",
        "subtitle": "നിങ്ങളുടെ കഴിവുകൾ, മൂലധനം, ബിസിനസ് താൽപര്യങ്ങൾ എന്നിവ മനസ്സിലാക്കാൻ സഹായിക്കൂ.",
        "skills": "കഴിവുകൾ",
        "select_skills": "നിങ്ങളുടെ കഴിവുകൾ തിരഞ്ഞെടുക്കുക",
        "custom_skill": "മറ്റൊരു കഴിവ് ചേർക്കുക",
        "custom_skill_placeholder": "ഉദാഹരണം: മൊബൈൽ റിപ്പയർ",
        "experience": "പരിചയമുള്ള വർഷങ്ങൾ",
        "capital": "ലഭ്യമായ മൂലധനം",
        "interests": "ബിസിനസ് താൽപര്യങ്ങൾ",
        "select_interests": "താൽപര്യങ്ങൾ തിരഞ്ഞെടുക്കുക",
        "custom_interest": "മറ്റൊരു ബിസിനസ് താൽപര്യം ചേർക്കുക",
        "custom_interest_placeholder": "ഉദാഹരണം: ഫ്രഷ് ജ്യൂസ് കട",
        "risk": "റിസ്ക് മുൻഗണന",
        "low": "കുറവ്",
        "medium": "ഇടത്തരം",
        "high": "കൂടുതൽ",
        "low_desc": "കൂടുതൽ സുരക്ഷിതവും സ്ഥിരതയുള്ളതുമായ ബിസിനസുകൾ",
        "medium_desc": "മിതമായ അനിശ്ചിതത്വം സ്വീകരിക്കാൻ തയ്യാറാണ്",
        "high_desc": "കൂടുതൽ സാധ്യതയ്ക്കായി കൂടുതൽ റിസ്ക് സ്വീകരിക്കാൻ തയ്യാറാണ്",
        "existing": "എനിക്ക് ഇതിനകം ഒരു ബിസിനസ് ഉണ്ട്",
        "existing_placeholder": "ഉദാഹരണം: ചെറിയ തയ്യൽക്കട",
        "continue": "തുടരുക",
        "profile_saved": "പ്രൊഫൈൽ വിജയകരമായി സേവ് ചെയ്തു.",
        "dashboard": "പ്രാദേശിക ഡാഷ്ബോർഡ്",
        "dashboard_subtitle": "നിങ്ങളുടെ പ്രാദേശിക ബിസിനസ് വിവരങ്ങൾ ഇവിടെ കാണിക്കും.",
    },
}


def t(key):
    """Return translated text."""
    language = st.session_state.get("language", "en")
    return TEXTS[language].get(key, key)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>

    /* =====================================================
       MAIN APP
       ===================================================== */

    .stApp {{
        background-color: {BACKGROUND};
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    /* =====================================================
       GENERAL TEXT
       ===================================================== */

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
    }}

    p {{
        color: {TEXT};
    }}

    /* =====================================================
       BRAND
       ===================================================== */

    .brand {{
        font-size: 28px;
        font-weight: 800;
        color: {PRIMARY};
        margin-bottom: 2px;
    }}

    .tagline {{
        font-size: 14px;
        color: {SECONDARY};
        font-weight: 500;
    }}

    /* =====================================================
       TOP LANGUAGE SELECTOR
       ===================================================== */

    div[data-testid="stSelectbox"] {{
        margin-top: 0px;
    }}

    div[data-testid="stSelectbox"] > div {{
        background-color: {WHITE} !important;
    }}

    div[data-baseweb="select"] {{
        background-color: {WHITE} !important;
        border-radius: 12px !important;
        border: 1px solid #D8DCCF !important;
    }}

    div[data-baseweb="select"] * {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    div[data-baseweb="select"] input {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
        background-color: {WHITE} !important;
    }}

    /* Dropdown selected value */
    div[data-baseweb="select"] [role="button"] {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    /* =====================================================
       PROGRESS
       ===================================================== */

    .progress-container {{
        width: 100%;
        height: 7px;
        background-color: #E5E8DD;
        border-radius: 10px;
        margin: 25px 0 35px 0;
        overflow: hidden;
    }}

    .progress-bar {{
        width: 10%;
        height: 100%;
        background-color: {PRIMARY};
        border-radius: 10px;
    }}

    .step-text {{
        color: {SECONDARY};
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 8px;
    }}

    /* =====================================================
       INTRO
       ===================================================== */

    .intro-title {{
        font-size: 34px;
        font-weight: 800;
        color: {TEXT};
        margin-bottom: 8px;
    }}

    .intro-subtitle {{
        font-size: 16px;
        color: #6C6F65;
        margin-bottom: 30px;
    }}

    /* =====================================================
       FIELD LABELS
       ===================================================== */

    .field-label {{
        font-size: 16px;
        font-weight: 700;
        color: {TEXT};
        margin-top: 15px;
        margin-bottom: 8px;
    }}

    /* =====================================================
       MULTISELECT
       ===================================================== */

    div[data-baseweb="select"] {{
        border-radius: 12px !important;
    }}

    div[data-baseweb="tag"] {{
        background-color: {PRIMARY} !important;
        border-radius: 8px !important;
    }}

    div[data-baseweb="tag"] span {{
        color: {WHITE} !important;
    }}

    /* =====================================================
       NORMAL TEXT INPUTS
       ===================================================== */

    /*
       This fixes:
       - Custom skill
       - Custom business interest
       - Existing business
    */

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextInputRootElement"] input,
    div[data-testid="stTextInput"] input[type="text"],
    div[data-testid="stTextInputRootElement"] input[type="text"] {{
        background-color: {PRIMARY} !important;
        color: {WHITE} !important;
        -webkit-text-fill-color: {WHITE} !important;
        caret-color: {WHITE} !important;

        border: 1px solid {PRIMARY} !important;
        border-radius: 12px !important;

        font-size: 16px !important;
        font-weight: 600 !important;
    }}

    /* Placeholder */
    div[data-testid="stTextInput"] input::placeholder,
    div[data-testid="stTextInputRootElement"] input::placeholder {{
        color: #E8EDE1 !important;
        -webkit-text-fill-color: #E8EDE1 !important;
        opacity: 1 !important;
    }}

    /* When clicked/focused */
    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextInputRootElement"] input:focus {{
        background-color: {PRIMARY} !important;
        color: {WHITE} !important;
        -webkit-text-fill-color: {WHITE} !important;
        border-color: {SECONDARY} !important;
        caret-color: {WHITE} !important;
        box-shadow: 0 0 0 1px {SECONDARY} !important;
    }}

    /* =====================================================
       NUMBER INPUT
       ===================================================== */

    div[data-testid="stNumberInput"] input {{
        background-color: {PRIMARY} !important;
        color: {WHITE} !important;
        -webkit-text-fill-color: {WHITE} !important;
        caret-color: {WHITE} !important;

        border: 1px solid {PRIMARY} !important;
        border-radius: 12px !important;

        font-size: 16px !important;
        font-weight: 600 !important;
    }}

    div[data-testid="stNumberInput"] input:focus {{
        background-color: {PRIMARY} !important;
        color: {WHITE} !important;
        -webkit-text-fill-color: {WHITE} !important;
        border-color: {SECONDARY} !important;
    }}

    /* Number input buttons */
    div[data-testid="stNumberInput"] button {{
        color: {PRIMARY} !important;
    }}

    /* =====================================================
       SLIDER
       ===================================================== */

    div[data-testid="stSlider"] {{
        padding-top: 5px;
    }}

    div[data-testid="stSlider"] p {{
        color: {TEXT} !important;
    }}

    /* =====================================================
       RISK DESCRIPTION CARDS
       ===================================================== */

    .risk-card {{
        background-color: {WHITE};
        border: 1px solid #E1E4D9;
        border-radius: 14px;
        padding: 15px;
        min-height: 85px;
        margin-top: 5px;
    }}

    .risk-title {{
        font-size: 16px;
        font-weight: 700;
        color: {TEXT};
        margin-bottom: 5px;
    }}

    .risk-description {{
        font-size: 13px;
        color: #70736A;
        line-height: 1.4;
    }}

    /* =====================================================
       RADIO BUTTON
       ===================================================== */

    div[data-testid="stRadio"] label {{
        color: {TEXT} !important;
    }}

    /* =====================================================
       TOGGLE
       ===================================================== */

    div[data-testid="stToggle"] label {{
        color: {TEXT} !important;
        font-weight: 600 !important;
    }}

    /* =====================================================
       BUTTON
       ===================================================== */

    div.stButton > button {{
        background-color: {PRIMARY} !important;
        color: {WHITE} !important;
        border: none !important;
        border-radius: 12px !important;

        font-size: 16px !important;
        font-weight: 700 !important;

        padding: 12px 28px !important;
        min-height: 48px !important;
    }}

    div.stButton > button:hover {{
        background-color: {SECONDARY} !important;
        color: {WHITE} !important;
    }}

    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {{
        border: none !important;
        border-top: 1px solid #E1E4D9 !important;
        margin: 30px 0 !important;
    }}

    /* =====================================================
       SUCCESS MESSAGE
       ===================================================== */

    div[data-testid="stAlert"] {{
        border-radius: 12px !important;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "language" not in st.session_state:
    st.session_state.language = "en"

if "page" not in st.session_state:
    st.session_state.page = 1

if "profile" not in st.session_state:
    st.session_state.profile = {}


# =========================================================
# SAVE PROFILE
# =========================================================

def save_profile(
    skills,
    custom_skill,
    experience,
    capital,
    interests,
    custom_interest,
    risk,
    existing_business,
    existing_details,
):

    final_skills = list(skills)

    if custom_skill.strip():
        final_skills.append(custom_skill.strip())

    final_interests = list(interests)

    if custom_interest.strip():
        final_interests.append(custom_interest.strip())

    st.session_state.profile = {
        "skills": final_skills,
        "experience_years": experience,
        "available_capital": capital,
        "business_interests": final_interests,
        "risk_preference": risk,
        "existing_business": existing_business,
        "existing_business_details": existing_details.strip(),
    }

    st.session_state.page = 2


# =========================================================
# HEADER
# =========================================================

def render_header():

    col1, col2 = st.columns([7, 2])

    with col1:
        st.markdown(
            f"""
            <div class="brand">{t("brand")}</div>
            <div class="tagline">{t("tagline")}</div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

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

        new_language = LANGUAGES[selected_language]

        if new_language != st.session_state.language:
            st.session_state.language = new_language
            st.rerun()


# =========================================================
# FRAME 1 — PROFILE INPUT
# =========================================================

def render_profile():

    render_header()

    st.markdown(
        """
        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="step-text">{t("step")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="intro-title">{t("title")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="intro-subtitle">{t("subtitle")}</div>',
        unsafe_allow_html=True,
    )

    # =====================================================
    # SKILLS
    # =====================================================

    st.markdown(
        f'<div class="field-label">{t("skills")}</div>',
        unsafe_allow_html=True,
    )

    skills = st.multiselect(
        "Skills",
        [
            "Tailoring",
            "Cooking",
            "Carpentry",
            "Farming",
            "Dairy",
            "Poultry",
            "Repair",
            "Food Processing",
            "Other",
        ],
        placeholder=t("select_skills"),
        label_visibility="collapsed",
        key="skills",
    )

    custom_skill = st.text_input(
        t("custom_skill"),
        placeholder=t("custom_skill_placeholder"),
        label_visibility="collapsed",
        key="custom_skill",
    )

    # =====================================================
    # EXPERIENCE
    # =====================================================

    st.markdown(
        f'<div class="field-label">{t("experience")}</div>',
        unsafe_allow_html=True,
    )

    experience = st.number_input(
        t("experience"),
        min_value=0,
        max_value=50,
        value=0,
        step=1,
        label_visibility="collapsed",
        key="experience",
    )

    # =====================================================
    # CAPITAL
    # =====================================================

    st.markdown(
        f'<div class="field-label">{t("capital")}</div>',
        unsafe_allow_html=True,
    )

    capital = st.slider(
        t("capital"),
        min_value=0,
        max_value=500000,
        value=50000,
        step=5000,
        format="₹%d",
        label_visibility="collapsed",
        key="capital",
    )

    # =====================================================
    # BUSINESS INTERESTS
    # =====================================================

    st.markdown(
        f'<div class="field-label">{t("interests")}</div>',
        unsafe_allow_html=True,
    )

    interests = st.multiselect(
        "Business Interests",
        [
            "Dairy",
            "Bakery",
            "Tailoring",
            "Grocery",
            "Poultry",
            "Food Processing",
            "Repair Services",
            "Other",
        ],
        placeholder=t("select_interests"),
        label_visibility="collapsed",
        key="interests",
    )

    custom_interest = st.text_input(
        t("custom_interest"),
        placeholder=t("custom_interest_placeholder"),
        label_visibility="collapsed",
        key="custom_interest",
    )

    # =====================================================
    # RISK PREFERENCE
    # =====================================================

    st.markdown(
        f'<div class="field-label">{t("risk")}</div>',
        unsafe_allow_html=True,
    )

    risk = st.radio(
        "Risk",
        [
            t("low"),
            t("medium"),
            t("high"),
        ],
        index=1,
        horizontal=True,
        label_visibility="collapsed",
        key="risk",
    )

    # Risk descriptions

    risk_col1, risk_col2, risk_col3 = st.columns(3)

    with risk_col1:
        st.markdown(
            f"""
            <div class="risk-card">
                <div class="risk-title">🟢 {t("low")}</div>
                <div class="risk-description">
                    {t("low_desc")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with risk_col2:
        st.markdown(
            f"""
            <div class="risk-card">
                <div class="risk-title">🟠 {t("medium")}</div>
                <div class="risk-description">
                    {t("medium_desc")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with risk_col3:
        st.markdown(
            f"""
            <div class="risk-card">
                <div class="risk-title">🔴 {t("high")}</div>
                <div class="risk-description">
                    {t("high_desc")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================================
    # EXISTING BUSINESS
    # =====================================================

    st.markdown("---")

    existing_business = st.toggle(
        t("existing"),
        value=False,
        key="existing_business",
    )

    existing_details = ""

    if existing_business:

        existing_details = st.text_input(
            "Existing business",
            placeholder=t("existing_placeholder"),
            label_visibility="collapsed",
            key="existing_details",
        )

    # =====================================================
    # CONTINUE
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    button_col1, button_col2, button_col3 = st.columns([5, 2, 5])

    with button_col2:

        if st.button(
            t("continue"),
            use_container_width=True,
        ):

            save_profile(
                skills=skills,
                custom_skill=custom_skill,
                experience=experience,
                capital=capital,
                interests=interests,
                custom_interest=custom_interest,
                risk=risk,
                existing_business=existing_business,
                existing_details=existing_details,
            )

            st.rerun()


# =========================================================
# FRAME 2 — LOCAL DASHBOARD
# =========================================================

def render_local_dashboard():

    render_header()

    st.markdown(
        """
        <div class="progress-container">
            <div class="progress-bar" style="width:20%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="step-text">Step 2 of 10</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="intro-title">{t("dashboard")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="intro-subtitle">{t("dashboard_subtitle")}</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "Frame 2 will contain the Kerala local market dashboard."
    )

    # Temporary profile display for testing

    if st.session_state.profile:

        st.markdown("### Profile received")

        profile = st.session_state.profile

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Skills:**", ", ".join(profile["skills"]))
            st.write(
                "**Experience:**",
                profile["experience_years"],
                "years",
            )
            st.write(
                "**Available capital:**",
                f'₹{profile["available_capital"]:,}',
            )

        with col2:
            st.write(
                "**Business interests:**",
                ", ".join(profile["business_interests"]),
            )
            st.write(
                "**Risk preference:**",
                profile["risk_preference"],
            )
            st.write(
                "**Existing business:**",
                "Yes" if profile["existing_business"] else "No",
            )

            if profile["existing_business_details"]:
                st.write(
                    "**Business details:**",
                    profile["existing_business_details"],
                )


# =========================================================
# ROUTER
# =========================================================

if st.session_state.page == 1:
    render_profile()

elif st.session_state.page == 2:
    render_local_dashboard()
