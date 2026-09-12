import streamlit as st
import pandas as pd
import numpy as np
from frames.frame3_opportunity import render_frame3

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GRAMVYAPAR AI PALETTE
# ============================================================

PRIMARY_GREEN = "#526A3A"
SECONDARY_GREEN = "#7D9A55"
ACCENT_ORANGE = "#C88A3D"
BACKGROUND_CREAM = "#FAF8F1"
TEXT_BROWN = "#33352C"
WHITE = "#FFFFFF"


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {
    "en": {
        "app_title": "GramVyapar AI",
        "tagline": "Know Before You Borrow",

        "step1": "Your Profile",
        "step2": "Local Market",
        "step3": "Opportunities",

        "profile_title": "Tell us about yourself",
        "profile_subtitle": "This helps us understand which business opportunities may fit you.",

        "skills": "What skills do you have?",
        "experience": "Years of experience",
        "capital": "Available own capital",
        "interests": "Which business areas interest you?",
        "risk_preference": "Risk preference",
        "existing_business": "Do you already have a business?",
        "business_name": "Existing business name",

        "low": "Low",
        "medium": "Medium",
        "high": "High",

        "yes": "Yes",
        "no": "No",

        "continue": "Continue",
        "back": "Back",

        "local_title": "Local Market Dashboard",
        "local_subtitle": "Understand the local business environment before making a decision.",

        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward",

        "data_level": "Data level",
        "data_source": "Data source",
        "prototype_source": "Prototype dataset",
        "data_status": "Data status",
        "prototype_status": "Prototype estimate",

        "business_density": "Business Density",
        "population": "Population",
        "seasonal_demand": "Seasonal Demand",
        "resource_availability": "Resource Availability",

        "map_title": "Local business map",
        "map_note": "Prototype map marker represents the selected district reference point.",

        "opportunity_title": "Opportunity Radar",
        "opportunity_subtitle": "Explore business opportunities that match your profile and local market.",

        "profile_summary": "Your profile",
        "location_summary": "Your selected location",
        "interest_summary": "Which business areas interest you?",

        "years_experience": "years experience",
        "risk_preference_text": "Risk preference",

        "prototype_disclaimer": (
            "These rankings are prototype recommendations. "
            "They are not loan approval or guaranteed business success."
        ),

        "opportunity_score": "Opportunity Score",
        "why_fits": "Why this fits",
        "confidence": "Confidence",
        "prototype_estimate": "Prototype estimate",

        "demand": "Demand",
        "competition": "Competition",
        "skill_fit": "Skill Fit",
        "capital_fit": "Capital Fit",
        "risk_fit": "Risk Fit",

        "back_to_market": "Back to Local Market",
    },

    "ml": {
        "app_title": "ഗ്രാമവ്യാപാർ AI",
        "tagline": "വായ്പ എടുക്കുന്നതിന് മുമ്പ് അറിയൂ",

        "step1": "നിങ്ങളുടെ പ്രൊഫൈൽ",
        "step2": "പ്രാദേശിക വിപണി",
        "step3": "അവസരങ്ങൾ",

        "profile_title": "നിങ്ങളെക്കുറിച്ച് പറയൂ",
        "profile_subtitle": "നിങ്ങൾക്ക് അനുയോജ്യമായ ബിസിനസ് അവസരങ്ങൾ കണ്ടെത്താൻ ഇത് സഹായിക്കും.",

        "skills": "നിങ്ങളുടെ കഴിവുകൾ എന്തൊക്കെയാണ്?",
        "experience": "പരിചയമുള്ള വർഷങ്ങൾ",
        "capital": "ലഭ്യമായ സ്വന്തം മൂലധനം",
        "interests": "ഏത് ബിസിനസ് മേഖലകളിലാണ് താൽപര്യം?",
        "risk_preference": "റിസ്ക് മുൻഗണന",
        "existing_business": "നിങ്ങൾക്ക് ഇതിനകം ഒരു ബിസിനസ് ഉണ്ടോ?",
        "business_name": "നിലവിലുള്ള ബിസിനസിന്റെ പേര്",

        "low": "കുറഞ്ഞത്",
        "medium": "ഇടത്തരം",
        "high": "ഉയർന്നത്",

        "yes": "അതെ",
        "no": "ഇല്ല",

        "continue": "തുടരുക",
        "back": "തിരികെ",

        "local_title": "പ്രാദേശിക വിപണി ഡാഷ്ബോർഡ്",
        "local_subtitle": "തീരുമാനം എടുക്കുന്നതിന് മുമ്പ് പ്രാദേശിക ബിസിനസ് സാഹചര്യം മനസ്സിലാക്കുക.",

        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ്",

        "data_level": "ഡാറ്റാ നിലവാരം",
        "data_source": "ഡാറ്റാ ഉറവിടം",
        "prototype_source": "പ്രോട്ടോടൈപ്പ് ഡാറ്റാസെറ്റ്",
        "data_status": "ഡാറ്റാ സ്ഥിതി",
        "prototype_status": "പ്രോട്ടോടൈപ്പ് കണക്ക്",

        "business_density": "ബിസിനസ് സാന്ദ്രത",
        "population": "ജനസംഖ്യ",
        "seasonal_demand": "കാലാവസ്ഥാനുസൃത ആവശ്യം",
        "resource_availability": "വിഭവ ലഭ്യത",

        "map_title": "പ്രാദേശിക ബിസിനസ് മാപ്പ്",
        "map_note": "തിരഞ്ഞെടുത്ത ജില്ലയുടെ റഫറൻസ് പോയിന്റാണ് മാപ്പിൽ കാണിക്കുന്നത്.",

        "opportunity_title": "അവസര റഡാർ",
        "opportunity_subtitle": "നിങ്ങളുടെ പ്രൊഫൈലിനും പ്രാദേശിക വിപണിക്കും അനുയോജ്യമായ ബിസിനസ് അവസരങ്ങൾ പരിശോധിക്കുക.",

        "profile_summary": "നിങ്ങളുടെ പ്രൊഫൈൽ",
        "location_summary": "നിങ്ങൾ തിരഞ്ഞെടുത്ത സ്ഥലം",
        "interest_summary": "നിങ്ങൾക്ക് താൽപര്യമുള്ള മേഖലകൾ",

        "years_experience": "വർഷത്തെ പരിചയം",
        "risk_preference_text": "റിസ്ക് മുൻഗണന",

        "prototype_disclaimer": (
            "ഈ റാങ്കിംഗുകൾ പ്രോട്ടോടൈപ്പ് ശുപാർശകളാണ്. "
            "ഇവ വായ്പ അംഗീകാരമോ വിജയത്തിനുള്ള ഉറപ്പോ അല്ല."
        ),

        "opportunity_score": "അവസര സ്കോർ",
        "why_fits": "എന്തുകൊണ്ട് അനുയോജ്യം",
        "confidence": "വിശ്വാസ്യത",
        "prototype_estimate": "പ്രോട്ടോടൈപ്പ് കണക്ക്",

        "demand": "ആവശ്യം",
        "competition": "മത്സരം",
        "skill_fit": "കഴിവ് അനുയോജ്യത",
        "capital_fit": "മൂലധന അനുയോജ്യത",
        "risk_fit": "റിസ്ക് അനുയോജ്യത",

        "back_to_market": "പ്രാദേശിക വിപണിയിലേക്ക് തിരികെ",
    },
}


# ============================================================
# KERALA DATA
# ============================================================

KERALA_DISTRICTS = [
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


LOCAL_BODIES = {
    "Alappuzha": [
        "Alappuzha Municipality",
        "Cherthala Municipality",
        "Kayamkulam Municipality",
    ],
    "Ernakulam": [
        "Kochi Municipal Corporation",
        "Aluva Municipality",
        "Perumbavoor Municipality",
    ],
    "Idukki": [
        "Thodupuzha Municipality",
        "Kattappana Municipality",
        "Adimali",
    ],
    "Kannur": [
        "Kannur Municipal Corporation",
        "Payyannur Municipality",
        "Thalassery Municipality",
    ],
    "Kasaragod": [
        "Kasaragod Municipality",
        "Kanhangad Municipality",
        "Nileshwar Municipality",
    ],
    "Kollam": [
        "Kollam Municipal Corporation",
        "Karunagappally Municipality",
        "Kottarakkara Municipality",
    ],
    "Kottayam": [
        "Kottayam Municipality",
        "Changanassery Municipality",
        "Pala Municipality",
    ],
    "Kozhikode": [
        "Kozhikode Municipal Corporation",
        "Vadakara Municipality",
        "Koyilandy Municipality",
    ],
    "Malappuram": [
        "Malappuram Municipality",
        "Manjeri Municipality",
        "Tirur Municipality",
    ],
    "Palakkad": [
        "Palakkad Municipality",
        "Ottappalam Municipality",
        "Shoranur Municipality",
    ],
    "Pathanamthitta": [
        "Pathanamthitta Municipality",
        "Adoor Municipality",
        "Thiruvalla Municipality",
    ],
    "Thiruvananthapuram": [
        "Thiruvananthapuram Municipal Corporation",
        "Nedumangad Municipality",
        "Attingal Municipality",
    ],
    "Thrissur": [
        "Thrissur Municipal Corporation",
        "Chalakudy Municipality",
        "Kunnamkulam Municipality",
    ],
    "Wayanad": [
        "Kalpetta Municipality",
        "Mananthavady Municipality",
        "Sulthan Bathery Municipality",
    ],
}


DISTRICT_COORDS = {
    "Alappuzha": (9.4981, 76.3388),
    "Ernakulam": (9.9816, 76.2999),
    "Idukki": (9.9189, 76.9410),
    "Kannur": (11.8745, 75.3704),
    "Kasaragod": (12.5102, 74.9852),
    "Kollam": (8.8932, 76.6141),
    "Kottayam": (9.5916, 76.5222),
    "Kozhikode": (11.2588, 75.7804),
    "Malappuram": (11.0510, 76.0711),
    "Palakkad": (10.7867, 76.6548),
    "Pathanamthitta": (9.2648, 76.7870),
    "Thiruvananthapuram": (8.5241, 76.9366),
    "Thrissur": (10.5276, 76.2144),
    "Wayanad": (11.6854, 76.1320),
}


# ============================================================
# PROFILE OPTIONS
# ============================================================

SKILL_KEYS = [
    "Tailoring",
    "Cooking / Food Preparation",
    "Repair / Technical Work",
    "Farming / Agriculture",
    "Handicrafts",
    "Sales / Retail",
    "Digital / Computer Skills",
    "Driving / Transport",
]


INTEREST_KEYS = [
    "Agriculture",
    "Food & Bakery",
    "Tailoring",
    "Repair Services",
    "Handicrafts",
    "Retail",
    "Livestock / Dairy",
    "Digital Services",
]


# ============================================================
# SESSION STATE
# ============================================================

DEFAULT_STATE = {
    "page": 1,
    "language": "en",

    "skills": [],
    "experience": 0,
    "capital": 50000,
    "interests": [],
    "risk": "Medium",

    "existing_business": "No",
    "business_name": "",

    "district": "Kozhikode",
    "local_body": "Kozhikode Municipal Corporation",
    "ward": 1,

    "selected_business": None,
}


for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# TRANSLATION HELPER
# ============================================================

def t(key):
    language = st.session_state.get("language", "en")
    return TEXT.get(language, TEXT["en"]).get(key, key)


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* --------------------------------------------------------
       GLOBAL
       -------------------------------------------------------- */

    .stApp {{
        background-color: {BACKGROUND_CREAM};
        color: {TEXT_BROWN};
    }}

    .block-container {{
        max-width: 1400px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }}

    h1, h2, h3, h4, h5, h6 {{
        color: {TEXT_BROWN} !important;
    }}

    p, label, span, div {{
        color: {TEXT_BROWN};
    }}


    /* --------------------------------------------------------
       HEADER
       -------------------------------------------------------- */

    .gv-header {{
        background: {WHITE};
        border: 1px solid #E7E3D8;
        border-radius: 18px;
        padding: 20px 24px;
        margin-bottom: 10px;
        box-shadow: 0 4px 14px rgba(82, 106, 58, 0.05);
    }}

    .gv-header-title {{
        font-size: 28px;
        font-weight: 750;
        color: {PRIMARY_GREEN};
        line-height: 1.2;
    }}

    .gv-header-subtitle {{
        font-size: 14px;
        color: #6F7467;
        margin-top: 5px;
    }}


    /* --------------------------------------------------------
       STEPS
       -------------------------------------------------------- */

    .gv-steps {{
        display: flex;
        gap: 10px;
        margin: 14px 0 24px 0;
    }}

    .gv-step {{
        flex: 1;
        padding: 10px 14px;
        border-radius: 12px;
        text-align: center;
        font-size: 13px;
        font-weight: 650;
        border: 1px solid #DDD9CD;
        background: #F2F0E8;
        color: #74786D;
    }}

    .gv-step.active {{
        background: {PRIMARY_GREEN};
        color: white !important;
        border-color: {PRIMARY_GREEN};
    }}


    /* --------------------------------------------------------
       GENERIC CARDS
       -------------------------------------------------------- */

    .gv-card {{
        background: {WHITE};
        border: 1px solid #E7E3D8;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 3px 12px rgba(51, 53, 44, 0.04);
    }}

    .gv-card-title {{
        font-size: 18px;
        font-weight: 700;
        color: {TEXT_BROWN};
        margin-bottom: 5px;
    }}

    .gv-card-subtitle {{
        font-size: 13px;
        color: #75796F;
    }}


    /* --------------------------------------------------------
       METRIC CARDS
       -------------------------------------------------------- */

    .gv-metric {{
        background: {WHITE};
        border: 1px solid #E7E3D8;
        border-radius: 16px;
        padding: 18px;
        min-height: 110px;
        box-shadow: 0 3px 12px rgba(51, 53, 44, 0.04);
    }}

    .gv-metric-label {{
        font-size: 13px;
        color: #73776D;
        margin-bottom: 7px;
    }}

    .gv-metric-value {{
        font-size: 25px;
        font-weight: 750;
        color: {PRIMARY_GREEN};
    }}

    .gv-metric-note {{
        font-size: 12px;
        color: #8A8D83;
        margin-top: 4px;
    }}


    /* --------------------------------------------------------
       SOURCE BOX
       -------------------------------------------------------- */

    .gv-source {{
        background: #F4F2EB;
        border: 1px solid #E1DDD1;
        border-radius: 12px;
        padding: 12px 15px;
        margin-top: 12px;
        font-size: 12px;
        color: #686C62;
    }}


    /* ========================================================
       FRAME 3 — OPPORTUNITY RADAR
       ======================================================== */

    .gv3-page-title {{
        font-size: 32px;
        font-weight: 780;
        color: {TEXT_BROWN};
        margin-bottom: 4px;
    }}

    .gv3-page-subtitle {{
        font-size: 15px;
        color: #74786E;
        margin-bottom: 22px;
    }}


    /* --------------------------------------------------------
       SUMMARY CARDS
       -------------------------------------------------------- */

    .gv3-summary-card {{
        background: {WHITE};
        border: 1px solid #E5E1D7;
        border-radius: 16px;
        padding: 18px 20px;
        min-height: 128px;
        box-shadow: 0 3px 12px rgba(51, 53, 44, 0.04);
    }}

    .gv3-summary-title {{
        font-size: 13px;
        font-weight: 650;
        color: #73776D;
        margin-bottom: 10px;
    }}

    .gv3-summary-main {{
        font-size: 22px;
        font-weight: 760;
        color: {PRIMARY_GREEN};
        line-height: 1.2;
    }}

    .gv3-summary-small {{
        font-size: 13px;
        color: #777B72;
        margin-top: 7px;
    }}


    /* --------------------------------------------------------
       DISCLAIMER
       -------------------------------------------------------- */

    .gv3-disclaimer {{
        background: #FFF8EA;
        border: 1px solid #E7D3AA;
        border-radius: 13px;
        padding: 13px 16px;
        margin: 18px 0 20px 0;
        font-size: 12px;
        line-height: 1.5;
        color: #725A31;
    }}


    /* --------------------------------------------------------
       OPPORTUNITY CARD
       -------------------------------------------------------- */

    .gv3-opportunity-card {{
        background: {WHITE};
        border: 1px solid #E3DFD4;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 14px rgba(51, 53, 44, 0.045);
    }}

    .gv3-opportunity-card.top {{
        border: 2px solid {SECONDARY_GREEN};
        background: #FBFCF8;
    }}

    .gv3-opportunity-top {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 20px;
        margin-bottom: 17px;
    }}

    .gv3-opportunity-left {{
        display: flex;
        align-items: flex-start;
        gap: 13px;
    }}

    .gv3-opportunity-rank {{
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: {PRIMARY_GREEN};
        color: white !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 750;
        font-size: 15px;
        flex-shrink: 0;
    }}

    .gv3-opportunity-name {{
        font-size: 22px;
        font-weight: 760;
        color: {TEXT_BROWN};
        line-height: 1.2;
    }}

    .gv3-opportunity-score-text {{
        font-size: 13px;
        color: #777B72;
        margin-top: 5px;
    }}

    .gv3-score-box {{
        min-width: 82px;
        text-align: center;
        background: #F1F4EA;
        border-radius: 13px;
        padding: 9px 10px;
        border: 1px solid #DCE4CF;
    }}

    .gv3-score-number {{
        font-size: 27px;
        font-weight: 800;
        color: {PRIMARY_GREEN};
        line-height: 1;
    }}

    .gv3-score-label {{
        font-size: 10px;
        color: #73786C;
        margin-top: 4px;
    }}


    /* --------------------------------------------------------
       FIT BARS
       -------------------------------------------------------- */

    .gv3-fit-row {{
        display: grid;
        grid-template-columns: 145px 1fr 45px;
        align-items: center;
        gap: 12px;
        margin: 9px 0;
    }}

    .gv3-fit-label {{
        font-size: 12px;
        color: #666B61;
    }}

    .gv3-fit-track {{
        height: 9px;
        background: #E9E7DF;
        border-radius: 20px;
        overflow: hidden;
    }}

    .gv3-fit-fill {{
        height: 100%;
        background: {SECONDARY_GREEN};
        border-radius: 20px;
    }}

    .gv3-fit-value {{
        font-size: 12px;
        font-weight: 700;
        text-align: right;
        color: {TEXT_BROWN};
    }}


    /* --------------------------------------------------------
       WHY THIS FITS
       -------------------------------------------------------- */

    .gv3-why {{
        background: #F8F7F2;
        border-radius: 12px;
        padding: 13px 15px;
        margin-top: 17px;
        font-size: 13px;
        line-height: 1.5;
        color: #62665D;
    }}

    .gv3-why-title {{
        font-size: 12px;
        font-weight: 750;
        color: {TEXT_BROWN};
        margin-bottom: 5px;
    }}


    /* --------------------------------------------------------
       CONFIDENCE
       -------------------------------------------------------- */

    .gv3-confidence {{
        display: inline-block;
        background: #F2F0E9;
        border: 1px solid #DFDBCF;
        border-radius: 20px;
        padding: 6px 11px;
        font-size: 11px;
        color: #676B62;
        margin-top: 13px;
    }}


    /* --------------------------------------------------------
       BUTTONS
       -------------------------------------------------------- */

    .stButton > button {{
        border-radius: 10px !important;
        font-weight: 650 !important;
        min-height: 42px;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

def render_header():
    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown(
            f"""
            <div class="gv-header">
                <div class="gv-header-title">🌱 {t("app_title")}</div>
                <div class="gv-header-subtitle">{t("tagline")}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        language_options = ["English", "മലയാളം"]

        current_language_display = (
            "English"
            if st.session_state.language == "en"
            else "മലയാളം"
        )

        selected_language = st.selectbox(
            "Language",
            language_options,
            index=language_options.index(current_language_display),
            key="language_selector",
        )

        new_language = "en" if selected_language == "English" else "ml"

        if new_language != st.session_state.language:
            st.session_state.language = new_language
            st.rerun()


# ============================================================
# STEP INDICATOR
# ============================================================

def render_steps():
    current_page = st.session_state.page

    step1_class = "active" if current_page == 1 else ""
    step2_class = "active" if current_page == 2 else ""
    step3_class = "active" if current_page == 3 else ""

    st.markdown(
        f"""
        <div class="gv-steps">

            <div class="gv-step {step1_class}">
                1 · {t("step1")}
            </div>

            <div class="gv-step {step2_class}">
                2 · {t("step2")}
            </div>

            <div class="gv-step {step3_class}">
                3 · {t("step3")}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# FRAME 1 — PROFILE INPUT
# ============================================================

def render_frame_1():

    st.markdown(
        f"""
        <div class="gv-card">
            <div class="gv-card-title">{t("profile_title")}</div>
            <div class="gv-card-subtitle">{t("profile_subtitle")}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"### {t('skills')}")

        skills = st.multiselect(
            t("skills"),
            SKILL_KEYS,
            default=st.session_state.skills,
            key="skills_input",
        )

        st.session_state.skills = skills

        experience = st.number_input(
            t("experience"),
            min_value=0,
            max_value=50,
            value=int(st.session_state.experience),
            step=1,
            key="experience_input",
        )

        st.session_state.experience = experience

        capital = st.slider(
            t("capital"),
            min_value=0,
            max_value=500000,
            value=int(st.session_state.capital),
            step=5000,
            key="capital_input",
            format="₹%d",
        )

        st.session_state.capital = capital

    with col2:

        interests = st.multiselect(
            t("interests"),
            INTEREST_KEYS,
            default=st.session_state.interests,
            key="interests_input",
        )

        st.session_state.interests = interests

        risk = st.radio(
            t("risk_preference"),
            ["Low", "Medium", "High"],
            index=["Low", "Medium", "High"].index(
                st.session_state.risk
            ),
            horizontal=True,
            key="risk_input",
        )

        st.session_state.risk = risk

        existing_business = st.radio(
            t("existing_business"),
            ["No", "Yes"],
            index=["No", "Yes"].index(
                st.session_state.existing_business
            ),
            horizontal=True,
            key="existing_business_input",
        )

        st.session_state.existing_business = existing_business

        if existing_business == "Yes":

            business_name = st.text_input(
                t("business_name"),
                value=st.session_state.business_name,
                key="business_name_input",
            )

            st.session_state.business_name = business_name

    st.write("")

    if st.button(
        t("continue"),
        use_container_width=True,
        key="continue_frame1",
    ):
        st.session_state.page = 2
        st.rerun()


# ============================================================
# LOCATION DATA
# ============================================================

def generate_location_data(district, local_body, ward):

    district_seed = sum(
        ord(char) for char in district
    )

    local_seed = sum(
        ord(char) for char in local_body
    )

    seed = district_seed + local_seed + int(ward)

    rng = np.random.default_rng(seed)

    population = int(
        rng.integers(45000, 180000)
    )

    business_density = int(
        rng.integers(35, 85)
    )

    seasonal_demand = int(
        rng.integers(50, 90)
    )

    resource_availability = int(
        rng.integers(45, 88)
    )

    return {
        "population": population,
        "business_density": business_density,
        "seasonal_demand": seasonal_demand,
        "resource_availability": resource_availability,
    }


# ============================================================
# MAP DATA
# ============================================================

def generate_business_points(
    district,
    local_body,
    ward,
):

    lat, lon = DISTRICT_COORDS.get(
        district,
        (11.2588, 75.7804),
    )

    return pd.DataFrame(
        [
            {
                "lat": lat,
                "lon": lon,
            }
        ]
    )


# ============================================================
# FRAME 2 — LOCAL DASHBOARD
# ============================================================

def render_frame_2():

    st.markdown(
        f"""
        <div class="gv-card">
            <div class="gv-card-title">
                {t("local_title")}
            </div>

            <div class="gv-card-subtitle">
                {t("local_subtitle")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        district = st.selectbox(
            t("district"),
            KERALA_DISTRICTS,
            index=KERALA_DISTRICTS.index(
                st.session_state.district
            ),
            key="district_selector",
        )

        st.session_state.district = district

    available_local_bodies = LOCAL_BODIES.get(
        district,
        [],
    )

    if (
        st.session_state.local_body
        not in available_local_bodies
    ):
        st.session_state.local_body = (
            available_local_bodies[0]
            if available_local_bodies
            else ""
        )

    with col2:

        local_body = st.selectbox(
            t("local_body"),
            available_local_bodies,
            index=available_local_bodies.index(
                st.session_state.local_body
            ),
            key="local_body_selector",
        )

        st.session_state.local_body = local_body

    with col3:

        ward = st.number_input(
            t("ward"),
            min_value=1,
            max_value=100,
            value=int(st.session_state.ward),
            step=1,
            key="ward_selector",
        )

        st.session_state.ward = ward

    st.write("")

    data = generate_location_data(
        district,
        local_body,
        ward,
    )

    info_col1, info_col2 = st.columns(2)

    with info_col1:

        st.markdown(
            f"""
            <div class="gv-source">

                <b>{t("data_level")}</b><br>

                Ward-level selection with district
                prototype reference data.

            </div>
            """,
            unsafe_allow_html=True,
        )

    with info_col2:

        st.markdown(
            f"""
            <div class="gv-source">

                <b>{t("data_source")}</b><br>

                {t("prototype_source")} ·
                {t("prototype_status")}

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:

        st.markdown(
            f"""
            <div class="gv-metric">

                <div class="gv-metric-label">
                    {t("business_density")}
                </div>

                <div class="gv-metric-value">
                    {data["business_density"]}/100
                </div>

                <div class="gv-metric-note">
                    Prototype estimate
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric2:

        st.markdown(
            f"""
            <div class="gv-metric">

                <div class="gv-metric-label">
                    {t("population")}
                </div>

                <div class="gv-metric-value">
                    {data["population"]:,}
                </div>

                <div class="gv-metric-note">
                    Prototype reference
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric3:

        st.markdown(
            f"""
            <div class="gv-metric">

                <div class="gv-metric-label">
                    {t("seasonal_demand")}
                </div>

                <div class="gv-metric-value">
                    {data["seasonal_demand"]}/100
                </div>

                <div class="gv-metric-note">
                    Prototype estimate
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric4:

        st.markdown(
            f"""
            <div class="gv-metric">

                <div class="gv-metric-label">
                    {t("resource_availability")}
                </div>

                <div class="gv-metric-value">
                    {data["resource_availability"]}/100
                </div>

                <div class="gv-metric-note">
                    Prototype estimate
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    st.markdown(
        f"""
        <div class="gv-card">

            <div class="gv-card-title">
                {t("map_title")}
            </div>

            <div class="gv-card-subtitle">
                {district} · {local_body} · Ward {ward}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    map_data = generate_business_points(
        district,
        local_body,
        ward,
    )

    st.map(
        map_data,
        latitude="lat",
        longitude="lon",
        size=80,
    )

    st.markdown(
        f"""
        <div class="gv-source">
            {t("map_note")}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col_back, col_continue = st.columns(2)

    with col_back:

        if st.button(
            t("back"),
            use_container_width=True,
            key="back_frame2",
        ):
            st.session_state.page = 1
            st.rerun()

    with col_continue:

        if st.button(
            t("continue"),
            use_container_width=True,
            key="continue_frame2",
        ):
            st.session_state.page = 3
            st.rerun()





# ============================================================
# MAIN APP
# ============================================================

render_header()

st.write("")

render_steps()

st.write("")


if st.session_state.page == 1:

    render_frame_1()

elif st.session_state.page == 2:

    render_frame_2()
    
elif st.session_state.page == 3:
    
    render_frame3()

