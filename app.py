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
# GRAMVYAPAR COLOR PALETTE
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

        "step1": "1. Your Profile",
        "step2": "2. Local Dashboard",
        "step3": "3. Opportunity Radar",

        "profile_title": "Tell us about yourself",
        "profile_subtitle": "This helps us understand which businesses may fit you best.",

        "skills_title": "What skills do you have?",
        "select_skills": "Select your skills",

        "experience_title": "How much experience do you have?",
        "experience_help": "Years of relevant experience",
        "years": "years",

        "capital_title": "How much capital can you invest?",
        "capital_help": "Your available own contribution",

        "business_interest_question": "Which business areas interest you?",

        "risk_title": "What level of business risk are you comfortable with?",

        "existing_business_question": "Do you already have a business?",
        "yes": "Yes",
        "no": "No",

        "business_name": "Business name (optional)",

        "continue": "Continue",
        "back": "Back",

        "local_title": "Your Local Business Dashboard",
        "local_subtitle": "Understand the business environment around you before investing.",

        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward Number",

        "ward_data": "Ward-level data",
        "district_data": "District-level fallback",

        "location_note": "Data availability varies by location. Some values are prototype estimates until verified local data is connected.",

        "business_density": "Business Density",
        "population": "Population",
        "seasonal_demand": "Seasonal Demand",
        "resource_availability": "Resource Availability",

        "business_density_help": "Estimated businesses per 1,000 people",
        "population_help": "Reference population",
        "seasonal_demand_help": "Estimated local demand strength",
        "resource_help": "Estimated availability of relevant resources",

        "map_title": "Local Business Map",
        "map_caption": "Prototype business locations for the selected area.",

        "data_source": "Source",
        "prototype_source": "Prototype / demo estimate",

        "language": "Language",

        "profile_complete": "Profile saved successfully.",

        "malayalam": "Malayalam",
        "english": "English",

        "skill_tailoring": "Tailoring",
        "skill_baking": "Baking",
        "skill_cooking": "Cooking",
        "skill_farming": "Farming",
        "skill_dairy": "Dairy",
        "skill_handicraft": "Handicrafts",
        "skill_repair": "Repair & Maintenance",
        "skill_sales": "Sales",
        "skill_digital": "Digital Skills",
        "skill_driving": "Driving",
        "skill_food_processing": "Food Processing",

        "interest_food": "Food & Bakery",
        "interest_dairy": "Dairy",
        "interest_tailoring": "Tailoring",
        "interest_farming": "Agriculture",
        "interest_repair": "Repair Services",
        "interest_handicraft": "Handicrafts",

        "risk_low": "Low",
        "risk_medium": "Medium",
        "risk_high": "High",

        "risk_low_desc": "Prefer stable and predictable businesses.",
        "risk_medium_desc": "Comfortable with moderate uncertainty.",
        "risk_high_desc": "Comfortable with higher uncertainty for higher potential returns.",
    },

    "ml": {
        "app_title": "ഗ്രാംവ്യാപാർ AI",
        "tagline": "വായ്പ എടുക്കുന്നതിന് മുമ്പ് അറിയൂ",

        "step1": "1. നിങ്ങളുടെ പ്രൊഫൈൽ",
        "step2": "2. പ്രാദേശിക ഡാഷ്ബോർഡ്",
        "step3": "3. അവസര റഡാർ",

        "profile_title": "നിങ്ങളെക്കുറിച്ച് പറയൂ",
        "profile_subtitle": "നിങ്ങൾക്ക് അനുയോജ്യമായ ബിസിനസുകൾ കണ്ടെത്താൻ ഇത് സഹായിക്കും.",

        "skills_title": "നിങ്ങൾക്ക് എന്തെല്ലാം കഴിവുകളുണ്ട്?",
        "select_skills": "നിങ്ങളുടെ കഴിവുകൾ തിരഞ്ഞെടുക്കുക",

        "experience_title": "നിങ്ങൾക്ക് എത്ര പരിചയമുണ്ട്?",
        "experience_help": "ബന്ധപ്പെട്ട ജോലി പരിചയം",
        "years": "വർഷം",

        "capital_title": "നിങ്ങൾക്ക് എത്ര മൂലധനം നിക്ഷേപിക്കാനാകും?",
        "capital_help": "നിങ്ങളുടെ സ്വന്തം നിക്ഷേപ തുക",

        "business_interest_question": "ഏത് ബിസിനസ് മേഖലകളിലാണ് നിങ്ങൾക്ക് താൽപ്പര്യം?",

        "risk_title": "എത്രത്തോളം ബിസിനസ് റിസ്ക് നിങ്ങൾ സ്വീകരിക്കും?",

        "existing_business_question": "നിങ്ങൾക്ക് ഇതിനകം ഒരു ബിസിനസ് ഉണ്ടോ?",
        "yes": "അതെ",
        "no": "ഇല്ല",

        "business_name": "ബിസിനസ് പേര് (ഓപ്ഷണൽ)",

        "continue": "തുടരുക",
        "back": "പിന്നോട്ട്",

        "local_title": "നിങ്ങളുടെ പ്രാദേശിക ബിസിനസ് ഡാഷ്ബോർഡ്",
        "local_subtitle": "നിക്ഷേപിക്കുന്നതിന് മുമ്പ് നിങ്ങളുടെ പ്രദേശത്തെ ബിസിനസ് സാഹചര്യം മനസ്സിലാക്കുക.",

        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ് നമ്പർ",

        "ward_data": "വാർഡ് തല ഡാറ്റ",
        "district_data": "ജില്ലാ തല ഡാറ്റ",

        "location_note": "ഡാറ്റ ലഭ്യത സ്ഥലത്തിനനുസരിച്ച് വ്യത്യാസപ്പെടാം. യഥാർത്ഥ പ്രാദേശിക ഡാറ്റ ബന്ധിപ്പിക്കുന്നതുവരെ ചില മൂല്യങ്ങൾ പ്രോട്ടോടൈപ്പ് കണക്കുകളാണ്.",

        "business_density": "ബിസിനസ് സാന്ദ്രത",
        "population": "ജനസംഖ്യ",
        "seasonal_demand": "കാലാനുസൃത ആവശ്യം",
        "resource_availability": "വിഭവ ലഭ്യത",

        "business_density_help": "1,000 ആളുകളിൽ കണക്കാക്കിയ ബിസിനസുകൾ",
        "population_help": "റഫറൻസ് ജനസംഖ്യ",
        "seasonal_demand_help": "കണക്കാക്കിയ പ്രാദേശിക ആവശ്യത്തിന്റെ ശക്തി",
        "resource_help": "ബന്ധപ്പെട്ട വിഭവങ്ങളുടെ കണക്കാക്കിയ ലഭ്യത",

        "map_title": "പ്രാദേശിക ബിസിനസ് മാപ്പ്",
        "map_caption": "തിരഞ്ഞെടുത്ത പ്രദേശത്തിനുള്ള പ്രോട്ടോടൈപ്പ് ബിസിനസ് ലൊക്കേഷനുകൾ.",

        "data_source": "ഉറവിടം",
        "prototype_source": "പ്രോട്ടോടൈപ്പ് / ഡെമോ കണക്ക്",

        "language": "ഭാഷ",

        "profile_complete": "പ്രൊഫൈൽ വിജയകരമായി സംരക്ഷിച്ചു.",

        "malayalam": "മലയാളം",
        "english": "ഇംഗ്ലീഷ്",

        "skill_tailoring": "തയ്യൽ",
        "skill_baking": "ബേക്കിംഗ്",
        "skill_cooking": "പാചകം",
        "skill_farming": "കൃഷി",
        "skill_dairy": "ക്ഷീര മേഖല",
        "skill_handicraft": "കൈത്തൊഴിൽ",
        "skill_repair": "റിപ്പയർ & മെയിന്റനൻസ്",
        "skill_sales": "വിൽപ്പന",
        "skill_digital": "ഡിജിറ്റൽ കഴിവുകൾ",
        "skill_driving": "ഡ്രൈവിംഗ്",
        "skill_food_processing": "ഭക്ഷ്യ സംസ്കരണം",

        "interest_food": "ഭക്ഷണം & ബേക്കറി",
        "interest_dairy": "ക്ഷീര മേഖല",
        "interest_tailoring": "തയ്യൽ",
        "interest_farming": "കൃഷി",
        "interest_repair": "റിപ്പയർ സേവനങ്ങൾ",
        "interest_handicraft": "കൈത്തൊഴിൽ",

        "risk_low": "കുറവ്",
        "risk_medium": "ഇടത്തരം",
        "risk_high": "ഉയർന്നത്",

        "risk_low_desc": "സ്ഥിരതയുള്ളതും പ്രവചിക്കാവുന്നതുമായ ബിസിനസുകൾ ഇഷ്ടപ്പെടുന്നു.",
        "risk_medium_desc": "മിതമായ അനിശ്ചിതത്വം സ്വീകരിക്കാൻ തയ്യാറാണ്.",
        "risk_high_desc": "കൂടുതൽ സാധ്യതയ്ക്കായി ഉയർന്ന അനിശ്ചിതത്വവും സ്വീകരിക്കാൻ തയ്യാറാണ്.",
    },
}


# ============================================================
# ALL 14 KERALA DISTRICTS
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


# ============================================================
# DISTRICT MALAYALAM NAMES
# ============================================================

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
# LOCAL BODY DATA
#
# Prototype data for UI behavior.
# Replace with official LGD data later.
# ============================================================

LOCAL_BODIES = {

    "Alappuzha": [
        "Alappuzha Municipality",
        "Cherthala Municipality",
        "Chengannur Municipality",
        "Ambalappuzha South",
        "Kuttanad",
    ],

    "Ernakulam": [
        "Kochi Municipal Corporation",
        "Aluva Municipality",
        "Angamaly Municipality",
        "Perumbavoor Municipality",
        "Kunnathunad",
    ],

    "Idukki": [
        "Thodupuzha Municipality",
        "Kattappana Municipality",
        "Adimali",
        "Nedumkandam",
        "Devikulam",
    ],

    "Kannur": [
        "Kannur Municipal Corporation",
        "Thalassery Municipality",
        "Payyannur Municipality",
        "Mattannur Municipality",
        "Taliparamba Municipality",
    ],

    "Kasaragod": [
        "Kasaragod Municipality",
        "Kanhangad Municipality",
        "Nileshwar Municipality",
        "Manjeshwar",
        "Hosdurg",
    ],

    "Kollam": [
        "Kollam Municipal Corporation",
        "Karunagappally Municipality",
        "Kottarakkara Municipality",
        "Paravur Municipality",
        "Punalur Municipality",
    ],

    "Kottayam": [
        "Kottayam Municipality",
        "Changanassery Municipality",
        "Pala Municipality",
        "Vaikom Municipality",
        "Ettumanoor Municipality",
    ],

    "Kozhikode": [
        "Kozhikode Municipal Corporation",
        "Vadakara Municipality",
        "Koyilandy Municipality",
        "Feroke Municipality",
        "Ramanattukara",
    ],

    "Malappuram": [
        "Malappuram Municipality",
        "Manjeri Municipality",
        "Tirur Municipality",
        "Perinthalmanna Municipality",
        "Ponnani Municipality",
    ],

    "Palakkad": [
        "Palakkad Municipality",
        "Ottapalam Municipality",
        "Shoranur Municipality",
        "Chittur-Thathamangalam",
        "Mannarkkad Municipality",
    ],

    "Pathanamthitta": [
        "Pathanamthitta Municipality",
        "Adoor Municipality",
        "Thiruvalla Municipality",
        "Pandalam Municipality",
        "Ranni",
    ],

    "Thiruvananthapuram": [
        "Thiruvananthapuram Municipal Corporation",
        "Neyyattinkara Municipality",
        "Attingal Municipality",
        "Nedumangad Municipality",
        "Varkala Municipality",
    ],

    "Thrissur": [
        "Thrissur Municipal Corporation",
        "Chalakudy Municipality",
        "Kodungallur Municipality",
        "Kunnamkulam Municipality",
        "Guruvayur Municipality",
    ],

    "Wayanad": [
        "Kalpetta Municipality",
        "Mananthavady Municipality",
        "Sulthan Bathery Municipality",
        "Panamaram",
        "Meppadi",
    ],
}


# ============================================================
# LOCAL BODY MALAYALAM NAMES
# ============================================================

LOCAL_BODY_ML = {

    "Alappuzha Municipality": "ആലപ്പുഴ മുനിസിപ്പാലിറ്റി",
    "Cherthala Municipality": "ചേർത്തല മുനിസിപ്പാലിറ്റി",
    "Chengannur Municipality": "ചെങ്ങന്നൂർ മുനിസിപ്പാലിറ്റി",
    "Ambalappuzha South": "അമ്പലപ്പുഴ സൗത്ത്",
    "Kuttanad": "കുട്ടനാട്",

    "Kochi Municipal Corporation": "കൊച്ചി മുനിസിപ്പൽ കോർപ്പറേഷൻ",
    "Aluva Municipality": "ആലുവ മുനിസിപ്പാലിറ്റി",
    "Angamaly Municipality": "അങ്കമാലി മുനിസിപ്പാലിറ്റി",
    "Perumbavoor Municipality": "പെരുമ്പാവൂർ മുനിസിപ്പാലിറ്റി",
    "Kunnathunad": "കുന്നത്തുനാട്",

    "Thodupuzha Municipality": "തൊടുപുഴ മുനിസിപ്പാലിറ്റി",
    "Kattappana Municipality": "കട്ടപ്പന മുനിസിപ്പാലിറ്റി",
    "Adimali": "അടിമാലി",
    "Nedumkandam": "നെടുങ്കണ്ടം",
    "Devikulam": "ദേവികുളം",

    "Kannur Municipal Corporation": "കണ്ണൂർ മുനിസിപ്പൽ കോർപ്പറേഷൻ",
    "Thalassery Municipality": "തലശ്ശേരി മുനിസിപ്പാലിറ്റി",
    "Payyannur Municipality": "പയ്യന്നൂർ മുനിസിപ്പാലിറ്റി",
    "Mattannur Municipality": "മട്ടന്നൂർ മുനിസിപ്പാലിറ്റി",
    "Taliparamba Municipality": "തളിപ്പറമ്പ് മുനിസിപ്പാലിറ്റി",

    "Kasaragod Municipality": "കാസർഗോഡ് മുനിസിപ്പാലിറ്റി",
    "Kanhangad Municipality": "കാഞ്ഞങ്ങാട് മുനിസിപ്പാലിറ്റി",
    "Nileshwar Municipality": "നീലേശ്വരം മുനിസിപ്പാലിറ്റി",
    "Manjeshwar": "മഞ്ചേശ്വരം",
    "Hosdurg": "ഹോസ്ദുർഗ്",

    "Kollam Municipal Corporation": "കൊല്ലം മുനിസിപ്പൽ കോർപ്പറേഷൻ",
    "Karunagappally Municipality": "കരുനാഗപ്പള്ളി മുനിസിപ്പാലിറ്റി",
    "Kottarakkara Municipality": "കൊട്ടാരക്കര മുനിസിപ്പാലിറ്റി",
    "Paravur Municipality": "പരവൂർ മുനിസിപ്പാലിറ്റി",
    "Punalur Municipality": "പുനലൂർ മുനിസിപ്പാലിറ്റി",

    "Kottayam Municipality": "കോട്ടയം മുനിസിപ്പാലിറ്റി",
    "Changanassery Municipality": "ചങ്ങനാശ്ശേരി മുനിസിപ്പാലിറ്റി",
    "Pala Municipality": "പാലാ മുനിസിപ്പാലിറ്റി",
    "Vaikom Municipality": "വൈക്കം മുനിസിപ്പാലിറ്റി",
    "Ettumanoor Municipality": "ഏറ്റുമാനൂർ മുനിസിപ്പാലിറ്റി",

    "Kozhikode Municipal Corporation": "കോഴിക്കോട് മുനിസിപ്പൽ കോർപ്പറേഷൻ",
    "Vadakara Municipality": "വടകര മുനിസിപ്പാലിറ്റി",
    "Koyilandy Municipality": "കൊയിലാണ്ടി മുനിസിപ്പാലിറ്റി",
    "Feroke Municipality": "ഫറോക്ക് മുനിസിപ്പാലിറ്റി",
    "Ramanattukara": "രാമനാട്ടുകര",

    "Malappuram Municipality": "മലപ്പുറം മുനിസിപ്പാലിറ്റി",
    "Manjeri Municipality": "മഞ്ചേരി മുനിസിപ്പാലിറ്റി",
    "Tirur Municipality": "തിരൂർ മുനിസിപ്പാലിറ്റി",
    "Perinthalmanna Municipality": "പെരിന്തൽമണ്ണ മുനിസിപ്പാലിറ്റി",
    "Ponnani Municipality": "പൊന്നാനി മുനിസിപ്പാലിറ്റി",

    "Palakkad Municipality": "പാലക്കാട് മുനിസിപ്പാലിറ്റി",
    "Ottapalam Municipality": "ഒറ്റപ്പാലം മുനിസിപ്പാലിറ്റി",
    "Shoranur Municipality": "ഷൊർണൂർ മുനിസിപ്പാലിറ്റി",
    "Chittur-Thathamangalam": "ചിറ്റൂർ-തത്തമംഗലം",
    "Mannarkkad Municipality": "മണ്ണാർക്കാട് മുനിസിപ്പാലിറ്റി",

    "Pathanamthitta Municipality": "പത്തനംതിട്ട മുനിസിപ്പാലിറ്റി",
    "Adoor Municipality": "അടൂർ മുനിസിപ്പാലിറ്റി",
    "Thiruvalla Municipality": "തിരുവല്ല മുനിസിപ്പാലിറ്റി",
    "Pandalam Municipality": "പന്തളം മുനിസിപ്പാലിറ്റി",
    "Ranni": "റാന്നി",

    "Thiruvananthapuram Municipal Corporation": "തിരുവനന്തപുരം മുനിസിപ്പൽ കോർപ്പറേഷൻ",
    "Neyyattinkara Municipality": "നെയ്യാറ്റിൻകര മുനിസിപ്പാലിറ്റി",
    "Attingal Municipality": "ആറ്റിങ്ങൽ മുനിസിപ്പാലിറ്റി",
    "Nedumangad Municipality": "നെടുമങ്ങാട് മുനിസിപ്പാലിറ്റി",
    "Varkala Municipality": "വർക്കല മുനിസിപ്പാലിറ്റി",

    "Thrissur Municipal Corporation": "തൃശ്ശൂർ മുനിസിപ്പൽ കോർപ്പറേഷൻ",
    "Chalakudy Municipality": "ചാലക്കുടി മുനിസിപ്പാലിറ്റി",
    "Kodungallur Municipality": "കൊടുങ്ങല്ലൂർ മുനിസിപ്പാലിറ്റി",
    "Kunnamkulam Municipality": "കുന്നംകുളം മുനിസിപ്പാലിറ്റി",
    "Guruvayur Municipality": "ഗുരുവായൂർ മുനിസിപ്പാലിറ്റി",

    "Kalpetta Municipality": "കൽപ്പറ്റ മുനിസിപ്പാലിറ്റി",
    "Mananthavady Municipality": "മാനന്തവാടി മുനിസിപ്പാലിറ്റി",
    "Sulthan Bathery Municipality": "സുൽത്താൻ ബത്തേരി മുനിസിപ്പാലിറ്റി",
    "Panamaram": "പനമരം",
    "Meppadi": "മേപ്പാടി",
}


# ============================================================
# APPROXIMATE DISTRICT CENTERS
#
# Prototype coordinates.
# Used only to make the map respond to selection.
# ============================================================

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
}


for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# TRANSLATION HELPER
# ============================================================

def t(key):

    language = st.session_state.language

    return TEXT[language].get(key, key)


# ============================================================
# OPTION TRANSLATION DEFINITIONS
# ============================================================

SKILL_KEYS = [

    ("Tailoring", "skill_tailoring"),

    ("Baking", "skill_baking"),

    ("Cooking", "skill_cooking"),

    ("Farming", "skill_farming"),

    ("Dairy", "skill_dairy"),

    ("Handicrafts", "skill_handicraft"),

    ("Repair & Maintenance", "skill_repair"),

    ("Sales", "skill_sales"),

    ("Digital Skills", "skill_digital"),

    ("Driving", "skill_driving"),

    ("Food Processing", "skill_food_processing"),
]


INTEREST_KEYS = [

    ("Food & Bakery", "interest_food"),

    ("Dairy", "interest_dairy"),

    ("Tailoring", "interest_tailoring"),

    ("Agriculture", "interest_farming"),

    ("Repair Services", "interest_repair"),

    ("Handicrafts", "interest_handicraft"),
]


RISK_KEYS = [

    ("Low", "risk_low"),

    ("Medium", "risk_medium"),

    ("High", "risk_high"),
]


# ============================================================
# OPTION TRANSLATION HELPERS
# ============================================================

def translated_options(option_pairs):

    return [
        t(key)
        for _, key in option_pairs
    ]


def original_from_translated(selected, option_pairs):

    mapping = {
        t(key): original
        for original, key in option_pairs
    }

    return [
        mapping[x]
        for x in selected
        if x in mapping
    ]


def translated_risk_options():

    return [
        t(key)
        for _, key in RISK_KEYS
    ]


def original_risk_from_translated(value):

    mapping = {
        t(key): original
        for original, key in RISK_KEYS
    }

    return mapping.get(
        value,
        "Medium",
    )


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {{
        background-color: {WARM_CREAM};
        color: {DARK_BROWN};
    }}

    .main .block-container {{
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }}

    h1,
    h2,
    h3,
    h4 {{
        color: {DARK_BROWN} !important;
    }}

    p,
    label {{
        color: {DARK_BROWN};
    }}


    /* ========================================================
       HEADER
       ======================================================== */

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


    /* ========================================================
       STEP INDICATORS
       ======================================================== */

    .step-active {{
        background: {PRIMARY_GREEN};
        color: white !important;
        border-radius: 12px;
        padding: 10px 15px;
        text-align: center;
        font-weight: 700;
    }}

    .step-inactive {{
        background: #E6E8E1;
        color: {DARK_BROWN} !important;
        border-radius: 12px;
        padding: 10px 15px;
        text-align: center;
        font-weight: 600;
    }}


    /* ========================================================
       METRIC CARDS
       ======================================================== */

    .metric-card {{
        background: {WHITE};
        border: 1px solid #E5E4DC;
        border-radius: 16px;
        padding: 20px;
        min-height: 150px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.04);
    }}

    .metric-title {{
        color: {DARK_BROWN} !important;
        font-size: 14px;
        font-weight: 650;
    }}

    .metric-value {{
        color: {PRIMARY_GREEN} !important;
        font-size: 29px;
        font-weight: 800;
        margin-top: 8px;
    }}

    .metric-help {{
        color: #696B61 !important;
        font-size: 12px;
        margin-top: 5px;
    }}


    /* ========================================================
       DATA BADGE
       ======================================================== */

    .data-badge {{
        display: inline-block;
        background: #DDE8EF;
        color: {DARK_BROWN} !important;
        padding: 8px 13px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 13px;
        border: 1px solid #C5D5DF;
    }}

    .data-badge * {{
        color: {DARK_BROWN} !important;
    }}


    /* ========================================================
       INFO BOX
       ======================================================== */

    div[data-testid="stAlert"] {{
        border-radius: 12px;
    }}

    div[data-testid="stAlert"] p {{
        color: {DARK_BROWN} !important;
    }}

    div[data-testid="stAlert"] span {{
        color: {DARK_BROWN} !important;
    }}

    div[data-testid="stAlert"] div {{
        color: {DARK_BROWN} !important;
    }}


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {{
        border-radius: 10px;
        border: 1px solid {PRIMARY_GREEN};
        font-weight: 650;
    }}

    .stButton > button[kind="primary"] {{
        background: {PRIMARY_GREEN};
        color: white;
    }}


    /* ========================================================
       FRAME 1 + FRAME 2 SELECTBOXES
       SELECTED TEXT = WHITE
       ======================================================== */

    div[data-baseweb="select"] > div {{
        background-color: {PRIMARY_GREEN} !important;
        border-radius: 10px !important;
        border: 1px solid {PRIMARY_GREEN} !important;
    }}

    /* Main selected text */

    div[data-baseweb="select"] span {{
        color: white !important;
    }}

    /* Selected value containers */

    div[data-baseweb="select"] div {{
        color: white !important;
    }}

    /* Selected value text */

    div[data-baseweb="select"] input {{
        color: white !important;
        caret-color: white !important;
    }}

    /* Dropdown arrow */

    div[data-baseweb="select"] svg {{
        fill: white !important;
        color: white !important;
    }}


    /* ========================================================
       MULTISELECT SELECTED TAGS
       ======================================================== */

    div[data-baseweb="select"] [data-baseweb="tag"] {{
        background-color: {PRIMARY_GREEN} !important;
        color: white !important;
        border-radius: 7px !important;
    }}

    div[data-baseweb="select"] [data-baseweb="tag"] span {{
        color: white !important;
    }}

    div[data-baseweb="select"] [data-baseweb="tag"] svg {{
        fill: white !important;
        color: white !important;
    }}


    /* ========================================================
       DROPDOWN OPTIONS
       Keep these DARK because dropdown background is WHITE.
       ======================================================== */

    ul[role="listbox"] li {{
        color: {DARK_BROWN} !important;
        background-color: white !important;
    }}

    ul[role="listbox"] li span {{
        color: {DARK_BROWN} !important;
    }}

    ul[role="listbox"] li div {{
        color: {DARK_BROWN} !important;
    }}

    ul[role="listbox"] li:hover {{
        background-color: {LIGHT_GREEN} !important;
        color: {DARK_BROWN} !important;
    }}


    /* ========================================================
       RADIO BUTTON LABELS
       ======================================================== */

    div[data-testid="stRadio"] label p {{
        color: {DARK_BROWN} !important;
    }}


    /* ========================================================
       SLIDER
       ======================================================== */

    div[data-testid="stSlider"] {{
        padding-bottom: 10px;
    }}


    /* ========================================================
       NUMBER INPUT
       ======================================================== */

    div[data-testid="stNumberInput"] input {{
        color: {DARK_BROWN} !important;
        background-color: white !important;
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

                <div class="gv-header-title">
                    🌱 {t("app_title")}
                </div>

                <div class="gv-header-subtitle">
                    {t("tagline")}
                </div>

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
# STEP NAVIGATION
# ============================================================

def render_steps():

    cols = st.columns(3)

    steps = [

        (1, t("step1")),

        (2, t("step2")),

        (3, t("step3")),
    ]

    for col, (number, label) in zip(
        cols,
        steps,
    ):

        with col:

            if st.session_state.page == number:

                st.markdown(
                    f"""
                    <div class="step-active">
                        {label}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:

                st.markdown(
                    f"""
                    <div class="step-inactive">
                        {label}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.write("")


# ============================================================
# FRAME 1
# PROFILE INPUT
# ============================================================

def render_frame_1():

    st.markdown(
        f"## {t('profile_title')}"
    )

    st.caption(
        t("profile_subtitle")
    )


    # --------------------------------------------------------
    # SKILLS
    # --------------------------------------------------------

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

    st.session_state.skills = (
        original_from_translated(
            selected_skills,
            SKILL_KEYS,
        )
    )


    # --------------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # CAPITAL
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # BUSINESS INTERESTS
    # --------------------------------------------------------

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

    st.session_state.interests = (
        original_from_translated(
            interests,
            INTEREST_KEYS,
        )
    )


    # --------------------------------------------------------
    # RISK
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # EXISTING BUSINESS
    # --------------------------------------------------------

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

        st.session_state.business_name = (
            business_name
        )


    st.write("")


    # --------------------------------------------------------
    # CONTINUE
    # --------------------------------------------------------

    if st.button(

        t("continue"),

        type="primary",

        use_container_width=True,

        key="continue_frame1_v4",
    ):

        st.session_state.page = 2

        st.rerun()


# ============================================================
# FRAME 2 DATA GENERATOR
# ============================================================

def generate_location_data(
    district,
    local_body,
    ward,
):

    """
    Prototype deterministic location engine.

    This is NOT official data.

    It exists so the prototype visibly responds to:
        District
        Local Body
        Ward

    Real datasets will replace this later.
    """

    district_index = (

        KERALA_DISTRICTS.index(
            district
        )

        if district in KERALA_DISTRICTS

        else 0
    )

    body_list = LOCAL_BODIES.get(
        district,
        [],
    )

    body_index = (

        body_list.index(
            local_body
        )

        if local_body in body_list

        else 0
    )

    seed = (

        district_index * 1000

        + body_index * 100

        + int(ward)
    )

    rng = np.random.default_rng(
        seed
    )


    # --------------------------------------------------------
    # POPULATION
    # --------------------------------------------------------

    base_population = (
        18000
        + district_index * 900
    )

    population = int(

        base_population

        + body_index * 1700

        + int(ward) * 120

        + rng.integers(
            -500,
            501,
        )
    )


    # --------------------------------------------------------
    # BUSINESS DENSITY
    # --------------------------------------------------------

    business_density = round(

        8.5

        + district_index * 0.35

        + body_index * 0.6

        + (int(ward) % 10) * 0.15

        + rng.uniform(
            -0.4,
            0.4,
        ),

        1,
    )


    # --------------------------------------------------------
    # SEASONAL DEMAND
    # --------------------------------------------------------

    seasonal_demand = int(

        np.clip(

            55

            + district_index * 1.7

            + body_index * 3

            + (int(ward) % 12)

            + rng.integers(
                -4,
                5,
            ),

            0,

            100,
        )
    )


    # --------------------------------------------------------
    # RESOURCE AVAILABILITY
    # --------------------------------------------------------

    resource_availability = int(

        np.clip(

            58

            + body_index * 4

            + (int(ward) % 8)

            + rng.integers(
                -5,
                6,
            ),

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
# MAP DATA GENERATOR
# ============================================================

def generate_business_points(
    district,
    local_body,
    ward,
):

    """
    Generate tightly clustered prototype points.

    The previous version used a spread that was too large,
    which caused points to appear in the sea for some districts.

    This version keeps the points close to the selected center.
    """

    lat, lon = DISTRICT_COORDS[
        district
    ]

    body_list = LOCAL_BODIES.get(
        district,
        [],
    )

    body_index = (

        body_list.index(
            local_body
        )

        if local_body in body_list

        else 0
    )


    # --------------------------------------------------------
    # DETERMINISTIC SEED
    # --------------------------------------------------------

    seed = (

        KERALA_DISTRICTS.index(
            district
        ) * 100

        + body_index * 10

        + int(ward)
    )

    rng = np.random.default_rng(
        seed
    )


    # --------------------------------------------------------
    # VERY SMALL LOCATION OFFSET
    # --------------------------------------------------------
    #
    # We deliberately keep these offsets small.
    # This prevents the prototype points from drifting
    # into the Arabian Sea.
    #

    center_lat = (

        lat

        + (body_index - 2) * 0.0025

        + (int(ward) % 10) * 0.00015
    )

    center_lon = (

        lon

        + (body_index - 2) * 0.0025

        + (int(ward) % 8) * 0.00015
    )


    # --------------------------------------------------------
    # CREATE POINTS
    # --------------------------------------------------------

    points = []

    for i in range(10):

        point_lat = (

            center_lat

            + rng.normal(
                0,
                0.0018,
            )
        )

        point_lon = (

            center_lon

            + rng.normal(
                0,
                0.0018,
            )
        )

        points.append({

            "lat": point_lat,

            "lon": point_lon,
        })


    return pd.DataFrame(
        points
    )


# ============================================================
# METRIC CARD
# ============================================================

def metric_card(
    title,
    value,
    help_text,
):

    st.markdown(

        f"""
        <div class="metric-card">

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-help">
                {help_text}
            </div>

        </div>
        """,

        unsafe_allow_html=True,
    )


# ============================================================
# FRAME 2
# LOCAL DASHBOARD
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

    st.markdown(
        "### 📍 Location"
    )

    location_col1, location_col2, location_col3 = st.columns(
        [1, 1.4, 0.7]
    )


    # ========================================================
    # DISTRICT
    # ========================================================

    with location_col1:

        district_display_options = [

            DISTRICT_ML[district]

            if st.session_state.language == "ml"

            else district

            for district in KERALA_DISTRICTS
        ]

        current_district = (
            st.session_state.district
        )

        current_district_display = (

            DISTRICT_ML[
                current_district
            ]

            if st.session_state.language == "ml"

            else current_district
        )

        selected_district_display = st.selectbox(

            t("district"),

            district_display_options,

            index=district_display_options.index(
                current_district_display
            ),

            key="district_selector_v5",
        )


        # Reverse translation

        reverse_district = {

            (
                DISTRICT_ML[district]

                if st.session_state.language == "ml"

                else district
            ): district

            for district in KERALA_DISTRICTS
        }


        selected_district = reverse_district[
            selected_district_display
        ]


    # ========================================================
    # LOCAL BODY
    # ========================================================

    available_local_bodies = LOCAL_BODIES.get(

        selected_district,

        [],
    )


    # If district changes, make sure the local body
    # belongs to that district.

    if (

        st.session_state.local_body

        not in available_local_bodies
    ):

        st.session_state.local_body = (

            available_local_bodies[0]

            if available_local_bodies

            else ""
        )


    with location_col2:

        local_body_display_options = [

            LOCAL_BODY_ML.get(
                local_body,
                local_body,
            )

            if st.session_state.language == "ml"

            else local_body

            for local_body
            in available_local_bodies
        ]


        current_local_body = (
            st.session_state.local_body
        )


        current_local_body_display = (

            LOCAL_BODY_ML.get(

                current_local_body,

                current_local_body,
            )

            if st.session_state.language == "ml"

            else current_local_body
        )


        selected_local_body_display = st.selectbox(

            t("local_body"),

            local_body_display_options,

            index=local_body_display_options.index(

                current_local_body_display

            )

            if current_local_body_display
            in local_body_display_options

            else 0,

            key="local_body_selector_v5",
        )


        # Reverse translation

        reverse_local_body = {

            (
                LOCAL_BODY_ML.get(
                    local_body,
                    local_body,
                )

                if st.session_state.language == "ml"

                else local_body
            ): local_body

            for local_body
            in available_local_bodies
        }


        selected_local_body = reverse_local_body[
            selected_local_body_display
        ]


    # ========================================================
    # WARD
    # ========================================================

    with location_col3:

        selected_ward = st.number_input(

            t("ward"),

            min_value=1,

            max_value=100,

            value=int(
                st.session_state.ward
            ),

            step=1,

            key="ward_selector_v5",
        )


    # ========================================================
    # SAVE CURRENT LOCATION
    # ========================================================

    st.session_state.district = (
        selected_district
    )

    st.session_state.local_body = (
        selected_local_body
    )

    st.session_state.ward = int(
        selected_ward
    )


    # ========================================================
    # DATA LEVEL BADGE
    # ========================================================

    st.write("")

    st.markdown(

        f"""
        <div class="data-badge">

            🟢 {t("district_data")}

        </div>
        """,

        unsafe_allow_html=True,
    )

    st.write("")


    # ========================================================
    # INFO BOX
    # ========================================================

    st.info(
        t("location_note")
    )


    # ========================================================
    # LOCATION-SPECIFIC DATA
    # ========================================================

    location_data = generate_location_data(

        st.session_state.district,

        st.session_state.local_body,

        st.session_state.ward,
    )


    # ========================================================
    # FOUR METRIC CARDS
    # ========================================================

    metric_cols = st.columns(4)


    with metric_cols[0]:

        metric_card(

            t("business_density"),

            f"{location_data['business_density']}",

            t("business_density_help"),
        )


    with metric_cols[1]:

        metric_card(

            t("population"),

            f"{location_data['population']:,}",

            t("population_help"),
        )


    with metric_cols[2]:

        metric_card(

            t("seasonal_demand"),

            f"{location_data['seasonal_demand']}/100",

            t("seasonal_demand_help"),
        )


    with metric_cols[3]:

        metric_card(

            t("resource_availability"),

            f"{location_data['resource_availability']}/100",

            t("resource_help"),
        )


    st.write("")


    # ========================================================
    # MAP
    # ========================================================

    st.markdown(
        f"### {t('map_title')}"
    )


    st.caption(

        f"{st.session_state.district} → "

        f"{st.session_state.local_body} → "

        f"Ward {st.session_state.ward}"
    )


    map_df = generate_business_points(

        st.session_state.district,

        st.session_state.local_body,

        st.session_state.ward,
    )


    st.map(

        map_df,

        latitude="lat",

        longitude="lon",

        size=80,
    )


    st.caption(
        t("map_caption")
    )


    # ========================================================
    # SOURCE / DATA STATUS
    # ========================================================

    source_col1, source_col2 = st.columns(2)


    with source_col1:

        st.markdown(

            f"**{t('data_source')}:** "
            f"{t('prototype_source')}"
        )


    with source_col2:

        st.markdown(
            "**Data status:** Prototype / demo"
        )


    st.write("")


    # ========================================================
    # NAVIGATION
    # ========================================================

    nav1, nav2 = st.columns(2)


    with nav1:

        if st.button(

            t("back"),

            use_container_width=True,

            key="back_frame2_v5",
        ):

            st.session_state.page = 1

            st.rerun()


    with nav2:

        if st.button(

            t("continue"),

            type="primary",

            use_container_width=True,

            key="continue_frame2_v5",
        ):

            st.session_state.page = 3

            st.rerun()


# ============================================================
# FRAME 3 PLACEHOLDER
# ============================================================

def render_frame_3():

    st.markdown(
        f"## {t('step3')}"
    )

    st.info(
        "Frame 3 will be built after Frame 2 is verified."
    )


    if st.button(

        t("back"),

        use_container_width=True,

        key="back_frame3_v4",
    ):

        st.session_state.page = 2

        st.rerun()


# ============================================================
# MAIN APP ROUTER
# ============================================================

render_header()

render_steps()


if st.session_state.page == 1:

    render_frame_1()


elif st.session_state.page == 2:

    render_frame_2()


elif st.session_state.page == 3:

    render_frame_3()
