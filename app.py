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
# COLORS
# =========================================================

PRIMARY = "#526A3A"
SECONDARY = "#7D9A55"
ACCENT = "#C88A3D"
BACKGROUND = "#FAF8F1"
TEXT = "#33352C"
WHITE = "#FFFFFF"
LIGHT_GREY = "#F0F1ED"
BORDER_GREY = "#B8BDB2"
MUTED = "#6C6F65"


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

        # Frame 1
        "step1": "Step 1 of 10",
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

        # Frame 2
        "step2": "Step 2 of 10",
        "dashboard": "Local Dashboard",
        "dashboard_subtitle": "Understand the local market before choosing a business.",
        "choose_location": "Choose your location",
        "location_help": "Select the area where you want to explore business opportunities.",
        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward",
        "data_coverage": "Data coverage",
        "demo_data": "DEMO DATA",
        "ward_level": "Ward-level data",
        "snapshot": "Local Market Snapshot",
        "business_density": "Business Density",
        "population": "Population",
        "seasonal_demand": "Seasonal Demand",
        "resources": "Resource Availability",
        "map_title": "Local Market Area",
        "map_subtitle": "Approximate 5–10 km market reach",
        "local_signals": "Local signals",
        "signal1": "Food and daily-use businesses show strong local activity.",
        "signal2": "Residential population supports recurring demand.",
        "signal3": "Seasonal demand varies around festivals and agricultural cycles.",
        "market_reach": "Market reach",
        "market_reach_value": "5–10 km",
        "source": "Source",
        "date": "Data date",
        "back": "← Back to Profile",
        "continue_opportunity": "Continue to Opportunities",

        "profile_received": "Profile received",
        "skills_display": "Skills",
        "experience_display": "Experience",
        "capital_display": "Available capital",
        "interests_display": "Business interests",
        "risk_display": "Risk preference",
        "existing_display": "Existing business",
        "business_details": "Business details",
        "yes": "Yes",
        "no": "No",
    },

    "ml": {
        "brand": "ഗ്രാംവ്യാപാർ AI",
        "tagline": "വായ്പ എടുക്കുന്നതിന് മുമ്പ് അറിയുക",

        # Frame 1
        "step1": "ഘട്ടം 1 / 10",
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

        # Frame 2
        "step2": "ഘട്ടം 2 / 10",
        "dashboard": "പ്രാദേശിക ഡാഷ്ബോർഡ്",
        "dashboard_subtitle": "ബിസിനസ് തിരഞ്ഞെടുക്കുന്നതിന് മുമ്പ് പ്രാദേശിക വിപണി മനസ്സിലാക്കുക.",
        "choose_location": "നിങ്ങളുടെ സ്ഥലം തിരഞ്ഞെടുക്കുക",
        "location_help": "ബിസിനസ് അവസരങ്ങൾ പരിശോധിക്കേണ്ട പ്രദേശം തിരഞ്ഞെടുക്കുക.",
        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ്",
        "data_coverage": "ഡാറ്റ ലഭ്യത",
        "demo_data": "ഡെമോ ഡാറ്റ",
        "ward_level": "വാർഡ് തല ഡാറ്റ",
        "snapshot": "പ്രാദേശിക വിപണി സ്ഥിതിവിവരം",
        "business_density": "ബിസിനസ് സാന്ദ്രത",
        "population": "ജനസംഖ്യ",
        "seasonal_demand": "സീസണൽ ഡിമാൻഡ്",
        "resources": "വിഭവ ലഭ്യത",
        "map_title": "പ്രാദേശിക വിപണി മേഖല",
        "map_subtitle": "ഏകദേശം 5–10 കി.മീ വിപണി പരിധി",
        "local_signals": "പ്രാദേശിക സൂചനകൾ",
        "signal1": "ഭക്ഷണം, ദൈനംദിന ആവശ്യങ്ങൾ എന്നിവയുമായി ബന്ധപ്പെട്ട ബിസിനസുകളിൽ ശക്തമായ പ്രവർത്തനം കാണുന്നു.",
        "signal2": "താമസക്കാരുടെ എണ്ണം സ്ഥിരമായ ഡിമാൻഡിന് പിന്തുണ നൽകുന്നു.",
        "signal3": "ഉത്സവങ്ങളും കാർഷിക സീസണുകളും അനുസരിച്ച് ഡിമാൻഡ് മാറുന്നു.",
        "market_reach": "വിപണി പരിധി",
        "market_reach_value": "5–10 കി.മീ",
        "source": "ഉറവിടം",
        "date": "ഡാറ്റ തീയതി",
        "back": "← പ്രൊഫൈലിലേക്ക് മടങ്ങുക",
        "continue_opportunity": "അവസരങ്ങളിലേക്ക് തുടരുക",

        "profile_received": "പ്രൊഫൈൽ ലഭിച്ചു",
        "skills_display": "കഴിവുകൾ",
        "experience_display": "പരിചയം",
        "capital_display": "ലഭ്യമായ മൂലധനം",
        "interests_display": "ബിസിനസ് താൽപര്യങ്ങൾ",
        "risk_display": "റിസ്ക് മുൻഗണന",
        "existing_display": "നിലവിലുള്ള ബിസിനസ്",
        "business_details": "ബിസിനസ് വിശദാംശങ്ങൾ",
        "yes": "ഉണ്ട്",
        "no": "ഇല്ല",
    },
}


def t(key):
    language = st.session_state.get("language", "en")
    return TEXTS[language].get(key, key)


# =========================================================
# SESSION STATE
# =========================================================

if "language" not in st.session_state:
    st.session_state.language = "en"

if "page" not in st.session_state:
    st.session_state.page = 1

if "profile" not in st.session_state:
    st.session_state.profile = {}

if "existing_business" not in st.session_state:
    st.session_state.existing_business = False

if "district" not in st.session_state:
    st.session_state.district = "Ernakulam"

if "local_body" not in st.session_state:
    st.session_state.local_body = "Kochi Municipal Corporation"

if "ward" not in st.session_state:
    st.session_state.ward = "Ward 42"


# =========================================================
# CSS
# =========================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {BACKGROUND};
    }}

    .block-container {{
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
    }}

    p {{
        color: {TEXT};
    }}

    /* Header */

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

    /* Progress */

    .progress-container {{
        width: 100%;
        height: 7px;
        background-color: #E5E8DD;
        border-radius: 10px;
        margin: 25px 0 35px 0;
        overflow: hidden;
    }}

    .progress-bar {{
        height: 100%;
        background-color: {PRIMARY};
        border-radius: 10px;
    }}

    .progress-10 {{
        width: 10%;
    }}

    .progress-20 {{
        width: 20%;
    }}

    .step-text {{
        color: {SECONDARY};
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 8px;
    }}

    .intro-title {{
        font-size: 34px;
        font-weight: 800;
        color: {TEXT};
        margin-bottom: 8px;
    }}

    .intro-subtitle {{
        font-size: 16px;
        color: {MUTED};
        margin-bottom: 30px;
    }}

    .field-label {{
        font-size: 16px;
        font-weight: 700;
        color: {TEXT};
        margin-top: 15px;
        margin-bottom: 8px;
    }}

    /* Inputs */

    div[data-baseweb="select"] {{
        background-color: {WHITE} !important;
        border-radius: 12px !important;
        border: 1px solid #D8DCCF !important;
    }}

    div[data-baseweb="select"] * {{
        color: {TEXT} !important;
        -webkit-text-fill-color: {TEXT} !important;
    }}

    div[data-baseweb="tag"] {{
        background-color: {PRIMARY} !important;
        border-radius: 8px !important;
    }}

    div[data-baseweb="tag"] span {{
        color: {WHITE} !important;
    }}

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextInputRootElement"] input {{
        background-color: {PRIMARY} !important;
        color: {WHITE} !important;
        -webkit-text-fill-color: {WHITE} !important;
        caret-color: {WHITE} !important;
        border: 1px solid {PRIMARY} !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }}

    div[data-testid="stTextInput"] input::placeholder,
    div[data-testid="stTextInputRootElement"] input::placeholder {{
        color: #E8EDE1 !important;
        -webkit-text-fill-color: #E8EDE1 !important;
        opacity: 1 !important;
    }}

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

    /* Risk cards */

    .risk-card {{
        background-color: {WHITE};
        border: 1px solid #E1E4D9;
        border-radius: 14px;
        padding: 15px;
        min-height: 85px;
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

    /* Existing business */

    div[data-testid="stCheckbox"] {{
        background-color: {LIGHT_GREY} !important;
        border: 2px solid {BORDER_GREY} !important;
        border-radius: 14px !important;
        padding: 12px 16px !important;
    }}

    div[data-testid="stCheckbox"] label {{
        color: {TEXT} !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }}

    div[data-testid="stCheckbox"] label p {{
        color: {TEXT} !important;
        font-weight: 700 !important;
    }}

    /* Buttons */

    div.stButton > button {{
        background-color: {PRIMARY} !important;
        color: {WHITE} !important;
        border: none !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        padding: 12px 20px !important;
        min-height: 48px !important;
    }}

    div.stButton > button:hover {{
        background-color: {SECONDARY} !important;
        color: {WHITE} !important;
    }}

    /* =====================================================
       FRAME 2
       ===================================================== */

    .location-card {{
        background-color: {WHITE};
        border: 1px solid #E1E4D9;
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 25px;
    }}

    .section-title {{
        font-size: 20px;
        font-weight: 800;
        color: {TEXT};
        margin-bottom: 5px;
    }}

    .section-help {{
        font-size: 14px;
        color: {MUTED};
        margin-bottom: 20px;
    }}

    .coverage-box {{
        background-color: {LIGHT_GREY};
        border: 1px solid {BORDER_GREY};
        border-radius: 12px;
        padding: 12px 16px;
        margin-top: 18px;
    }}

    .coverage-title {{
        font-size: 13px;
        font-weight: 700;
        color: {MUTED};
    }}

    .coverage-value {{
        font-size: 14px;
        font-weight: 800;
        color: {PRIMARY};
        margin-top: 3px;
    }}

    .demo-label {{
        background-color: #FFF1DD;
        border: 1px solid #E8C994;
        color: #9A641D;
        border-radius: 20px;
        padding: 4px 10px;
        font-size: 11px;
        font-weight: 800;
        display: inline-block;
        margin-left: 8px;
    }}

    .metric-card {{
        background-color: {WHITE};
        border: 1px solid #E1E4D9;
        border-radius: 16px;
        padding: 20px;
        min-height: 150px;
    }}

    .metric-title {{
        font-size: 14px;
        font-weight: 700;
        color: {MUTED};
        margin-bottom: 12px;
    }}

    .metric-value {{
        font-size: 27px;
        font-weight: 800;
        color: {TEXT};
        margin-bottom: 12px;
    }}

    .metric-source {{
        font-size: 11px;
        color: #85887F;
        line-height: 1.5;
    }}

    .map-box {{
        background-color: #EEF0E9;
        border: 1px solid #D7DCCF;
        border-radius: 18px;
        padding: 25px;
        min-height: 310px;
        text-align: center;
    }}

    .map-icon {{
        font-size: 60px;
        margin-top: 70px;
    }}

    .map-heading {{
        font-size: 20px;
        font-weight: 800;
        color: {TEXT};
    }}

    .map-text {{
        font-size: 14px;
        color: {MUTED};
    }}

    .map-area {{
        margin: 25px auto 0 auto;
        max-width: 300px;
        background-color: #E1E6DA;
        border: 2px dashed {SECONDARY};
        border-radius: 100px;
        padding: 20px;
        color: {PRIMARY};
        font-weight: 800;
    }}

    .signal-box {{
        background-color: {WHITE};
        border: 1px solid #E1E4D9;
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 10px;
    }}

    .signal-text {{
        font-size: 14px;
        color: {TEXT};
        line-height: 1.5;
    }}

    .reach-card {{
        background-color: {WHITE};
        border: 1px solid #E1E4D9;
        border-radius: 14px;
        padding: 18px;
        margin-top: 15px;
    }}

    .reach-title {{
        font-size: 13px;
        font-weight: 700;
        color: {MUTED};
    }}

    .reach-value {{
        font-size: 25px;
        font-weight: 800;
        color: {TEXT};
        margin-top: 5px;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


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
# FRAME 1
# =========================================================

def render_profile():

    render_header()

    st.markdown(
        """
        <div class="progress-container">
            <div class="progress-bar progress-10"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="step-text">{t("step1")}</div>',
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

    # Skills

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

    # Experience

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

    # Capital

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

    # Interests

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

    # Risk

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

    risk_col1, risk_col2, risk_col3 = st.columns(3)

    with risk_col1:
        st.markdown(
            f"""
            <div class="risk-card">
                <div class="risk-title">🟢 {t("low")}</div>
                <div class="risk-description">{t("low_desc")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with risk_col2:
        st.markdown(
            f"""
            <div class="risk-card">
                <div class="risk-title">🟠 {t("medium")}</div>
                <div class="risk-description">{t("medium_desc")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with risk_col3:
        st.markdown(
            f"""
            <div class="risk-card">
                <div class="risk-title">🔴 {t("high")}</div>
                <div class="risk-description">{t("high_desc")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Existing business

    existing_business = st.checkbox(
        t("existing"),
        value=st.session_state.existing_business,
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

    st.markdown("<br>", unsafe_allow_html=True)

    button_col1, button_col2, button_col3 = st.columns([5, 2, 5])

    with button_col2:

        if st.button(
            t("continue"),
            use_container_width=True,
        ):

            save_profile(
                skills,
                custom_skill,
                experience,
                capital,
                interests,
                custom_interest,
                risk,
                existing_business,
                existing_details,
            )

            st.rerun()


# =========================================================
# FRAME 2
# =========================================================

def render_local_dashboard():

    render_header()

    # Progress

    st.markdown(
        """
        <div class="progress-container">
            <div class="progress-bar progress-20"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="step-text">{t("step2")}</div>',
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

    # =====================================================
    # LOCATION
    # =====================================================

    st.markdown(
        f"""
        <div class="location-card">

            <div class="section-title">
                {t("choose_location")}
            </div>

            <div class="section-help">
                {t("location_help")}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    # District

    with col1:

        st.markdown(
            f'<div class="field-label">{t("district")}</div>',
            unsafe_allow_html=True,
        )

        district = st.selectbox(
            t("district"),
            [
                "Ernakulam",
                "Kozhikode",
                "Thrissur",
                "Malappuram",
                "Kannur",
            ],
            key="district",
            label_visibility="collapsed",
        )

    # Local body

    local_bodies = {

        "Ernakulam": [
            "Kochi Municipal Corporation",
            "Aluva Municipality",
            "Perumbavoor Municipality",
        ],

        "Kozhikode": [
            "Kozhikode Municipal Corporation",
            "Vadakara Municipality",
            "Koyilandy Municipality",
        ],

        "Thrissur": [
            "Thrissur Municipal Corporation",
            "Chalakudy Municipality",
            "Kodungallur Municipality",
        ],

        "Malappuram": [
            "Manjeri Municipality",
            "Tirur Municipality",
            "Perinthalmanna Municipality",
        ],

        "Kannur": [
            "Kannur Municipal Corporation",
            "Thalassery Municipality",
            "Payyannur Municipality",
        ],
    }

    with col2:

        st.markdown(
            f'<div class="field-label">{t("local_body")}</div>',
            unsafe_allow_html=True,
        )

        local_body = st.selectbox(
            t("local_body"),
            local_bodies[district],
            key="local_body",
            label_visibility="collapsed",
        )

    # Ward

    with col3:

        st.markdown(
            f'<div class="field-label">{t("ward")}</div>',
            unsafe_allow_html=True,
        )

        ward = st.selectbox(
            t("ward"),
            [
                "Ward 12",
                "Ward 24",
                "Ward 35",
                "Ward 42",
                "Ward 51",
            ],
            key="ward",
            label_visibility="collapsed",
        )

    # Save structured location

    st.session_state.location = {
        "district": district,
        "local_body": local_body,
        "ward": ward,
    }

    # Coverage

    st.markdown(
        f"""
        <div class="coverage-box">

            <div class="coverage-title">
                {t("data_coverage")}

                <span class="demo-label">
                    {t("demo_data")}
                </span>
            </div>

            <div class="coverage-value">
                ✓ {t("ward_level")}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # SNAPSHOT
    # =====================================================

    st.markdown(
        f'<div class="section-title">{t("snapshot")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)

    with m1:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("business_density")}
                </div>

                <div class="metric-value">
                    128 businesses
                </div>

                <div class="metric-source">
                    {t("source")}: Demo local dataset<br>
                    {t("date")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with m2:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("population")}
                </div>

                <div class="metric-value">
                    4,820 people
                </div>

                <div class="metric-source">
                    {t("source")}: Demo demographic dataset<br>
                    {t("date")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with m3:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("seasonal_demand")}
                </div>

                <div class="metric-value">
                    High
                </div>

                <div class="metric-source">
                    {t("source")}: Demo seasonal model<br>
                    {t("date")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with m4:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("resources")}
                </div>

                <div class="metric-value">
                    Good
                </div>

                <div class="metric-source">
                    {t("source")}: Demo resource dataset<br>
                    {t("date")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # MAP + SIGNALS
    # =====================================================

    map_col, signal_col = st.columns([1.35, 1])

    # Map

    with map_col:

        st.markdown(
            f"""
            <div class="map-box">

                <div class="map-heading">
                    {t("map_title")}
                </div>

                <div class="map-text">
                    {t("map_subtitle")}
                </div>

                <div class="map-icon">
                    📍
                </div>

                <div class="map-area">
                    {district} · {ward}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    # Signals

    with signal_col:

        st.markdown(
            f'<div class="section-title">{t("local_signals")}</div>',
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        signals = [
            t("signal1"),
            t("signal2"),
            t("signal3"),
        ]

        for signal in signals:

            st.markdown(
                f"""
                <div class="signal-box">
                    <div class="signal-text">
                        <b style="color:{PRIMARY};">●</b>
                        {signal}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="reach-card">

                <div class="reach-title">
                    {t("market_reach")}
                </div>

                <div class="reach-value">
                    {t("market_reach_value")}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    # =====================================================
    # NAVIGATION
    # =====================================================

    st.markdown("---")

    nav1, nav2, nav3 = st.columns([3, 4, 3])

    with nav1:

        if st.button(
            t("back"),
            use_container_width=True,
        ):

            st.session_state.page = 1
            st.rerun()

    with nav3:

        if st.button(
            t("continue_opportunity"),
            use_container_width=True,
        ):

            st.session_state.page = 3
            st.rerun()


# =========================================================
# FRAME 3 PLACEHOLDER
# =========================================================

def render_opportunity_placeholder():

    render_header()

    st.markdown(
        """
        <div class="progress-container">
            <div class="progress-bar" style="width:30%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="step-text">Step 3 of 10</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="intro-title">Opportunity Radar</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="intro-subtitle">
            This is where GramVyapar AI will rank the best business
            opportunities for the user.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info("Frame 3 will be built next.")

    if st.button(t("back")):

        st.session_state.page = 2
        st.rerun()


# =========================================================
# APP ROUTER
# =========================================================

if st.session_state.page == 1:

    render_profile()

elif st.session_state.page == 2:

    render_local_dashboard()

elif st.session_state.page == 3:

    render_opportunity_placeholder()
