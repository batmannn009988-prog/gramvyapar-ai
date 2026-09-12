import streamlit as st


# ============================================================
# GRAMVYAPAR AI
# "Know Before You Borrow"
# ============================================================


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GLOBAL STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background-color: #F8FAF9;
    }

    /* Main content width */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Brand */
    .brand-title {
        font-size: 36px;
        font-weight: 700;
        color: #17483D;
        margin-bottom: 0;
    }

    .brand-subtitle {
        font-size: 17px;
        color: #66736F;
        margin-top: 2px;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        font-size: 24px;
        font-weight: 650;
        color: #17483D;
        margin-top: 24px;
        margin-bottom: 8px;
    }

    /* Small explanatory text */
    .helper-text {
        font-size: 15px;
        color: #66736F;
        line-height: 1.5;
    }

    /* Confidence badges */
    .confidence-high {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #E5F4EC;
        color: #176B4D;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    .confidence-medium {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #FFF3D6;
        color: #8A6500;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    .confidence-low {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #FBE4E4;
        color: #A33A3A;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    /* Buttons */
    div.stButton > button {
        min-height: 48px;
        border-radius: 12px;
        font-weight: 600;
    }

    /* Form inputs */
    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    /* Progress */
    .step-label {
        text-align: center;
        color: #66736F;
        font-size: 14px;
        margin-bottom: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

def initialize_session_state():
    """
    Creates the application's temporary frontend state.

    Later, these values can be sent to a backend API instead
    of being used only inside Streamlit.
    """

    defaults = {
        "current_screen": "profile",
        "profile": {},
        "location": {},
        "selected_business": None,
        "opportunities": [],
        "financial_plan": {},
        "risk_analysis": {},
        "scenario": {},
        "financing": {},
        "action_plan": [],
        "monthly_actuals": [],
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


initialize_session_state()


# ============================================================
# DATA / BACKEND SERVICE LAYER
# ============================================================

def save_profile(profile_data):
    """
    Temporary local implementation.

    Later:
        This function can call something like:

        POST /api/profile

    without changing the Profile UI.
    """

    st.session_state.profile = profile_data


def get_local_analysis(location):
    """
    Temporary placeholder for local analysis.

    Later this will call the backend/local-data service.

    Example future response:

        population
        households
        business_density
        seasonal_signal
        resource_availability
        data_level
        confidence
        sources
    """

    return {
        "population": "Demo",
        "business_density": "Demo",
        "seasonal_signal": "Demo",
        "resource_availability": "Demo",
        "data_level": "Demo",
        "confidence": "Estimate",
    }


def get_opportunities(profile, local_data):
    """
    Temporary opportunity service.

    Later this will call the real Opportunity Engine.
    """

    return []


# ============================================================
# REUSABLE UI COMPONENTS
# ============================================================

def confidence_badge(level="high", label="High confidence"):

    if level == "high":
        css_class = "confidence-high"
        dot = "●"

    elif level == "medium":
        css_class = "confidence-medium"
        dot = "●"

    else:
        css_class = "confidence-low"
        dot = "●"

    st.markdown(
        f'<span class="{css_class}">{dot} {label}</span>',
        unsafe_allow_html=True,
    )


def page_header(title, description=""):

    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True,
    )

    if description:
        st.markdown(
            f'<div class="helper-text">{description}</div>',
            unsafe_allow_html=True,
        )


# ============================================================
# FRAME 1 — PROFILE INPUT
# ============================================================

def render_profile_screen():

    # Brand
    st.markdown(
        '<div class="brand-title">🌾 GramVyapar AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="brand-subtitle">Know Before You Borrow</div>',
        unsafe_allow_html=True,
    )

    # Progress
    st.markdown(
        '<div class="step-label">Step 1 of 6</div>',
        unsafe_allow_html=True,
    )

    st.progress(1 / 6)

    page_header(
        "Tell us about yourself",
        "This helps us understand which business opportunities may fit you best.",
    )

    # --------------------------------------------------------
    # Skills
    # --------------------------------------------------------

    skills = st.multiselect(
        "🛠️ Your skills",
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
        help="Select the skills you already have.",
    )

    # --------------------------------------------------------
    # Experience
    # --------------------------------------------------------

    experience = st.number_input(
        "🧑‍🔧 Years of experience",
        min_value=0,
        max_value=50,
        value=0,
        step=1,
    )

    # --------------------------------------------------------
    # Capital
    # --------------------------------------------------------

    capital = st.slider(
        "💰 Available capital",
        min_value=0,
        max_value=500000,
        value=100000,
        step=5000,
    )

    st.markdown(
        f"### ₹{capital:,.0f}"
    )

    st.caption(
        "Your own funds available for starting or expanding the business."
    )

    # --------------------------------------------------------
    # Business interests
    # --------------------------------------------------------

    interests = st.multiselect(
        "💡 Business interests",
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
    )

    # --------------------------------------------------------
    # Risk preference
    # --------------------------------------------------------

    risk = st.radio(
        "⚖️ Risk preference",
        [
            "Low — Prefer stable and predictable businesses",
            "Medium — Comfortable with some uncertainty",
            "High — Willing to take higher risk for higher potential",
        ],
        index=1,
    )

    # --------------------------------------------------------
    # Existing business
    # --------------------------------------------------------

    existing_business = st.toggle(
        "🏪 I already have a business"
    )

    existing_details = ""

    if existing_business:

        existing_details = st.text_input(
            "Tell us briefly about your existing business",
            placeholder="Example: Small tailoring shop",
        )

    # --------------------------------------------------------
    # Continue
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

        # For now we simply move to Frame 2.
        # Frame 2 will be implemented next.

        st.session_state.current_screen = "local_dashboard"

        st.success(
            "Profile saved. Local analysis is the next step."
        )


# ============================================================
# FRAME 2 PLACEHOLDER
# ============================================================

def render_local_dashboard():

    st.markdown(
        '<div class="brand-title">🌾 GramVyapar AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="brand-subtitle">Know Before You Borrow</div>',
        unsafe_allow_html=True,
    )

    page_header(
        "Local Dashboard",
        "We will analyze your selected Kerala locality using available evidence.",
    )

    confidence_badge(
        "medium",
        "Demo — local data not connected yet",
    )

    st.info(
        "Frame 2 is ready for implementation. "
        "The real Kerala location and local-data engine will be connected here."
    )

    if st.button("← Back to Profile"):
        st.session_state.current_screen = "profile"


# ============================================================
# FUTURE SCREENS
# ============================================================

def render_opportunity_radar():
    page_header("Opportunity Radar")
    st.info("Frame 3 — Opportunity Radar will be implemented next.")


def render_business_detail():
    page_header("Business Detail")
    st.info("Frame 4 — Business Detail will be implemented next.")


def render_financial_dashboard():
    page_header("Financial Dashboard")
    st.info("Frame 5 — Financial Dashboard will be implemented next.")


def render_risk_dashboard():
    page_header("Risk Dashboard")
    st.info("Frame 6 — Risk Dashboard will be implemented next.")


def render_what_if():
    page_header("What-if Simulator")
    st.info("Frame 7 — What-if Simulator will be implemented next.")


def render_financing():
    page_header("Financing Guidance")
    st.info("Frame 8 — Financing Guidance will be implemented next.")


def render_action_plan():
    page_header("Action Plan")
    st.info("Frame 9 — Action Plan will be implemented next.")


def render_monitoring():
    page_header("Monthly Monitoring")
    st.info("Frame 10 — Monthly Monitoring will be implemented next.")


# ============================================================
# APPLICATION ROUTER
# ============================================================

def render_app():

    screen = st.session_state.current_screen

    if screen == "profile":
        render_profile_screen()

    elif screen == "local_dashboard":
        render_local_dashboard()

    elif screen == "opportunity_radar":
        render_opportunity_radar()

    elif screen == "business_detail":
        render_business_detail()

    elif screen == "financial_dashboard":
        render_financial_dashboard()

    elif screen == "risk_dashboard":
        render_risk_dashboard()

    elif screen == "what_if":
        render_what_if()

    elif screen == "financing":
        render_financing()

    elif screen == "action_plan":
        render_action_plan()

    elif screen == "monitoring":
        render_monitoring()

    else:
        st.session_state.current_screen = "profile"
        render_profile_screen()


# ============================================================
# START APPLICATION
# ============================================================

render_app()
