import streamlit as st
from frames.frame4_business_detail import BUSINESS_DATA, calculate_financials


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {
    "en": {
        "title": "Financial Dashboard",
        "subtitle": "Understand the investment, funding gap, loan need and repayment safety.",
        "selected_business": "Selected Business",
        "own_capital": "Your Available Capital",
        "project_cost": "Estimated Project Cost",
        "funding_gap": "Funding Gap",
        "loan_need": "Indicative Loan Requirement",
        "monthly_revenue": "Estimated Monthly Revenue",
        "monthly_expenses": "Estimated Monthly Expenses",
        "monthly_surplus": "Estimated Monthly Surplus",
        "financial_summary": "Financial Summary",
        "loan_section": "Indicative Financing Plan",
        "scheme": "Indicative Financing Route",
        "interest": "Illustrative Interest Rate",
        "tenure": "Illustrative Tenure",
        "moratorium": "Illustrative Moratorium",
        "emi": "Estimated Monthly EMI",
        "after_emi": "Surplus After EMI",
        "safety": "Repayment Safety",
        "comfortable": "COMFORTABLE",
        "manageable": "MANAGEABLE",
        "unsafe": "NOT FINANCIALLY SAFE",
        "dont_borrow": "DON'T BORROW / START SMALLER",
        "review": "REVIEW FINANCING",
        "safe_message": "The projected business surplus appears sufficient to cover the indicative EMI.",
        "manageable_message": "The projected business surplus can cover the indicative EMI, but the repayment margin is limited.",
        "unsafe_message": "The projected business surplus is lower than the indicative EMI.",
        "scheme_note": "Illustrative routing based on the SIH problem-statement example. Verify current official scheme rules and eligibility before applying.",
        "approval_note": "This is a financial planning prototype. Loan approval is not guaranteed.",
        "moratorium_note": "Moratorium treatment can vary by lender and scheme. EMI shown is a standard illustrative EMI after the moratorium period.",
        "calculation": "Loan Calculation",
        "formula": "Indicative loan need = Project cost − Your available capital",
        "back": "← Back to Business Detail",
        "continue": "Continue to Risk Dashboard →",
        "no_business": "Please select a business from Opportunity Radar first.",
    },

    "ml": {
        "title": "സാമ്പത്തിക ഡാഷ്ബോർഡ്",
        "subtitle": "നിക്ഷേപം, ഫണ്ടിംഗ് ആവശ്യം, വായ്പ, തിരിച്ചടവ് സുരക്ഷ എന്നിവ മനസ്സിലാക്കുക.",
        "selected_business": "തിരഞ്ഞെടുത്ത ബിസിനസ്",
        "own_capital": "നിങ്ങളുടെ ലഭ്യമായ മൂലധനം",
        "project_cost": "അനുമാനിച്ച പ്രോജക്റ്റ് ചെലവ്",
        "funding_gap": "ഫണ്ടിംഗ് ആവശ്യം",
        "loan_need": "സൂചനാപരമായ വായ്പ ആവശ്യം",
        "monthly_revenue": "അനുമാനിച്ച മാസ വരുമാനം",
        "monthly_expenses": "അനുമാനിച്ച മാസ ചെലവ്",
        "monthly_surplus": "അനുമാനിച്ച മാസ മിച്ചം",
        "financial_summary": "സാമ്പത്തിക സംഗ്രഹം",
        "loan_section": "സൂചനാപരമായ ഫിനാൻസിംഗ് പ്ലാൻ",
        "scheme": "സൂചനാപരമായ ഫിനാൻസിംഗ് മാർഗം",
        "interest": "ഉദാഹരണ പലിശ നിരക്ക്",
        "tenure": "ഉദാഹരണ കാലാവധി",
        "moratorium": "ഉദാഹരണ മൊറട്ടോറിയം",
        "emi": "അനുമാനിച്ച മാസ EMI",
        "after_emi": "EMI കഴിഞ്ഞുള്ള മിച്ചം",
        "safety": "തിരിച്ചടവ് സുരക്ഷ",
        "comfortable": "സുരക്ഷിതം",
        "manageable": "നിയന്ത്രിക്കാവുന്നത്",
        "unsafe": "സാമ്പത്തികമായി സുരക്ഷിതമല്ല",
        "dont_borrow": "വായ്പ എടുക്കരുത് / ചെറിയ രീതിയിൽ തുടങ്ങുക",
        "review": "ഫിനാൻസിംഗ് പരിശോധിക്കുക",
        "safe_message": "അനുമാനിച്ച ബിസിനസ് മിച്ചം സൂചനാപരമായ EMI അടയ്ക്കാൻ മതിയായതായി തോന്നുന്നു.",
        "manageable_message": "EMI അടയ്ക്കാൻ മിച്ചം മതിയാകാം, പക്ഷേ സുരക്ഷാ മാർജിൻ കുറവാണ്.",
        "unsafe_message": "അനുമാനിച്ച ബിസിനസ് മിച്ചം സൂചനാപരമായ EMI-നേക്കാൾ കുറവാണ്.",
        "scheme_note": "SIH പ്രശ്ന പ്രസ്താവനയിലെ ഉദാഹരണത്തെ അടിസ്ഥാനമാക്കിയുള്ള സൂചനാപരമായ റൂട്ടിംഗ് മാത്രം. നിലവിലെ ഔദ്യോഗിക നിയമങ്ങളും യോഗ്യതയും പരിശോധിക്കുക.",
        "approval_note": "ഇത് ഒരു സാമ്പത്തിക പ്ലാനിംഗ് പ്രോട്ടോടൈപ്പാണ്. വായ്പ അംഗീകാരം ഉറപ്പില്ല.",
        "moratorium_note": "മൊറട്ടോറിയം വ്യവസ്ഥകൾ ബാങ്കിനും പദ്ധതിക്കും അനുസരിച്ച് മാറാം. EMI ഒരു സാധാരണ ഉദാഹരണ കണക്കാണ്.",
        "calculation": "വായ്പ കണക്കുകൂട്ടൽ",
        "formula": "സൂചനാപരമായ വായ്പ = പ്രോജക്റ്റ് ചെലവ് − നിങ്ങളുടെ മൂലധനം",
        "back": "← ബിസിനസ് വിശദാംശങ്ങളിലേക്ക്",
        "continue": "റിസ്ക് ഡാഷ്ബോർഡിലേക്ക് തുടരുക →",
        "no_business": "ആദ്യം Opportunity Radar-ൽ നിന്ന് ഒരു ബിസിനസ് തിരഞ്ഞെടുക്കുക.",
    },
}


# ============================================================
# LOAN / FINANCE ENGINE
# ============================================================

def calculate_emi(principal, annual_interest_rate, months):
    """
    Standard reducing-balance EMI calculation.
    """

    if principal <= 0:
        return 0

    if months <= 0:
        return 0

    monthly_rate = annual_interest_rate / 12 / 100

    if monthly_rate == 0:
        return principal / months

    emi = (
        principal
        * monthly_rate
        * ((1 + monthly_rate) ** months)
        / (((1 + monthly_rate) ** months) - 1)
    )

    return round(emi)


def get_financing_route(loan_amount):
    """
    Illustrative SIH-style financing route.

    These are prototype assumptions based on the
    example rules in the problem statement.
    """

    if loan_amount <= 0:

        return {
            "scheme": "No Loan Required",
            "interest_rate": 0,
            "tenure_years": 0,
            "moratorium_months": 0,
            "scheme_type": "self_funded",
        }

    if loan_amount <= 140000:

        return {
            "scheme": "Micro Finance",
            "interest_rate": 6.5,
            "tenure_years": 3,
            "moratorium_months": 3,
            "scheme_type": "micro",
        }

    return {
        "scheme": "Term Loan",
        "interest_rate": 8.0,
        "tenure_years": 7,
        "moratorium_months": 6,
        "scheme_type": "term",
    }


def calculate_repayment_safety(monthly_surplus, emi):
    """
    Repayment safety based on monthly surplus / EMI.

    >= 1.5x EMI = Comfortable
    >= 1.0x EMI = Manageable
    < 1.0x EMI = Unsafe
    """

    if emi <= 0:
        return {
            "status": "self_funded",
            "ratio": 999,
        }

    ratio = monthly_surplus / emi

    if ratio >= 1.5:

        return {
            "status": "comfortable",
            "ratio": ratio,
        }

    if ratio >= 1.0:

        return {
            "status": "manageable",
            "ratio": ratio,
        }

    return {
        "status": "unsafe",
        "ratio": ratio,
    }


# ============================================================
# MAIN FRAME
# ============================================================

def render_frame5():

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
    # SELECTED BUSINESS
    # --------------------------------------------------------

    selected_business = st.session_state.get(
        "selected_business",
        None
    )

    if not selected_business:

        st.error(
            t["no_business"]
        )

        return

    # --------------------------------------------------------
    # FIND BUSINESS
    # --------------------------------------------------------

    business = BUSINESS_DATA.get(
        selected_business
    )

    if business is None:

        st.error(
            t["no_business"]
        )

        return

    # --------------------------------------------------------
    # USER CAPITAL
    # --------------------------------------------------------

    own_capital = st.session_state.get(
        "capital",
        0
    )

    try:
        own_capital = float(own_capital)
    except:
        own_capital = 0

    # --------------------------------------------------------
    # BUSINESS FINANCIALS
    # --------------------------------------------------------

    financials = calculate_financials(
        business
    )

    project_cost = financials["startup_total"]

    monthly_revenue = financials["monthly_revenue"]

    monthly_expenses = financials["monthly_expenses"]

    monthly_surplus = financials["monthly_surplus"]

    # --------------------------------------------------------
    # FUNDING GAP
    # --------------------------------------------------------

    funding_gap = max(
        0,
        project_cost - own_capital
    )

    loan_need = funding_gap

    # --------------------------------------------------------
    # FINANCING ROUTE
    # --------------------------------------------------------

    financing = get_financing_route(
        loan_need
    )

    interest_rate = financing[
        "interest_rate"
    ]

    tenure_years = financing[
        "tenure_years"
    ]

    moratorium_months = financing[
        "moratorium_months"
    ]

    tenure_months = (
        tenure_years * 12
    )

    # --------------------------------------------------------
    # EMI
    # --------------------------------------------------------

    emi = calculate_emi(
        principal=loan_need,
        annual_interest_rate=interest_rate,
        months=tenure_months,
    )

    # --------------------------------------------------------
    # REPAYMENT SAFETY
    # --------------------------------------------------------

    safety = calculate_repayment_safety(
        monthly_surplus,
        emi
    )

    safety_status = safety["status"]

    safety_ratio = safety["ratio"]

    surplus_after_emi = (
        monthly_surplus - emi
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
    # SELECTED BUSINESS
    # --------------------------------------------------------

    business_name = (
        business["name_ml"]
        if language == "ml"
        else business["name_en"]
    )

    st.info(
        f"**{t['selected_business']}:** "
        f"{business_name}"
    )

    st.write("")

    # ========================================================
    # FINANCIAL SUMMARY
    # ========================================================

    st.markdown(
        f"### {t['financial_summary']}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            t["own_capital"],
            f"₹{own_capital:,.0f}"
        )

    with col2:

        st.metric(
            t["project_cost"],
            f"₹{project_cost:,.0f}"
        )

    with col3:

        st.metric(
            t["funding_gap"],
            f"₹{funding_gap:,.0f}"
        )

    col4, col5, col6 = st.columns(3)

    with col4:

        st.metric(
            t["monthly_revenue"],
            f"₹{monthly_revenue:,.0f}"
        )

    with col5:

        st.metric(
            t["monthly_expenses"],
            f"₹{monthly_expenses:,.0f}"
        )

    with col6:

        st.metric(
            t["monthly_surplus"],
            f"₹{monthly_surplus:,.0f}"
        )

    st.write("")

    # ========================================================
    # FUNDING GAP
    # ========================================================

    st.markdown(
        f"### {t['calculation']}"
    )

    st.write(
        t["formula"]
    )

    st.write(
        f"₹{project_cost:,.0f} − "
        f"₹{own_capital:,.0f} = "
        f"**₹{funding_gap:,.0f}**"
    )

    if funding_gap == 0:

        st.success(
            "✓ No loan is required for the prototype project size."
            if language == "en"
            else
            "✓ പ്രോട്ടോടൈപ്പ് പ്രോജക്റ്റ് വലുപ്പത്തിന് വായ്പ ആവശ്യമില്ല."
        )

    else:

        st.warning(
            f"{t['loan_need']}: "
            f"₹{loan_need:,.0f}"
        )

    st.write("")

    # ========================================================
    # LOAN PLAN
    # ========================================================

    st.markdown(
        f"### {t['loan_section']}"
    )

    if loan_need <= 0:

        st.success(
            "Self-funded business plan"
            if language == "en"
            else
            "സ്വന്തം മൂലധനം ഉപയോഗിച്ചുള്ള ബിസിനസ് പ്ലാൻ"
        )

    else:

        loan_col1, loan_col2 = st.columns(2)

        with loan_col1:

            st.metric(
                t["loan_need"],
                f"₹{loan_need:,.0f}"
            )

            st.metric(
                t["scheme"],
                financing["scheme"]
            )

            st.metric(
                t["interest"],
                f"{interest_rate:.1f}%"
            )

        with loan_col2:

            st.metric(
                t["tenure"],
                f"{tenure_years} years"
            )

            st.metric(
                t["moratorium"],
                f"{moratorium_months} months"
            )

            st.metric(
                t["emi"],
                f"₹{emi:,.0f}"
            )

        st.write("")

        st.caption(
            t["moratorium_note"]
        )

    st.write("")

    # ========================================================
    # REPAYMENT SAFETY
    # ========================================================

    st.markdown(
        f"### {t['safety']}"
    )

    if loan_need <= 0:

        st.success(
            "🟢 SELF-FUNDED — No EMI burden"
            if language == "en"
            else
            "🟢 സ്വന്തം മൂലധനം — EMI ബാധ്യതയില്ല"
        )

    elif safety_status == "comfortable":

        st.success(
            f"🟢 {t['comfortable']}"
        )

        st.write(
            t["safe_message"]
        )

    elif safety_status == "manageable":

        st.warning(
            f"🟠 {t['manageable']}"
        )

        st.write(
            t["manageable_message"]
        )

    else:

        st.error(
            f"🔴 {t['unsafe']}"
        )

        st.write(
            t["unsafe_message"]
        )

        st.error(
            f"**{t['dont_borrow']}**"
        )

    # --------------------------------------------------------
    # SURPLUS AFTER EMI
    # --------------------------------------------------------

    if loan_need > 0:

        safety_col1, safety_col2, safety_col3 = st.columns(3)

        with safety_col1:

            st.metric(
                t["monthly_surplus"],
                f"₹{monthly_surplus:,.0f}"
            )

        with safety_col2:

            st.metric(
                t["emi"],
                f"₹{emi:,.0f}"
            )

        with safety_col3:

            st.metric(
                t["after_emi"],
                f"₹{surplus_after_emi:,.0f}"
            )

        st.progress(
            min(
                1.0,
                max(
                    0.0,
                    monthly_surplus / max(
                        emi,
                        1
                    )
                )
            )
        )

        st.caption(
            f"Surplus / EMI coverage: "
            f"{safety_ratio:.2f}×"
        )

    st.write("")

    # ========================================================
    # IMPORTANT DISCLAIMER
    # ========================================================

    with st.expander(
        "Important financing note"
        if language == "en"
        else
        "പ്രധാന ഫിനാൻസിംഗ് കുറിപ്പ്"
    ):

        st.write(
            t["scheme_note"]
        )

        st.write(
            t["approval_note"]
        )

    st.write("")

    # ========================================================
    # NAVIGATION
    # ========================================================

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            t["back"],
            use_container_width=True,
            key="back_frame5",
        ):

            st.session_state.page = 4
            st.rerun()

    with continue_col:

        if st.button(
            t["continue"],
            type="primary",
            use_container_width=True,
            key="continue_frame5",
        ):

            st.session_state.page = 6
            st.rerun()
