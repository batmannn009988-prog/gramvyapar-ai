# frames/frame5_financial_dashboard.py

import math
import requests
import streamlit as st


# ============================================================
# LIVE BACKEND
# ============================================================

BACKEND_URL = "https://kerala-business-advisor.onrender.com"


# ============================================================
# TRANSLATIONS
# ============================================================

T = {
    "en": {
        "title": "💰 Financial Dashboard",
        "subtitle": "Understand your investment, funding gap, loan requirement and repayment capacity.",

        "selected_business": "Selected Business",
        "financial_summary": "📊 Financial Summary",

        "available_capital": "Available Capital",
        "project_cost": "Estimated Project Cost",
        "funding_gap": "Funding Gap",
        "monthly_revenue": "Estimated Monthly Revenue",
        "monthly_expenses": "Estimated Monthly Expenses",
        "monthly_surplus": "Estimated Monthly Surplus",

        "loan_calculation": "🏦 Loan Calculation",
        "required_capital": "Required Capital",
        "own_capital": "Your Own Capital",
        "loan_needed": "Loan Needed",

        "loan_amount": "Loan Amount",
        "no_loan_required": "No loan required",
        "selected_loan_amount": "Selected Loan Amount",
        "remaining_gap": "Remaining Funding Gap",

        "financing_plan": "📋 Indicative Financing Plan",
        "self_funded": "Self-funded business plan",
        "micro_finance": "Micro Finance",
        "term_loan": "Term Loan",
        "interest": "Interest",
        "tenure": "Tenure",
        "moratorium": "Moratorium",
        "monthly_emi": "Estimated Monthly EMI",
        "estimated_loan_amount": "Estimated Loan Amount",

        "repayment_safety": "🛡️ Repayment Safety",
        "coverage": "Surplus / EMI Coverage",
        "comfortable": "Comfortable",
        "manageable": "Manageable",
        "unsafe": "Unsafe",
        "self_funded_status": "SELF-FUNDED — No EMI burden",

        "recommendation": "🎯 Recommendation",
        "go": "GO — FINANCIALLY FEASIBLE",
        "review": "REVIEW — CHECK BEFORE BORROWING",
        "dont_borrow": "DON'T BORROW / START SMALLER",

        "go_message": "The current business plan appears financially feasible based on the prototype assumptions.",
        "review_message": "The business may be feasible, but repayment capacity should be reviewed carefully before borrowing.",
        "dont_borrow_message": "Expected monthly surplus is not strong enough to safely support the selected loan. Consider reducing the project size or increasing your own contribution.",

        "underfunded_warning": "⚠️ The selected loan does not fully cover the funding gap. Increase the loan amount or add more own capital.",

        "disclaimer_title": "⚠️ Prototype Disclaimer",
        "disclaimer": (
            "Financing routes, interest rates, tenure and moratorium shown here are "
            "illustrative prototype values. Actual scheme rules, eligibility, interest "
            "rates, repayment terms and approval must be verified with the relevant "
            "official source. Loan approval is not guaranteed."
        ),

        "back": "← Back to Business Detail",
        "continue": "Continue to Risk Analysis →",

        "years": "years",
        "months": "months",
        "per_month": "/ month",
    },

    "ml": {
        "title": "💰 സാമ്പത്തിക ഡാഷ്ബോർഡ്",
        "subtitle": "നിക്ഷേപം, ഫണ്ടിംഗ് കുറവ്, വായ്പ ആവശ്യകത, തിരിച്ചടവ് ശേഷി എന്നിവ മനസ്സിലാക്കുക.",

        "selected_business": "തിരഞ്ഞെടുത്ത ബിസിനസ്",
        "financial_summary": "📊 സാമ്പത്തിക സംഗ്രഹം",

        "available_capital": "ലഭ്യമായ മൂലധനം",
        "project_cost": "കണക്കാക്കിയ പ്രോജക്ട് ചെലവ്",
        "funding_gap": "ഫണ്ടിംഗ് കുറവ്",
        "monthly_revenue": "കണക്കാക്കിയ മാസ വരുമാനം",
        "monthly_expenses": "കണക്കാക്കിയ മാസ ചെലവ്",
        "monthly_surplus": "കണക്കാക്കിയ മാസ മിച്ചം",

        "loan_calculation": "🏦 വായ്പ കണക്കുകൂട്ടൽ",
        "required_capital": "ആവശ്യമായ മൂലധനം",
        "own_capital": "നിങ്ങളുടെ സ്വന്തം മൂലധനം",
        "loan_needed": "ആവശ്യമായ വായ്പ",

        "loan_amount": "വായ്പ തുക",
        "no_loan_required": "വായ്പ ആവശ്യമില്ല",
        "selected_loan_amount": "തിരഞ്ഞെടുത്ത വായ്പ തുക",
        "remaining_gap": "ശേഷിക്കുന്ന ഫണ്ടിംഗ് കുറവ്",

        "financing_plan": "📋 സൂചനാത്മക ധനസഹായ പദ്ധതി",
        "self_funded": "സ്വന്തം മൂലധനം ഉപയോഗിച്ചുള്ള പദ്ധതി",
        "micro_finance": "മൈക്രോ ഫിനാൻസ്",
        "term_loan": "ടേം ലോൺ",
        "interest": "പലിശ",
        "tenure": "കാലാവധി",
        "moratorium": "മൊറട്ടോറിയം",
        "monthly_emi": "കണക്കാക്കിയ മാസ EMI",
        "estimated_loan_amount": "കണക്കാക്കിയ വായ്പ തുക",

        "repayment_safety": "🛡️ തിരിച്ചടവ് സുരക്ഷ",
        "coverage": "മിച്ചം / EMI കവറേജ്",
        "comfortable": "സുരക്ഷിതം",
        "manageable": "നിയന്ത്രിക്കാവുന്നത്",
        "unsafe": "സുരക്ഷിതമല്ല",
        "self_funded_status": "സ്വന്തം മൂലധനം — EMI ബാധ്യതയില്ല",

        "recommendation": "🎯 ശുപാർശ",
        "go": "GO — സാമ്പത്തികമായി സാധ്യമാണ്",
        "review": "REVIEW — വായ്പയ്ക്ക് മുമ്പ് പരിശോധിക്കുക",
        "dont_borrow": "വായ്പ എടുക്കരുത് / ചെറിയ തോതിൽ ആരംഭിക്കുക",

        "go_message": "നിലവിലെ പ്രോട്ടോടൈപ്പ് കണക്കുകൾ പ്രകാരം ഈ ബിസിനസ് പദ്ധതി സാമ്പത്തികമായി സാധ്യമാണ്.",
        "review_message": "ബിസിനസ് സാധ്യമായേക്കാം, എന്നാൽ വായ്പ എടുക്കുന്നതിന് മുമ്പ് തിരിച്ചടവ് ശേഷി ശ്രദ്ധാപൂർവ്വം പരിശോധിക്കണം.",
        "dont_borrow_message": "പ്രതീക്ഷിക്കുന്ന മാസ മിച്ചം തിരഞ്ഞെടുത്ത വായ്പ സുരക്ഷിതമായി തിരിച്ചടയ്ക്കാൻ പര്യാപ്തമല്ല.",

        "underfunded_warning": "⚠️ തിരഞ്ഞെടുത്ത വായ്പ മുഴുവൻ ഫണ്ടിംഗ് കുറവ് നികത്തുന്നില്ല.",

        "disclaimer_title": "⚠️ പ്രോട്ടോടൈപ്പ് അറിയിപ്പ്",
        "disclaimer": (
            "ഇവിടെ കാണിക്കുന്ന ധനസഹായ മാർഗങ്ങൾ, പലിശ നിരക്ക്, കാലാവധി, മൊറട്ടോറിയം "
            "എന്നിവ പ്രോട്ടോടൈപ്പ് മൂല്യങ്ങളാണ്. യഥാർത്ഥ പദ്ധതി നിയമങ്ങളും യോഗ്യതയും "
            "ഔദ്യോഗിക ഉറവിടത്തിൽ പരിശോധിക്കണം."
        ),

        "back": "← ബിസിനസ് വിശദാംശങ്ങളിലേക്ക്",
        "continue": "റിസ്ക് വിശകലനത്തിലേക്ക് →",

        "years": "വർഷം",
        "months": "മാസം",
        "per_month": "/ മാസം",
    },
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_language():
    return st.session_state.get("language", "en")


def tr(key):
    language = get_language()

    if language not in T:
        language = "en"

    return T[language].get(key, T["en"].get(key, key))


def format_rupees(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        value = 0

    return f"₹{value:,.0f}"


def calculate_emi(principal, annual_rate, years):

    principal = float(principal)
    annual_rate = float(annual_rate)
    years = float(years)

    if principal <= 0 or years <= 0:
        return 0.0

    monthly_rate = annual_rate / 12 / 100
    months = int(years * 12)

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

    loan_amount = float(loan_amount)

    if loan_amount <= 0:
        return {
            "type": "self_funded",
            "name_en": "Self-funded business plan",
            "name_ml": "സ്വന്തം മൂലധനം ഉപയോഗിച്ചുള്ള പദ്ധതി",
            "interest_rate": 0.0,
            "tenure_years": 0,
            "moratorium_months": 0,
        }

    if loan_amount <= 140000:
        return {
            "type": "micro",
            "name_en": "Micro Finance",
            "name_ml": "മൈക്രോ ഫിനാൻസ്",
            "interest_rate": 6.5,
            "tenure_years": 3,
            "moratorium_months": 3,
        }

    return {
        "type": "term",
        "name_en": "Term Loan",
        "name_ml": "ടേം ലോൺ",
        "interest_rate": 8.0,
        "tenure_years": 7,
        "moratorium_months": 6,
    }


def calculate_repayment_safety(monthly_surplus, emi):

    monthly_surplus = float(monthly_surplus)
    emi = float(emi)

    if emi <= 0:
        return {
            "coverage": float("inf"),
            "status": "self_funded",
        }

    coverage = monthly_surplus / emi

    if coverage >= 1.5:
        status = "comfortable"
    elif coverage >= 1.0:
        status = "manageable"
    else:
        status = "unsafe"

    return {
        "coverage": coverage,
        "status": status,
    }


# ============================================================
# MAIN FRAME
# ============================================================

def render_frame5():

    try:
        from frames.frame4_business_detail import (
            BUSINESS_DATA,
            calculate_financials,
        )
    except Exception:
        BUSINESS_DATA = {}
        calculate_financials = None

    # --------------------------------------------------------
    # SELECTED BUSINESS
    # --------------------------------------------------------

    selected_business = st.session_state.get(
        "selected_business",
        ""
    )

    if not selected_business:
        st.warning("Please select a business first.")

        if st.button(tr("back")):
            st.session_state.page = 3
            st.rerun()

        return

    business = BUSINESS_DATA.get(selected_business)

    if business is None:
        st.error("Selected business data could not be found.")

        if st.button(tr("back")):
            st.session_state.page = 3
            st.rerun()

        return

    # --------------------------------------------------------
    # BUSINESS NAME
    # --------------------------------------------------------

    if get_language() == "ml":
        business_name = business.get(
            "name_ml",
            selected_business
        )
    else:
        business_name = business.get(
            "name_en",
            selected_business
        )

    if not business_name:
        business_name = selected_business

    # --------------------------------------------------------
    # BUSINESS FINANCIALS
    # --------------------------------------------------------

    try:

        financials = calculate_financials(business)

        project_cost = float(
            financials.get("startup_total", 0)
        )

        monthly_revenue = float(
            financials.get("monthly_revenue", 0)
        )

        monthly_expenses = float(
            financials.get("monthly_expenses", 0)
        )

        monthly_surplus = float(
            financials.get("monthly_surplus", 0)
        )

    except Exception:

        project_cost = float(
            business.get("startup_total", 0)
        )

        monthly_revenue = float(
            business.get("monthly_revenue", 0)
        )

        monthly_expenses = float(
            business.get("monthly_expenses", 0)
        )

        monthly_surplus = (
            monthly_revenue - monthly_expenses
        )

    # --------------------------------------------------------
    # OWN CAPITAL
    # --------------------------------------------------------

    own_capital = float(
        st.session_state.get("capital", 0)
    )

    funding_gap = max(
        0,
        project_cost - own_capital
    )

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.title(tr("title"))
    st.caption(tr("subtitle"))
    st.divider()

    # --------------------------------------------------------
    # SELECTED BUSINESS
    # --------------------------------------------------------

    st.subheader(tr("selected_business"))

    st.info(
        f"### {business_name}"
    )

    # --------------------------------------------------------
    # FINANCIAL SUMMARY
    # --------------------------------------------------------

    st.subheader(tr("financial_summary"))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            tr("available_capital"),
            format_rupees(own_capital),
        )

    with col2:
        st.metric(
            tr("project_cost"),
            format_rupees(project_cost),
        )

    with col3:
        st.metric(
            tr("funding_gap"),
            format_rupees(funding_gap),
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            tr("monthly_revenue"),
            format_rupees(monthly_revenue),
        )

    with col5:
        st.metric(
            tr("monthly_expenses"),
            format_rupees(monthly_expenses),
        )

    with col6:
        st.metric(
            tr("monthly_surplus"),
            format_rupees(monthly_surplus),
        )

    st.divider()

    # --------------------------------------------------------
    # LOAN CALCULATION
    # --------------------------------------------------------

    st.subheader(tr("loan_calculation"))

    loan_col1, loan_col2, loan_col3 = st.columns(3)

    with loan_col1:
        st.metric(
            tr("required_capital"),
            format_rupees(project_cost),
        )

    with loan_col2:
        st.metric(
            tr("own_capital"),
            format_rupees(own_capital),
        )

    with loan_col3:
        st.metric(
            tr("loan_needed"),
            format_rupees(funding_gap),
        )

    st.divider()

    # --------------------------------------------------------
    # LOAN AMOUNT
    # --------------------------------------------------------

    st.subheader(tr("loan_amount"))

    previous_loan = float(
        st.session_state.get(
            "loan_amount",
            funding_gap
        )
    )

    if funding_gap <= 0:

        loan_amount = 0.0

    else:

        previous_loan = min(
            max(previous_loan, 0),
            funding_gap
        )

        if funding_gap <= 100000:
            step = 5000
        elif funding_gap <= 500000:
            step = 10000
        else:
            step = 25000

        loan_amount = st.slider(
            tr("selected_loan_amount"),
            min_value=0.0,
            max_value=float(funding_gap),
            value=float(previous_loan),
            step=float(step),
            format="₹%.0f",
        )

    st.session_state.loan_amount = float(
        loan_amount
    )

    # --------------------------------------------------------
    # REMAINING GAP
    # --------------------------------------------------------

    remaining_funding_gap = max(
        0,
        project_cost - own_capital - loan_amount
    )

    if funding_gap <= 0:

        st.success(
            f"✅ {tr('no_loan_required')}"
        )

    elif remaining_funding_gap > 0:

        st.warning(
            tr("underfunded_warning")
        )

        st.metric(
            tr("remaining_gap"),
            format_rupees(remaining_funding_gap),
        )

    else:

        st.success(
            f"✅ {tr('loan_needed')}: "
            f"{format_rupees(loan_amount)}"
        )

    st.divider()

    # --------------------------------------------------------
    # FINANCING ROUTE
    # --------------------------------------------------------

    st.subheader(tr("financing_plan"))

    route = get_financing_route(
        loan_amount
    )

    route_type = route["type"]

    if route_type == "self_funded":

        st.success(
            f"🟢 {tr('self_funded')}"
        )

        interest_rate = 0.0
        tenure_years = 0
        moratorium_months = 0
        emi = 0.0

    else:

        if get_language() == "ml":
            route_name = route["name_ml"]
        else:
            route_name = route["name_en"]

        st.info(
            f"🏦 **{route_name}**"
        )

        interest_rate = route["interest_rate"]
        tenure_years = route["tenure_years"]
        moratorium_months = route["moratorium_months"]

        emi = calculate_emi(
            loan_amount,
            interest_rate,
            tenure_years,
        )

    # --------------------------------------------------------
    # FINANCING METRICS
    # --------------------------------------------------------

    finance_col1, finance_col2, finance_col3 = st.columns(3)

    with finance_col1:

        if route_type == "self_funded":
            st.metric(
                tr("interest"),
                "—",
            )
        else:
            st.metric(
                tr("interest"),
                f"{interest_rate:.1f}%",
            )

    with finance_col2:

        if route_type == "self_funded":
            st.metric(
                tr("tenure"),
                "—",
            )
        else:
            st.metric(
                tr("tenure"),
                f"{tenure_years} {tr('years')}",
            )

    with finance_col3:

        if route_type == "self_funded":
            st.metric(
                tr("moratorium"),
                "—",
            )
        else:
            st.metric(
                tr("moratorium"),
                f"{moratorium_months} {tr('months')}",
            )

    finance_col4, finance_col5 = st.columns(2)

    with finance_col4:

        if emi > 0:
            st.metric(
                tr("monthly_emi"),
                format_rupees(emi),
            )
        else:
            st.metric(
                tr("monthly_emi"),
                "—",
            )

    with finance_col5:

        st.metric(
            tr("estimated_loan_amount"),
            format_rupees(loan_amount),
        )

    # --------------------------------------------------------
    # STORE FINANCIAL STATE
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

    # ========================================================
    # LIVE BACKEND CALL
    # ========================================================

    backend_payload = {
        "location": st.session_state.get(
            "district",
            "Kozhikode"
        ),
        "business_category": selected_business,
        "available_capital": float(own_capital),
        "project_cost": float(project_cost),
        "monthly_revenue": float(monthly_revenue),
        "monthly_expenses": float(monthly_expenses),
        "interest_rate": float(interest_rate),
        "tenure_years": int(tenure_years)
        if tenure_years > 0 else 7,
        "is_sc": False,
        "annual_family_income": 0,
    }

    backend_result = None

    try:

        response = requests.post(
            f"{BACKEND_URL}/advisory-report",
            json=backend_payload,
            timeout=30,
        )

        if response.status_code == 200:

            backend_result = response.json()

            st.session_state.backend_result = (
                backend_result
            )

        else:

            st.error(
                f"Backend error: HTTP {response.status_code}"
            )

    except requests.exceptions.RequestException as e:

        st.error(
            f"Could not connect to RuralBiz AI backend: {e}"
        )

    # ========================================================
    # LIVE RURALBIZ AI RESULT
    # ========================================================

    if backend_result:

        if backend_result.get("status") == "success":

            st.divider()

            st.subheader(
                "🤖 RuralBiz AI Analysis"
            )

            recommendation_data = (
                backend_result.get(
                    "recommendation",
                    {}
                )
            )

            decision = recommendation_data.get(
                "decision",
                "MODIFY"
            )

            if decision == "GO":

                st.success(
                    "🟢 GO — BUSINESS PLAN LOOKS FEASIBLE"
                )

            elif decision == "MODIFY":

                st.warning(
                    "🟠 MODIFY — CHECK BEFORE PROCEEDING"
                )

            else:

                st.error(
                    "🔴 DON'T PROCEED — HIGH FINANCIAL RISK"
                )

            st.write(
                recommendation_data.get(
                    "reason",
                    "Backend analysis completed."
                )
            )

            # ------------------------------------------------
            # OPPORTUNITY
            # ------------------------------------------------

            opportunity = backend_result.get(
                "opportunity",
                {}
            )

            st.markdown(
                "### 📍 Local Opportunity"
            )

            opp_col1, opp_col2 = st.columns(2)

            with opp_col1:

                st.metric(
                    "Opportunity Score",
                    opportunity.get(
                        "score",
                        "—"
                    )
                )

            with opp_col2:

                st.write(
                    f"**Rating:** "
                    f"{opportunity.get(
                        'rating',
                        'Unknown'
                    )}"
                )

            st.caption(
                opportunity.get(
                    "note",
                    opportunity.get(
                        "data_status",
                        "Based on available local indicators."
                    )
                )
            )

            # ------------------------------------------------
            # FINANCIAL RESULT
            # ------------------------------------------------

            financial = backend_result.get(
                "financial",
                {}
            )

            st.markdown(
                "### 💰 Backend Financial Analysis"
            )

            financial_col1, financial_col2, financial_col3 = (
                st.columns(3)
            )

            with financial_col1:

                st.metric(
                    "Loan Required",
                    format_rupees(
                        financial.get(
                            "loan_required",
                            0
                        )
                    )
                )

            with financial_col2:

                st.metric(
                    "Estimated EMI",
                    format_rupees(
                        financial.get(
                            "estimated_emi",
                            0
                        )
                    )
                )

            with financial_col3:

                st.metric(
                    "Cash After EMI",
                    format_rupees(
                        financial.get(
                            "remaining_cash_after_emi",
                            0
                        )
                    )
                )

            # ------------------------------------------------
            # RISK
            # ------------------------------------------------

            risk = backend_result.get(
                "risk",
                {}
            )

            st.markdown(
                "### 🛡️ Repayment Risk"
            )

            st.write(
                f"**Risk Level:** "
                f"{risk.get(
                    'risk',
                    'Unknown'
                )}"
            )

            st.write(
                risk.get(
                    "reason",
                    ""
                )
            )

            # ------------------------------------------------
            # STRESS TEST
            # ------------------------------------------------

            stress = backend_result.get(
                "stress_test",
                {}
            )

            if stress:

                st.markdown(
                    "### 📉 Revenue Stress Test"
                )

                for scenario_name, scenario in stress.items():

                    st.write(
                        f"**{scenario_name.replace('_', ' ').title()}** — "
                        f"Cash after EMI: "
                        f"{format_rupees(
                            scenario.get(
                                'cash_after_emi',
                                0
                            )
                        )} — "
                        f"{scenario.get(
                            'status',
                            'Unknown'
                        )}"
                    )

            # ------------------------------------------------
            # CONFIDENCE
            # ------------------------------------------------

            confidence = backend_result.get(
                "confidence",
                {}
            )

            st.caption(
                f"Confidence: "
                f"{confidence.get(
                    'confidence',
                    'Unknown'
                )} "
                f"({confidence.get(
                    'score',
                    0
                )})"
            )

            # ------------------------------------------------
            # DATA SOURCE
            # ------------------------------------------------

            local_evidence = backend_result.get(
                "local_evidence",
                {}
            )

            if local_evidence:

                st.caption(
                    f"District evidence: "
                    f"{local_evidence.get(
                        'district',
                        ''
                    )} | "
                    f"Data level: "
                    f"{local_evidence.get(
                        'data_level',
                        ''
                    )} | "
                    f"Updated: "
                    f"{local_evidence.get(
                        'last_updated',
                        ''
                    )}"
                )

        elif backend_result.get("status") == "data_gap":

            st.warning(
                "⚠️ No verified district-level evidence "
                "is available for this location."
            )

    # --------------------------------------------------------
    # REPAYMENT SAFETY
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        tr("repayment_safety")
    )

    safety = calculate_repayment_safety(
        monthly_surplus,
        emi,
    )

    coverage = safety["coverage"]
    safety_status = safety["status"]

    if safety_status == "self_funded":

        st.success(
            f"🟢 {tr('self_funded_status')}"
        )

        st.session_state.repayment_status = (
            "Self-funded"
        )

        st.session_state.repayment_coverage = 0.0

    else:

        safety_col1, safety_col2 = st.columns(2)

        with safety_col1:

            st.metric(
                tr("coverage"),
                f"{coverage:.2f}x",
            )

        with safety_col2:

            if safety_status == "comfortable":

                st.success(
                    f"🟢 {tr('comfortable')}"
                )

                status_text = "Comfortable"

            elif safety_status == "manageable":

                st.warning(
                    f"🟠 {tr('manageable')}"
                )

                status_text = "Manageable"

            else:

                st.error(
                    f"🔴 {tr('unsafe')}"
                )

                status_text = "Unsafe"

        st.session_state.repayment_status = (
            status_text
        )

        st.session_state.repayment_coverage = (
            coverage
        )

    # --------------------------------------------------------
    # FRONTEND RECOMMENDATION
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        tr("recommendation")
    )

    if loan_amount <= 0:

        recommendation = "GO"

        st.success(
            f"✅ {tr('go')}"
        )

        st.write(
            tr("go_message")
        )

    elif remaining_funding_gap > 0:

        recommendation = "REVIEW"

        st.warning(
            f"🟠 {tr('review')}"
        )

        st.write(
            tr("underfunded_warning")
        )

    elif safety_status == "unsafe":

        recommendation = "DONT_BORROW"

        st.error(
            f"🔴 {tr('dont_borrow')}"
        )

        st.write(
            tr("dont_borrow_message")
        )

    elif safety_status == "manageable":

        recommendation = "REVIEW"

        st.warning(
            f"🟠 {tr('review')}"
        )

        st.write(
            tr("review_message")
        )

    else:

        recommendation = "GO"

        st.success(
            f"✅ {tr('go')}"
        )

        st.write(
            tr("go_message")
        )

    st.session_state.financial_recommendation = (
        recommendation
    )

    # --------------------------------------------------------
    # DISCLAIMER
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        tr("disclaimer_title")
    )

    st.warning(
        tr("disclaimer")
    )

    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    st.divider()

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            tr("back"),
            use_container_width=True,
        ):

            st.session_state.page = 4
            st.rerun()

    with continue_col:

        if st.button(
            tr("continue"),
            use_container_width=True,
        ):

            st.session_state.page = 6
            st.rerun()
