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
        padding-top: 35px;
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
        color: #6F7466;
        font-size: 16px;
        margin-left: 51px;
        margin-bottom: 30px;
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
        color: #6F7466;
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
        color: #777A70;
        margin-bottom: 8px;
    }}


    /* ==============================
       STREAMLIT INPUT TEXT
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

    input {{
        color: {TEXT} !important;
    }}

    textarea {{
        color: {TEXT} !important;
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
        border: 1px solid #D9DED1;
        min-height: 48px;
    }}

    [data-baseweb="tag"] {{
        background-color: #E8EEDC !important;
        color: {PRIMARY} !important;
        border-radius: 20px !important;
    }}


    /* ==============================
       NUMBER INPUT
       ============================== */

    [data-testid="stNumberInput"] {{
        background-color: {CARD};
        border-radius: 12px;
    }}


    /* ==============================
       SLIDER
       ============================== */

    [data-testid="stSlider"] {{
        padding-top: 5px;
        padding-bottom: 5px;
    }}


    /* ==============================
       RISK CARDS
       ============================== */

    .risk-description {{
        background-color: {CARD};
        border: 1px solid #E1E3DB;
        border-radius: 14px;
        padding: 14px 16px;
        margin-top: 10px;
        color: #62665C;
        font-size: 14px;
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

    Later this function can send the same structured data
    to our Python backend/API.
    """

    st.session_state.profile = profile_data


# ============================================================
# FRAME 1 — PROFILE INPUT
# ============================================================

def render_profile():

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
        '<div class="tagline">Know Before You Borrow</div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    st.markdown(
        '<div class="progress-text">Step 1 of 6</div>',
        unsafe_allow_html=True,
    )

    st.progress(1 / 6)


    # --------------------------------------------------------
    # INTRO
    # --------------------------------------------------------

    st.markdown(
        '<div class="intro-title">Tell us about yourself</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="intro-description">'
        'This helps us understand which business opportunities may fit you best.'
        '</div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # SKILLS
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">🛠️ Your skills</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="field-description">'
        'Choose the skills you already have.'
        '</div>',
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
        placeholder="Select your skills",
        label_visibility="collapsed",
    )


    # --------------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">🧑‍🔧 Years of experience</div>',
        unsafe_allow_html=True,
    )

    experience = st.number_input(
        "Experience",
        min_value=0,
        max_value=50,
        value=0,
        step=1,
        label_visibility="collapsed",
    )

    st.caption("Enter the number of years you have worked in your main skill.")


    # --------------------------------------------------------
    # CAPITAL
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">💰 Available capital</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="field-description">'
        'How much of your own money can you invest?'
        '</div>',
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

    st.caption(
        "Your own funds available for starting or expanding the business."
    )


    # --------------------------------------------------------
    # BUSINESS INTERESTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">💡 Business interests</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="field-description">'
        'Choose the types of businesses you are interested in.'
        '</div>',
        unsafe_allow_html=True,
    )

    interests = st.multiselect(
        "Interests",
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
        placeholder="Select your interests",
        label_visibility="collapsed",
    )


    # --------------------------------------------------------
    # RISK PREFERENCE
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">⚖️ Risk preference</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="field-description">'
        'How comfortable are you with uncertainty when starting a business?'
        '</div>',
        unsafe_allow_html=True,
    )

    risk = st.radio(
        "Risk",
        [
            "Low",
            "Medium",
            "High",
        ],
        index=1,
        horizontal=True,
        label_visibility="collapsed",
    )

    if risk == "Low":

        st.markdown(
            '<div class="risk-description">'
            '🟢 <b>Low risk</b> — Prefer stable and predictable businesses.'
            '</div>',
            unsafe_allow_html=True,
        )

    elif risk == "Medium":

        st.markdown(
            '<div class="risk-description">'
            '🟠 <b>Medium risk</b> — Comfortable with some uncertainty.'
            '</div>',
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            '<div class="risk-description">'
            '🔴 <b>High risk</b> — Willing to accept more uncertainty '
            'for higher potential.'
            '</div>',
            unsafe_allow_html=True,
        )


    # --------------------------------------------------------
    # EXISTING BUSINESS
    # --------------------------------------------------------

    st.markdown(
        '<div class="field-label">🏪 Existing business</div>',
        unsafe_allow_html=True,
    )

    existing_business = st.toggle(
        "I already have a business"
    )

    existing_details = ""

    if existing_business:

        existing_details = st.text_input(
            "Existing business",
            placeholder="Example: Small tailoring shop",
            label_visibility="collapsed",
        )


    # --------------------------------------------------------
    # CONTINUE
    # --------------------------------------------------------

    st.divider()

    if st.button(
        "Continue →",
        type="primary",
        use_container_width=True,
    ):

        profile_data = {
            "skills": skills,
            "experience_years": experience,
            "available_capital": capital,
            "business_interests": interests,
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
        '<div class="tagline">Know Before You Borrow</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="intro-title">Local Dashboard</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="intro-description">'
        'Your Kerala locality will be analyzed using available local evidence.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "Frame 2 will connect to the Kerala location and local-data engine."
    )

    if st.button("← Back to Profile"):

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
