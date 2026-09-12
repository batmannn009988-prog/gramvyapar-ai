import streamlit as st
import pandas as pd
import numpy as np


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# COLOUR PALETTE
# =========================================================

OLIVE = "#526A3A"
GREEN = "#7D9A55"
ORANGE = "#C88A3D"
CREAM = "#FAF8F1"
BROWN = "#33352C"
WHITE = "#FFFFFF"

LIGHT_GREEN = "#E8EDDF"
LIGHT_ORANGE = "#F4E8D5"
LIGHT_GREY = "#F0F1ED"
BORDER = "#D7D9D1"


# =========================================================
# TRANSLATIONS
# =========================================================

TEXT = {

    "English": {

        "step1": "Step 1 of 10",
        "step2": "Step 2 of 10",
        "step3": "Step 3 of 10",

        "profile_title": "Tell us about yourself",
        "profile_desc":
            "We'll use your skills, experience, capital and interests "
            "to identify suitable local business opportunities.",

        "skills": "Your skills",
        "select_skills": "Select your skills",
        "other_skill": "Other skill (optional)",
        "other_skill_placeholder": "Type another skill...",

        "experience": "Experience",
        "years_experience": "Years of relevant experience",

        "capital": "Available capital",
        "capital_question":
            "How much own capital can you invest?",

        "interests": "Business interests",
        "business_interest_question":
            "What type of business interests you?",
        "other_interest": "Other interest (optional)",
        "other_interest_placeholder":
            "Type another business interest...",

        "risk": "Risk preference",
        "risk_question":
            "How much business risk are you comfortable with?",

        "low": "Low",
        "medium": "Medium",
        "high": "High",

        "existing": "Existing business",
        "existing_checkbox": "I already have a business",
        "business_name": "Business name",
        "business_name_placeholder": "Enter your business name",

        "continue": "Continue →",
        "back": "← Back",

        "local_market": "Your Local Market",
        "local_market_desc":
            "Let's understand the local market before recommending a business.",

        "choose_location": "Choose your location",

        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward Number",

        "ward_help":
            "Enter the ward number of the selected local body.",

        "demo_location":
            "📌 Demo location data is being used for this prototype.",

        "coverage": "Data coverage",

        "district_fallback":
            "Current analysis level: District-level fallback",

        "confidence": "Confidence",
        "medium_confidence": "Medium",

        "market_snapshot": "Local market snapshot",

        "business_density": "Business Density",
        "population": "Population",
        "seasonal_demand": "Seasonal Demand",
        "resource_availability": "Resource Availability",

        "demo": "Demo",
        "census": "2011 Census",
        "estimated": "Estimated",

        "map_title": "Local market area",

        "map_caption":
            "Map points are illustrative only. Connect verified local "
            "business/location data later.",

        "market_signals": "Market signals",

        "demand_signal": "📈 Demand signal",

        "demand_text":
            "Local demand appears **moderate** for essential household "
            "and food-related services.",

        "competition_signal": "🏪 Competition signal",

        "competition_text":
            "Competition appears **moderate**. More detailed competitor "
            "mapping will improve confidence.",

        "source_estimate": "Source status: Estimate",

        "market_reach": "Recommended market reach",

        "primary_reach": "Primary Reach",
        "extended_reach": "Extended Reach",
        "analysis_radius": "Analysis Radius",

        "immediate_customers": "Immediate local customers",
        "nearby_markets": "Nearby villages / markets",
        "prototype_radius": "Prototype target radius",

        "frame3": "Opportunity Radar",

        "frame3_desc":
            "Frame 3 will rank business opportunities using "
            "Demand, Competition, Skills, Capital and Risk.",

        "coming_next": "Coming next",

        "demand": "Demand",
        "competition": "Competition",
        "capital_fit": "Capital Fit",

        "demand_description":
            "Estimated local customer demand.",

        "competition_description":
            "Number and strength of nearby competitors.",

        "capital_description":
            "Fit with the user's available capital.",

        "back_dashboard": "← Back to Local Dashboard",

        "language": "Language",
    },


    "Malayalam": {

        "step1": "ഘട്ടം 1 / 10",
        "step2": "ഘട്ടം 2 / 10",
        "step3": "ഘട്ടം 3 / 10",

        "profile_title": "നിങ്ങളെക്കുറിച്ച് പറയൂ",

        "profile_desc":
            "നിങ്ങളുടെ കഴിവുകൾ, പരിചയം, മൂലധനം, താൽപ്പര്യങ്ങൾ "
            "എന്നിവ ഉപയോഗിച്ച് അനുയോജ്യമായ പ്രാദേശിക ബിസിനസുകൾ കണ്ടെത്താം.",

        "skills": "നിങ്ങളുടെ കഴിവുകൾ",
        "select_skills": "നിങ്ങളുടെ കഴിവുകൾ തിരഞ്ഞെടുക്കുക",

        "other_skill": "മറ്റ് കഴിവ് (ഓപ്ഷണൽ)",
        "other_skill_placeholder": "മറ്റൊരു കഴിവ് നൽകുക...",

        "experience": "പരിചയം",
        "years_experience": "പ്രസക്തമായ പരിചയത്തിന്റെ വർഷങ്ങൾ",

        "capital": "ലഭ്യമായ മൂലധനം",

        "capital_question":
            "നിങ്ങൾക്ക് നിക്ഷേപിക്കാൻ കഴിയുന്ന സ്വന്തം മൂലധനം എത്രയാണ്?",

        "interests": "ബിസിനസ് താൽപ്പര്യങ്ങൾ",

        "business_interest_question":
            "ഏത് തരത്തിലുള്ള ബിസിനസിലാണ് നിങ്ങൾക്ക് താൽപ്പര്യം?",

        "other_interest": "മറ്റ് താൽപ്പര്യം (ഓപ്ഷണൽ)",

        "other_interest_placeholder":
            "മറ്റൊരു ബിസിനസ് താൽപ്പര്യം നൽകുക...",

        "risk": "റിസ്ക് മുൻഗണന",

        "risk_question":
            "നിങ്ങൾക്ക് എത്രത്തോളം ബിസിനസ് റിസ്ക് സ്വീകരിക്കാൻ കഴിയും?",

        "low": "കുറവ്",
        "medium": "ഇടത്തരം",
        "high": "ഉയർന്നത്",

        "existing": "നിലവിലുള്ള ബിസിനസ്",

        "existing_checkbox":
            "എനിക്ക് ഇതിനകം ഒരു ബിസിനസ് ഉണ്ട്",

        "business_name": "ബിസിനസിന്റെ പേര്",

        "business_name_placeholder":
            "ബിസിനസിന്റെ പേര് നൽകുക",

        "continue": "തുടരുക →",
        "back": "← പിന്നിലേക്ക്",

        "local_market": "നിങ്ങളുടെ പ്രാദേശിക വിപണി",

        "local_market_desc":
            "ഒരു ബിസിനസ് നിർദ്ദേശിക്കുന്നതിന് മുമ്പ് നിങ്ങളുടെ പ്രാദേശിക വിപണി മനസ്സിലാക്കാം.",

        "choose_location": "നിങ്ങളുടെ സ്ഥലം തിരഞ്ഞെടുക്കുക",

        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ് നമ്പർ",

        "ward_help":
            "തിരഞ്ഞെടുത്ത തദ്ദേശ സ്ഥാപനത്തിലെ വാർഡ് നമ്പർ നൽകുക.",

        "demo_location":
            "📌 ഈ പ്രോട്ടോടൈപ്പിൽ ഡെമോ ലൊക്കേഷൻ ഡാറ്റയാണ് ഉപയോഗിക്കുന്നത്.",

        "coverage": "ഡാറ്റാ കവറേജ്",

        "district_fallback":
            "നിലവിലെ വിശകലന തല: ജില്ലാ തലത്തിലുള്ള ഡാറ്റ",

        "confidence": "വിശ്വാസ്യത",
        "medium_confidence": "ഇടത്തരം",

        "market_snapshot": "പ്രാദേശിക വിപണി അവലോകനം",

        "business_density": "ബിസിനസ് സാന്ദ്രത",
        "population": "ജനസംഖ്യ",
        "seasonal_demand": "കാലാനുസൃത ഡിമാൻഡ്",
        "resource_availability": "വിഭവ ലഭ്യത",

        "demo": "ഡെമോ",
        "census": "2011 സെൻസസ്",
        "estimated": "അനുമാനം",

        "map_title": "പ്രാദേശിക വിപണി പ്രദേശം",

        "map_caption":
            "മാപ്പിലെ പോയിന്റുകൾ ഉദാഹരണത്തിന് മാത്രമാണ്. പിന്നീട് "
            "പരിശോധിച്ച പ്രാദേശിക ഡാറ്റ ബന്ധിപ്പിക്കാം.",

        "market_signals": "വിപണി സൂചനകൾ",

        "demand_signal": "📈 ഡിമാൻഡ് സൂചന",

        "demand_text":
            "അത്യാവശ്യ ഗാർഹിക, ഭക്ഷ്യ സേവനങ്ങൾക്ക് പ്രാദേശിക "
            "ഡിമാൻഡ് **ഇടത്തരം** ആണെന്ന് കണക്കാക്കുന്നു.",

        "competition_signal": "🏪 മത്സരം സംബന്ധിച്ച സൂചന",

        "competition_text":
            "മത്സരം **ഇടത്തരം** ആണെന്ന് കണക്കാക്കുന്നു. കൂടുതൽ "
            "വിശദമായ മത്സര ഡാറ്റ വിശ്വാസ്യത മെച്ചപ്പെടുത്തും.",

        "source_estimate": "ഡാറ്റ നില: അനുമാനം",

        "market_reach": "ശുപാർശ ചെയ്യുന്ന വിപണി പരിധി",

        "primary_reach": "പ്രാഥമിക പരിധി",
        "extended_reach": "വിപുലീകരിച്ച പരിധി",
        "analysis_radius": "വിശകലന പരിധി",

        "immediate_customers":
            "അടുത്തുള്ള പ്രാദേശിക ഉപഭോക്താക്കൾ",

        "nearby_markets":
            "സമീപ ഗ്രാമങ്ങൾ / വിപണികൾ",

        "prototype_radius":
            "പ്രോട്ടോടൈപ്പ് ലക്ഷ്യ പരിധി",

        "frame3": "ബിസിനസ് അവസരങ്ങൾ",

        "frame3_desc":
            "ഡിമാൻഡ്, മത്സരം, കഴിവുകൾ, മൂലധനം, റിസ്ക് "
            "എന്നിവ ഉപയോഗിച്ച് ബിസിനസ് അവസരങ്ങൾ റാങ്ക് ചെയ്യും.",

        "coming_next": "അടുത്ത ഘട്ടം",

        "demand": "ഡിമാൻഡ്",
        "competition": "മത്സരം",
        "capital_fit": "മൂലധന അനുയോജ്യത",

        "demand_description":
            "പ്രാദേശിക ഉപഭോക്തൃ ഡിമാൻഡിന്റെ അനുമാനം.",

        "competition_description":
            "സമീപത്തുള്ള മത്സരക്കാരുടെ എണ്ണം, ശക്തി.",

        "capital_description":
            "ലഭ്യമായ മൂലധനവുമായി ബിസിനസിന്റെ അനുയോജ്യത.",

        "back_dashboard":
            "← പ്രാദേശിക ഡാഷ്ബോർഡിലേക്ക്",

        "language": "ഭാഷ",
    }
}


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = 1

if "language" not in st.session_state:
    st.session_state.language = "English"

if "skills" not in st.session_state:
    st.session_state.skills = []

if "experience" not in st.session_state:
    st.session_state.experience = 0

if "capital" not in st.session_state:
    st.session_state.capital = 50000

if "interests" not in st.session_state:
    st.session_state.interests = []

if "risk" not in st.session_state:
    st.session_state.risk = "Medium"

if "existing_business" not in st.session_state:
    st.session_state.existing_business = False

if "business_name" not in st.session_state:
    st.session_state.business_name = ""


# =========================================================
# TRANSLATION HELPER
# =========================================================

def t(key):

    language = st.session_state.language

    return TEXT.get(
        language,
        TEXT["English"]
    ).get(
        key,
        TEXT["English"].get(key, key)
    )


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {CREAM};
        color: {BROWN};
    }}

    [data-testid="stHeader"] {{
        background-color: {CREAM};
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1350px;
    }}

    h1, h2, h3, h4 {{
        color: {BROWN} !important;
    }}

    p {{
        color: {BROWN};
    }}


    /* =====================================================
       BUTTONS
       ===================================================== */

    div.stButton > button {{
        background-color: {OLIVE};
        color: white !important;
        border: 1px solid {OLIVE};
        border-radius: 10px;
        min-height: 44px;
        font-weight: 600;
    }}

    div.stButton > button:hover {{
        background-color: {GREEN};
        color: white !important;
        border-color: {GREEN};
    }}


    /* =====================================================
       SELECT BOX
       ===================================================== */

    div[data-baseweb="select"] > div {{
        background-color: white !important;
        color: {BROWN} !important;
        border-color: {BORDER};
    }}

    div[data-baseweb="select"] span {{
        color: {BROWN} !important;
    }}


    /* =====================================================
       TEXT INPUTS
       ===================================================== */

    input {{
        color: {BROWN} !important;
        background-color: white !important;
    }}

    textarea {{
        color: {BROWN} !important;
        background-color: white !important;
    }}


    /* =====================================================
       NUMBER INPUT
       ===================================================== */

    div[data-testid="stNumberInput"] input {{
        color: {BROWN} !important;
        background-color: white !important;
    }}


    /* =====================================================
       CHECKBOX
       ===================================================== */

    div[data-testid="stCheckbox"] {{
        background-color: {LIGHT_GREY};
        border: 2px solid #B8BDB2;
        border-radius: 10px;
        padding: 10px 14px;
    }}

    div[data-testid="stCheckbox"] label {{
        color: {BROWN} !important;
    }}

    div[data-testid="stCheckbox"] label p {{
        color: {BROWN} !important;
    }}


    /* =====================================================
       RADIO
       ===================================================== */

    div[data-testid="stRadio"] {{
        color: {BROWN} !important;
    }}

    div[data-testid="stRadio"] label {{
        color: {BROWN} !important;
    }}

    div[data-testid="stRadio"] label p {{
        color: {BROWN} !important;
    }}


    /* =====================================================
       SLIDER
       ===================================================== */

    div[data-testid="stSlider"] {{
        padding-top: 5px;
    }}

    div[data-testid="stSlider"] label {{
        color: {BROWN} !important;
    }}

    div[data-testid="stSlider"] p {{
        color: {BROWN} !important;
    }}


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    div[data-testid="stMetric"] {{
        background-color: white;
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 15px;
    }}

    div[data-testid="stMetric"] label {{
        color: {BROWN} !important;
    }}

    div[data-testid="stMetricValue"] {{
        color: {BROWN} !important;
    }}


    /* =====================================================
       INFO / BLUE BOXES
       White text for readability
       ===================================================== */

    div[data-testid="stAlert"] {{
        border-radius: 10px;
    }}

    div[data-testid="stAlert"] p {{
        color: white !important;
    }}

    div[data-testid="stAlert"] span {{
        color: white !important;
    }}

    div[data-testid="stAlert"] div {{
        color: white !important;
    }}


    /* =====================================================
       WIDGET LABELS
       ===================================================== */

    [data-testid="stWidgetLabel"] p {{
        color: {BROWN} !important;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HEADER
# =========================================================

def render_header():

    col1, col2 = st.columns([4, 1])

    with col1:

        st.title("🌱 GramVyapar AI")
        st.caption("Know Before You Borrow.")

    with col2:

        selected_language = st.selectbox(
            t("language"),
            ["English", "Malayalam"],
            index=(
                0
                if st.session_state.language == "English"
                else 1
            ),
            key="language_selector_v2",
        )

        if selected_language != st.session_state.language:

            st.session_state.language = selected_language

            st.rerun()


# =========================================================
# FRAME 1
# =========================================================

def render_frame_1():

    st.subheader(t("step1"))

    st.title(t("profile_title"))

    st.write(t("profile_desc"))

    st.divider()


    # =====================================================
    # SKILLS
    # =====================================================

    st.subheader("🛠️ " + t("skills"))

    skill_options = [
        "Cooking",
        "Tailoring",
        "Farming",
        "Dairy",
        "Handicrafts",
        "Food Processing",
        "Sales",
        "Repair & Maintenance",
        "Digital Skills",
        "Driving",
    ]

    # Remove any old values that are no longer valid.
    valid_saved_skills = [
        skill
        for skill in st.session_state.skills
        if skill in skill_options
    ]

    st.session_state.skills = valid_saved_skills

    skills = st.multiselect(
        t("select_skills"),
        skill_options,
        default=valid_saved_skills,
        key="skills_input_v2",
    )

    custom_skill = st.text_input(
        t("other_skill"),
        placeholder=t("other_skill_placeholder"),
        key="custom_skill_v2",
    )

    if custom_skill.strip():

        if custom_skill.strip() not in skills:

            skills = skills + [
                custom_skill.strip()
            ]

    st.session_state.skills = skills


    # =====================================================
    # EXPERIENCE
    # =====================================================

    st.subheader("📈 " + t("experience"))

    experience = st.number_input(
        t("years_experience"),
        min_value=0,
        max_value=50,
        value=int(st.session_state.experience),
        step=1,
        key="experience_input_v2",
    )

    st.session_state.experience = experience


    # =====================================================
    # CAPITAL
    # =====================================================

    st.subheader("💰 " + t("capital"))

    capital = st.slider(
        t("capital_question"),
        min_value=0,
        max_value=500000,
        value=int(st.session_state.capital),
        step=5000,
        format="₹%d",
        key="capital_input_v2",
    )

    st.session_state.capital = capital

    st.success(
        f"₹{capital:,.0f}"
    )


    # =====================================================
    # INTERESTS
    # =====================================================

    st.subheader("🎯 " + t("interests"))

    interest_options = [
        "Food & Bakery",
        "Dairy",
        "Tailoring",
        "Retail",
        "Agriculture",
        "Food Processing",
        "Services",
        "Handicrafts",
        "Small Manufacturing",
    ]

    valid_saved_interests = [
        interest
        for interest in st.session_state.interests
        if interest in interest_options
    ]

    st.session_state.interests = valid_saved_interests

    interests = st.multiselect(
        t("business_interest_question"),
        interest_options,
        default=valid_saved_interests,
        key="interests_input_v2",
    )

    custom_interest = st.text_input(
        t("other_interest"),
        placeholder=t("other_interest_placeholder"),
        key="custom_interest_v2",
    )

    if custom_interest.strip():

        if custom_interest.strip() not in interests:

            interests = interests + [
                custom_interest.strip()
            ]

    st.session_state.interests = interests


    # =====================================================
    # RISK
    # =====================================================

    st.subheader("⚖️ " + t("risk"))

    risk_options = [
        t("low"),
        t("medium"),
        t("high"),
    ]

    current_risk_index = {
        "Low": 0,
        "Medium": 1,
        "High": 2,
    }.get(
        st.session_state.risk,
        1
    )

    selected_risk = st.radio(
        t("risk_question"),
        risk_options,
        index=current_risk_index,
        horizontal=True,
        key="risk_input_v2",
    )

    reverse_risk = {
        t("low"): "Low",
        t("medium"): "Medium",
        t("high"): "High",
    }

    st.session_state.risk = reverse_risk[
        selected_risk
    ]


    # =====================================================
    # EXISTING BUSINESS
    # =====================================================

    st.subheader("🏪 " + t("existing"))

    existing = st.checkbox(
        t("existing_checkbox"),
        value=st.session_state.existing_business,
        key="existing_business_input_v2",
    )

    st.session_state.existing_business = existing

    if existing:

        business_name = st.text_input(
            t("business_name"),
            value=st.session_state.business_name,
            placeholder=t("business_name_placeholder"),
            key="business_name_input_v2",
        )

        st.session_state.business_name = business_name


    # =====================================================
    # NAVIGATION
    # =====================================================

    st.divider()

    col1, col2, col3 = st.columns(
        [1, 2, 1]
    )

    with col2:

        if st.button(
            t("continue"),
            use_container_width=True,
            type="primary",
            key="frame1_continue_v2",
        ):

            st.session_state.page = 2

            st.rerun()


# =========================================================
# FRAME 2
# =========================================================

def render_frame_2():

    st.subheader(t("step2"))

    st.title(
        "📍 " + t("local_market")
    )

    st.write(
        t("local_market_desc")
    )

    st.divider()


    # =====================================================
    # LOCATION
    # =====================================================

    st.subheader(
        t("choose_location")
    )

    # ALL 14 KERALA DISTRICTS

    kerala_districts = [
        "Alappuzha",
        "Ernakulam",
        "Idukki",
        "Kannur",
        "Kasaragod",
        "Kollam",
        "Kottayam",
        "Kozhikode",
        "Malappuram",
        "Palakkad",
        "Pathanamthitta",
        "Thiruvananthapuram",
        "Thrissur",
        "Wayanad",
    ]

    col1, col2, col3 = st.columns(3)


    # =====================================================
    # DISTRICT
    # =====================================================

    with col1:

        district = st.selectbox(
            t("district"),
            kerala_districts,
            index=1,
            key="district_selection_v2",
        )


    # =====================================================
    # LOCAL BODY
    # =====================================================

    with col2:

        local_body = st.selectbox(
            t("local_body"),
            [
                "Sample Grama Panchayat",
                "Sample Municipality",
                "Sample Corporation",
            ],
            key="local_body_selection_v2",
        )


    # =====================================================
    # WARD NUMBER
    # =====================================================

    with col3:

        ward = st.number_input(
            t("ward"),
            min_value=1,
            max_value=100,
            value=1,
            step=1,
            help=t("ward_help"),
            key="ward_number_v2",
        )


    st.info(
        t("demo_location")
    )


    # =====================================================
    # DATA COVERAGE
    # =====================================================

    st.subheader(
        t("coverage")
    )

    coverage_col1, coverage_col2 = st.columns(
        [3, 1]
    )

    with coverage_col1:

        st.info(
            t("district_fallback")
        )

    with coverage_col2:

        st.metric(
            t("confidence"),
            t("medium_confidence"),
        )


    # =====================================================
    # LOCAL MARKET SNAPSHOT
    # =====================================================

    st.subheader(
        t("market_snapshot")
    )

    m1, m2, m3, m4 = st.columns(4)


    with m1:

        st.metric(
            t("business_density"),
            "42 / km²",
            t("demo"),
        )


    with m2:

        st.metric(
            t("population"),
            "18,420",
            t("census"),
        )


    with m3:

        st.metric(
            t("seasonal_demand"),
            t("medium"),
            t("estimated"),
        )


    with m4:

        st.metric(
            t("resource_availability"),
            "Good",
            t("estimated"),
        )


    if st.session_state.language == "English":

        st.caption(
            "Each value should be replaced with verified "
            "local data in the production version."
        )

    else:

        st.caption(
            "പ്രൊഡക്ഷൻ പതിപ്പിൽ ഓരോ മൂല്യവും പരിശോധിച്ച "
            "പ്രാദേശിക ഡാറ്റ ഉപയോഗിച്ച് മാറ്റണം."
        )


    # =====================================================
    # MAP
    # =====================================================

    st.subheader(
        "🗺️ " + t("map_title")
    )

    map_data = pd.DataFrame(
        {
            "lat": [
                10.0159,
                10.0200,
                10.0100,
            ],

            "lon": [
                76.3419,
                76.3500,
                76.3350,
            ],
        }
    )

    st.map(
        map_data,
        latitude="lat",
        longitude="lon",
        zoom=11,
    )

    st.caption(
        t("map_caption")
    )


    # =====================================================
    # MARKET SIGNALS
    # =====================================================

    st.subheader(
        t("market_signals")
    )

    signal_col1, signal_col2 = st.columns(2)


    with signal_col1:

        with st.container(border=True):

            st.markdown(
                "### " + t("demand_signal")
            )

            st.write(
                t("demand_text")
            )

            st.caption(
                t("source_estimate")
            )


    with signal_col2:

        with st.container(border=True):

            st.markdown(
                "### " + t("competition_signal")
            )

            st.write(
                t("competition_text")
            )

            st.caption(
                t("source_estimate")
            )


    # =====================================================
    # MARKET REACH
    # =====================================================

    st.subheader(
        t("market_reach")
    )

    reach_col1, reach_col2, reach_col3 = st.columns(3)


    with reach_col1:

        with st.container(border=True):

            st.metric(
                t("primary_reach"),
                "0–5 km",
            )

            st.caption(
                t("immediate_customers")
            )


    with reach_col2:

        with st.container(border=True):

            st.metric(
                t("extended_reach"),
                "5–10 km",
            )

            st.caption(
                t("nearby_markets")
            )


    with reach_col3:

        with st.container(border=True):

            st.metric(
                t("analysis_radius"),
                "10 km",
            )

            st.caption(
                t("prototype_radius")
            )


    # =====================================================
    # NAVIGATION
    # =====================================================

    st.divider()

    back_col, empty_col, next_col = st.columns(
        [1, 2, 1]
    )


    with back_col:

        if st.button(
            t("back"),
            use_container_width=True,
            key="frame2_back_v2",
        ):

            st.session_state.page = 1

            st.rerun()


    with next_col:

        if st.button(
            t("continue"),
            use_container_width=True,
            type="primary",
            key="frame2_continue_v2",
        ):

            st.session_state.page = 3

            st.rerun()


# =========================================================
# FRAME 3
# =========================================================

def render_frame_3():

    st.subheader(
        t("step3")
    )

    st.title(
        "🎯 " + t("frame3")
    )

    st.info(
        t("frame3_desc")
    )

    st.divider()

    st.subheader(
        t("coming_next")
    )

    col1, col2, col3 = st.columns(3)


    with col1:

        with st.container(border=True):

            st.metric(
                t("demand"),
                t("high")
            )

            st.write(
                t("demand_description")
            )


    with col2:

        with st.container(border=True):

            st.metric(
                t("competition"),
                t("medium")
            )

            st.write(
                t("competition_description")
            )


    with col3:

        with st.container(border=True):

            st.metric(
                t("capital_fit"),
                "Good"
            )

            st.write(
                t("capital_description")
            )


    st.divider()

    if st.button(
        t("back_dashboard"),
        key="frame3_back_v2",
    ):

        st.session_state.page = 2

        st.rerun()


# =========================================================
# MAIN APPLICATION
# =========================================================

render_header()

st.divider()


if st.session_state.page == 1:

    render_frame_1()


elif st.session_state.page == 2:

    render_frame_2()


elif st.session_state.page == 3:

    render_frame_3()
