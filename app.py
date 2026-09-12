import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# GLOBAL STYLE
# -----------------------------

st.markdown("""
<style>

    .stApp {
        background-color: #F8FAF9;
    }

    .main-title {
        font-size: 36px;
        font-weight: 700;
        color: #173F35;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #66736F;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 650;
        color: #173F35;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    .info-card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #E4EAE7;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
        margin-bottom: 18px;
    }

    .confidence-high {
        display: inline-block;
        background: #E4F4EC;
        color: #176B4D;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    .confidence-medium {
        display: inline-block;
        background: #FFF3D6;
        color: #8A6500;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    .confidence-low {
        display: inline-block;
        background: #FBE4E4;
        color: #A33A3A;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    .step-text {
        text-align: center;
        color: #66736F;
        font-size: 14px;
        margin-bottom: 8px;
    }

    div.stButton > button {
        border-radius: 12px;
        min-height: 48px;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE
# -----------------------------

if "step" not in st.session_state:
    st.session_state.step = 1

if "skills" not in st.session_state:
    st.session_state.skills = []

if "interests" not in st.session_state:
    st.session_state.interests = []


# -----------------------------
# FRAME 1 — PROFILE INPUT
# -----------------------------

st.markdown(
    '<div class="main-title">🌾 GramVyapar AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Know Before You Borrow</div>',
    unsafe_allow_html=True
)

# Progress indicator

st.markdown(
    '<div class="step-text">Step 1 of 6</div>',
    unsafe_allow_html=True
)

progress = st.progress(1 / 6)

st.markdown(
    '<div class="section-title">Tell us about yourself</div>',
    unsafe_allow_html=True
)

st.write(
    "This helps us understand which business opportunities may fit you best."
)


# -----------------------------
# SKILLS
# -----------------------------

st.markdown("### 🛠️ Your skills")

skills = st.multiselect(
    "Select the skills you already have",
    [
        "Tailoring",
        "Cooking",
        "Carpentry",
        "Farming",
        "Dairy",
        "Poultry",
        "Repair",
        "Food Processing",
        "Other"
    ],
    default=st.session_state.skills
)

st.session_state.skills = skills


# -----------------------------
# EXPERIENCE
# -----------------------------

st.markdown("### 🧑‍🔧 Experience")

experience = st.number_input(
    "Years of experience",
    min_value=0,
    max_value=50,
    value=0,
    step=1
)


# -----------------------------
# CAPITAL
# -----------------------------

st.markdown("### 💰 Available capital")

capital = st.slider(
    "How much own capital can you invest?",
    min_value=0,
    max_value=500000,
    value=100000,
    step=5000
)

st.markdown(
    f"### ₹{capital:,.0f}"
)

st.caption(
    "This is the amount you can contribute from your own funds."
)


# -----------------------------
# BUSINESS INTERESTS
# -----------------------------

st.markdown("### 💡 Business interests")

interests = st.multiselect(
    "What types of businesses interest you?",
    [
        "Dairy",
        "Bakery",
        "Tailoring",
        "Grocery",
        "Poultry",
        "Food Processing",
        "Repair Services",
        "Other"
    ],
    default=st.session_state.interests
)

st.session_state.interests = interests


# -----------------------------
# RISK PREFERENCE
# -----------------------------

st.markdown("### ⚖️ Risk preference")

risk = st.radio(
    "How much business risk are you comfortable taking?",
    [
        "🟢 Low — Prefer stable and predictable businesses",
        "🟡 Medium — Comfortable with some uncertainty",
        "🔴 High — Willing to take higher risk for higher potential"
    ],
    index=1
)


# -----------------------------
# EXISTING BUSINESS
# -----------------------------

st.markdown("### 🏪 Existing business")

existing_business = st.toggle(
    "I already have a business"
)

existing_details = ""

if existing_business:
    existing_details = st.text_input(
        "Tell us briefly about your existing business",
        placeholder="Example: Small tailoring shop"
    )


# -----------------------------
# CONTINUE
# -----------------------------

st.divider()

if st.button(
    "Continue →",
    type="primary",
    use_container_width=True
):

    st.session_state.profile = {
        "skills": skills,
        "experience": experience,
        "capital": capital,
        "interests": interests,
        "risk": risk,
        "existing_business": existing_business,
        "existing_details": existing_details
    }

    st.session_state.step = 2

    st.success(
        "Profile saved! Next we will analyze your local area."
    )
