
import streamlit as st


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {
    "en": {
        "title": "Opportunity Radar",
        "subtitle": "Business opportunities ranked for your profile and local market.",
        "your_profile": "Your Profile",
        "capital": "Available Capital",
        "skills": "Skills",
        "experience": "Experience",
        "interests": "Business Interests",
        "recommendations": "Recommended Opportunities",
        "score": "Match Score",
        "demand": "Demand",
        "competition": "Competition",
        "skill_fit": "Skill Fit",
        "capital_fit": "Capital Fit",
        "experience_fit": "Experience Fit",
        "interest_fit": "Interest Fit",
        "risk_fit": "Risk Fit",
        "why": "Why this fits you",
        "select": "Select this business",
        "continue": "Continue to Business Detail →",
        "no_selection": "Please select a business first.",
        "selected": "Selected",
        "strong_match": "Strong Match",
        "good_match": "Good Match",
        "review": "Needs Review",
        "local_adjustment": "Local market adjustment",
    },

    "ml": {
        "title": "അവസര റഡാർ",
        "subtitle": "നിങ്ങളുടെ പ്രൊഫൈലിനും പ്രാദേശിക വിപണിക്കും അനുയോജ്യമായ ബിസിനസുകൾ.",
        "your_profile": "നിങ്ങളുടെ പ്രൊഫൈൽ",
        "capital": "ലഭ്യമായ മൂലധനം",
        "skills": "കഴിവുകൾ",
        "experience": "അനുഭവം",
        "interests": "ബിസിനസ് താൽപര്യങ്ങൾ",
        "recommendations": "ശുപാർശ ചെയ്യുന്ന അവസരങ്ങൾ",
        "score": "പൊരുത്ത സ്കോർ",
        "demand": "ഡിമാൻഡ്",
        "competition": "മത്സരം",
        "skill_fit": "കഴിവ് പൊരുത്തം",
        "capital_fit": "മൂലധന പൊരുത്തം",
        "experience_fit": "അനുഭവ പൊരുത്തം",
        "interest_fit": "താൽപര്യ പൊരുത്തം",
        "risk_fit": "റിസ്ക് പൊരുത്തം",
        "why": "എന്തുകൊണ്ട് ഇത് നിങ്ങൾക്ക് അനുയോജ്യം",
        "select": "ഈ ബിസിനസ് തിരഞ്ഞെടുക്കുക",
        "continue": "ബിസിനസ് വിശദാംശങ്ങളിലേക്ക് തുടരുക →",
        "no_selection": "ആദ്യം ഒരു ബിസിനസ് തിരഞ്ഞെടുക്കുക.",
        "selected": "തിരഞ്ഞെടുത്തത്",
        "strong_match": "വളരെ നല്ല പൊരുത്തം",
        "good_match": "നല്ല പൊരുത്തം",
        "review": "കൂടുതൽ പരിശോധിക്കുക",
        "local_adjustment": "പ്രാദേശിക വിപണി ക്രമീകരണം",
    },
}


# ============================================================
# BUSINESS DATA
# Prototype / demo data
# ============================================================

BUSINESSES = [
    {
        "name_en": "Bakery / Food",
        "name_ml": "ബേക്കറി / ഭക്ഷ്യ ബിസിനസ്",

        "demand": 82,
        "competition": 62,
        "risk": 65,

        "min_capital": 40000,
        "ideal_capital": 150000,
        "max_capital": 500000,

        "ideal_experience": 3,

        "skills": [
            "Cooking / Food Preparation",
            "Business Management",
            "Sales / Marketing",
        ],

        "interests": [
            "Food / Bakery",
        ],
    },

    {
        "name_en": "Tailoring",
        "name_ml": "ടെയിലറിംഗ്",

        "demand": 76,
        "competition": 68,
        "risk": 80,

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
    },

    {
        "name_en": "Dairy",
        "name_ml": "ക്ഷീര / ഡയറി ബിസിനസ്",

        "demand": 72,
        "competition": 58,
        "risk": 60,

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
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def normalize_list(value):
    """
    Convert session-state values into a clean list.
    Handles strings, lists, tuples and None.
    """

    if value is None:
        return []

    if isinstance(value, str):
        return [value]

    if isinstance(value, (list, tuple, set)):
        return list(value)

    return []


def calculate_capital_fit(capital, business):
    """
    Capital fit:
    - Below minimum = low
    - Around minimum = moderate
    - Near ideal = high
    - Above ideal = high
    """

    minimum = business["min_capital"]
    ideal = business["ideal_capital"]
    maximum = business["max_capital"]

    if capital <= 0:
        return 0

    if capital < minimum:
        # Some partial credit, but clearly low
        ratio = capital / minimum
        return max(0, min(45, ratio * 45))

    if capital <= ideal:
        # From 60 to 100
        ratio = (
            capital - minimum
        ) / max(1, ideal - minimum)

        return round(
            60 + (ratio * 40)
        )

    if capital <= maximum:
        return 100

    # Too much capital is not a major problem,
    # but do not give extra advantage.
    return 100


def calculate_skill_fit(user_skills, business):
    """
    Strong skill matching.

    Exact matching skill = 100
    Multiple matching skills can reinforce the score.
    """

    user_skills = set(normalize_list(user_skills))
    business_skills = set(business["skills"])

    if not user_skills:
        return 50

    matches = user_skills.intersection(
        business_skills
    )

    if len(matches) == 0:
        return 25

    if len(matches) == 1:
        return 75

    if len(matches) >= 2:
        return 100

    return 50


def calculate_interest_fit(user_interests, business):
    """
    Strong interest matching.

    Exact interest match = 100
    Related interest match = 85
    No match = 25
    """

    user_interests = set(
        normalize_list(user_interests)
    )

    business_interests = set(
        business["interests"]
    )

    if not user_interests:
        return 50

    matches = user_interests.intersection(
        business_interests
    )

    if len(matches) >= 1:
        return 100

    # Related farming/agriculture signal
    # can support Dairy even when the exact
    # Dairy / Livestock interest is not selected.
    if (
        "Farming / Agriculture" in user_interests
        and business["name_en"] == "Dairy"
    ):
        return 85

    return 25


def calculate_experience_fit(experience, business):
    """
    Experience is useful but should not dominate
    the recommendation.
    """

    try:
        experience = float(experience)
    except:
        experience = 0

    ideal = business["ideal_experience"]

    if experience <= 0:
        return 50

    if experience >= ideal:
        return 100

    if experience >= ideal * 0.5:
        return 75

    return 50


def calculate_risk_fit(business):
    """
    Lower business risk = better score.
    """

    risk = business["risk"]

    return max(
        0,
        min(
            100,
            100 - risk
        )
    )


def calculate_local_adjustment(
    business,
    local_body
):
    """
    Small local-market adjustment.

    This is deliberately small so that local adjustment
    cannot overpower the user's actual profile.
    """

    if not local_body:
        return 0

    # Prototype adjustment only.
    # Keep this small until real local data is connected.
    return 0


# ============================================================
# MAIN SCORING ENGINE
# ============================================================

def calculate_business_score(
    business,
    capital,
    skills,
    experience,
    interests,
    local_body,
):
    """
    Main opportunity scoring engine.

    IMPORTANT:
    Skill + Interest = 50% combined.

    This means the system does not simply recommend
    the business with the highest generic demand.
    """

    demand_score = business["demand"]

    # Competition is treated as suitability:
    # lower competition = better opportunity.
    competition_score = (
        100 - business["competition"]
    )

    skill_score = calculate_skill_fit(
        skills,
        business
    )

    capital_score = calculate_capital_fit(
        capital,
        business
    )

    experience_score = calculate_experience_fit(
        experience,
        business
    )

    interest_score = calculate_interest_fit(
        interests,
        business
    )

    risk_score = calculate_risk_fit(
        business
    )

    local_adjustment = calculate_local_adjustment(
        business,
        local_body
    )

    # --------------------------------------------------------
    # NEW WEIGHTS
    # --------------------------------------------------------
    #
    # Skill       = 30%
    # Interest    = 20%
    # Capital     = 15%
    # Demand      = 15%
    # Competition = 10%
    # Experience  = 5%
    # Risk        = 5%
    #
    # Total       = 100%
    # --------------------------------------------------------

    base_score = (
        (skill_score * 0.30)
        + (interest_score * 0.20)
        + (capital_score * 0.15)
        + (demand_score * 0.15)
        + (competition_score * 0.10)
        + (experience_score * 0.05)
        + (risk_score * 0.05)
    )

    final_score = (
        base_score
        + local_adjustment
    )

    final_score = max(
        0,
        min(
            100,
            round(final_score)
        )
    )

    return {
        "score": final_score,
        "demand_score": round(demand_score),
        "competition_score": round(competition_score),
        "skill_score": round(skill_score),
        "capital_score": round(capital_score),
        "experience_score": round(experience_score),
        "interest_score": round(interest_score),
        "risk_score": round(risk_score),
        "local_adjustment": local_adjustment,
    }


# ============================================================
# MATCH LABEL
# ============================================================

def get_match_label(score, language):

    if score >= 75:

        return (
            "Strong Match"
            if language == "en"
            else "വളരെ നല്ല പൊരുത്തം"
        )

    if score >= 55:

        return (
            "Good Match"
            if language == "en"
            else "നല്ല പൊരുത്തം"
        )

    return (
        "Needs Review"
        if language == "en"
        else "കൂടുതൽ പരിശോധിക്കുക"
    )


# ============================================================
# WHY THIS BUSINESS
# ============================================================

def get_reasons(
    result,
    business,
    language,
):

    reasons = []

    if result["skill_score"] >= 75:

        reasons.append(
            "Your skills strongly match this business."
            if language == "en"
            else
            "നിങ്ങളുടെ കഴിവുകൾ ഈ ബിസിനസുമായി ശക്തമായി പൊരുത്തപ്പെടുന്നു."
        )

    if result["interest_score"] >= 75:

        reasons.append(
            "Your interests match this opportunity."
            if language == "en"
            else
            "നിങ്ങളുടെ താൽപര്യങ്ങൾ ഈ അവസരവുമായി പൊരുത്തപ്പെടുന്നു."
        )

    if result["capital_score"] >= 75:

        reasons.append(
            "Your available capital is suitable."
            if language == "en"
            else
            "നിങ്ങളുടെ ലഭ്യമായ മൂലധനം അനുയോജ്യമാണ്."
        )

    if result["demand_score"] >= 75:

        reasons.append(
            "The business has relatively strong demand potential."
            if language == "en"
            else
            "ഈ ബിസിനസിന് താരതമ്യേന നല്ല ഡിമാൻഡ് സാധ്യതയുണ്ട്."
        )

    if result["competition_score"] >= 45:

        reasons.append(
            "Competition is not excessively high in the prototype model."
            if language == "en"
            else
            "പ്രോട്ടോടൈപ്പ് മോഡലിൽ മത്സരം വളരെ കൂടുതലല്ല."
        )

    if not reasons:

        reasons.append(
            "This opportunity requires further validation."
            if language == "en"
            else
            "ഈ അവസരത്തിന് കൂടുതൽ പരിശോധന ആവശ്യമാണ്."
        )

    return reasons[:3]


# ============================================================
# MAIN FRAME
# ============================================================

def render_frame3():

    # --------------------------------------------------------
    # LANGUAGE
    # --------------------------------------------------------

    language = st.session_state.get(
        "language",
        "en"
    )

    if language not in TEXT:
        language = "en"

    t = TEXT[language]

    # --------------------------------------------------------
    # GET USER PROFILE
    # --------------------------------------------------------

    capital = st.session_state.get(
        "capital",
        0
    )

    skills = normalize_list(
        st.session_state.get(
            "skills",
            []
        )
    )

    experience = st.session_state.get(
        "experience",
        0
    )

    interests = normalize_list(
        st.session_state.get(
            "interests",
            []
        )
    )

    local_body = st.session_state.get(
        "local_body",
        ""
    )

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        f"## {t['title']}"
    )

    st.caption(
        t["subtitle"]
    )

    st.write("")

    # --------------------------------------------------------
    # PROFILE SUMMARY
    # --------------------------------------------------------

    st.markdown(
        f"### {t['your_profile']}"
    )

    profile_col1, profile_col2, profile_col3 = st.columns(3)

    with profile_col1:

        st.metric(
            t["capital"],
            f"₹{capital:,.0f}"
        )

    with profile_col2:

        st.write(
            f"**{t['skills']}**"
        )

        if skills:
            st.write(
                ", ".join(skills)
            )
        else:
            st.write("-")

    with profile_col3:

        st.write(
            f"**{t['experience']}**"
        )

        st.write(
            f"{experience}"
        )

    st.write("")

    st.write(
        f"**{t['interests']}:** "
        + (
            ", ".join(interests)
            if interests
            else "-"
        )
    )

    st.write("")

    # --------------------------------------------------------
    # CALCULATE ALL RECOMMENDATIONS
    # --------------------------------------------------------

    ranked_businesses = []

    for business in BUSINESSES:

        result = calculate_business_score(
            business=business,
            capital=capital,
            skills=skills,
            experience=experience,
            interests=interests,
            local_body=local_body,
        )

        ranked_businesses.append(
            {
                "business": business,
                "result": result,
            }
        )

    # Highest score first
    ranked_businesses.sort(
        key=lambda x: x["result"]["score"],
        reverse=True
    )

    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    st.markdown(
        f"### {t['recommendations']}"
    )

    # --------------------------------------------------------
    # BUSINESS CARDS
    # --------------------------------------------------------

    for index, item in enumerate(
        ranked_businesses
    ):

        business = item["business"]
        result = item["result"]

        business_name = (
            business["name_ml"]
            if language == "ml"
            else business["name_en"]
        )

        score = result["score"]

        match_label = get_match_label(
            score,
            language
        )

        # ----------------------------------------------------
        # Card container
        # ----------------------------------------------------

        with st.container(border=True):

            title_col, score_col = st.columns(
                [3, 1]
            )

            with title_col:

                if index == 0:

                    st.markdown(
                        f"### 🥇 {business_name}"
                    )

                else:

                    st.markdown(
                        f"### {index + 1}. {business_name}"
                    )

                st.caption(
                    match_label
                )

            with score_col:

                st.metric(
                    t["score"],
                    f"{score}/100"
                )

            st.progress(
                score / 100
            )

            st.write("")

            # ------------------------------------------------
            # Score components
            # ------------------------------------------------

            metric_col1, metric_col2, metric_col3 = st.columns(3)

            with metric_col1:

                st.write(
                    f"**{t['skill_fit']}**"
                )

                st.progress(
                    result["skill_score"] / 100
                )

                st.caption(
                    f"{result['skill_score']}/100"
                )

            with metric_col2:

                st.write(
                    f"**{t['interest_fit']}**"
                )

                st.progress(
                    result["interest_score"] / 100
                )

                st.caption(
                    f"{result['interest_score']}/100"
                )

            with metric_col3:

                st.write(
                    f"**{t['capital_fit']}**"
                )

                st.progress(
                    result["capital_score"] / 100
                )

                st.caption(
                    f"{result['capital_score']}/100"
                )

            metric_col4, metric_col5, metric_col6 = st.columns(3)

            with metric_col4:

                st.write(
                    f"**{t['demand']}**"
                )

                st.progress(
                    result["demand_score"] / 100
                )

                st.caption(
                    f"{result['demand_score']}/100"
                )

            with metric_col5:

                st.write(
                    f"**{t['competition']}**"
                )

                st.progress(
                    result["competition_score"] / 100
                )

                st.caption(
                    f"{result['competition_score']}/100"
                )

            with metric_col6:

                st.write(
                    f"**{t['experience_fit']}**"
                )

                st.progress(
                    result["experience_score"] / 100
                )

                st.caption(
                    f"{result['experience_score']}/100"
                )

            st.write("")

            # ------------------------------------------------
            # Why
            # ------------------------------------------------

            st.markdown(
                f"**{t['why']}**"
            )

            reasons = get_reasons(
                result,
                business,
                language
            )

            for reason in reasons:

                st.write(
                    f"✓ {reason}"
                )

            # ------------------------------------------------
            # Select button
            # ------------------------------------------------

            button_label = (
                f"{t['select']}: "
                f"{business_name}"
            )

            if st.button(
                button_label,
                key=f"select_business_{index}",
                use_container_width=True,
            ):

                st.session_state.selected_business = (
                    business["name_en"]
                )

                st.session_state.selected_business_ml = (
                    business["name_ml"]
                )

                st.session_state.selected_business_score = (
                    score
                )

                st.session_state.selected_business_rank = (
                    index + 1
                )

                st.session_state.selected_business_scores = (
                    result
                )

                st.rerun()

            # ------------------------------------------------
            # Show currently selected
            # ------------------------------------------------

            if (
                st.session_state.get(
                    "selected_business",
                    None
                )
                == business["name_en"]
            ):

                st.success(
                    f"✓ {t['selected']}: "
                    f"{business_name}"
                )

    st.write("")

    # --------------------------------------------------------
    # SELECTED BUSINESS
    # --------------------------------------------------------

    selected_business = st.session_state.get(
        "selected_business",
        None
    )

    if selected_business:

        selected_item = None

        for item in ranked_businesses:

            if (
                item["business"]["name_en"]
                == selected_business
            ):

                selected_item = item
                break

        if selected_item:

            selected_score = (
                selected_item["result"]["score"]
            )

            selected_name = (
                selected_item["business"]["name_ml"]
                if language == "ml"
                else selected_item["business"]["name_en"]
            )

            st.success(
                f"✓ {t['selected']}: "
                f"**{selected_name}** — "
                f"{selected_score}/100"
            )

    # --------------------------------------------------------
    # CONTINUE TO BUSINESS DETAIL
    # --------------------------------------------------------

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

                st.session_state.page = 4
                st.rerun()
