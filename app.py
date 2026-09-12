import streamlit as st
import pandas as pd
import numpy as np


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
# PALETTE
# ============================================================

PRIMARY_GREEN = "#526A3A"
SECONDARY_GREEN = "#7D9A55"
EARTH_ORANGE = "#C88A3D"
WARM_CREAM = "#FAF8F1"
DARK_BROWN = "#33352C"
WHITE = "#FFFFFF"

LIGHT_GREEN = "#EAF0E3"
LIGHT_ORANGE = "#F5E8D5"
LIGHT_BLUE = "#E7F1F7"


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {
    "en": {
        "app_title": "GramVyapar AI",
        "tagline": "Know Before You Borrow",

        "step1": "1. Profile",
        "step2": "2. Local Market",
        "step3": "3. Business Plan",

        "profile_title": "Tell us about yourself",
        "profile_subtitle": "This helps GramVyapar AI understand your skills, capital and business interests.",

        "skills_title": "What skills do you have?",
        "select_skills": "Select your skills",

        "experience_title": "How much experience do you have?",
        "experience_help": "Years of experience",
        "years": "years",

        "capital_title": "How much capital can you invest?",
        "capital_help": "Available capital",

        "business_interest_question": "Which business areas interest you?",

        "risk_title": "How much business risk are you comfortable with?",

        "existing_business_question": "Do you already have an existing business?",
        "yes": "Yes",
        "no": "No",

        "business_name": "Existing business name",

        "continue": "Continue",
        "back": "Back",

        "local_title": "Your Local Market",
        "local_subtitle": "Understand the local business environment before investing.",

        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward",

        "ward_data": "Ward-level data",
        "district_data": "District-level fallback",

        "location_note": "The current prototype uses structured demo estimates for the selected location.",

        "business_density": "Business Density",
        "population": "Population",
        "seasonal_demand": "Seasonal Demand",
        "resource_availability": "Resource Availability",

        "business_density_help": "Estimated number of businesses in the selected area.",
        "population_help": "Population reference for the selected administrative area.",
        "seasonal_demand_help": "Estimated seasonal demand level.",
        "resource_availability_help": "Availability of relevant local resources.",

        "map_title": "Local Area Reference Map",
        "map_caption": "The marker represents the selected district/local-area reference point. It is not an exact business location.",

        "data_source": "Source",
        "prototype_source": "Prototype / demo estimate",
        "data_status": "Data status",
        "prototype_status": "Prototype / demo",

        "language": "Language",

        "skill_farming": "Farming",
        "skill_cooking": "Cooking",
        "skill_tailoring": "Tailoring",
        "skill_repair": "Repair / Technical",
        "skill_sales": "Sales",
        "skill_accounting": "Accounting",
        "skill_driving": "Driving",
        "skill_handicraft": "Handicrafts",

        "interest_dairy": "Dairy",
        "interest_bakery": "Bakery / Food",
        "interest_tailoring": "Tailoring",
        "interest_retail": "Retail",
        "interest_agriculture": "Agriculture",
        "interest_repair": "Repair Services",
        "interest_beauty": "Beauty / Personal Care",
        "interest_handicraft": "Handicrafts",

        "risk_low": "Low",
        "risk_medium": "Medium",
        "risk_high": "High",

        # ----------------------------------------------------
        # FRAME 3
        # ----------------------------------------------------

        "opportunity_title": "Opportunity Radar",
        "opportunity_subtitle": "Explore business opportunities that match your profile and local market.",

        "your_location": "Your selected location",
        "your_profile": "Your profile",

        "opportunity_score": "Opportunity Score",
        "demand": "Demand",
        "competition": "Competition",
        "skill_fit": "Skill Fit",
        "capital_fit": "Capital Fit",
        "risk_fit": "Risk Fit",

        "high": "High",
        "medium": "Medium",
        "low": "Low",

        "why_fit": "Why this fits you",
        "confidence": "Confidence",
        "prototype_confidence": "Prototype estimate",

        "rank_1": "Strongest match",
        "rank_2": "Good match",
        "rank_3": "Potential match",

        "opportunity_note": "These rankings are prototype recommendations. They are not loan approval or guaranteed business success.",

        "view_business": "View Business",
        "frame3_back": "Back",
    },

    "ml": {
        "app_title": "ഗ്രാമവ്യാപാർ AI",
        "tagline": "വായ്പ എടുക്കുന്നതിന് മുമ്പ് അറിയൂ",

        "step1": "1. പ്രൊഫൈൽ",
        "step2": "2. പ്രാദേശിക വിപണി",
        "step3": "3. ബിസിനസ് പ്ലാൻ",

        "profile_title": "നിങ്ങളെക്കുറിച്ച് പറയൂ",
        "profile_subtitle": "നിങ്ങളുടെ കഴിവുകൾ, മൂലധനം, ബിസിനസ് താൽപര്യങ്ങൾ എന്നിവ മനസ്സിലാക്കാൻ ഇത് സഹായിക്കും.",

        "skills_title": "നിങ്ങളുടെ കഴിവുകൾ എന്തൊക്കെയാണ്?",
        "select_skills": "നിങ്ങളുടെ കഴിവുകൾ തിരഞ്ഞെടുക്കുക",

        "experience_title": "നിങ്ങൾക്ക് എത്ര വർഷത്തെ പരിചയമുണ്ട്?",
        "experience_help": "പരിചയമുള്ള വർഷങ്ങൾ",
        "years": "വർഷങ്ങൾ",

        "capital_title": "നിങ്ങൾക്ക് എത്ര മൂലധനം നിക്ഷേപിക്കാനാകും?",
        "capital_help": "ലഭ്യമായ മൂലധനം",

        "business_interest_question": "ഏത് ബിസിനസ് മേഖലകളിലാണ് നിങ്ങൾക്ക് താൽപര്യം?",

        "risk_title": "എത്രത്തോളം ബിസിനസ് റിസ്ക് എടുക്കാൻ നിങ്ങൾ തയ്യാറാണ്?",

        "existing_business_question": "നിങ്ങൾക്ക് നിലവിൽ ഒരു ബിസിനസ് ഉണ്ടോ?",
        "yes": "അതെ",
        "no": "ഇല്ല",

        "business_name": "നിലവിലുള്ള ബിസിനസിന്റെ പേര്",

        "continue": "തുടരുക",
        "back": "തിരികെ",

        "local_title": "നിങ്ങളുടെ പ്രാദേശിക വിപണി",
        "local_subtitle": "നിക്ഷേപിക്കുന്നതിന് മുമ്പ് പ്രാദേശിക ബിസിനസ് സാഹചര്യം മനസ്സിലാക്കുക.",

        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ്",

        "ward_data": "വാർഡ് തല ഡാറ്റ",
        "district_data": "ജില്ലാ തലത്തിലുള്ള പകരം ഡാറ്റ",

        "location_note": "തിരഞ്ഞെടുത്ത സ്ഥലത്തിനായി നിലവിലെ പ്രോട്ടോടൈപ്പ് ഘടനാപരമായ ഡെമോ കണക്കുകൾ ഉപയോഗിക്കുന്നു.",

        "business_density": "ബിസിനസ് സാന്ദ്രത",
        "population": "ജനസംഖ്യ",
        "seasonal_demand": "കാലാവസ്ഥാനുസൃത ആവശ്യകത",
        "resource_availability": "വിഭവ ലഭ്യത",

        "business_density_help": "തിരഞ്ഞെടുത്ത പ്രദേശത്തെ കണക്കാക്കിയ ബിസിനസുകളുടെ എണ്ണം.",
        "population_help": "തിരഞ്ഞെടുത്ത ഭരണപ്രദേശത്തിന്റെ ജനസംഖ്യാ റഫറൻസ്.",
        "seasonal_demand_help": "കണക്കാക്കിയ കാലാവസ്ഥാനുസൃത ആവശ്യകത.",
        "resource_availability_help": "പ്രാദേശികമായി ലഭ്യമായ ബന്ധപ്പെട്ട വിഭവങ്ങൾ.",

        "map_title": "പ്രാദേശിക പ്രദേശ റഫറൻസ് മാപ്പ്",
        "map_caption": "തിരഞ്ഞെടുത്ത ജില്ല/പ്രാദേശിക പ്രദേശത്തിന്റെ റഫറൻസ് പോയിന്റാണ് മാപ്പിലെ മാർക്കർ. ഇത് കൃത്യമായ ബിസിനസ് ലൊക്കേഷൻ അല്ല.",

        "data_source": "ഉറവിടം",
        "prototype_source": "പ്രോട്ടോടൈപ്പ് / ഡെമോ കണക്ക്",
        "data_status": "ഡാറ്റാ നില",
        "prototype_status": "പ്രോട്ടോടൈപ്പ് / ഡെമോ",

        "language": "ഭാഷ",

        "skill_farming": "കൃഷി",
        "skill_cooking": "പാചകം",
        "skill_tailoring": "തയ്യൽ",
        "skill_repair": "റിപ്പയർ / സാങ്കേതികം",
        "skill_sales": "വിൽപ്പന",
        "skill_accounting": "അക്കൗണ്ടിംഗ്",
        "skill_driving": "ഡ്രൈവിംഗ്",
        "skill_handicraft": "കരകൗശലം",

        "interest_dairy": "ക്ഷീരവ്യവസായം",
        "interest_bakery": "ബേക്കറി / ഭക്ഷണം",
        "interest_tailoring": "തയ്യൽ",
        "interest_retail": "റീട്ടെയിൽ",
        "interest_agriculture": "കൃഷി",
        "interest_repair": "റിപ്പയർ സേവനങ്ങൾ",
        "interest_beauty": "ബ്യൂട്ടി / വ്യക്തിഗത പരിചരണം",
        "interest_handicraft": "കരകൗശലം",

        "risk_low": "കുറവ്",
        "risk_medium": "മിതമായ",
        "risk_high": "ഉയർന്ന",

        # ----------------------------------------------------
        # FRAME 3
        # ----------------------------------------------------

        "opportunity_title": "ബിസിനസ് അവസരങ്ങൾ",
        "opportunity_subtitle": "നിങ്ങളുടെ പ്രൊഫൈലിനും പ്രാദേശിക വിപണിക്കും അനുയോജ്യമായ ബിസിനസ് അവസരങ്ങൾ കണ്ടെത്തുക.",

        "your_location": "തിരഞ്ഞെടുത്ത സ്ഥലം",
        "your_profile": "നിങ്ങളുടെ പ്രൊഫൈൽ",

        "opportunity_score": "അവസര സ്കോർ",
        "demand": "ആവശ്യകത",
        "competition": "മത്സരം",
        "skill_fit": "കഴിവ് അനുയോജ്യത",
        "capital_fit": "മൂലധന അനുയോജ്യത",
        "risk_fit": "റിസ്ക് അനുയോജ്യത",

        "high": "ഉയർന്ന",
        "medium": "മിതമായ",
        "low": "കുറവ്",

        "why_fit": "ഇത് നിങ്ങൾക്ക് അനുയോജ്യമാകുന്നത് എന്തുകൊണ്ട്",
        "confidence": "വിശ്വാസ്യത",
        "prototype_confidence": "പ്രോട്ടോടൈപ്പ് കണക്ക്",

        "rank_1": "ഏറ്റവും ശക്തമായ പൊരുത്തം",
        "rank_2": "നല്ല പൊരുത്തം",
        "rank_3": "സാധ്യതയുള്ള പൊരുത്തം",

        "opportunity_note": "ഈ റാങ്കിംഗുകൾ പ്രോട്ടോടൈപ്പ് ശുപാർശകളാണ്. ഇവ വായ്പാ അംഗീകാരമോ ബിസിനസ് വിജയത്തിനുള്ള ഉറപ്പോ അല്ല.",

        "view_business": "ബിസിനസ് കാണുക",
        "frame3_back": "തിരികെ",
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
        "Chengannur Municipality",
        "Cherthala Municipality",
    ],
    "Ernakulam": [
        "Kochi Municipal Corporation",
        "Aluva Municipality",
        "Perumbavoor Municipality",
        "Thrippunithura Municipality",
    ],
    "Idukki": [
        "Thodupuzha Municipality",
        "Kattappana Municipality",
    ],
    "Kannur": [
        "Kannur Municipal Corporation",
        "Thalassery Municipality",
        "Payyannur Municipality",
    ],
    "Kasaragod": [
        "Kasaragod Municipality",
        "Kanhangad Municipality",
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
        "Ramanattukara Municipality",
    ],
    "Malappuram": [
        "Malappuram Municipality",
        "Manjeri Municipality",
        "Tirur Municipality",
        "Ponnani Municipality",
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
        "Thiruvananthapuram Corporation",
        "Neyyattinkara Municipality",
        "Attingal Municipality",
    ],
    "Thrissur": [
        "Thrissur Municipal Corporation",
        "Chalakudy Municipality",
        "Kunnamkulam Municipality",
        "Kodungallur Municipality",
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
    "Idukki": (9.8494, 76.9724),
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
# SKILLS / INTERESTS
# ============================================================

SKILL_KEYS = [
    ("Farming", "skill_farming"),
    ("Cooking", "skill_cooking"),
    ("Tailoring", "skill_tailoring"),
    ("Repair / Technical", "skill_repair"),
    ("Sales", "skill_sales"),
    ("Accounting", "skill_accounting"),
    ("Driving", "skill_driving"),
    ("Handicrafts", "skill_handicraft"),
]


INTEREST_KEYS = [
    ("Dairy", "interest_dairy"),
    ("Bakery / Food", "interest_bakery"),
    ("Tailoring", "interest_tailoring"),
    ("Retail", "interest_retail"),
    ("Agriculture", "interest_agriculture"),
    ("Repair Services", "interest_repair"),
    ("Beauty / Personal Care", "interest_beauty"),
    ("Handicrafts", "interest_handicraft"),
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
    "selected_opportunity": None,
}


for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {WARM_CREAM};
        color: {DARK_BROWN};
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }}

    /* Header */
    .gv-header {{
        background: {PRIMARY_GREEN};
        padding: 22px 28px;
        border-radius: 18px;
        margin-bottom: 22px;
    }}

    .gv-header-title {{
        color: white !important;
        font-size: 30px;
        font-weight: 750;
        margin: 0;
    }}

    .gv-header-subtitle {{
        color: #F2F5EC !important;
        font-size: 15px;
        margin-top: 4px;
    }}

    /* Normal page text */
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6,
    .stApp p,
    .stApp label {{
        color: {DARK_BROWN};
    }}

    .stApp [data-testid="stMarkdownContainer"] {{
        color: {DARK_BROWN};
    }}

    .stApp [data-testid="stCaptionContainer"] {{
        color: {DARK_BROWN} !important;
    }}

    /* Steps */
    .step-active {{
        background: {PRIMARY_GREEN};
        color: white !important;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-weight: 700;
    }}

    .step-inactive {{
        background: #EDEDE7;
        color: {DARK_BROWN} !important;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-weight: 600;
    }}

    /* White cards */
    .metric-card {{
        background: {WHITE};
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #E7E4D9;
        min-height: 150px;
    }}

    .metric-title {{
        font-size: 15px;
        font-weight: 700;
        color: {DARK_BROWN};
    }}

    .metric-value {{
        font-size: 30px;
        font-weight: 800;
        color: {PRIMARY_GREEN};
        margin-top: 8px;
    }}

    .metric-help {{
        font-size: 13px;
        color: #66685F;
        margin-top: 8px;
        line-height: 1.4;
    }}

    .info-card {{
        background: {WHITE};
        border-radius: 16px;
        padding: 18px;
        border: 1px solid #E7E4D9;
    }}

    .source-box {{
        background: {LIGHT_GREEN};
        border-radius: 12px;
        padding: 12px 15px;
        font-size: 13px;
    }}

    .map-note {{
        background: {LIGHT_BLUE};
        border-radius: 12px;
        padding: 12px 15px;
        font-size: 13px;
        margin-bottom: 12px;
    }}

    /* ========================================================
       FRAME 3
       ======================================================== */

    .opportunity-card {{
        background: {WHITE};
        border-radius: 18px;
        padding: 22px;
        border: 1px solid #E7E4D9;
        margin-bottom: 18px;
    }}

    .opportunity-card-top {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }}

    .opportunity-rank {{
        color: {PRIMARY_GREEN};
        font-size: 18px;
        font-weight: 800;
    }}

    .opportunity-name {{
        color: {DARK_BROWN};
        font-size: 23px;
        font-weight: 800;
        margin-bottom: 3px;
    }}

    .opportunity-match {{
        color: #66685F;
        font-size: 13px;
        margin-bottom: 15px;
    }}

    .score-box {{
        background: {LIGHT_GREEN};
        border-radius: 14px;
        padding: 12px 18px;
        text-align: center;
        min-width: 105px;
    }}

    .score-number {{
        color: {PRIMARY_GREEN};
        font-size: 27px;
        font-weight: 850;
    }}

    .score-label {{
        color: {DARK_BROWN};
        font-size: 11px;
        font-weight: 700;
    }}

    .fit-row {{
        margin-top: 10px;
    }}

    .fit-label {{
        font-size: 13px;
        font-weight: 700;
        color: {DARK_BROWN};
        margin-bottom: 4px;
    }}

    .fit-track {{
        background: #E9E8E0;
        height: 9px;
        border-radius: 8px;
        overflow: hidden;
    }}

    .fit-fill {{
        background: {SECONDARY_GREEN};
        height: 9px;
        border-radius: 8px;
    }}

    .why-box {{
        background: {LIGHT_ORANGE};
        border-radius: 12px;
        padding: 13px 15px;
        margin-top: 17px;
        font-size: 13px;
        line-height: 1.5;
        color: {DARK_BROWN};
    }}

    .confidence-box {{
        background: #F4F3ED;
        border-radius: 10px;
        padding: 9px 12px;
        margin-top: 12px;
        font-size: 12px;
        color: #66685F;
    }}

    .profile-summary {{
        background: {WHITE};
        border: 1px solid #E7E4D9;
        border-radius: 16px;
        padding: 18px;
        min-height: 130px;
    }}

    .summary-title {{
        font-size: 13px;
        font-weight: 700;
        color: #66685F;
        margin-bottom: 6px;
    }}

    .summary-main {{
        font-size: 17px;
        font-weight: 800;
        color: {DARK_BROWN};
    }}

    .summary-small {{
        font-size: 13px;
        color: #66685F;
        margin-top: 5px;
    }}

    div.stButton > button {{
        border-radius: 10px;
        font-weight: 700;
    }}

    .stSelectbox label,
    .stMultiSelect label,
    .stNumberInput label,
    .stSlider label,
    .stRadio label,
    .stTextInput label {{
        color: {DARK_BROWN} !important;
        font-weight: 600;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# TRANSLATION HELPERS
# ============================================================

def t(key):

    return TEXT[
        st.session_state.language
    ].get(key, key)


def translated_options(items):

    return [
        t(key)
        for _, key in items
    ]


def original_from_translated(
    selected_values,
    items,
):

    mapping = {
        t(key): original
        for original, key in items
    }

    return [
        mapping[value]
        for value in selected_values
        if value in mapping
    ]


def translated_risk_options():

    return [
        t("risk_low"),
        t("risk_medium"),
        t("risk_high"),
    ]


def original_risk_from_translated(value):

    mapping = {
        t("risk_low"): "Low",
        t("risk_medium"): "Medium",
        t("risk_high"): "High",
    }

    return mapping.get(
        value,
        "Medium",
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

        language_options = [
            "English",
            "Malayalam",
        ]

        current_language_display = (
            "English"
            if st.session_state.language == "en"
            else "Malayalam"
        )

        selected_language = st.selectbox(
            t("language"),
            language_options,
            index=language_options.index(
                current_language_display
            ),
            key="language_selector_v4",
        )

        new_language = (
            "en"
            if selected_language == "English"
            else "ml"
        )

        if new_language != st.session_state.language:

            st.session_state.language = new_language

            st.rerun()


# ============================================================
# STEP INDICATOR
# ============================================================

def render_steps():

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.session_state.page == 1:

            st.markdown(
                f'<div class="step-active">{t("step1")}</div>',
                unsafe_allow_html=True,
            )

        else:

            st.markdown(
                f'<div class="step-inactive">{t("step1")}</div>',
                unsafe_allow_html=True,
            )

    with col2:

        if st.session_state.page == 2:

            st.markdown(
                f'<div class="step-active">{t("step2")}</div>',
                unsafe_allow_html=True,
            )

        else:

            st.markdown(
                f'<div class="step-inactive">{t("step2")}</div>',
                unsafe_allow_html=True,
            )

    with col3:

        if st.session_state.page == 3:

            st.markdown(
                f'<div class="step-active">{t("step3")}</div>',
                unsafe_allow_html=True,
            )

        else:

            st.markdown(
                f'<div class="step-inactive">{t("step3")}</div>',
                unsafe_allow_html=True,
            )


# ============================================================
# FRAME 1
# ============================================================

def render_frame_1():

    st.markdown(
        f"## {t('profile_title')}"
    )

    st.caption(
        t("profile_subtitle")
    )

    # ========================================================
    # SKILLS
    # ========================================================

    st.markdown(
        f"### {t('skills_title')}"
    )

    skill_options = translated_options(
        SKILL_KEYS
    )

    valid_saved_skills = [
        skill
        for skill in st.session_state.skills
        if any(
            original == skill
            for original, _ in SKILL_KEYS
        )
    ]

    translated_saved_skills = [
        t(key)
        for original, key in SKILL_KEYS
        if original in valid_saved_skills
    ]

    selected_skills = st.multiselect(
        t("select_skills"),
        skill_options,
        default=translated_saved_skills,
        key="skills_input_v4",
    )

    st.session_state.skills = original_from_translated(
        selected_skills,
        SKILL_KEYS,
    )

    # ========================================================
    # EXPERIENCE
    # ========================================================

    st.markdown(
        f"### {t('experience_title')}"
    )

    experience = st.number_input(
        t("experience_help"),
        min_value=0,
        max_value=50,
        value=int(
            st.session_state.experience
        ),
        step=1,
        key="experience_input_v4",
    )

    st.session_state.experience = experience

    st.caption(
        f"{experience} {t('years')}"
    )

    # ========================================================
    # CAPITAL
    # ========================================================

    st.markdown(
        f"### {t('capital_title')}"
    )

    capital = st.slider(
        t("capital_help"),
        min_value=0,
        max_value=500000,
        value=int(
            st.session_state.capital
        ),
        step=5000,
        key="capital_input_v4",
    )

    st.session_state.capital = capital

    st.write(
        f"**₹{capital:,.0f}**"
    )

    # ========================================================
    # BUSINESS INTERESTS
    # ========================================================

    interest_options = translated_options(
        INTEREST_KEYS
    )

    valid_saved_interests = [
        interest
        for interest in st.session_state.interests
        if any(
            original == interest
            for original, _ in INTEREST_KEYS
        )
    ]

    translated_saved_interests = [
        t(key)
        for original, key in INTEREST_KEYS
        if original in valid_saved_interests
    ]

    interests = st.multiselect(
        t("business_interest_question"),
        interest_options,
        default=translated_saved_interests,
        key="interests_input_v4",
    )

    st.session_state.interests = original_from_translated(
        interests,
        INTEREST_KEYS,
    )

    # ========================================================
    # RISK
    # ========================================================

    st.markdown(
        f"### {t('risk_title')}"
    )

    risk_options = translated_risk_options()

    current_risk_display = t(
        {
            "Low": "risk_low",
            "Medium": "risk_medium",
            "High": "risk_high",
        }.get(
            st.session_state.risk,
            "risk_medium",
        )
    )

    selected_risk = st.radio(
        t("risk_title"),
        risk_options,
        index=risk_options.index(
            current_risk_display
        ),
        horizontal=True,
        key="risk_input_v4",
    )

    st.session_state.risk = (
        original_risk_from_translated(
            selected_risk
        )
    )

    # ========================================================
    # EXISTING BUSINESS
    # ========================================================

    st.markdown(
        f"### {t('existing_business_question')}"
    )

    existing_options = [
        t("yes"),
        t("no"),
    ]

    current_existing_display = (
        t("yes")
        if st.session_state.existing_business == "Yes"
        else t("no")
    )

    existing_business = st.radio(
        t("existing_business_question"),
        existing_options,
        index=existing_options.index(
            current_existing_display
        ),
        horizontal=True,
        key="existing_business_v4",
    )

    st.session_state.existing_business = (
        "Yes"
        if existing_business == t("yes")
        else "No"
    )

    if st.session_state.existing_business == "Yes":

        business_name = st.text_input(
            t("business_name"),
            value=st.session_state.business_name,
            key="business_name_v4",
        )

        st.session_state.business_name = business_name

    st.write("")

    if st.button(
        t("continue"),
        type="primary",
        use_container_width=True,
        key="continue_frame1_v4",
    ):

        st.session_state.page = 2

        st.rerun()


# ============================================================
# LOCATION DATA
# ============================================================

def generate_location_data(
    district,
    local_body,
    ward,
):

    district_index = KERALA_DISTRICTS.index(
        district
    )

    body_list = LOCAL_BODIES.get(
        district,
        [],
    )

    body_index = (
        body_list.index(local_body)
        if local_body in body_list
        else 0
    )

    ward = int(ward)

    population = (
        2500
        + district_index * 175
        + body_index * 250
        + ward * 35
    )

    business_density = (
        35
        + district_index * 2
        + body_index * 4
        + (ward % 10)
    )

    seasonal_demand = int(
        np.clip(
            55
            + ((district_index * 7) % 30)
            + (body_index * 3)
            + (ward % 8),
            0,
            100,
        )
    )

    resource_availability = int(
        np.clip(
            50
            + ((district_index * 5) % 35)
            + body_index * 4,
            0,
            100,
        )
    )

    return {
        "population": population,
        "business_density": business_density,
        "seasonal_demand": seasonal_demand,
        "resource_availability": resource_availability,
    }


# ============================================================
# SAFE MAP POINT
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
# FRAME 2
# ============================================================

def render_frame_2():

    st.markdown(
        f"## {t('local_title')}"
    )

    st.caption(
        t("local_subtitle")
    )

    # ========================================================
    # LOCATION SELECTORS
    # ========================================================

    col1, col2, col3 = st.columns(
        [1.2, 1.5, 0.7]
    )

    with col1:

        district_options = KERALA_DISTRICTS

        district = st.selectbox(
            t("district"),
            district_options,
            index=district_options.index(
                st.session_state.district
            ),
            key="district_input_v4",
        )

        st.session_state.district = district

    with col2:

        body_options = LOCAL_BODIES.get(
            st.session_state.district,
            [],
        )

        if not body_options:
            body_options = ["Local Body"]

        if (
            st.session_state.local_body
            not in body_options
        ):

            st.session_state.local_body = (
                body_options[0]
            )

        local_body = st.selectbox(
            t("local_body"),
            body_options,
            index=body_options.index(
                st.session_state.local_body
            ),
            key="local_body_input_v4",
        )

        st.session_state.local_body = local_body

    with col3:

        ward = st.number_input(
            t("ward"),
            min_value=1,
            max_value=100,
            value=int(
                st.session_state.ward
            ),
            step=1,
            key="ward_input_v4",
        )

        st.session_state.ward = ward

    # ========================================================
    # DATA LEVEL
    # ========================================================

    st.write("")

    data_level_col1, data_level_col2 = st.columns(2)

    with data_level_col1:

        st.markdown(
            f"""
            <div class="source-box">
                <strong>{t("ward_data")}</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with data_level_col2:

        st.markdown(
            f"""
            <div class="source-box">
                <strong>{t("data_status")}:</strong>
                {t("prototype_status")}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    st.info(
        t("location_note")
    )

    # ========================================================
    # LOCATION DATA
    # ========================================================

    location_data = generate_location_data(
        st.session_state.district,
        st.session_state.local_body,
        st.session_state.ward,
    )

    # ========================================================
    # METRICS
    # ========================================================

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    with metric_col1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">
                    {t("business_density")}
                </div>
                <div class="metric-value">
                    {location_data["business_density"]}
                </div>
                <div class="metric-help">
                    {t("business_density_help")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_col2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">
                    {t("population")}
                </div>
                <div class="metric-value">
                    {location_data["population"]:,}
                </div>
                <div class="metric-help">
                    {t("population_help")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_col3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">
                    {t("seasonal_demand")}
                </div>
                <div class="metric-value">
                    {location_data["seasonal_demand"]}%
                </div>
                <div class="metric-help">
                    {t("seasonal_demand_help")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_col4:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">
                    {t("resource_availability")}
                </div>
                <div class="metric-value">
                    {location_data["resource_availability"]}%
                </div>
                <div class="metric-help">
                    {t("resource_availability_help")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ========================================================
    # MAP
    # ========================================================

    st.write("")

    st.markdown(
        f"### {t('map_title')}"
    )

    st.markdown(
        f"""
        <div class="map-note">
            📍 {t("map_caption")}
        </div>
        """,
        unsafe_allow_html=True,
    )

    map_data = generate_business_points(
        st.session_state.district,
        st.session_state.local_body,
        st.session_state.ward,
    )

    st.map(
        map_data,
        latitude="lat",
        longitude="lon",
        zoom=10,
    )

    # ========================================================
    # SOURCE
    # ========================================================

    st.write("")

    source_col1, source_col2 = st.columns(2)

    with source_col1:

        st.markdown(
            f"""
            <div class="source-box">
                <strong>{t("data_source")}:</strong>
                {t("prototype_source")}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with source_col2:

        st.markdown(
            f"""
            <div class="source-box">
                <strong>{t("data_status")}:</strong>
                {t("prototype_status")}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ========================================================
    # NAVIGATION
    # ========================================================

    st.write("")

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            t("back"),
            use_container_width=True,
            key="back_frame2_v4",
        ):

            st.session_state.page = 1
            st.rerun()

    with continue_col:

        if st.button(
            t("continue"),
            type="primary",
            use_container_width=True,
            key="continue_frame2_v4",
        ):

            st.session_state.page = 3
            st.rerun()


# ============================================================
# FRAME 3 — OPPORTUNITY RADAR
# ============================================================

def calculate_opportunity_score(
    business,
    skills,
    interests,
    capital,
    risk,
    location_data,
):

    # --------------------------------------------------------
    # Base prototype values
    # --------------------------------------------------------

    base_values = {

        "Bakery / Food": {
            "demand": 82,
            "competition": 62,
            "skill_fit": 55,
            "capital_fit": 82,
            "risk_fit": 72,
        },

        "Dairy": {
            "demand": 78,
            "competition": 58,
            "skill_fit": 62,
            "capital_fit": 60,
            "risk_fit": 65,
        },

        "Tailoring": {
            "demand": 72,
            "competition": 52,
            "skill_fit": 72,
            "capital_fit": 88,
            "risk_fit": 82,
        },

        "Retail": {
            "demand": 70,
            "competition": 45,
            "skill_fit": 55,
            "capital_fit": 58,
            "risk_fit": 60,
        },

        "Agriculture": {
            "demand": 75,
            "competition": 60,
            "skill_fit": 60,
            "capital_fit": 55,
            "risk_fit": 55,
        },

        "Repair Services": {
            "demand": 76,
            "competition": 65,
            "skill_fit": 70,
            "capital_fit": 78,
            "risk_fit": 76,
        },

        "Beauty / Personal Care": {
            "demand": 74,
            "competition": 60,
            "skill_fit": 55,
            "capital_fit": 72,
            "risk_fit": 74,
        },

        "Handicrafts": {
            "demand": 64,
            "competition": 68,
            "skill_fit": 68,
            "capital_fit": 80,
            "risk_fit": 70,
        },
    }

    values = base_values.get(
        business,
        {
            "demand": 65,
            "competition": 60,
            "skill_fit": 60,
            "capital_fit": 60,
            "risk_fit": 60,
        },
    ).copy()

    # --------------------------------------------------------
    # Demand adjustment from local market
    # --------------------------------------------------------

    demand_adjustment = (
        location_data["seasonal_demand"] - 60
    ) * 0.25

    values["demand"] = int(
        np.clip(
            values["demand"] + demand_adjustment,
            0,
            100,
        )
    )

    # --------------------------------------------------------
    # Competition adjustment
    #
    # Higher competition means lower opportunity fit.
    # --------------------------------------------------------

    competition_pressure = (
        location_data["business_density"] - 40
    ) * 0.25

    values["competition"] = int(
        np.clip(
            values["competition"] - competition_pressure,
            0,
            100,
        )
    )

    # --------------------------------------------------------
    # Skill matching
    # --------------------------------------------------------

    skill_matches = {

        "Bakery / Food": [
            "Cooking",
            "Sales",
        ],

        "Dairy": [
            "Farming",
            "Sales",
        ],

        "Tailoring": [
            "Tailoring",
        ],

        "Retail": [
            "Sales",
            "Accounting",
        ],

        "Agriculture": [
            "Farming",
        ],

        "Repair Services": [
            "Repair / Technical",
        ],

        "Beauty / Personal Care": [
            "Sales",
        ],

        "Handicrafts": [
            "Handicrafts",
            "Sales",
        ],
    }

    matching_skills = [
        skill
        for skill in skills
        if skill in skill_matches.get(
            business,
            [],
        )
    ]

    if matching_skills:

        values["skill_fit"] = int(
            np.clip(
                values["skill_fit"] + 25,
                0,
                100,
            )
        )

    # --------------------------------------------------------
    # Interest matching
    # --------------------------------------------------------

    if business in interests:

        values["demand"] = int(
            np.clip(
                values["demand"] + 10,
                0,
                100,
            )
        )

    # --------------------------------------------------------
    # Capital matching
    # --------------------------------------------------------

    capital_requirements = {

        "Bakery / Food": 80000,
        "Dairy": 100000,
        "Tailoring": 50000,
        "Retail": 100000,
        "Agriculture": 75000,
        "Repair Services": 60000,
        "Beauty / Personal Care": 70000,
        "Handicrafts": 45000,
    }

    required_capital = capital_requirements.get(
        business,
        75000,
    )

    if capital >= required_capital:

        values["capital_fit"] = int(
            np.clip(
                values["capital_fit"] + 12,
                0,
                100,
            )
        )

    elif capital < required_capital * 0.5:

        values["capital_fit"] = int(
            np.clip(
                values["capital_fit"] - 20,
                0,
                100,
            )
        )

    # --------------------------------------------------------
    # Risk preference
    # --------------------------------------------------------

    if risk == "Low":

        if values["risk_fit"] >= 70:
            values["risk_fit"] += 8

        else:
            values["risk_fit"] -= 5

    elif risk == "High":

        values["risk_fit"] = min(
            100,
            values["risk_fit"] + 8,
        )

    values["risk_fit"] = int(
        np.clip(
            values["risk_fit"],
            0,
            100,
        )
    )

    # --------------------------------------------------------
    # Overall score
    #
    # Prototype weighting:
    #
    # Demand        25%
    # Competition   20%
    # Skill Fit     20%
    # Capital Fit   20%
    # Risk Fit      15%
    # --------------------------------------------------------

    score = (
        values["demand"] * 0.25
        + values["competition"] * 0.20
        + values["skill_fit"] * 0.20
        + values["capital_fit"] * 0.20
        + values["risk_fit"] * 0.15
    )

    return values, int(round(score))


# ============================================================
# FRAME 3 DATA
# ============================================================

def generate_opportunities():

    location_data = generate_location_data(
        st.session_state.district,
        st.session_state.local_body,
        st.session_state.ward,
    )

    interests = st.session_state.interests
    skills = st.session_state.skills
    capital = st.session_state.capital
    risk = st.session_state.risk

    all_businesses = [
        "Bakery / Food",
        "Dairy",
        "Tailoring",
        "Retail",
        "Agriculture",
        "Repair Services",
        "Beauty / Personal Care",
        "Handicrafts",
    ]

    opportunities = []

    for business in all_businesses:

        values, score = calculate_opportunity_score(
            business,
            skills,
            interests,
            capital,
            risk,
            location_data,
        )

        opportunities.append(
            {
                "business": business,
                "score": score,
                "demand": values["demand"],
                "competition": values["competition"],
                "skill_fit": values["skill_fit"],
                "capital_fit": values["capital_fit"],
                "risk_fit": values["risk_fit"],
            }
        )

    opportunities = sorted(
        opportunities,
        key=lambda x: x["score"],
        reverse=True,
    )

    return opportunities[:3]


# ============================================================
# FRAME 3 CARD
# ============================================================

def render_opportunity_card(
    opportunity,
    rank,
):

    business = opportunity["business"]

    score = opportunity["score"]

    rank_labels = {
        1: t("rank_1"),
        2: t("rank_2"),
        3: t("rank_3"),
    }

    st.markdown(
        f"""
        <div class="opportunity-card">

            <div class="opportunity-card-top">

                <div>

                    <div class="opportunity-rank">
                        #{rank} · {rank_labels.get(rank, "")}
                    </div>

                    <div class="opportunity-name">
                        {business}
                    </div>

                    <div class="opportunity-match">
                        {t("opportunity_score")}: {score}/100
                    </div>

                </div>

                <div class="score-box">

                    <div class="score-number">
                        {score}
                    </div>

                    <div class="score-label">
                        {t("opportunity_score")}
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Fit metrics
    # --------------------------------------------------------

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:

        st.markdown(
            f"""
            <div class="fit-row">

                <div class="fit-label">
                    {t("demand")} · {opportunity["demand"]}%
                </div>

                <div class="fit-track">

                    <div
                        class="fit-fill"
                        style="width:{opportunity["demand"]}%"
                    ></div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_col2:

        st.markdown(
            f"""
            <div class="fit-row">

                <div class="fit-label">
                    {t("competition")} · {opportunity["competition"]}%
                </div>

                <div class="fit-track">

                    <div
                        class="fit-fill"
                        style="width:{opportunity["competition"]}%"
                    ></div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    metric_col3, metric_col4 = st.columns(2)

    with metric_col3:

        st.markdown(
            f"""
            <div class="fit-row">

                <div class="fit-label">
                    {t("skill_fit")} · {opportunity["skill_fit"]}%
                </div>

                <div class="fit-track">

                    <div
                        class="fit-fill"
                        style="width:{opportunity["skill_fit"]}%"
                    ></div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_col4:

        st.markdown(
            f"""
            <div class="fit-row">

                <div class="fit-label">
                    {t("capital_fit")} · {opportunity["capital_fit"]}%
                </div>

                <div class="fit-track">

                    <div
                        class="fit-fill"
                        style="width:{opportunity["capital_fit"]}%"
                    ></div>

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="fit-row">

            <div class="fit-label">
                {t("risk_fit")} · {opportunity["risk_fit"]}%
            </div>

            <div class="fit-track">

                <div
                    class="fit-fill"
                    style="width:{opportunity["risk_fit"]}%"
                ></div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Why this fits
    # --------------------------------------------------------

    matching_skills = []

    skill_matches = {

        "Bakery / Food": [
            "Cooking",
            "Sales",
        ],

        "Dairy": [
            "Farming",
            "Sales",
        ],

        "Tailoring": [
            "Tailoring",
        ],

        "Retail": [
            "Sales",
            "Accounting",
        ],

        "Agriculture": [
            "Farming",
        ],

        "Repair Services": [
            "Repair / Technical",
        ],

        "Beauty / Personal Care": [
            "Sales",
        ],

        "Handicrafts": [
            "Handicrafts",
            "Sales",
        ],
    }

    for skill in st.session_state.skills:

        if skill in skill_matches.get(
            business,
            [],
        ):

            matching_skills.append(skill)

    if matching_skills:

        skill_text = ", ".join(
            matching_skills
        )

        why_text = (
            f"{business} matches your "
            f"skills ({skill_text}) and "
            f"your selected local-market profile."
        )

    elif business in st.session_state.interests:

        why_text = (
            f"{business} is one of your selected "
            f"business interests and shows a "
            f"promising prototype opportunity score "
            f"for the selected location."
        )

    else:

        why_text = (
            f"{business} shows a relatively strong "
            f"balance of local demand, competition, "
            f"capital fit and risk fit in this prototype."
        )

    st.markdown(
        f"""
        <div class="why-box">

            <strong>
                {t("why_fit")}
            </strong>

            <br>

            {why_text}

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Confidence
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="confidence-box">

            <strong>
                {t("confidence")}:
            </strong>

            {t("prototype_confidence")}

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        t("view_business"),
        use_container_width=True,
        key=f"view_business_{rank}_{business}",
    ):

        st.session_state.selected_opportunity = business

        st.info(
            f"{business} selected. "
            "The detailed business analysis will be connected in Frame 4."
        )


# ============================================================
# FRAME 3
# ============================================================

def render_frame_3():

    st.markdown(
        f"## {t('opportunity_title')}"
    )

    st.caption(
        t("opportunity_subtitle")
    )

    st.write("")

    # ========================================================
    # PROFILE / LOCATION SUMMARY
    # ========================================================

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:

        interests = (
            ", ".join(
                st.session_state.interests
            )
            if st.session_state.interests
            else "No interests selected"
        )

        st.markdown(
            f"""
            <div class="profile-summary">

                <div class="summary-title">
                    {t("your_profile")}
                </div>

                <div class="summary-main">
                    ₹{st.session_state.capital:,.0f}
                </div>

                <div class="summary-small">
                    {st.session_state.experience}
                    {t("years")} experience
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with summary_col2:

        st.markdown(
            f"""
            <div class="profile-summary">

                <div class="summary-title">
                    {t("your_location")}
                </div>

                <div class="summary-main">
                    {st.session_state.district}
                </div>

                <div class="summary-small">
                    {st.session_state.local_body}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with summary_col3:

        st.markdown(
            f"""
            <div class="profile-summary">

                <div class="summary-title">
                    {t("business_interest_question")}
                </div>

                <div class="summary-main">
                    {interests}
                </div>

                <div class="summary-small">
                    Risk preference:
                    {st.session_state.risk}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # ========================================================
    # EXPLANATION
    # ========================================================

    st.info(
        t("opportunity_note")
    )

    # ========================================================
    # OPPORTUNITIES
    # ========================================================

    opportunities = generate_opportunities()

    for rank, opportunity in enumerate(
        opportunities,
        start=1,
    ):

        render_opportunity_card(
            opportunity,
            rank,
        )

    # ========================================================
    # NAVIGATION
    # ========================================================

    st.write("")

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            t("back"),
            use_container_width=True,
            key="back_frame3_v4",
        ):

            st.session_state.page = 2

            st.rerun()

    with continue_col:

        if st.button(
            t("continue"),
            type="primary",
            use_container_width=True,
            key="continue_frame3_v4",
        ):

            # ------------------------------------------------
            # Frame 4 will be connected here next.
            # ------------------------------------------------

            st.session_state.page = 4

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

    render_frame_3()


elif st.session_state.page == 4:

    # Temporary placeholder until we build Frame 4.
    st.markdown("## Business Detail")

    st.info(
        "Frame 4 will be built next."
    )

    if st.button(
        t("back"),
        use_container_width=True,
        key="back_frame4_temp",
    ):

        st.session_state.page = 3

        st.rerun()
