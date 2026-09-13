import streamlit as st


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {
    "en": {
        "title": "Opportunity Radar",
        "subtitle": (
            "Explore business opportunities that fit your skills, "
            "capital and local market."
        ),
        "profile": "Your Profile",
        "capital": "Available Capital",
        "experience": "Experience",
        "years": "years",
        "skills": "Skills",
        "business_interests": "Business Interests",
        "local_market": "Local Market",
        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward",
        "recommended": "Recommended Opportunities",
        "score_note": (
            "Prototype opportunity score calculated from demand, "
            "competition fit, skill fit, capital fit, experience "
            "and risk fit."
        ),
        "demand": "Demand",
        "competition": "Competition Fit",
        "skill": "Skill Fit",
        "capital_fit": "Capital Fit",
        "experience_fit": "Experience Fit",
        "risk_fit": "Risk Fit",
        "why": "Why this fits",
        "select": "Select this business",
        "selected": "Selected",
        "selected_message": "You selected",
        "confidence": "Data Confidence",
        "prototype_warning": (
            "Prototype / demo estimates are currently being used. "
            "These scores are calculated by the demo recommendation "
            "engine and are NOT verified local market statistics."
        ),
        "engine": "Recommendation Engine Status",
        "engine_working": (
            "The recommendation engine is active. Your profile "
            "inputs are being used to calculate the scores."
        ),
        "back": "← Back",
        "continue": "Continue →",
        "no_selection": (
            "Please select a business opportunity before continuing."
        ),
        "select_first": "Select a business first.",
        "high_match": "Strong match based on your profile.",
        "medium_match": "Moderate match. Further validation is recommended.",
        "lower_match": "Lower match for your current profile.",
        "skill_reason": "Your skills support this business.",
        "interest_reason": "This matches your stated business interests.",
        "capital_reason": "Your available capital is suitable for this business.",
        "experience_reason": "Your experience supports this type of business.",
        "risk_reason": "The risk profile is relatively suitable for your preference.",
        "location_reason": "This opportunity can be explored in your selected local market.",
    },

    "ml": {
        "title": "ബിസിനസ് അവസരങ്ങൾ",
        "subtitle": (
            "നിങ്ങളുടെ കഴിവുകൾ, മൂലധനം, അനുഭവം, താൽപര്യങ്ങൾ "
            "എന്നിവയ്ക്ക് അനുയോജ്യമായ ബിസിനസ് അവസരങ്ങൾ കണ്ടെത്തുക."
        ),
        "profile": "നിങ്ങളുടെ പ്രൊഫൈൽ",
        "capital": "ലഭ്യമായ മൂലധനം",
        "experience": "അനുഭവം",
        "years": "വർഷം",
        "skills": "കഴിവുകൾ",
        "business_interests": "ബിസിനസ് താൽപര്യങ്ങൾ",
        "local_market": "പ്രാദേശിക വിപണി",
        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ്",
        "recommended": "ശുപാർശ ചെയ്യുന്ന ബിസിനസ് അവസരങ്ങൾ",
        "score_note": (
            "ഡിമാൻഡ്, മത്സരം, കഴിവ്, മൂലധനം, അനുഭവം, "
            "റിസ്ക് എന്നിവ അടിസ്ഥാനമാക്കി കണക്കാക്കിയ ഡെമോ സ്കോർ."
        ),
        "demand": "ഡിമാൻഡ്",
        "competition": "മത്സര അനുയോജ്യത",
        "skill": "കഴിവ് അനുയോജ്യത",
        "capital_fit": "മൂലധന അനുയോജ്യത",
        "experience_fit": "അനുഭവ അനുയോജ്യത",
        "risk_fit": "റിസ്ക് അനുയോജ്യത",
        "why": "എന്തുകൊണ്ട് ഇത് അനുയോജ്യമാണ്",
        "select": "ഈ ബിസിനസ് തിരഞ്ഞെടുക്കുക",
        "selected": "തിരഞ്ഞെടുത്തു",
        "selected_message": "നിങ്ങൾ തിരഞ്ഞെടുത്തത്",
        "confidence": "ഡാറ്റാ വിശ്വാസ്യത",
        "prototype_warning": (
            "നിലവിൽ പ്രോട്ടോടൈപ്പ് / ഡെമോ കണക്കുകളാണ് ഉപയോഗിക്കുന്നത്. "
            "ഈ സ്കോറുകൾ ഡെമോ ശുപാർശ എഞ്ചിൻ കണക്കാക്കുന്നതാണ്; "
            "ഇവ പരിശോധിച്ച പ്രാദേശിക വിപണി കണക്കുകളല്ല."
        ),
        "engine": "ശുപാർശ എഞ്ചിൻ നില",
        "engine_working": (
            "ശുപാർശ എഞ്ചിൻ പ്രവർത്തിക്കുന്നു. നിങ്ങളുടെ പ്രൊഫൈൽ "
            "വിവരങ്ങൾ ഉപയോഗിച്ചാണ് സ്കോറുകൾ കണക്കാക്കുന്നത്."
        ),
        "back": "← പിന്നിലേക്ക്",
        "continue": "തുടരുക →",
        "no_selection": (
            "തുടരുന്നതിന് മുമ്പ് ഒരു ബിസിനസ് അവസരം തിരഞ്ഞെടുക്കുക."
        ),
        "select_first": "ആദ്യം ഒരു ബിസിനസ് തിരഞ്ഞെടുക്കുക.",
        "high_match": "നിങ്ങളുടെ പ്രൊഫൈലുമായി വളരെ നല്ല പൊരുത്തം.",
        "medium_match": "മിതമായ പൊരുത്തം. കൂടുതൽ പരിശോധന ശുപാർശ ചെയ്യുന്നു.",
        "lower_match": "നിലവിലെ പ്രൊഫൈലിന് താരതമ്യേന കുറഞ്ഞ പൊരുത്തം.",
        "skill_reason": "നിങ്ങളുടെ കഴിവുകൾ ഈ ബിസിനസിന് അനുയോജ്യമാണ്.",
        "interest_reason": "ഇത് നിങ്ങൾ നൽകിയ ബിസിനസ് താൽപര്യവുമായി പൊരുത്തപ്പെടുന്നു.",
        "capital_reason": "നിങ്ങളുടെ ലഭ്യമായ മൂലധനം ഈ ബിസിനസിന് അനുയോജ്യമാണ്.",
        "experience_reason": "നിങ്ങളുടെ അനുഭവം ഈ ബിസിനസിനെ പിന്തുണയ്ക്കുന്നു.",
        "risk_reason": "നിങ്ങളുടെ റിസ്ക് മുൻഗണനയ്ക്ക് ഇത് താരതമ്യേന അനുയോജ്യമാണ്.",
        "location_reason": "നിങ്ങൾ തിരഞ്ഞെടുത്ത പ്രാദേശിക വിപണിയിൽ ഇത് പരിശോധിക്കാവുന്നതാണ്.",
    },
}


# ============================================================
# BUSINESS DATA
# Prototype data only
# ============================================================

BUSINESSES = [
    {
        "name_en": "Bakery / Food",
        "name_ml": "ബേക്കറി / ഭക്ഷ്യ ബിസിനസ്",

        # Prototype base market scores
        "demand": 82,
        "competition": 62,

        # Recommended capital range
        "min_capital": 40000,
        "ideal_capital": 150000,
        "max_capital": 500000,

        # Experience requirement
        "ideal_experience": 3,

        # Relevant profile words
        "skills": [
            "Cooking / Food Preparation",
            "Business Management",
            "Sales / Marketing",
        ],
        "interests": [
            "Food / Bakery",
        ],

        # Risk baseline
        "risk": 65,
    },

    {
        "name_en": "Tailoring",
        "name_ml": "ടെയിലറിംഗ്",

        "demand": 76,
        "competition": 68,

        "min_capital": 25000,
        "ideal_capital": 80000,
        "max_capital": 250000,

        "ideal_experience": 2,

        "skills": [
            "Tailoring / Sewing",
            "Design / Handicrafts",
            "Sales / Marketing",
        ],
        "interests": [
            "Tailoring / Fashion",
        ],

        "risk": 80,
    },

    {
        "name_en": "Dairy",
        "name_ml": "ക്ഷീര / ഡയറി ബിസിനസ്",

        "demand": 72,
        "competition": 58,

        "min_capital": 75000,
        "ideal_capital": 250000,
        "max_capital": 500000,

        "ideal_experience": 3,

        "skills": [
            "Animal Care",
            "Farming / Agriculture",
            "Business Management",
        ],
        "interests": [
            "Dairy / Livestock",
            "Farming / Agriculture",
        ],

        "risk": 60,
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def calculate_capital_fit(capital, business):
    """
    Calculates how suitable the user's available capital is
    for the business.

    Returns 0-100.
    """

    minimum = business["min_capital"]
    ideal = business["ideal_capital"]
    maximum = business["max_capital"]

    if capital < minimum:
        # Strong penalty when capital is below minimum requirement
        ratio = capital / minimum if minimum > 0 else 0
        return max(20, min(60, ratio * 60))

    if minimum <= capital <= ideal:
        # Excellent fit
        return 95

    if ideal < capital <= maximum:
        # Still good, but extra capital does not increase fit
        return 88

    # Capital significantly above expected range
    return 75


def calculate_skill_fit(user_skills, business):
    """
    Calculates skill compatibility.
    """

    if not user_skills:
        return 50

    matches = 0

    for skill in user_skills:
        if skill in business["skills"]:
            matches += 1

    if matches >= 2:
        return 95

    if matches == 1:
        return 82

    return 45


def calculate_interest_fit(user_interests, business):
    """
    Calculates business-interest compatibility.
    """

    if not user_interests:
        return 50

    matches = 0

    for interest in user_interests:
        if interest in business["interests"]:
            matches += 1

    if matches >= 2:
        return 100

    if matches == 1:
        return 95

    return 35


def calculate_experience_fit(experience, business):
    """
    Calculates experience compatibility.
    """

    ideal = business["ideal_experience"]

    if experience >= ideal:
        return 95

    if experience == 0:
        return 45

    # Partial experience
    return int(45 + (experience / ideal) * 45)


def calculate_risk_fit(user_risk, business):
    """
    User risk preference:
        Low
        Medium
        High

    Business risk is represented as a compatibility score.
    """

    if user_risk == "Low":
        if business["risk"] >= 75:
            return 90
        elif business["risk"] >= 60:
            return 70
        else:
            return 50

    if user_risk == "High":
        if business["risk"] >= 70:
            return 90
        elif business["risk"] >= 55:
            return 75
        else:
            return 60

    # Medium
    if business["risk"] >= 60:
        return 85

    return 70


def calculate_location_bonus(local_body):
    """
    Prototype location adjustment.

    This is intentionally small because we do not yet have
    verified ward-level market data.
    """

    if not local_body:
        return 50

    # Municipality / corporation environments can support
    # more consumer-facing businesses in this prototype.
    if "Municipal" in local_body or "Corporation" in local_body:
        return 80

    return 70


def calculate_opportunity(business):
    """
    Main recommendation engine.

    Final score:

    20% Demand
    15% Competition
    20% Skill Fit
    20% Capital Fit
    10% Experience Fit
    10% Interest Fit
    5% Risk Fit

    Returns all calculated components.
    """

    capital = float(st.session_state.get("capital", 0))
    experience = int(st.session_state.get("experience", 0))
    skills = st.session_state.get("skills", [])
    interests = st.session_state.get("interests", [])
    risk = st.session_state.get("risk", "Medium")
    local_body = st.session_state.get("local_body", "")

    demand = business["demand"]
    competition = business["competition"]

    skill_fit = calculate_skill_fit(
        skills,
        business
    )

    capital_fit = calculate_capital_fit(
        capital,
        business
    )

    experience_fit = calculate_experience_fit(
        experience,
        business
    )

    interest_fit = calculate_interest_fit(
        interests,
        business
    )

    risk_fit = calculate_risk_fit(
        risk,
        business
    )

    location_fit = calculate_location_bonus(
        local_body
    )

    # Small local adjustment
    adjusted_demand = int(
        demand * 0.90 +
        location_fit * 0.10
    )

    score = (
        adjusted_demand * 0.20
        + competition * 0.15
        + skill_fit * 0.20
        + capital_fit * 0.20
        + experience_fit * 0.10
        + interest_fit * 0.10
        + risk_fit * 0.05
    )

    score = max(0, min(100, round(score)))

    return {
        "name_en": business["name_en"],
        "name_ml": business["name_ml"],
        "score": score,
        "demand": adjusted_demand,
        "competition": competition,
        "skill": skill_fit,
        "capital": capital_fit,
        "experience": experience_fit,
        "interest": interest_fit,
        "risk": risk_fit,
        "business_risk": business["risk"],
        "business": business,
    }


def get_match_message(score, lang):
    if score >= 80:
        return TEXT[lang]["high_match"]

    if score >= 65:
        return TEXT[lang]["medium_match"]

    return TEXT[lang]["lower_match"]


def build_reasons(result, lang):
    """
    Creates dynamic explanations based on the actual
    calculated scores.
    """

    reasons = []

    if result["skill"] >= 80:
        reasons.append(TEXT[lang]["skill_reason"])

    if result["interest"] >= 80:
        reasons.append(TEXT[lang]["interest_reason"])

    if result["capital"] >= 80:
        reasons.append(TEXT[lang]["capital_reason"])

    if result["experience"] >= 80:
        reasons.append(TEXT[lang]["experience_reason"])

    if result["risk"] >= 80:
        reasons.append(TEXT[lang]["risk_reason"])

    if not reasons:
        reasons.append(TEXT[lang]["location_reason"])

    return " ".join(reasons)


# ============================================================
# MAIN FRAME
# ============================================================

def render_frame3():

    # --------------------------------------------------------
    # LANGUAGE
    # --------------------------------------------------------

    language = st.session_state.get("language", "en")

    if language not in TEXT:
        language = "en"

    t = TEXT[language]

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(f"## {t['title']}")

    st.caption(t["subtitle"])

    st.write("")

    # --------------------------------------------------------
    # USER PROFILE SUMMARY
    # --------------------------------------------------------

    st.markdown(f"### {t['profile']}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        capital = st.session_state.get("capital", 0)

        st.metric(
            t["capital"],
            f"₹{capital:,.0f}"
        )

    with col2:
        experience = st.session_state.get("experience", 0)

        st.metric(
            t["experience"],
            f"{experience} {t['years']}"
        )

    with col3:
        skills = st.session_state.get("skills", [])

        st.metric(
            t["skills"],
            len(skills)
        )

    with col4:
        interests = st.session_state.get("interests", [])

        st.metric(
            t["business_interests"],
            len(interests)
        )

    st.write("")

    # --------------------------------------------------------
    # LOCATION
    # --------------------------------------------------------

    st.markdown(f"### {t['local_market']}")

    location_col1, location_col2, location_col3 = st.columns(3)

    with location_col1:
        st.write(f"**{t['district']}**")
        st.write(
            st.session_state.get(
                "district",
                "-"
            )
        )

    with location_col2:
        st.write(f"**{t['local_body']}**")
        st.write(
            st.session_state.get(
                "local_body",
                "-"
            )
        )

    with location_col3:
        st.write(f"**{t['ward']}**")
        st.write(
            st.session_state.get(
                "ward",
                "-"
            )
        )

    st.write("")

    # --------------------------------------------------------
    # CALCULATE RECOMMENDATIONS
    # --------------------------------------------------------

    results = []

    for business in BUSINESSES:

        result = calculate_opportunity(
            business
        )

        results.append(result)

    # Highest score first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    st.markdown(
        f"### {t['recommended']}"
    )

    st.caption(
        t["score_note"]
    )

    st.write("")

    # --------------------------------------------------------
    # BUSINESS CARDS
    # --------------------------------------------------------

    for index, result in enumerate(results):

        business = result["business"]

        if language == "ml":
            business_name = result["name_ml"]
        else:
            business_name = result["name_en"]

        # Rank heading
        st.markdown(
            f"### #{index + 1}  {business_name}"
        )

        # Main score
        score_col1, score_col2 = st.columns(
            [1, 4]
        )

        with score_col1:
            st.metric(
                "Score",
                f"{result['score']}/100"
            )

        with score_col2:
            st.progress(
                result["score"] / 100
            )

            st.caption(
                get_match_message(
                    result["score"],
                    language
                )
            )

        st.write("")

        # Five/six scoring factors
        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                f"**{t['demand']}**"
            )

            st.progress(
                result["demand"] / 100
            )

            st.caption(
                f"{result['demand']}%"
            )

        with col2:

            st.write(
                f"**{t['competition']}**"
            )

            st.progress(
                result["competition"] / 100
            )

            st.caption(
                f"{result['competition']}%"
            )

        with col3:

            st.write(
                f"**{t['skill']}**"
            )

            st.progress(
                result["skill"] / 100
            )

            st.caption(
                f"{result['skill']}%"
            )

        col4, col5, col6 = st.columns(3)

        with col4:

            st.write(
                f"**{t['capital_fit']}**"
            )

            st.progress(
                result["capital"] / 100
            )

            st.caption(
                f"{result['capital']}%"
            )

        with col5:

            st.write(
                f"**{t['experience_fit']}**"
            )

            st.progress(
                result["experience"] / 100
            )

            st.caption(
                f"{result['experience']}%"
            )

        with col6:

            st.write(
                f"**{t['risk_fit']}**"
            )

            st.progress(
                result["risk"] / 100
            )

            st.caption(
                f"{result['risk']}%"
            )

        st.write("")

        # ----------------------------------------------------
        # WHY THIS FITS
        # ----------------------------------------------------

        reasons = build_reasons(
            result,
            language
        )

        st.info(
            f"**{t['why']}:** {reasons}"
        )

        st.write("")

        # ----------------------------------------------------
        # SELECT BUSINESS
        # ----------------------------------------------------

        selected_business = st.session_state.get(
            "selected_business",
            None
        )

        is_selected = (
            selected_business
            == result["name_en"]
        )

        if is_selected:

            st.success(
                f"✓ {t['selected']}: "
                f"{business_name}"
            )

        else:

            if st.button(
                f"{t['select']} — {business_name}",
                use_container_width=True,
                key=f"select_business_{index}",
            ):

                st.session_state.selected_business = (
                    result["name_en"]
                )

                st.session_state.selected_business_ml = (
                    result["name_ml"]
                )

                st.session_state.selected_business_score = (
                    result["score"]
                )

                st.rerun()

        st.divider()

    # --------------------------------------------------------
    # ENGINE STATUS
    # --------------------------------------------------------

    st.markdown(
        f"### {t['engine']}"
    )

    st.success(
        f"✓ {t['engine_working']}"
    )

    # --------------------------------------------------------
    # DATA CONFIDENCE
    # --------------------------------------------------------

    st.markdown(
        f"### {t['confidence']}"
    )

    st.warning(
        t["prototype_warning"]
    )

    # --------------------------------------------------------
    # SELECTED BUSINESS SUMMARY
    # --------------------------------------------------------

    selected_business = st.session_state.get(
        "selected_business",
        None
    )

    if selected_business:

        if language == "ml":

            selected_display = st.session_state.get(
                "selected_business_ml",
                selected_business
            )

        else:

            selected_display = selected_business

        selected_score = st.session_state.get(
            "selected_business_score",
            0
        )

        st.info(
            f"**{t['selected_message']}:** "
            f"{selected_display} "
            f"({selected_score}/100)"
        )

    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    st.write("")

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            t["back"],
            use_container_width=True,
            key="back_frame3",
        ):

            st.session_state.page = 2
            st.rerun()

    with continue_col:

        if st.button(
            t["continue"],
            type="primary",
            use_container_width=True,
            key="continue_frame3",
        ):

            if not selected_business:

                st.error(
                    t["no_selection"]
                )

            else:

                # Store everything Frame 4 will need
                st.session_state.selected_business = (
                    selected_business
                )

                st.session_state.page = 4

                st.rerun()
