import streamlit as st
import math

# ============================================================
# TRANSLATIONS
# ============================================================

T = {
    "en": {
        "title": "💰 Financial Dashboard",
        "subtitle": "Understand your investment, funding gap, loan requirement and repayment capacity.",
        "selected_business": "Selected Business",
        "available_capital": "Available Capital",
        "project_cost": "Estimated Project Cost",
        "funding_gap": "Funding Gap",
        "loan_amount": "Estimated Loan Amount",
        "monthly_revenue": "Estimated Monthly Revenue",
        "monthly_expenses": "Estimated Monthly Expenses",
        "monthly_surplus": "Estimated Monthly Surplus",

        "loan_calculation": "🏦 Loan Calculation",
        "required_capital": "Required Capital",
        "own_capital": "Your Own Capital",
        "loan_needed": "Loan Needed",

        "loan_amount_title": "💳 Loan Amount",
        "loan_amount_help": "Adjust the loan amount if you want to borrow less than the calculated funding gap.",
        "no_loan_required": "No loan is required for this business plan.",
        "loan_required": "Estimated loan required:",

        "financing_plan": "📋 Indicative Financing Plan",
        "finance_type": "Financing Type",
        "interest_rate": "Interest Rate",
        "tenure": "Tenure",
        "moratorium": "Moratorium",
        "emi": "Estimated Monthly EMI",

        "self_funded": "Self-funded business plan",
        "micro_finance": "Micro Finance",
        "term_loan": "Term Loan",

        "repayment_safety": "🛡️ Repayment Safety",
        "surplus": "Monthly Business Surplus",
        "emi_burden": "Monthly EMI",
        "coverage": "Surplus / EMI Coverage",
        "comfortable": "COMFORTABLE",
        "manageable": "MANAGEABLE",
        "unsafe": "UNSAFE",
        "self_funded_safe": "SELF-FUNDED — No EMI burden",

        "comfortable_msg": "The projected surplus provides a reasonable buffer above the EMI.",
        "manageable_msg": "The business may be able to repay, but the repayment buffer is limited.",
        "unsafe_msg": "The projected surplus is lower than the EMI. Borrowing at this level is not financially safe.",

        "dont_borrow": "🚫 DON'T BORROW / START SMALLER",
        "review": "⚠️ REVIEW BEFORE BORROWING",
        "go": "✅ GO — FINANCIALLY FEASIBLE",

        "continue": "Continue to Risk Analysis →",
        "back": "← Back to Business Detail",

        "disclaimer_title": "⚠️ Prototype Disclaimer",
        "disclaimer": (
            "The financing route shown here is illustrative for the SIH prototype. "
            "Actual government scheme rules, interest rates, eligibility, moratorium "
            "conditions and loan approval must be verified with the relevant official source."
        ),

        "adjust_loan": "Choose Loan Amount",
        "loan_amount_selected": "Selected Loan Amount",

        "interest": "Interest",
        "years": "years",
        "months": "months",
    },

    "ml": {
        "title": "💰 സാമ്പത്തിക ഡാഷ്ബോർഡ്",
        "subtitle": "നിക്ഷേപം, ഫണ്ടിംഗ് കുറവ്, ലോൺ ആവശ്യം, തിരിച്ചടവ് ശേഷി എന്നിവ മനസ്സിലാക്കുക.",
        "selected_business": "തിരഞ്ഞെടുത്ത ബിസിനസ്",
        "available_capital": "ലഭ്യമായ മൂലധനം",
        "project_cost": "അനുമാനിച്ച പദ്ധതി ചെലവ്",
        "funding_gap": "ഫണ്ടിംഗ് കുറവ്",
        "loan_amount": "അനുമാനിച്ച ലോൺ തുക",
        "monthly_revenue": "അനുമാനിച്ച മാസ വരുമാനം",
        "monthly_expenses": "അനുമാനിച്ച മാസ ചെലവ്",
        "monthly_surplus": "അനുമാനിച്ച മാസ മിച്ചം",

        "loan_calculation": "🏦 ലോൺ കണക്കുകൂട്ടൽ",
        "required_capital": "ആവശ്യമായ മൂലധനം",
        "own_capital": "നിങ്ങളുടെ സ്വന്തം മൂലധനം",
        "loan_needed": "ആവശ്യമായ ലോൺ",

        "loan_amount_title": "💳 ലോൺ തുക",
        "loan_amount_help": "കണക്കാക്കിയ ഫണ്ടിംഗ് കുറവിനേക്കാൾ കുറച്ച് തുക വായ്പയെടുക്കണമെങ്കിൽ മാറ്റാം.",
        "no_loan_required": "ഈ ബിസിനസ് പദ്ധതിക്ക് ലോൺ ആവശ്യമില്ല.",
        "loan_required": "അനുമാനിച്ച ആവശ്യമായ ലോൺ:",

        "financing_plan": "📋 സൂചനാത്മക ധനസഹായ പദ്ധതി",
        "finance_type": "ധനസഹായ തരം",
        "interest_rate": "പലിശ നിരക്ക്",
        "tenure": "കാലാവധി",
        "moratorium": "മൊറട്ടോറിയം",
        "emi": "അനുമാനിച്ച മാസ EMI",

        "self_funded": "സ്വന്തം മൂലധനം ഉപയോഗിച്ചുള്ള പദ്ധതി",
        "micro_finance": "മൈക്രോ ഫിനാൻസ്",
        "term_loan": "ടേം ലോൺ",

        "repayment_safety": "🛡️ തിരിച്ചടവ് സുരക്ഷ",
        "surplus": "മാസ ബിസിനസ് മിച്ചം",
        "emi_burden": "മാസ EMI",
        "coverage": "മിച്ചം / EMI അനുപാതം",
        "comfortable": "സുരക്ഷിതം",
        "manageable": "നിയന്ത്രിക്കാവുന്നത്",
        "unsafe": "സുരക്ഷിതമല്ല",
        "self_funded_safe": "സ്വന്തം മൂലധനം — EMI ബാധ്യതയില്ല",

        "comfortable_msg": "അനുമാനിച്ച മിച്ചം EMI-യേക്കാൾ നല്ല സുരക്ഷാ ബഫർ നൽകുന്നു.",
        "manageable_msg": "ബിസിനസിന് തിരിച്ചടയ്ക്കാൻ കഴിയാം, പക്ഷേ സുരക്ഷാ ബഫർ കുറവാണ്.",
        "unsafe_msg": "അനുമാനിച്ച മിച്ചം EMI-യേക്കാൾ കുറവാണ്. ഈ തോതിൽ വായ്പയെടുക്കുന്നത് സാമ്പത്തികമായി സുരക്ഷിതമല്ല.",

        "dont_borrow": "🚫 ലോൺ എടുക്കരുത് / ചെറിയ രീതിയിൽ തുടങ്ങുക",
        "review": "⚠️ ലോൺ എടുക്കുന്നതിന് മുമ്പ് പരിശോധിക്കുക",
        "go": "✅ GO — സാമ്പത്തികമായി സാധ്യമാണ്",

        "continue": "റിസ്ക് വിശകലനത്തിലേക്ക് →",
        "back": "← ബിസിനസ് വിശദാംശങ്ങളിലേക്ക്",

        "disclaimer_title": "⚠️ പ്രോട്ടോടൈപ്പ് അറിയിപ്പ്",
        "disclaimer": (
            "SIH പ്രോട്ടോടൈപ്പിനായി മാത്രമുള്ള സൂചനാത്മക ധനസഹായ കണക്കാണിത്. "
            "യഥാർത്ഥ സർക്കാർ പദ്ധതികളുടെ നിയമങ്ങൾ, പലിശ നിരക്ക്, യോഗ്യത, "
            "മൊറട്ടോറിയം, ലോൺ അംഗീകാരം എന്നിവ ഔദ്യോഗിക ഉറവിടത്തിൽ പരിശോധിക്കണം."
        ),

        "adjust_loan": "ലോൺ തുക തിരഞ്ഞെടുക്കുക",
        "loan_amount_selected": "തിരഞ്ഞെടുത്ത ലോൺ തുക",

        "interest": "പലിശ",
        "years": "വർഷം",
        "months": "മാസം",
    }
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def calculate_emi(principal, annual_rate, tenure_years):
    """
    Standard reducing-balance EMI calculation.
    """

    if principal <= 0:
        return 0

    months = int(tenure_years * 12)

    if months <= 0:
        return 0

    monthly_rate = annual_rate / 12 / 100

    if monthly_rate == 0:
        return principal / months

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

    return emi


def get_financing_route(loan_amount):
    """
    Illustrative financing route based on the SIH problem statement example.
    """

    if loan_amount <= 0:
        return {
            "type": "self_funded",
            "interest_rate": 0,
            "tenure_years": 0,
            "moratorium_months": 0,
        }

    if loan_amount <= 140000:
        return {
            "type": "micro_finance",
            "interest_rate": 6.5,
            "tenure_years": 3,
            "moratorium_months": 3,
        }

    return {
        "type": "term_loan",
        "interest_rate": 8.0,
        "tenure_years": 7,
        "moratorium_months": 6,
    }


def calculate_repayment_safety(monthly_surplus, emi):
    """
    Determine repayment safety using monthly surplus / EMI coverage.
    """

    if emi <= 0:
        return {
            "status": "self_funded",
            "coverage": None,
            "message": "self_funded"
        }

    coverage = monthly_surplus / emi

    if coverage >= 1.5:
        return {
            "status": "comfortable",
            "coverage": coverage,
            "message": "comfortable"
        }

    if coverage >= 1.0:
        return {
            "status": "manageable",
            "coverage": coverage,
            "message": "manageable"
        }

    return {
        "status": "unsafe",
        "coverage": coverage,
        "message": "unsafe"
    }


def format_rupees(value):
    """
    Simple Indian-style currency formatting.
    """

    try:
        return f"₹{value:,.0f}"
    except Exception:
        return "₹0"


# ============================================================
# FRAME 5
# ============================================================

def render_frame5():

    language = st.session_state.get("language", "en")
    tr = T[language]

    # --------------------------------------------------------
    # SELECTED BUSINESS
    # --------------------------------------------------------

    selected_business = st.session_state.get(
        "selected_business",
        "Bakery"
    )

    # Import Frame 4 data
    try:
        from frames.frame4_business_detail import (
            BUSINESS_DATA,
            calculate_financials
        )
    except Exception:
        BUSINESS_DATA = {}
        calculate_financials = None

    # --------------------------------------------------------
    # FIND BUSINESS
    # --------------------------------------------------------

    business = None

    if isinstance(BUSINESS_DATA, dict):

        # Direct lookup
        if selected_business in BUSINESS_DATA:
            business = BUSINESS_DATA[selected_business]

        else:

            # Search through dictionary values
            for key, value in BUSINESS_DATA.items():

                if not isinstance(value, dict):
                    continue

                name_en = value.get("name_en", "")
                name_ml = value.get("name_ml", "")
                name = value.get("name", "")

                if selected_business in [
                    key,
                    name_en,
                    name_ml,
                    name
                ]:
                    business = value
                    break

    # --------------------------------------------------------
    # BUSINESS NAME
    # --------------------------------------------------------

    if business:

        if language == "ml":

            business_name = business.get(
                "name_ml",
                selected_business
            )

        else:

            business_name = business.get(
                "name_en",
                selected_business
            )

    else:

        business_name = selected_business

    if not business_name:
        business_name = selected_business

    # --------------------------------------------------------
    # FINANCIAL VALUES FROM FRAME 4
    # --------------------------------------------------------

    project_cost = 0
    monthly_revenue = 0
    monthly_expenses = 0
    monthly_surplus = 0

    if business and calculate_financials:

        try:

            financials = calculate_financials(business)

            project_cost = float(
                financials.get(
                    "startup_total",
                    financials.get("project_cost", 0)
                )
            )

            monthly_revenue = float(
                financials.get(
                    "monthly_revenue",
                    financials.get("revenue", 0)
                )
            )

            monthly_expenses = float(
                financials.get(
                    "monthly_expenses",
                    financials.get("expenses", 0)
                )
            )

            monthly_surplus = float(
                financials.get(
                    "monthly_surplus",
                    financials.get("surplus", 0)
                )
            )

        except Exception:

            project_cost = 0
            monthly_revenue = 0
            monthly_expenses = 0
            monthly_surplus = 0

    # --------------------------------------------------------
    # OWN CAPITAL
    # --------------------------------------------------------

    own_capital = float(
        st.session_state.get(
            "capital",
            0
        )
    )

    # --------------------------------------------------------
    # FUNDING GAP
    # --------------------------------------------------------

    funding_gap = max(
        0,
        project_cost - own_capital
    )

    # --------------------------------------------------------
    # DEFAULT LOAN AMOUNT
    # --------------------------------------------------------
    # If user already selected a loan amount, preserve it.
    # Otherwise use the funding gap.

    previous_loan_amount = st.session_state.get(
        "loan_amount",
        None
    )

    if previous_loan_amount is None:

        loan_amount = funding_gap

    else:

        try:

            loan_amount = float(
                previous_loan_amount
            )

        except Exception:

            loan_amount = funding_gap

    # --------------------------------------------------------
    # LIMIT LOAN AMOUNT
    # --------------------------------------------------------
    # The loan cannot exceed the funding gap.

    loan_amount = min(
        loan_amount,
        funding_gap
    )

    loan_amount = max(
        0,
        loan_amount
    )

    # --------------------------------------------------------
    # FINANCING ROUTE
    # --------------------------------------------------------

    financing = get_financing_route(
        loan_amount
    )

    financing_type = financing["type"]

    interest_rate = financing["interest_rate"]

    tenure_years = financing["tenure_years"]

    moratorium_months = financing["moratorium_months"]

    # --------------------------------------------------------
    # EMI
    # --------------------------------------------------------

    emi = calculate_emi(
        loan_amount,
        interest_rate,
        tenure_years
    )

    # --------------------------------------------------------
    # REPAYMENT SAFETY
    # --------------------------------------------------------

    repayment = calculate_repayment_safety(
        monthly_surplus,
        emi
    )

    repayment_status = repayment["status"]

    coverage = repayment["coverage"]

    # --------------------------------------------------------
    # SAVE EVERYTHING FOR OTHER FRAMES
    # --------------------------------------------------------

    st.session_state.project_cost = project_cost

    st.session_state.own_capital = own_capital

    st.session_state.funding_gap = funding_gap

    st.session_state.loan_amount = loan_amount

    st.session_state.interest_rate = interest_rate

    st.session_state.loan_tenure_years = tenure_years

    st.session_state.moratorium_months = moratorium_months

    st.session_state.emi = emi

    st.session_state.monthly_revenue = monthly_revenue

    st.session_state.monthly_expenses = monthly_expenses

    st.session_state.monthly_surplus = monthly_surplus

    st.session_state.repayment_status = repayment_status

    st.session_state.repayment_coverage = coverage

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="
            background:#526A3A;
            padding:25px;
            border-radius:16px;
            margin-bottom:20px;
        ">

            <h1 style="
                color:white;
                margin-bottom:5px;
            ">
                {tr["title"]}
            </h1>

            <p style="
                color:#F5F2E8;
                font-size:16px;
                margin-bottom:0;
            ">
                {tr["subtitle"]}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SELECTED BUSINESS
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border:1px solid #E4E1D6;
            border-radius:12px;
            padding:15px 18px;
            margin-bottom:20px;
        ">

            <div style="
                color:#777;
                font-size:13px;
            ">
                {tr["selected_business"]}
            </div>

            <div style="
                color:#33352C;
                font-size:22px;
                font-weight:700;
            ">
                {business_name}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # FINANCIAL SUMMARY
    # --------------------------------------------------------

    st.subheader("📊 Financial Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            tr["available_capital"],
            format_rupees(own_capital)
        )

    with col2:

        st.metric(
            tr["project_cost"],
            format_rupees(project_cost)
        )

    with col3:

        st.metric(
            tr["funding_gap"],
            format_rupees(funding_gap)
        )

    col4, col5, col6 = st.columns(3)

    with col4:

        st.metric(
            tr["monthly_revenue"],
            format_rupees(monthly_revenue)
        )

    with col5:

        st.metric(
            tr["monthly_expenses"],
            format_rupees(monthly_expenses)
        )

    with col6:

        st.metric(
            tr["monthly_surplus"],
            format_rupees(monthly_surplus)
        )

    st.divider()

    # ========================================================
    # LOAN CALCULATION
    # ========================================================

    st.subheader(tr["loan_calculation"])

    calc_col1, calc_col2, calc_col3 = st.columns(3)

    with calc_col1:

        st.metric(
            tr["required_capital"],
            format_rupees(project_cost)
        )

    with calc_col2:

        st.metric(
            tr["own_capital"],
            format_rupees(own_capital)
        )

    with calc_col3:

        st.metric(
            tr["loan_needed"],
            format_rupees(funding_gap)
        )

    # --------------------------------------------------------
    # LOAN AMOUNT SECTION
    # --------------------------------------------------------

    st.markdown("### " + tr["loan_amount_title"])

    if funding_gap <= 0:

        st.success(
            f"✅ {tr['no_loan_required']}"
        )

        loan_amount = 0

    else:

        st.info(
            f"{tr['loan_required']} "
            f"**{format_rupees(funding_gap)}**"
        )

        # Slider step
        if funding_gap <= 10000:
            step = 1000
        elif funding_gap <= 100000:
            step = 5000
        else:
            step = 10000

        max_loan = int(
            math.ceil(funding_gap / step) * step
        )

        default_loan = int(
            min(
                loan_amount,
                max_loan
            )
        )

        # Ensure default follows step
        default_loan = int(
            round(default_loan / step) * step
        )

        default_loan = min(
            default_loan,
            max_loan
        )

        selected_loan_amount = st.slider(
            tr["adjust_loan"],
            min_value=0,
            max_value=max_loan,
            value=default_loan,
            step=step,
            help=tr["loan_amount_help"]
        )

        loan_amount = float(
            selected_loan_amount
        )

    # --------------------------------------------------------
    # RECALCULATE FINANCING BASED ON SELECTED LOAN
    # --------------------------------------------------------

    financing = get_financing_route(
        loan_amount
    )

    financing_type = financing["type"]

    interest_rate = financing["interest_rate"]

    tenure_years = financing["tenure_years"]

    moratorium_months = financing["moratorium_months"]

    emi = calculate_emi(
        loan_amount,
        interest_rate,
        tenure_years
    )

    repayment = calculate_repayment_safety(
        monthly_surplus,
        emi
    )

    repayment_status = repayment["status"]

    coverage = repayment["coverage"]

    # --------------------------------------------------------
    # SAVE UPDATED VALUES AGAIN
    # --------------------------------------------------------

    st.session_state.funding_gap = funding_gap

    st.session_state.loan_amount = loan_amount

    st.session_state.interest_rate = interest_rate

    st.session_state.loan_tenure_years = tenure_years

    st.session_state.moratorium_months = moratorium_months

    st.session_state.emi = emi

    st.session_state.repayment_status = repayment_status

    st.session_state.repayment_coverage = coverage

    # --------------------------------------------------------
    # DISPLAY SELECTED LOAN
    # --------------------------------------------------------

    loan_display_col1, loan_display_col2 = st.columns(2)

    with loan_display_col1:

        st.metric(
            tr["loan_amount_selected"],
            format_rupees(loan_amount)
        )

    with loan_display_col2:

        remaining_own_funding = max(
            0,
            project_cost - loan_amount
        )

        st.metric(
            "Own + Loan Coverage",
            format_rupees(
                remaining_own_funding
            )
        )

    st.divider()

    # ========================================================
    # FINANCING PLAN
    # ========================================================

    st.subheader(tr["financing_plan"])

    if financing_type == "self_funded":

        finance_name = tr["self_funded"]

    elif financing_type == "micro_finance":

        finance_name = tr["micro_finance"]

    else:

        finance_name = tr["term_loan"]

    plan_col1, plan_col2, plan_col3 = st.columns(3)

    with plan_col1:

        st.markdown(
            f"**{tr['finance_type']}**"
        )

        st.write(
            finance_name
        )

    with plan_col2:

        st.markdown(
            f"**{tr['interest_rate']}**"
        )

        if interest_rate > 0:

            st.write(
                f"{interest_rate:.1f}%"
            )

        else:

            st.write("—")

    with plan_col3:

        st.markdown(
            f"**{tr['tenure']}**"
        )

        if tenure_years > 0:

            st.write(
                f"{tenure_years} {tr['years']}"
            )

        else:

            st.write("—")

    plan_col4, plan_col5, plan_col6 = st.columns(3)

    with plan_col4:

        st.markdown(
            f"**{tr['moratorium']}**"
        )

        if moratorium_months > 0:

            st.write(
                f"{moratorium_months} {tr['months']}"
            )

        else:

            st.write("—")

    with plan_col5:

        st.markdown(
            f"**{tr['emi']}**"
        )

        if emi > 0:

            st.write(
                format_rupees(emi)
            )

        else:

            st.write("—")

    with plan_col6:

        st.markdown(
            f"**{tr['loan_amount']}**"
        )

        st.write(
            format_rupees(loan_amount)
        )

    # ========================================================
    # REPAYMENT SAFETY
    # ========================================================

    st.subheader(tr["repayment_safety"])

    if loan_amount <= 0:

        st.success(
            f"🟢 {tr['self_funded_safe']}"
        )

    else:

        safety_col1, safety_col2, safety_col3 = st.columns(3)

        with safety_col1:

            st.metric(
                tr["surplus"],
                format_rupees(monthly_surplus)
            )

        with safety_col2:

            st.metric(
                tr["emi_burden"],
                format_rupees(emi)
            )

        with safety_col3:

            if coverage is not None:

                st.metric(
                    tr["coverage"],
                    f"{coverage:.2f}×"
                )

            else:

                st.metric(
                    tr["coverage"],
                    "—"
                )

        # ----------------------------------------------------
        # SAFETY MESSAGE
        # ----------------------------------------------------

        if repayment_status == "comfortable":

            st.success(
                f"🟢 {tr['comfortable']} — "
                f"{tr['comfortable_msg']}"
            )

        elif repayment_status == "manageable":

            st.warning(
                f"🟠 {tr['manageable']} — "
                f"{tr['manageable_msg']}"
            )

        else:

            st.error(
                f"🔴 {tr['unsafe']} — "
                f"{tr['unsafe_msg']}"
            )

    # ========================================================
    # FINAL RECOMMENDATION
    # ========================================================

    st.subheader("🎯 Recommendation")

    if loan_amount <= 0:

        st.success(
            f"### {tr['go']}"
        )

        st.write(
            "The current prototype business plan can be funded "
            "with the available own capital, so there is no EMI burden."
        )

    elif repayment_status == "comfortable":

        st.success(
            f"### {tr['go']}"
        )

        st.write(
            "The projected monthly surplus provides a reasonable "
            "buffer above the estimated EMI."
        )

    elif repayment_status == "manageable":

        st.warning(
            f"### {tr['review']}"
        )

        st.write(
            "Consider reducing the loan amount, increasing own capital, "
            "or validating demand before borrowing."
        )

    else:

        st.error(
            f"### {tr['dont_borrow']}"
        )

        st.write(
            "The projected monthly surplus is not sufficient to safely "
            "cover the estimated EMI. Consider starting with a smaller "
            "project or increasing your own contribution."
        )

    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.divider()

    st.markdown(
        f"""
        <div style="
            background:#FAF8F1;
            border-left:5px solid #C88A3D;
            padding:16px;
            border-radius:8px;
        ">

            <strong>
                {tr["disclaimer_title"]}
            </strong>

            <p style="
                margin-top:8px;
                color:#555;
            ">
                {tr["disclaimer"]}
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # NAVIGATION
    # ========================================================

    st.divider()

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            tr["back"],
            use_container_width=True
        ):

            st.session_state.page = 4

            st.rerun()

    with continue_col:

        if st.button(
            tr["continue"],
            use_container_width=True
        ):

            st.session_state.page = 6

            st.rerun()

