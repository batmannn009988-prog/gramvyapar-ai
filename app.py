import streamlit as st
import pandas as pd
import numpy as np


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GRAMVYAPAR PALETTE
# ============================================================

OLIVE = "#526A3A"
GREEN = "#7D9A55"
ORANGE = "#C88A3D"
CREAM = "#FAF8F1"
BROWN = "#33352C"
WHITE = "#FFFFFF"


# ============================================================
# LANGUAGE TEXT
# ============================================================

TEXT = {
    "English": {
        "app_name": "GramVyapar AI",
        "tagline": "Know Before You Borrow",
        "language": "Language",

        "step_profile": "Profile",
        "step_local": "Local Area",
        "step_opportunity": "Opportunity",
        "step_finance": "Finance",

        "profile_title": "Tell us about yourself",
        "profile_subtitle": "This helps GramVyapar AI identify businesses that fit your skills, capital and risk comfort.",

        "skills": "Your skills",
        "skills_help": "Select all skills that apply.",
        "experience": "Years of business experience",
        "capital": "Available own capital",
        "interests": "Business interests",
        "risk": "Risk comfort",
        "existing_business": "Do you already run a business?",

        "continue": "Continue",
        "back": "Back",

        "location_title": "Understand your local market",
        "location_subtitle": "Select your district and local body to explore the available prototype market intelligence.",

        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward Number",

        "data_level": "Data level",
        "district_fallback": "District-level fallback",
        "prototype_data": "Prototype / demo",

        "business_density": "Business Density",
        "population": "Population",
        "seasonal_demand": "Seasonal Demand",
        "resource_availability": "Resource Availability",

        "reference_map": "Selected Area Reference",
        "map_note": "This marker represents the selected area reference point. It is not an individual business location.",

        "data_status": "Data status",
        "source": "Source",
        "prototype_source": "Prototype / demo estimate",

        "market_snapshot": "Local Market Snapshot",
        "opportunity_title": "Opportunity Radar",
        "opportunity_subtitle": "Potential business opportunities based on your profile and local conditions.",

        "bakery": "Bakery / Snacks",
        "dairy": "Dairy",
        "tailoring": "Tailoring",
        "grocery": "Neighbourhood Grocery",
        "food_processing": "Food Processing",

        "demand": "Demand",
        "competition": "Competition Fit",
        "skill": "Skill Fit",
        "capital_fit": "Capital Fit",
        "risk_fit": "Risk Fit",

        "why_fit": "Why this may fit",
        "confidence": "Confidence",

        "business_detail": "Business Detail",
        "local_evidence": "Local Evidence",
        "caveats": "Important caveats",

        "financial": "Financial Plan",
        "startup_cost": "Startup Cost",
        "monthly_revenue": "Monthly Revenue Estimate",
        "monthly_surplus": "Monthly Surplus",
        "break_even": "Break-even Quantity",
        "working_capital": "Working Capital",
        "financial_confidence": "Financial Confidence",

        "risk_dashboard": "Risk Dashboard",
        "overall_risk": "Overall Risk",

        "what_if": "What-if Simulator",
        "sales_change": "Sales change",
        "raw_material_change": "Raw material cost change",

        "base": "Base Case",
        "scenario": "Scenario",

        "financing": "Financing Guidance",
        "funding_gap": "Funding Gap",
        "eligibility": "Eligibility",
        "verify_source": "Verify with official source",
        "no_guarantee": "Loan approval is not guaranteed. Final eligibility depends on the lender and current scheme rules.",

        "action_plan": "Action Plan",
        "monitoring": "Monitoring",

        "data_insufficient": "Insufficient data",
        "derived": "Derived",
        "estimate": "Estimate",
        "verified": "Verified",

        "profile_saved": "Profile saved successfully.",
        "location_saved": "Local area selected successfully.",
    },

    "Malayalam": {
        "app_name": "ഗ്രാംവ്യാപാർ AI",
        "tagline": "വായ്പ എടുക്കുന്നതിന് മുമ്പ് അറിയുക",
        "language": "ഭാഷ",

        "step_profile": "പ്രൊഫൈൽ",
        "step_local": "പ്രാദേശിക മേഖല",
        "step_opportunity": "അവസരം",
        "step_finance": "ധനകാര്യം",

        "profile_title": "നിങ്ങളെക്കുറിച്ച് പറയൂ",
        "profile_subtitle": "നിങ്ങളുടെ കഴിവുകൾ, മൂലധനം, റിസ്ക് സൗകര്യം എന്നിവയ്ക്ക് അനുയോജ്യമായ ബിസിനസുകൾ കണ്ടെത്താൻ ഇത് സഹായിക്കും.",

        "skills": "നിങ്ങളുടെ കഴിവുകൾ",
        "skills_help": "ബാധകമായ എല്ലാ കഴിവുകളും തിരഞ്ഞെടുക്കുക.",
        "experience": "ബിസിനസ് പരിചയം (വർഷം)",
        "capital": "ലഭ്യമായ സ്വന്തം മൂലധനം",
        "interests": "ബിസിനസ് താൽപര്യങ്ങൾ",
        "risk": "റിസ്ക് സ്വീകരിക്കുന്ന തോത്",
        "existing_business": "നിങ്ങൾക്ക് ഇതിനകം ഒരു ബിസിനസ് ഉണ്ടോ?",

        "continue": "തുടരുക",
        "back": "തിരികെ",

        "location_title": "നിങ്ങളുടെ പ്രാദേശിക വിപണി മനസ്സിലാക്കുക",
        "location_subtitle": "ലഭ്യമായ പ്രോട്ടോടൈപ്പ് വിപണി വിവരങ്ങൾ പരിശോധിക്കാൻ ജില്ലയും പ്രാദേശിക സ്ഥാപനവും തിരഞ്ഞെടുക്കുക.",

        "district": "ജില്ല",
        "local_body": "പ്രാദേശിക സ്ഥാപനം",
        "ward": "വാർഡ് നമ്പർ",

        "data_level": "ഡാറ്റാ നില",
        "district_fallback": "ജില്ലാ തലത്തിലുള്ള പകരം ഡാറ്റ",
        "prototype_data": "പ്രോട്ടോടൈപ്പ് / ഡെമോ",

        "business_density": "ബിസിനസ് സാന്ദ്രത",
        "population": "ജനസംഖ്യ",
        "seasonal_demand": "കാലാവസ്ഥാനുസൃത ആവശ്യം",
        "resource_availability": "വിഭവ ലഭ്യത",

        "reference_map": "തിരഞ്ഞെടുത്ത മേഖലയുടെ സ്ഥാനം",
        "map_note": "ഈ അടയാളം തിരഞ്ഞെടുത്ത പ്രദേശത്തിന്റെ റഫറൻസ് പോയിന്റാണ്. ഇത് ഒരു വ്യക്തിഗത ബിസിനസ് ലൊക്കേഷൻ അല്ല.",

        "data_status": "ഡാറ്റാ നില",
        "source": "ഉറവിടം",
        "prototype_source": "പ്രോട്ടോടൈപ്പ് / ഡെമോ കണക്ക്",

        "market_snapshot": "പ്രാദേശിക വിപണി അവലോകനം",
        "opportunity_title": "അവസര റഡാർ",
        "opportunity_subtitle": "നിങ്ങളുടെ പ്രൊഫൈലും പ്രാദേശിക സാഹചര്യങ്ങളും അടിസ്ഥാനമാക്കിയുള്ള സാധ്യതയുള്ള ബിസിനസ് അവസരങ്ങൾ.",

        "bakery": "ബേക്കറി / പലഹാരം",
        "dairy": "ക്ഷീര ബിസിനസ്",
        "tailoring": "തയ്യൽ",
        "grocery": "അയൽപക്ക പലചരക്ക് കട",
        "food_processing": "ഭക്ഷ്യ സംസ്കരണം",

        "demand": "ആവശ്യം",
        "competition": "മത്സര അനുയോജ്യത",
        "skill": "കഴിവ് അനുയോജ്യത",
        "capital_fit": "മൂലധന അനുയോജ്യത",
        "risk_fit": "റിസ്ക് അനുയോജ്യത",

        "why_fit": "എന്തുകൊണ്ട് ഇത് അനുയോജ്യമാകാം",
        "confidence": "വിശ്വാസനില",

        "business_detail": "ബിസിനസ് വിശദാംശങ്ങൾ",
        "local_evidence": "പ്രാദേശിക തെളിവുകൾ",
        "caveats": "പ്രധാന പരിമിതികൾ",

        "financial": "ധനകാര്യ പദ്ധതി",
        "startup_cost": "ആരംഭ ചെലവ്",
        "monthly_revenue": "പ്രതീക്ഷിക്കുന്ന മാസ വരുമാനം",
        "monthly_surplus": "പ്രതീക്ഷിക്കുന്ന മാസ മിച്ചം",
        "break_even": "ബ്രേക്ക്-ഈവൻ അളവ്",
        "working_capital": "പ്രവർത്തന മൂലധനം",
        "financial_confidence": "ധനകാര്യ വിശ്വാസനില",

        "risk_dashboard": "റിസ്ക് ഡാഷ്ബോർഡ്",
        "overall_risk": "മൊത്തം റിസ്ക്",

        "what_if": "എന്ത് സംഭവിച്ചാൽ? സിമുലേറ്റർ",
        "sales_change": "വിൽപ്പനയിലെ മാറ്റം",
        "raw_material_change": "അസംസ്കൃത വസ്തു ചെലവിലെ മാറ്റം",

        "base": "അടിസ്ഥാന സാഹചര്യം",
        "scenario": "സാഹചര്യ കണക്ക്",

        "financing": "ധനസഹായ മാർഗനിർദേശം",
        "funding_gap": "ധനസഹായ കുറവ്",
        "eligibility": "യോഗ്യത",
        "verify_source": "ഔദ്യോഗിക ഉറവിടത്തിൽ പരിശോധിക്കുക",
        "no_guarantee": "വായ്പ അംഗീകാരം ഉറപ്പില്ല. അന്തിമ യോഗ്യത വായ്പദാതാവിനെയും നിലവിലെ പദ്ധതി നിയമങ്ങളെയും ആശ്രയിച്ചിരിക്കും.",

        "action_plan": "പ്രവർത്തന പദ്ധതി",
        "monitoring": "നിരീക്ഷണം",

        "data_insufficient": "മതിയായ ഡാറ്റ ലഭ്യമല്ല",
        "derived": "കണക്കാക്കിയ ഡാറ്റ",
        "estimate": "അനുമാനം",
        "verified": "സ്ഥിരീകരിച്ച ഡാറ്റ",

        "profile_saved": "പ്രൊഫൈൽ വിജയകരമായി സംരക്ഷിച്ചു.",
        "location_saved": "പ്രാദേശിക മേഖല വിജയകരമായി തിരഞ്ഞെടുത്തു.",
    },
}


# ============================================================
# KERALA DISTRICTS
# ============================================================

DISTRICTS = [
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


DISTRICT_ML = {
    "Alappuzha": "ആലപ്പുഴ",
    "Ernakulam": "എറണാകുളം",
    "Idukki": "ഇടുക്കി",
    "Kannur": "കണ്ണൂർ",
    "Kasaragod": "കാസർഗോഡ്",
    "Kollam": "കൊല്ലം",
    "Kottayam": "കോട്ടയം",
    "Kozhikode": "കോഴിക്കോട്",
    "Malappuram": "മലപ്പുറം",
    "Palakkad": "പാലക്കാട്",
    "Pathanamthitta": "പത്തനംതിട്ട",
    "Thiruvananthapuram": "തിരുവനന്തപുരം",
    "Thrissur": "തൃശ്ശൂർ",
    "Wayanad": "വയനാട്",
}


# ============================================================
# PROTOTYPE LOCAL BODIES
# ============================================================

LOCAL_BODIES = {
    "Alappuzha": [
        "Alappuzha Municipality",
        "Ambalappuzha",
        "Cherthala",
        "Kuttanad",
        "Chengannur",
    ],
    "Ernakulam": [
        "Kochi Corporation",
        "Aluva",
        "Kalamassery",
        "Perumbavoor",
        "Muvattupuzha",
    ],
    "Idukki": [
        "Thodupuzha",
        "Adimali",
        "Nedumkandam",
        "Kattappana",
        "Munnar",
    ],
    "Kannur": [
        "Kannur Corporation",
        "Thalassery",
        "Payyannur",
        "Taliparamba",
        "Iritty",
    ],
    "Kasaragod": [
        "Kasaragod Municipality",
        "Kanhangad",
        "Nileshwar",
        "Manjeshwar",
        "Udma",
    ],
    "Kollam": [
        "Kollam Corporation",
        "Karunagappally",
        "Kottarakkara",
        "Punalur",
        "Chathannoor",
    ],
    "Kottayam": [
        "Kottayam Municipality",
        "Changanassery",
        "Pala",
        "Ettumanoor",
        "Vaikom",
    ],
    "Kozhikode": [
        "Kozhikode Corporation",
        "Vadakara",
        "Koyilandy",
        "Balussery",
        "Thamarassery",
    ],
    "Malappuram": [
        "Malappuram Municipality",
        "Manjeri",
        "Perinthalmanna",
        "Tirur",
        "Nilambur",
    ],
    "Palakkad": [
        "Palakkad Municipality",
        "Ottappalam",
        "Shoranur",
        "Chittur",
        "Mannarkkad",
    ],
    "Pathanamthitta": [
        "Pathanamthitta Municipality",
        "Adoor",
        "Thiruvalla",
        "Ranni",
        "Konni",
    ],
    "Thiruvananthapuram": [
        "Thiruvananthapuram Corporation",
        "Nedumangad",
        "Neyyattinkara",
        "Attingal",
        "Varkala",
    ],
    "Thrissur": [
        "Thrissur Corporation",
        "Chalakudy",
        "Kunnamkulam",
        "Irinjalakuda",
        "Kodungallur",
    ],
    "Wayanad": [
        "Kalpetta",
        "Mananthavady",
        "Sulthan Bathery",
        "Panamaram",
        "Meppadi",
    ],
}


LOCAL_BODY_ML = {
    "Alappuzha Municipality": "ആലപ്പുഴ മുനിസിപ്പാലിറ്റി",
    "Kochi Corporation": "കൊച്ചി കോർപ്പറേഷൻ",
    "Idukki": "ഇടുക്കി",
    "Kannur Corporation": "കണ്ണൂർ കോർപ്പറേഷൻ",
    "Kasaragod Municipality": "കാസർഗോഡ് മുനിസിപ്പാലിറ്റി",
    "Kollam Corporation": "കൊല്ലം കോർപ്പറേഷൻ",
    "Kottayam Municipality": "കോട്ടയം മുനിസിപ്പാലിറ്റി",
    "Kozhikode Corporation": "കോഴിക്കോട് കോർപ്പറേഷൻ",
    "Malappuram Municipality": "മലപ്പുറം മുനിസിപ്പാലിറ്റി",
    "Palakkad Municipality": "പാലക്കാട് മുനിസിപ്പാലിറ്റി",
    "Pathanamthitta Municipality": "പത്തനംതിട്ട മുനിസിപ്പാലിറ്റി",
    "Thiruvananthapuram Corporation": "തിരുവനന്തപുരം കോർപ്പറേഷൻ",
    "Thrissur Corporation": "തൃശ്ശൂർ കോർപ്പറേഷൻ",
    "Kalpetta": "കൽപ്പറ്റ",
    "Mananthavady": "മാനന്തവാടി",
    "Sulthan Bathery": "സുൽത്താൻ ബത്തേരി",
    "Panamaram": "പനമരം",
    "Meppadi": "മേപ്പാടി",
}


# ============================================================
# SAFE MAP REFERENCE COORDINATES
# ============================================================
#
# IMPORTANT:
# These are NOT business locations.
# They are safe reference points for the selected district.
# We deliberately avoid randomly generating points because
# random points around coastal districts can fall into the sea.
#
# Coordinates are intentionally chosen around recognizable
# inland/urban reference areas for a stable demo.
# ============================================================

DISTRICT_COORDS = {
    "Alappuzha": (9.4981, 76.3388),
    "Ernakulam": (9.9816, 76.2999),
    "Idukki": (9.9189, 76.9497),
    "Kannur": (11.8745, 75.3704),
    "Kasaragod": (12.4996, 74.9869),
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
# SESSION STATE
# ============================================================

if "language" not in st.session_state:
    st.session_state.language = "English"

if "page" not in st.session_state:
    st.session_state.page = 1

if "profile" not in st.session_state:
    st.session_state.profile = {}

if "selected_district" not in st.session_state:
    st.session_state.selected_district = "Ernakulam"

if "selected_local_body" not in st.session_state:
    st.session_state.selected_local_body = LOCAL_BODIES["Ernakulam"][0]

if "selected_ward" not in st.session_state:
    st.session_state.selected_ward = 1

if "selected_business" not in st.session_state:
    st.session_state.selected_business = "Bakery / Snacks"


# ============================================================
# TRANSLATION HELPERS
# ============================================================

def t(key):
    return TEXT[st.session_state.language].get(
        key,
        TEXT["English"].get(key, key)
    )


def district_label(district):
    if st.session_state.language == "Malayalam":
        return DISTRICT_ML.get(district, district)
    return district


def local_body_label(body):
    if st.session_state.language == "Malayalam":
        return LOCAL_BODY_ML.get(body, body)
    return body


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {CREAM};
        color: {BROWN};
    }}

    .block-container {{
        max-width: 1350px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }}

    h1, h2, h3, h4 {{
        color: {BROWN};
    }}

    .brand {{
        font-size: 30px;
        font-weight: 800;
        color: {OLIVE};
        margin-bottom: 0;
    }}

    .tagline {{
        color: #6d705f;
        font-size: 14px;
        margin-top: -5px;
    }}

    .step {{
        padding: 9px 14px;
        border-radius: 20px;
        text-align: center;
        font-size: 13px;
        font-weight: 600;
        background: #ecebdd;
        color: #77796e;
    }}

    .step-active {{
        background: {OLIVE};
        color: white;
    }}

    .card {{
        background: {WHITE};
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #e7e5da;
        box-shadow: 0 2px 8px rgba(51,53,44,0.04);
    }}

    .metric {{
        background: {WHITE};
        border: 1px solid #e7e5da;
        border-radius: 14px;
        padding: 18px;
        min-height: 125px;
    }}

    .metric-title {{
        font-size: 13px;
        color: #77796e;
        margin-bottom: 7px;
    }}

    .metric-value {{
        font-size: 28px;
        font-weight: 800;
        color: {OLIVE};
    }}

    .metric-note {{
        font-size: 12px;
        color: #85877c;
        margin-top: 4px;
    }}

    .badge {{
        display: inline-block;
        padding: 5px 10px;
        border-radius: 14px;
        font-size: 12px;
        font-weight: 700;
        background: #ecebdd;
        color: {OLIVE};
    }}

    .evidence {{
        border-left: 4px solid {ORANGE};
        background: #fffaf2;
        padding: 12px 15px;
        border-radius: 8px;
        margin: 8px 0;
    }}

    .safe {{
        color: {OLIVE};
        font-weight: 700;
    }}

    .warning {{
        color: {ORANGE};
        font-weight: 700;
    }}

    .danger {{
        color: #a64b3c;
        font-weight: 700;
    }}

    div.stButton > button {{
        border-radius: 10px;
        font-weight: 700;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

def render_header():

    col1, col2 = st.columns([5, 1])

    with col1:
        st.markdown(
            f'<div class="brand">🌾 {t("app_name")}</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="tagline">{t("tagline")}</div>',
            unsafe_allow_html=True
        )

    with col2:
        language_options = ["English", "Malayalam"]

        current_index = language_options.index(
            st.session_state.language
        )

        selected_language = st.selectbox(
            t("language"),
            language_options,
            index=current_index,
            format_func=lambda x: "English" if x == "English" else "മലയാളം",
            key="language_selector"
        )

        if selected_language != st.session_state.language:
            st.session_state.language = selected_language
            st.rerun()


# ============================================================
# STEPS
# ============================================================

def render_steps():

    steps = [
        t("step_profile"),
        t("step_local"),
        t("step_opportunity"),
        t("step_finance"),
    ]

    cols = st.columns(4)

    for i, step in enumerate(steps, start=1):

        with cols[i - 1]:

            active_class = "step-active" if st.session_state.page == i else ""

            st.markdown(
                f"""
                <div class="step {active_class}">
                    {i}. {step}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")


# ============================================================
# FRAME 1 — PROFILE
# ============================================================

def render_frame_1():

    st.title(t("profile_title"))

    st.write(t("profile_subtitle"))

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        skill_options = [
            "Cooking",
            "Baking",
            "Tailoring",
            "Farming",
            "Dairy",
            "Handicraft",
            "Retail",
            "Food Processing",
            "Repair",
        ]

        selected_skills = st.multiselect(
            t("skills"),
            skill_options,
            key="skills_input_v5",
            help=t("skills_help")
        )

        experience = st.number_input(
            t("experience"),
            min_value=0,
            max_value=40,
            value=0,
            step=1
        )

        capital = st.slider(
            t("capital"),
            min_value=0,
            max_value=500000,
            value=50000,
            step=5000,
            format="₹%d"
        )

    with col2:

        interest_options = [
            t("bakery"),
            t("dairy"),
            t("tailoring"),
            t("grocery"),
            t("food_processing"),
        ]

        interests = st.multiselect(
            t("interests"),
            interest_options
        )

        risk = st.radio(
            t("risk"),
            ["Low", "Medium", "High"],
            horizontal=True
        )

        existing_business = st.radio(
            t("existing_business"),
            ["No", "Yes"],
            horizontal=True
        )

    st.write("")

    if st.button(
        t("continue"),
        type="primary",
        use_container_width=True
    ):

        st.session_state.profile = {
            "skills": selected_skills,
            "experience": experience,
            "capital": capital,
            "interests": interests,
            "risk": risk,
            "existing_business": existing_business,
        }

        st.session_state.page = 2

        st.rerun()


# ============================================================
# LOCAL DATA GENERATOR
# ============================================================

def generate_location_data(district, local_body, ward):

    seed = (
        sum(ord(c) for c in district)
        + sum(ord(c) for c in local_body)
        + int(ward) * 17
    )

    rng = np.random.default_rng(seed)

    population = int(
        8500
        + rng.integers(0, 12000)
    )

    business_density = round(
        3.5 + rng.random() * 5.5,
        1
    )

    seasonal_demand = int(
        55 + rng.integers(0, 40)
    )

    resource_availability = int(
        60 + rng.integers(0, 35)
    )

    return {
        "population": population,
        "business_density": business_density,
        "seasonal_demand": seasonal_demand,
        "resource_availability": resource_availability,
    }


# ============================================================
# SAFE MAP
# ============================================================

def generate_safe_map(district):

    lat, lon = DISTRICT_COORDS.get(
        district,
        DISTRICT_COORDS["Ernakulam"]
    )

    # ONE deterministic reference marker.
    # No random scatter.
    #
    # This prevents demo markers from appearing in the ocean.

    return pd.DataFrame(
        {
            "lat": [lat],
            "lon": [lon],
        }
    )


# ============================================================
# METRIC CARD
# ============================================================

def metric_card(title, value, note):

    st.markdown(
        f"""
        <div class="metric">

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-note">
                {note}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FRAME 2 — LOCAL DASHBOARD
# ============================================================

def render_frame_2():

    st.title(t("location_title"))

    st.write(t("location_subtitle"))

    st.write("")

    col1, col2, col3 = st.columns([1.2, 1.4, 0.7])

    with col1:

        district_names = DISTRICTS

        current_district_index = district_names.index(
            st.session_state.selected_district
        )

        selected_district = st.selectbox(
            t("district"),
            district_names,
            index=current_district_index,
            format_func=district_label,
            key="district_selector_v5"
        )

    with col2:

        body_options = LOCAL_BODIES[selected_district]

        previous_body = st.session_state.selected_local_body

        if previous_body in body_options:
            body_index = body_options.index(previous_body)
        else:
            body_index = 0

        selected_local_body = st.selectbox(
            t("local_body"),
            body_options,
            index=body_index,
            format_func=local_body_label,
            key="local_body_selector_v5"
        )

    with col3:

        selected_ward = st.number_input(
            t("ward"),
            min_value=1,
            max_value=100,
            value=int(st.session_state.selected_ward),
            step=1
        )

    st.session_state.selected_district = selected_district
    st.session_state.selected_local_body = selected_local_body
    st.session_state.selected_ward = selected_ward

    st.write("")

    # --------------------------------------------------------
    # DATA LEVEL
    # --------------------------------------------------------

    st.markdown(
        f"""
        <span class="badge">
            {t("data_level")}: {t("district_fallback")}
        </span>
        """,
        unsafe_allow_html=True
    )

    st.info(
        (
            "This prototype currently uses district-level fallback "
            "data where ward-level verified data is unavailable."
            if st.session_state.language == "English"
            else
            "വാർഡ് തലത്തിലുള്ള സ്ഥിരീകരിച്ച ഡാറ്റ ലഭ്യമല്ലാത്തിടത്ത് "
            "ഈ പ്രോട്ടോടൈപ്പ് ജില്ലാ തലത്തിലുള്ള പകരം ഡാറ്റയാണ് ഉപയോഗിക്കുന്നത്."
        )
    )

    # --------------------------------------------------------
    # DATA
    # --------------------------------------------------------

    data = generate_location_data(
        selected_district,
        selected_local_body,
        selected_ward
    )

    st.subheader(t("market_snapshot"))

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            t("business_density"),
            f'{data["business_density"]}/km²',
            t("estimate")
        )

    with c2:
        metric_card(
            t("population"),
            f'{data["population"]:,}',
            "Prototype estimate"
            if st.session_state.language == "English"
            else "പ്രോട്ടോടൈപ്പ് അനുമാനം"
        )

    with c3:
        metric_card(
            t("seasonal_demand"),
            f'{data["seasonal_demand"]}%',
            t("derived")
        )

    with c4:
        metric_card(
            t("resource_availability"),
            f'{data["resource_availability"]}%',
            t("derived")
        )

    st.write("")

    # --------------------------------------------------------
    # MAP
    # --------------------------------------------------------

    map_col, info_col = st.columns([2.3, 1])

    with map_col:

        st.subheader(t("reference_map"))

        map_df = generate_safe_map(selected_district)

        st.map(
            map_df,
            latitude="lat",
            longitude="lon",
            size=100,
            zoom=9
        )

        st.caption(t("map_note"))

    with info_col:

        st.markdown(
            f"""
            <div class="card">

                <h4>{district_label(selected_district)}</h4>

                <p>
                    <b>{t("local_body")}:</b><br>
                    {local_body_label(selected_local_body)}
                </p>

                <p>
                    <b>{t("ward")}:</b><br>
                    {selected_ward}
                </p>

                <hr>

                <p>
                    <b>{t("data_level")}:</b><br>
                    {t("district_fallback")}
                </p>

                <p>
                    <b>{t("data_status")}:</b><br>
                    {t("prototype_data")}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # --------------------------------------------------------
    # SOURCE / STATUS
    # --------------------------------------------------------

    left, right = st.columns([1, 1])

    with left:
        st.caption(
            f'{t("source")}: {t("prototype_source")}'
        )

    with right:
        st.markdown(
            f"""
            <div style="text-align:right; color:#77796e; font-size:13px;">
                <b>{t("data_status")}:</b> {t("prototype_data")}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col_back, col_continue = st.columns([1, 1])

    with col_back:

        if st.button(
            t("back"),
            use_container_width=True
        ):
            st.session_state.page = 1
            st.rerun()

    with col_continue:

        if st.button(
            t("continue"),
            type="primary",
            use_container_width=True
        ):
            st.session_state.page = 3
            st.rerun()


# ============================================================
# BUSINESS SCORING
# ============================================================

BUSINESS_MODELS = {
    "Bakery / Snacks": {
        "startup": 180000,
        "revenue": 65000,
        "cost": 44000,
        "risk": "Medium",
    },
    "Dairy": {
        "startup": 220000,
        "revenue": 72000,
        "cost": 51000,
        "risk": "Medium",
    },
    "Tailoring": {
        "startup": 120000,
        "revenue": 48000,
        "cost": 27000,
        "risk": "Low",
    },
    "Neighbourhood Grocery": {
        "startup": 250000,
        "revenue": 90000,
        "cost": 71000,
        "risk": "Medium",
    },
    "Food Processing": {
        "startup": 300000,
        "revenue": 105000,
        "cost": 78000,
        "risk": "Medium",
    },
}


def calculate_business_score(
    business,
    capital,
    skills,
    experience,
    risk
):

    model = BUSINESS_MODELS[business]

    # Capital fit
    if capital >= model["startup"] * 0.50:
        capital_score = 90
    elif capital >= model["startup"] * 0.25:
        capital_score = 70
    else:
        capital_score = 50

    # Skill fit
    skill_map = {
        "Bakery / Snacks": ["Baking", "Cooking"],
        "Dairy": ["Dairy", "Farming"],
        "Tailoring": ["Tailoring"],
        "Neighbourhood Grocery": ["Retail"],
        "Food Processing": ["Food Processing", "Cooking"],
    }

    matching_skills = [
        s for s in skills
        if s in skill_map[business]
    ]

    skill_score = 90 if matching_skills else 55

    # Experience
    experience_score = min(
        95,
        55 + experience * 5
    )

    # Simple prototype local demand
    demand_score = {
        "Bakery / Snacks": 78,
        "Dairy": 74,
        "Tailoring": 69,
        "Neighbourhood Grocery": 82,
        "Food Processing": 72,
    }[business]

    # Competition fit
    competition_score = {
        "Bakery / Snacks": 68,
        "Dairy": 73,
        "Tailoring": 76,
        "Neighbourhood Grocery": 61,
        "Food Processing": 71,
    }[business]

    # Risk
    if risk == "Low":
        risk_score = 85 if model["risk"] == "Low" else 65
    elif risk == "Medium":
        risk_score = 80
    else:
        risk_score = 90

    total = (
        0.25 * demand_score
        + 0.20 * competition_score
        + 0.20 * skill_score
        + 0.20 * capital_score
        + 0.15 * risk_score
    )

    return round(total)


# ============================================================
# FRAME 3 — OPPORTUNITY RADAR
# ============================================================

def render_frame_3():

    st.title(t("opportunity_title"))

    st.write(t("opportunity_subtitle"))

    profile = st.session_state.profile

    capital = profile.get("capital", 50000)
    skills = profile.get("skills", [])
    experience = profile.get("experience", 0)
    risk = profile.get("risk", "Medium")

    businesses = list(BUSINESS_MODELS.keys())

    scored = []

    for business in businesses:

        score = calculate_business_score(
            business,
            capital,
            skills,
            experience,
            risk
        )

        scored.append(
            {
                "business": business,
                "score": score,
            }
        )

    scored = sorted(
        scored,
        key=lambda x: x["score"],
        reverse=True
    )

    for rank, item in enumerate(scored, start=1):

        business = item["business"]
        score = item["score"]

        model = BUSINESS_MODELS[business]

        st.markdown(
            f"""
            <div class="card">

                <div style="display:flex; justify-content:space-between;">

                    <div>
                        <h3 style="margin-bottom:4px;">
                            #{rank} {business}
                        </h3>

                        <span class="badge">
                            {t("confidence")}: {score}%
                        </span>
                    </div>

                    <div style="font-size:32px; font-weight:800; color:{OLIVE};">
                        {score}
                    </div>

                </div>

                <br>

                <b>{t("demand")}</b>
                <div style="background:#ecebdd;border-radius:10px;height:8px;">
                    <div style="width:{score}%;background:{GREEN};height:8px;border-radius:10px;"></div>
                </div>

                <br>

                <b>{t("skill")}</b>
                <div style="background:#ecebdd;border-radius:10px;height:8px;">
                    <div style="width:{min(score + 5, 100)}%;background:{GREEN};height:8px;border-radius:10px;"></div>
                </div>

                <br>

                <b>{t("capital_fit")}</b>
                <div style="background:#ecebdd;border-radius:10px;height:8px;">
                    <div style="width:{min(score - 5, 100)}%;background:{ORANGE};height:8px;border-radius:10px;"></div>
                </div>

                <br>

                <b>{t("why_fit")}</b>

                <p>
                    {business} shows a prototype opportunity score of
                    <b>{score}/100</b> based on local demand,
                    competition fit, skill fit, capital fit and risk fit.
                </p>

                <p style="color:#77796e;font-size:13px;">
                    Startup estimate: ₹{model["startup"]:,}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

    st.subheader(t("business_detail"))

    selected = scored[0]["business"]

    if st.session_state.language == "Malayalam":
        display_selected = {
            "Bakery / Snacks": t("bakery"),
            "Dairy": t("dairy"),
            "Tailoring": t("tailoring"),
            "Neighbourhood Grocery": t("grocery"),
            "Food Processing": t("food_processing"),
        }.get(selected, selected)
    else:
        display_selected = selected

    st.success(
        f"{t('opportunity_title')}: {display_selected}"
    )

    st.markdown(
        f"""
        <div class="evidence">

        <b>{t("local_evidence")}</b>

        <br><br>

        • Prototype demand estimate based on business category<br>
        • District-level market fallback<br>
        • Capital-fit calculation based on user-entered capital<br>
        • Skill-fit calculation based on selected skills

        </div>
        """,
        unsafe_allow_html=True
    )

    st.warning(
        (
            "Prototype data is for demonstration. It must be replaced "
            "with verified local datasets before real-world lending decisions."
            if st.session_state.language == "English"
            else
            "പ്രോട്ടോടൈപ്പ് ഡാറ്റ ഡെമോ ആവശ്യത്തിനുള്ളതാണ്. യഥാർത്ഥ വായ്പാ "
            "തീരുമാനങ്ങൾക്ക് മുമ്പ് ഇത് സ്ഥിരീകരിച്ച പ്രാദേശിക ഡാറ്റ ഉപയോഗിച്ച് മാറ്റണം."
        )
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            t("back"),
            use_container_width=True
        ):
            st.session_state.page = 2
            st.rerun()

    with col2:

        if st.button(
            t("financial"),
            type="primary",
            use_container_width=True
        ):

            st.session_state.selected_business = selected
            st.session_state.page = 4
            st.rerun()


# ============================================================
# FINANCIAL CALCULATIONS
# ============================================================

def calculate_financials(
    business,
    sales_change=0,
    raw_material_change=0
):

    model = BUSINESS_MODELS[business]

    revenue = model["revenue"] * (
        1 + sales_change / 100
    )

    base_cost = model["cost"]

    adjusted_cost = base_cost * (
        1 + raw_material_change / 100
    )

    surplus = revenue - adjusted_cost

    startup = model["startup"]

    break_even = (
        startup / max(revenue, 1)
    )

    return {
        "startup": startup,
        "revenue": revenue,
        "cost": adjusted_cost,
        "surplus": surplus,
        "break_even": break_even,
    }


# ============================================================
# FRAME 4 — FINANCE
# ============================================================

def render_frame_4():

    business = st.session_state.selected_business

    if st.session_state.language == "Malayalam":

        display_business = {
            "Bakery / Snacks": t("bakery"),
            "Dairy": t("dairy"),
            "Tailoring": t("tailoring"),
            "Neighbourhood Grocery": t("grocery"),
            "Food Processing": t("food_processing"),
        }.get(business, business)

    else:
        display_business = business

    st.title(t("financial"))

    st.write(
        f"{display_business} — "
        + (
            "prototype financial model"
            if st.session_state.language == "English"
            else
            "പ്രോട്ടോടൈപ്പ് ധനകാര്യ മാതൃക"
        )
    )

    st.write("")

    financials = calculate_financials(business)

    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            t("startup_cost"),
            f'₹{financials["startup"]:,.0f}',
            t("estimate")
        )

    with c2:

        metric_card(
            t("monthly_revenue"),
            f'₹{financials["revenue"]:,.0f}',
            t("estimate")
        )

    with c3:

        surplus_value = financials["surplus"]

        metric_card(
            t("monthly_surplus"),
            f'₹{surplus_value:,.0f}',
            t("derived")
        )

    st.write("")

    # --------------------------------------------------------
    # FINANCIAL FLOW
    # --------------------------------------------------------

    st.subheader(
        (
            "Monthly financial flow"
            if st.session_state.language == "English"
            else
            "മാസ ധനകാര്യ പ്രവാഹം"
        )
    )

    flow1, flow2, flow3 = st.columns(3)

    with flow1:

        st.markdown(
            f"""
            <div class="card">

            <h4>Revenue</h4>

            <h2>
            ₹{financials["revenue"]:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )

    with flow2:

        st.markdown(
            f"""
            <div class="card">

            <h4>Expenses</h4>

            <h2>
            ₹{financials["cost"]:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )

    with flow3:

        st.markdown(
            f"""
            <div class="card">

            <h4>Surplus</h4>

            <h2>
            ₹{financials["surplus"]:,.0f}
            </h2>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # --------------------------------------------------------
    # BREAK EVEN
    # --------------------------------------------------------

    st.subheader(t("break_even"))

    st.info(
        (
            f"Prototype break-even indicator: "
            f"{financials['break_even']:.1f} months of revenue coverage."
            if st.session_state.language == "English"
            else
            f"പ്രോട്ടോടൈപ്പ് ബ്രേക്ക്-ഈവൻ സൂചിക: "
            f"{financials['break_even']:.1f} മാസത്തെ വരുമാന കവറേജ്."
        )
    )

    # --------------------------------------------------------
    # RISK
    # --------------------------------------------------------

    st.subheader(t("risk_dashboard"))

    if financials["surplus"] > 20000:
        risk_level = "Low"
        risk_class = "safe"
    elif financials["surplus"] > 5000:
        risk_level = "Medium"
        risk_class = "warning"
    else:
        risk_level = "High"
        risk_class = "danger"

    st.markdown(
        f"""
        <div class="card">

        <h3>{t("overall_risk")}</h3>

        <h2 class="{risk_class}">
            {risk_level}
        </h2>

        <p>
        {
            "Monthly surplus remains positive under the base prototype assumptions."
            if st.session_state.language == "English"
            else
            "അടിസ്ഥാന പ്രോട്ടോടൈപ്പ് കണക്കുകൾ പ്രകാരം മാസ മിച്ചം പോസിറ്റീവ് ആണ്."
        }
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # --------------------------------------------------------
    # WHAT IF
    # --------------------------------------------------------

    st.subheader(t("what_if"))

    sales_change = st.slider(
        t("sales_change"),
        min_value=-50,
        max_value=50,
        value=0,
        step=5
    )

    raw_material_change = st.slider(
        t("raw_material_change"),
        min_value=-30,
        max_value=50,
        value=0,
        step=5
    )

    scenario = calculate_financials(
        business,
        sales_change,
        raw_material_change
    )

    base_col, scenario_col = st.columns(2)

    with base_col:

        st.markdown(
            f"""
            <div class="card">

            <h3>{t("base")}</h3>

            <p>
            Revenue: ₹{financials["revenue"]:,.0f}
            </p>

            <p>
            Expenses: ₹{financials["cost"]:,.0f}
            </p>

            <p>
            Surplus: <b>₹{financials["surplus"]:,.0f}</b>
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with scenario_col:

        scenario_class = (
            "safe"
            if scenario["surplus"] > 0
            else "danger"
        )

        st.markdown(
            f"""
            <div class="card">

            <h3>{t("scenario")}</h3>

            <p>
            Revenue: ₹{scenario["revenue"]:,.0f}
            </p>

            <p>
            Expenses: ₹{scenario["cost"]:,.0f}
            </p>

            <p>
            Surplus:
            <b class="{scenario_class}">
            ₹{scenario["surplus"]:,.0f}
            </b>
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if scenario["surplus"] <= 0:

        st.error(
            (
                "NOT FINANCIALLY SAFE — reduce project size, "
                "increase own contribution or consider another business."
                if st.session_state.language == "English"
                else
                "സാമ്പത്തികമായി സുരക്ഷിതമല്ല — പദ്ധതിയുടെ വലുപ്പം കുറയ്ക്കുക, "
                "സ്വന്തം മൂലധനം വർധിപ്പിക്കുക, അല്ലെങ്കിൽ മറ്റൊരു ബിസിനസ് പരിഗണിക്കുക."
            )
        )

    else:

        st.success(
            (
                "Scenario remains financially positive under the selected assumptions."
                if st.session_state.language == "English"
                else
                "തിരഞ്ഞെടുത്ത സാഹചര്യത്തിലും പദ്ധതി സാമ്പത്തികമായി പോസിറ്റീവ് ആണ്."
            )
        )

    # --------------------------------------------------------
    # FINANCING
    # --------------------------------------------------------

    st.subheader(t("financing"))

    own_capital = st.session_state.profile.get(
        "capital",
        50000
    )

    funding_gap = max(
        0,
        financials["startup"] - own_capital
    )

    st.metric(
        t("funding_gap"),
        f"₹{funding_gap:,.0f}"
    )

    st.markdown(
        f"""
        <div class="card">

        <h3>
        {
            "Potential financing route"
            if st.session_state.language == "English"
            else
            "സാധ്യതയുള്ള ധനസഹായ മാർഗം"
        }
        </h3>

        <p>
        {
            "Micro / small enterprise financing may be explored depending on project size and eligibility."
            if st.session_state.language == "English"
            else
            "പദ്ധതിയുടെ വലുപ്പവും യോഗ്യതയും അനുസരിച്ച് മൈക്രോ / ചെറുകിട സംരംഭ ധനസഹായം പരിശോധിക്കാം."
        }
        </p>

        <p>
        <b>{t("eligibility")}:</b>
        {t("verify_source")}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.warning(t("no_guarantee"))

    st.write("")

    # --------------------------------------------------------
    # ACTION PLAN
    # --------------------------------------------------------

    st.subheader(t("action_plan"))

    actions = [
        "1. Validate local customer demand",
        "2. Verify supplier and raw-material costs",
        "3. Run a small pilot",
        "4. Collect customer feedback",
        "5. Launch at controlled scale",
        "6. Monitor sales and expenses monthly",
    ]

    if st.session_state.language == "Malayalam":

        actions = [
            "1. പ്രാദേശിക ഉപഭോക്തൃ ആവശ്യം പരിശോധിക്കുക",
            "2. വിതരണക്കാരുടെയും അസംസ്കൃത വസ്തുക്കളുടെയും ചെലവ് സ്ഥിരീകരിക്കുക",
            "3. ചെറിയ പൈലറ്റ് നടത്തുക",
            "4. ഉപഭോക്തൃ അഭിപ്രായം ശേഖരിക്കുക",
            "5. നിയന്ത്രിത രീതിയിൽ ആരംഭിക്കുക",
            "6. മാസത്തിൽ വിൽപ്പനയും ചെലവുകളും നിരീക്ഷിക്കുക",
        ]

    for action in actions:
        st.markdown(
            f"""
            <div class="card" style="margin-bottom:8px;">
                {action}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # --------------------------------------------------------
    # MONITORING
    # --------------------------------------------------------

    st.subheader(t("monitoring"))

    monitor_col1, monitor_col2, monitor_col3 = st.columns(3)

    with monitor_col1:
        st.number_input(
            (
                "Actual sales"
                if st.session_state.language == "English"
                else
                "യഥാർത്ഥ വിൽപ്പന"
            ),
            min_value=0,
            value=0,
            step=1000
        )

    with monitor_col2:
        st.number_input(
            (
                "Actual expenses"
                if st.session_state.language == "English"
                else
                "യഥാർത്ഥ ചെലവ്"
            ),
            min_value=0,
            value=0,
            step=1000
        )

    with monitor_col3:
        st.number_input(
            (
                "Orders"
                if st.session_state.language == "English"
                else
                "ഓർഡറുകൾ"
            ),
            min_value=0,
            value=0,
            step=1
        )

    st.info(
        (
            "Future backend integration can store monthly actuals and compare them with predictions."
            if st.session_state.language == "English"
            else
            "ഭാവിയിലെ backend integration വഴി മാസത്തിലെ യഥാർത്ഥ കണക്കുകൾ സൂക്ഷിച്ച് പ്രവചനങ്ങളുമായി താരതമ്യം ചെയ്യാം."
        )
    )

    st.write("")

    if st.button(
        t("back"),
        use_container_width=True
    ):
        st.session_state.page = 3
        st.rerun()


# ============================================================
# MAIN APP
# ============================================================

render_header()

render_steps()

if st.session_state.page == 1:

    render_frame_1()

elif st.session_state.page == 2:

    render_frame_2()

elif st.session_state.page == 3:

    render_frame_3()

elif st.session_state.page == 4:

    render_frame_4()
