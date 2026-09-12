import streamlit as st


# ============================================================
# GRAMVYAPAR AI
# Know Before You Borrow
# ============================================================

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌾",
    layout="wide",
)


# ============================================================
# SIMPLE GLOBAL STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* App background */
    .stApp {
        background: #F8FAF9;
    }

    /* Main content */
    .block-container {
        max-width: 1100px;
        padding-top: 40px;
        padding-bottom: 50px;
    }

    /* Brand */
    .brand-title {
        font-size: 36px;
        font-weight: 700;
        color: #17483D;
        margin-bottom: 4px;
    }

    .brand-subtitle {
        font-size: 17px;
        color: #66736F;
        margin-bottom: 30px;
    }

    /* Section heading */
    .section-title {
        font-size: 26px;
        font-weight: 700;
        color: #17483D;
        margin-top: 25px;
        margin-bottom: 8px;
    }

    .description {
        font-size: 16px;
        color: #5F6B67;
        margin-bottom: 25px;
    }

    /* Small information text */
    .small-text {
        font-size: 14px;
        color: #66736F;
    }

    /* Buttons */
    .stButton > button {
        min-height: 48px;
        border-radius: 10px;
        font-weight: 600;
    }

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
# PROFILE STORAGE
# ============================================================

def save_profile(profile_data):
    st.session_state.profile = profile_data


# ============================================================
# FRAME 1 — PROFILE INPUT
# ============================================================

def render_profile():

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        '<div class="brand-title">🌾 GramVyapar AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="brand-subtitle">Know Before You Borrow</div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    st.caption("Step 1 of 6")

    st.progress(1 / 6)


    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Tell us about yourself</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="description">'
        'This helps us understand which business opportunities may fit you best.'
        '</div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # SKILLS
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
        placeholder="Select your skills",
    )


    # --------------------------------------------------------
    # EXPERIENCE
    # --------------------------------------------------------

    experience = st.number_input(
        "🧑‍🔧 Years of experience",
        min_value=0,
        max_value=50,
        value=0,
        step=1,
    )


    # --------------------------------------------------------
    # CAPITAL
    # --------------------------------------------------------

    st.markdown("### 💰 Available capital")

    capital = st.slider(
        "Available capital",
        min_value=0,
        max_value=500000,
        value=100000,
        step=5000,
        format="₹%d",
        label_visibility="collapsed",
    )

    st.markdown(
        f"**₹{capital:,.0f}**"
    )

    st.caption(
        "Your own funds available for starting or expanding the business."
    )


    # --------------------------------------------------------
    # BUSINESS INTERESTS
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
        placeholder="Select businesses you are interested in",
    )


    # --------------------------------------------------------
    # RISK PREFERENCE
    # --------------------------------------------------------

    st.markdown("### ⚖️ Risk preference")

    st.caption(
        "How comfortable are you with uncertainty when starting a business?"
    )

    risk = st.radio(
        "Risk preference",
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
        st.info(
            "Low risk — Prefer stable and predictable businesses."
        )

    elif risk == "Medium":
        st.info(
            "Medium risk — Comfortable with some uncertainty."
        )

    else:
        st.warning(
            "High risk — Willing to accept more uncertainty for higher potential."
        )


    # --------------------------------------------------------
    # EXISTING BUSINESS
    # --------------------------------------------------------

    existing_business = st.toggle(
        "🏪 I already have a business"
    )

    existing_details = ""

    if existing_business:

        existing_details = st.text_input(
            "Tell us about your existing business",
            placeholder="Example: Small tailoring shop",
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
        '<div class="brand-title">🌾 GramVyapar AI</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="brand-subtitle">Know Before You Borrow</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="section-title">Local Dashboard</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="description">'
        'Your Kerala locality will be analyzed using available local evidence.'
        '</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "Frame 2 will be connected to the Kerala location and local-data engine next."
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
# RUN APP
# ============================================================

main()
