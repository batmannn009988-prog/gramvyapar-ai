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
# DESIGN SYSTEM
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
LIGHT_BORDER = "#E1E4D9"


# =========================================================
# LANGUAGES
# =========================================================

LANGUAGES = {
    "English": "en",
    "മലയാളം": "ml",
}


TEXTS = {

    "en": {

        # ---------- GLOBAL ----------
        "brand": "GramVyapar AI",
        "tagline": "Know Before You Borrow",

        # ---------- FRAME 1 ----------
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
        "back": "← Back to Profile",

        # ---------- FRAME 2 ----------
        "step2": "Step 2 of 10",
        "dashboard": "Local Dashboard",
        "dashboard_subtitle": "Understand the local market before choosing a business.",

        "location": "Choose your location",

        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward",

        "coverage": "Data coverage",
        "ward_level": "Ward-level data",
        "district_fallback": "District fallback",

        "demo_data": "DEMO DATA",

        "local_market": "Local Market Snapshot",

        "business_density": "Business Density",
        "population": "Population",
        "seasonal_demand": "Seasonal Demand",
        "resources": "Resource Availability",

        "business_density_value": "128 businesses",
        "population_value": "4,820 people",
        "seasonal_demand_value": "High",
        "resources_value": "Good",

        "source": "Source",
        "updated": "Data date",

        "map_title": "Local Market Area",
        "map_subtitle": "Approximate 5–10 km market reach",

        "market_radius": "Market reach",
        "market_radius_value": "5–10 km",

        "local_signals": "Local signals",
        "signal1": "Food and daily-use businesses show strong local activity.",
        "signal2": "Residential population supports recurring demand.",
        "signal3": "Seasonal demand varies around festivals and agricultural cycles.",

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

        # ---------- GLOBAL ----------
        "brand": "ഗ്രാംവ്യാപാർ AI",
        "tagline": "വായ്പ എടുക്കുന്നതിന് മുമ്പ് അറിയുക",

        # ---------- FRAME 1 ----------
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
        "back": "← പ്രൊഫൈലിലേക്ക് മടങ്ങുക",

        # ---------- FRAME 2 ----------
        "step2": "ഘട്ടം 2 / 10",
        "dashboard": "പ്രാദേശിക ഡാഷ്ബോർഡ്",
        "dashboard_subtitle": "ബിസിനസ് തിരഞ്ഞെടുക്കുന്നതിന് മുമ്പ് പ്രാദേശിക വിപണി മനസ്സിലാക്കുക.",

        "location": "നിങ്ങളുടെ സ്ഥലം തിരഞ്ഞെടുക്കുക",

        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ്",

        "coverage": "ഡാറ്റ ലഭ്യത",
        "ward_level": "വാർഡ് തല ഡാറ്റ",
        "district_fallback": "ജില്ലാ തല ഡാറ്റ",

        "demo_data": "ഡെമോ ഡാറ്റ",

        "local_market": "പ്രാദേശിക വിപണി സ്ഥിതിവിവരം",

        "business_density": "ബിസിനസ് സാന്ദ്രത",
        "population": "ജനസംഖ്യ",
        "seasonal_demand": "സീസണൽ ഡിമാൻഡ്",
        "resources": "വിഭവ ലഭ്യത",

        "business_density_value": "128 ബിസിനസുകൾ",
        "population_value": "4,820 ആളുകൾ",
        "seasonal_demand_value": "ഉയർന്നത്",
        "resources_value": "നല്ലത്",

        "source": "ഉറവിടം",
        "updated": "ഡാറ്റ തീയതി",

        "map_title": "പ്രാദേശിക വിപണി മേഖല",
        "map_subtitle": "ഏകദേശം 5–10 കി.മീ വിപണി പരിധി",

        "market_radius": "വിപണി പരിധി",
        "market_radius_value": "5–10 കി.മീ",

        "local_signals": "പ്രാദേശിക സൂചനകൾ",
        "signal1": "ഭക്ഷണം, ദൈനംദിന ആവശ്യങ്ങൾ എന്നിവയുമായി ബന്ധപ്പെട്ട ബിസിനസുകളിൽ ശക്തമായ പ്രവർത്തനം കാണുന്നു.",
        "signal2": "താമസക്കാരുടെ എണ്ണം സ്ഥിരമായ ഡിമാൻഡിന് പിന്തുണ നൽകുന്നു.",
        "signal3": "ഉത്സവങ്ങളും കാർഷിക സീസണുകളും അനുസരിച്ച് ഡിമാൻഡ് മാറുന്നു.",

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
    }
}


# =========================================================
# HELPER
# =========================================================

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

if "location" not in st.session_state:
    st.session_state.location = {
        "district": "Ernakulam",
        "local_body": "Kochi Municipal Corporation",
        "ward": "Ward 42",
    }


# =========================================================
# CSS
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

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
    }}

    p {{
        color: {TEXT};
    }}


    /* =====================================================
       HEADER
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
       LANGUAGE SELECTOR
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
       TEXT INPUT
       ===================================================== */

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

    div[data-testid="stTextInput"] input::placeholder,
    div[data-testid="stTextInputRootElement"] input::placeholder {{
        color: #E8EDE1 !important;
        -webkit-text-fill-color: #E8EDE1 !important;
        opacity: 1 !important;
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


    /* =====================================================
       RISK CARDS
       ===================================================== */

    .risk-card {{
        background-color: {WHITE};
        border: 1px solid {LIGHT_BORDER};
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

    div[data-testid="stRadio"] label {{
        color: {TEXT} !important;
    }}


    /* =====================================================
       EXISTING BUSINESS CHECKBOX
       ===================================================== */

    div[data-testid="stCheckbox"] {{
        background-color: {LIGHT_GREY} !important;
        border: 2px solid {BORDER_GREY} !important;
        border-radius: 14px !important;
        padding: 12px 16px !important;
        margin-top: 5px !important;
        margin-bottom: 5px !important;
    }}

    div[data-testid="stCheckbox"]:hover {{
        border-color: {PRIMARY} !important;
        background-color: #E8EBE3 !important;
    }}

    div[data-testid="stCheckbox"] label {{
        color: {TEXT} !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }}

    div[data-testid="stCheckbox"] label p {{
        color: {TEXT} !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }}


    /* =====================================================
       BUTTONS
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
       FRAME 2 LOCATION CARD
       ===================================================== */

    .location-section {{
        background-color: {WHITE};
        border: 1px solid {LIGHT_BORDER};
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 25px;
    }}

    .section-heading {{
        font-size: 20px;
        font-weight: 800;
        color: {TEXT};
        margin-bottom: 4px;
    }}

    .section-subheading {{
        font-size: 14px;
        color: {MUTED};
        margin-bottom: 20px;
    }}


    /* =====================================================
       DATA COVERAGE BADGE
       ===================================================== */

    .coverage-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 18px;
        padding-top: 15px;
        border-top: 1px solid {LIGHT_BORDER};
    }}

    .coverage-label {{
        font-size: 13px;
        font-weight: 700;
        color: {MUTED};
    }}

    .coverage-badge {{
        display: inline-block;
        background-color: #E9F0E1;
        color: {PRIMARY};
        border: 1px solid #C9D8BC;
        border-radius: 20px;
        padding: 6px 12px;
        font-size: 13px;
        font-weight: 800;
    }}


    /* =====================================================
       DEMO BADGE
       ===================================================== */

    .demo-badge {{
        display: inline-block;
        background-color: #FFF1DD;
        color: #9A641D;
        border: 1px solid #E8C994;
        border-radius: 20px;
        padding: 5px 11px;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.5px;
        margin-left: 8px;
    }}


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    .metric-card {{
        background-color: {WHITE};
        border: 1px solid {LIGHT_BORDER};
        border-radius: 16px;
        padding: 20px;
        min-height: 155px;
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


    /* =====================================================
       MAP PLACEHOLDER
       ===================================================== */

    .map-card {{
        background-color: #EEF0E9;
        border: 1px solid #D7DCCF;
        border-radius: 18px;
        min-height: 350px;
        position: relative;
        overflow: hidden;
        padding: 25px;
    }}

    .map-title {{
        font-size: 19px;
        font-weight: 800;
        color: {TEXT};
        margin-bottom: 4px;
    }}

    .map-subtitle {{
        font-size: 13px;
        color: {MUTED};
    }}

    .map-road {{
        position: absolute;
        background-color: #D3D8CA;
        border-radius: 50%;
        transform: rotate(-25deg);
    }}

    .road-one {{
        width: 520px;
        height: 28px;
        top: 150px;
        left: -50px;
    }}

    .road-two {{
        width: 430px;
        height: 24px;
        top: 245px;
        left: 130px;
        transform: rotate(25deg);
    }}

    .road-three {{
        width: 380px;
        height: 20px;
        top: 80px;
        left: 310px;
        transform: rotate(55deg);
    }}

    .map-center {{
        position: absolute;
        top: 135px;
        left: 48%;
        width: 75px;
        height: 75px;
        border-radius: 50%;
        background-color: rgba(82,106,58,0.12);
        border: 2px solid {PRIMARY};
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
    }}

    .map-radius {{
        position: absolute;
        top: 95px;
        left: 39%;
        width: 190px;
        height: 190px;
        border-radius: 50%;
        border: 2px dashed {SECONDARY};
    }}

    .map-label {{
        position: absolute;
        bottom: 25px;
        left: 25px;
        background-color: {WHITE};
        border: 1px solid {LIGHT_BORDER};
        border-radius: 10px;
        padding: 9px 13px;
        font-size: 12px;
        font-weight: 700;
        color: {TEXT};
    }}


    /* =====================================================
       SIGNALS
       ===================================================== */

    .signal-card {{
        background-color: {WHITE};
        border: 1px solid {LIGHT_BORDER};
        border-radius: 14px;
        padding: 15px 17px;
        margin-bottom: 10px;
    }}

    .signal-dot {{
        color: {PRIMARY};
        font-weight: 900;
        margin-right: 7px;
    }}

    .signal-text {{
        font-size: 14px;
        color: {TEXT};
        line-height: 1.5;
    }}


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {{
        border: none !important;
        border-top: 1px solid {LIGHT_BORDER} !important;
        margin: 30px 0 !important;
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
# FRAME 1 — PROFILE
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


    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # EXPERIENCE
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # CAPITAL
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # BUSINESS INTERESTS
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # RISK
    # -----------------------------------------------------

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

                <div class="risk-title">
                    🟢 {t("low")}
                </div>

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

                <div class="risk-title">
                    🟠 {t("medium")}
                </div>

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

                <div class="risk-title">
                    🔴 {t("high")}
                </div>

                <div class="risk-description">
                    {t("high_desc")}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown("---")


    # -----------------------------------------------------
    # EXISTING BUSINESS
    # -----------------------------------------------------

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


    # -----------------------------------------------------
    # CONTINUE
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # PROGRESS
    # -----------------------------------------------------

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
    # LOCATION SELECTION
    # =====================================================

    st.markdown(
        f"""
        <div class="location-section">

            <div class="section-heading">
                {t("location")}
            </div>

            <div class="section-subheading">
                Select the area where you want to explore business opportunities.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    location_col1, location_col2, location_col3 = st.columns(3)


    # -----------------------------------------------------
    # DISTRICT
    # -----------------------------------------------------

    with location_col1:

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
            index=0,
            label_visibility="collapsed",
            key="district_select",
        )


    # -----------------------------------------------------
    # LOCAL BODY
    # -----------------------------------------------------

    local_body_options = {

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


    with location_col2:

        st.markdown(
            f'<div class="field-label">{t("local_body")}</div>',
            unsafe_allow_html=True,
        )

        local_body = st.selectbox(
            t("local_body"),
            local_body_options[district],
            label_visibility="collapsed",
            key="local_body_select",
        )


    # -----------------------------------------------------
    # WARD
    # -----------------------------------------------------

    with location_col3:

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
            index=3,
            label_visibility="collapsed",
            key="ward_select",
        )


    # -----------------------------------------------------
    # SAVE STRUCTURED LOCATION STATE
    # -----------------------------------------------------

    st.session_state.location = {

        "district": district,

        "local_body": local_body,

        "ward": ward,
    }


    # -----------------------------------------------------
    # COVERAGE
    # -----------------------------------------------------

    st.markdown(
        f"""
        <div class="coverage-row">

            <div>
                <span class="coverage-label">
                    {t("coverage")}
                </span>

                <span class="demo-badge">
                    {t("demo_data")}
                </span>
            </div>

            <div class="coverage-badge">
                ✓ {t("ward_level")}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown("<br>", unsafe_allow_html=True)


    # =====================================================
    # LOCAL MARKET SNAPSHOT
    # =====================================================

    st.markdown(
        f"""
        <div class="section-heading">
            {t("local_market")}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)


    metric1, metric2, metric3, metric4 = st.columns(4)


    # -----------------------------------------------------
    # METRIC 1
    # -----------------------------------------------------

    with metric1:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("business_density")}
                </div>

                <div class="metric-value">
                    {t("business_density_value")}
                </div>

                <div class="metric-source">
                    {t("source")}: Demo local dataset<br>
                    {t("updated")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # -----------------------------------------------------
    # METRIC 2
    # -----------------------------------------------------

    with metric2:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("population")}
                </div>

                <div class="metric-value">
                    {t("population_value")}
                </div>

                <div class="metric-source">
                    {t("source")}: Demo demographic dataset<br>
                    {t("updated")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # -----------------------------------------------------
    # METRIC 3
    # -----------------------------------------------------

    with metric3:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("seasonal_demand")}
                </div>

                <div class="metric-value">
                    {t("seasonal_demand_value")}
                </div>

                <div class="metric-source">
                    {t("source")}: Demo seasonal model<br>
                    {t("updated")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # -----------------------------------------------------
    # METRIC 4
    # -----------------------------------------------------

    with metric4:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("resources")}
                </div>

                <div class="metric-value">
                    {t("resources_value")}
                </div>

                <div class="metric-source">
                    {t("source")}: Demo resource dataset<br>
                    {t("updated")}: 2026
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # =====================================================
    # MAP + LOCAL SIGNALS
    # =====================================================

    map_col, signal_col = st.columns([1.45, 1])


    # -----------------------------------------------------
    # MAP
    # -----------------------------------------------------

    with map_col:

        st.markdown(
            f"""
            <div class="map-card">

                <div class="map-title">
                    {t("map_title")}
                </div>

                <div class="map-subtitle">
                    {t("map_subtitle")}
                </div>

                <div class="map-road road-one"></div>
                <div class="map-road road-two"></div>
                <div class="map-road road-three"></div>

                <div class="map-radius"></div>

                <div class="map-center">
                    📍
                </div>

                <div class="map-label">
                    {district} · {ward}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


    # -----------------------------------------------------
    # LOCAL SIGNALS
    # -----------------------------------------------------

    with signal_col:

        st.markdown(
            f"""
            <div class="section-heading">
                {t("local_signals")}
            </div>
            """,
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
                <div class="signal-card">

                    <span class="signal-dot">●</span>

                    <span class="signal-text">
                        {signal}
                    </span>

                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-title">
                    {t("market_radius")}
                </div>

                <div class="metric-value">
                    {t("market_radius_value")}
                </div>

                <div class="metric-source">
                    Initial feasibility radius for local opportunity analysis.
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

            # Frame 3 will use page = 3
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
        '<div class="intro-subtitle">'
        'This is where GramVyapar AI will rank the best business opportunities for this user.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "Frame 3 is the next screen we will build."
    )

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
