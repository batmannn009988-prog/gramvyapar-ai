import streamlit as st


def render_frame3():
    st.markdown("## Opportunity Radar")

    st.caption(
        "Explore business opportunities that fit your skills, "
        "capital and local market."
    )

    st.write("")

    # --------------------------------------------------------
    # USER PROFILE SUMMARY
    # --------------------------------------------------------

    st.markdown("### Your Profile")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Available Capital",
            f"₹{st.session_state.capital:,.0f}"
        )

    with col2:
        st.metric(
            "Experience",
            f"{st.session_state.experience} years"
        )

    with col3:
        skills_count = len(
            st.session_state.skills
        )

        st.metric(
            "Skills",
            skills_count
        )

    with col4:
        interests_count = len(
            st.session_state.interests
        )

        st.metric(
            "Business Interests",
            interests_count
        )

    st.write("")

    # --------------------------------------------------------
    # LOCATION
    # --------------------------------------------------------

    st.markdown("### Local Market")

    location_col1, location_col2, location_col3 = st.columns(3)

    with location_col1:
        st.write("**District**")
        st.write(
            st.session_state.district
        )

    with location_col2:
        st.write("**Local Body**")
        st.write(
            st.session_state.local_body
        )

    with location_col3:
        st.write("**Ward**")
        st.write(
            st.session_state.ward
        )

    st.write("")

    # --------------------------------------------------------
    # OPPORTUNITY DATA
    # --------------------------------------------------------

    opportunities = [
        {
            "name": "Bakery / Food",
            "demand": 82,
            "competition": 62,
            "skill": 78,
            "capital": 85,
            "risk": 72,
        },
        {
            "name": "Tailoring",
            "demand": 76,
            "competition": 68,
            "skill": 90,
            "capital": 92,
            "risk": 82,
        },
        {
            "name": "Dairy",
            "demand": 72,
            "competition": 58,
            "skill": 70,
            "capital": 60,
            "risk": 65,
        },
    ]

    # --------------------------------------------------------
    # OPPORTUNITY CARDS
    # --------------------------------------------------------

    st.markdown("### Recommended Opportunities")

    for index, opportunity in enumerate(
        opportunities
    ):

        st.markdown(
            f"### #{index + 1}  {opportunity['name']}"
        )

        st.caption(
            "Prototype opportunity score based on "
            "demand, competition, skill, capital and risk fit."
        )

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.write("**Demand**")
            st.progress(
                opportunity["demand"] / 100
            )
            st.write(
                f"{opportunity['demand']}%"
            )

        with col2:
            st.write("**Competition Fit**")
            st.progress(
                opportunity["competition"] / 100
            )
            st.write(
                f"{opportunity['competition']}%"
            )

        with col3:
            st.write("**Skill Fit**")
            st.progress(
                opportunity["skill"] / 100
            )
            st.write(
                f"{opportunity['skill']}%"
            )

        with col4:
            st.write("**Capital Fit**")
            st.progress(
                opportunity["capital"] / 100
            )
            st.write(
                f"{opportunity['capital']}%"
            )

        with col5:
            st.write("**Risk Fit**")
            st.progress(
                opportunity["risk"] / 100
            )
            st.write(
                f"{opportunity['risk']}%"
            )

        st.write("")

        # Why this fits
        if index == 0:
            reason = (
                "Strong local demand potential with a "
                "reasonable capital requirement."
            )

        elif index == 1:
            reason = (
                "Good skill and capital fit with relatively "
                "lower business risk."
            )

        else:
            reason = (
                "Potentially suitable where dairy demand "
                "and local resource availability are strong."
            )

        st.info(
            f"**Why this fits:** {reason}"
        )

        st.divider()

    # --------------------------------------------------------
    # DATA CONFIDENCE
    # --------------------------------------------------------

    st.markdown("### Data Confidence")

    st.warning(
        "Prototype / demo estimates are currently being used. "
        "Final recommendations should be connected to verified "
        "local datasets before real financial decisions."
    )

    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    st.write("")

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            "← Back",
            use_container_width=True,
            key="back_frame3",
        ):

            st.session_state.page = 2
            st.rerun()

    with continue_col:

        if st.button(
            "Continue →",
            type="primary",
            use_container_width=True,
            key="continue_frame3",
        ):

            st.session_state.page = 4
            st.rerun()
