```python
import streamlit as st

# ============================================================
# TRANSLATIONS
# ============================================================

T = {
    "en": {
        "title": "Risk Dashboard",
        "subtitle": "Understand the main risks before investing or borrowing.",
        "selected_business": "Selected Business",
        "overall_risk": "Overall Risk",
        "risk_factors": "Risk Factors",
        "demand_risk": "Demand Risk",
        "competition_risk": "Competition Risk",
        "financial_risk": "Financial Risk",
        "cost_risk": "Startup Cost Risk",
        "operational_risk": "Operational Risk",
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "very_high": "Very High",
        "good": "Good",
        "moderate": "Moderate",
        "attention": "Needs Attention",
        "critical": "Critical",
        "why": "Why this matters",
        "recommendation": "Recommendation",
        "go": "GO",
        "review": "REVIEW",
        "dont_borrow": "DON'T BORROW",
        "start_smaller": "START SMALLER",
        "risk_summary": "Risk Summary",
        "key_warnings": "Key Warnings",
        "financial_note": "Financial risk is based on the estimated monthly surplus and financing burden.",
        "market_note": "Market risk is based on the prototype demand and competition indicators.",
        "cost_note": "Startup cost risk considers the project cost compared with available capital.",
        "operational_note": "Operational risk considers the type of business and the complexity of running it.",
        "self_funded_note": "You have enough available capital to cover the estimated project cost. No loan burden is assumed.",
        "loan_note": "A loan is required to cover the estimated funding gap. Repayment safety should be checked carefully.",
        "unsafe_note": "The estimated monthly surplus is not sufficient to safely cover the expected EMI.",
        "comfortable_note": "The estimated monthly surplus provides a reasonable buffer over the expected EMI.",
        "manageable_note": "The estimated monthly surplus can cover the EMI, but the safety buffer is limited.",
        "back": "← Back",
        "continue": "Continue →",
        "no_business": "No business has been selected. Please return to the Opportunity Radar.",
        "prototype": "Prototype assessment",
        "data_note": "Risk scores are prototype estimates based on the available demo data. They are not a guarantee of business success.",
        "recommendation_go_text": "The business appears reasonably suitable for the current assumptions. Validate local demand and costs before committing the full amount.",
        "recommendation_review_text": "The business may be viable, but some risk factors need validation. Consider starting with a smaller pilot before taking major financial commitments.",
        "recommendation_dont_text": "The current assumptions indicate that borrowing may create excessive repayment pressure. Reduce project size, increase own contribution, or reconsider the business.",
        "demand_low": "Demand indicator is relatively strong.",
        "demand_medium": "Demand exists, but local customer validation is still important.",
        "demand_high": "Demand indicator is relatively weak. Validate customers before investing.",
        "competition_low": "Competition appears manageable compared with the market opportunity.",
        "competition_medium": "There are competing businesses. Differentiation will be important.",
        "competition_high": "Competition appears strong. Entering the market without a clear advantage may be difficult.",
        "financial_low": "Monthly surplus provides a healthy cushion.",
        "financial_medium": "Monthly surplus is positive, but the safety margin should be monitored.",
        "financial_high": "Monthly surplus is weak relative to the financial commitment.",
        "cost_low": "Available capital comfortably covers the estimated project cost.",
        "cost_medium": "The project cost uses a significant share of available capital.",
        "cost_high": "The project cost is high relative to available capital and may require financing.",
        "operational_low": "The business model appears relatively straightforward to operate.",
        "operational_medium": "The business requires regular attention to operations, suppliers, or customers.",
        "operational_high": "The business may require stronger operational skills, supply management, or daily supervision.",
        "warning_demand": "Validate demand with real customers before launch.",
        "warning_competition": "Check nearby competitors, pricing, and customer preferences.",
        "warning_cost": "Verify equipment, inventory, rent, and working-capital costs locally.",
        "warning_finance": "Do not assume projected surplus will remain constant every month.",
        "warning_loan": "Do not borrow unless the repayment buffer remains comfortable under weaker sales.",
        "warning_data": "Some indicators are prototype estimates and should be replaced with verified local data."
    },

    "ml": {
        "title": "റിസ്ക് ഡാഷ്ബോർഡ്",
        "subtitle": "നിക്ഷേപിക്കുന്നതിനും വായ്പ എടുക്കുന്നതിനും മുമ്പ് പ്രധാന അപകടസാധ്യതകൾ മനസ്സിലാക്കുക.",
        "selected_business": "തിരഞ്ഞെടുത്ത ബിസിനസ്",
        "overall_risk": "മൊത്തം റിസ്ക്",
        "risk_factors": "റിസ്ക് ഘടകങ്ങൾ",
        "demand_risk": "ഡിമാൻഡ് റിസ്ക്",
        "competition_risk": "മത്സര റിസ്ക്",
        "financial_risk": "സാമ്പത്തിക റിസ്ക്",
        "cost_risk": "ആരംഭ ചെലവ് റിസ്ക്",
        "operational_risk": "ഓപ്പറേഷണൽ റിസ്ക്",
        "low": "കുറവ്",
        "medium": "മധ്യം",
        "high": "ഉയർന്നത്",
        "very_high": "വളരെ ഉയർന്നത്",
        "good": "നല്ലത്",
        "moderate": "മിതമായത്",
        "attention": "ശ്രദ്ധ ആവശ്യമാണ്",
        "critical": "ഗുരുതരം",
        "why": "എന്തുകൊണ്ട് ഇത് പ്രധാനമാണ്",
        "recommendation": "ശുപാർശ",
        "go": "GO",
        "review": "REVIEW",
        "dont_borrow": "DON'T BORROW",
        "start_smaller": "START SMALLER",
        "risk_summary": "റിസ്ക് സംഗ്രഹം",
        "key_warnings": "പ്രധാന മുന്നറിയിപ്പുകൾ",
        "financial_note": "പ്രതീക്ഷിക്കുന്ന മാസത്തിലെ മിച്ചവും വായ്പാ തിരിച്ചടവ് ഭാരവും അടിസ്ഥാനമാക്കിയാണ് സാമ്പത്തിക റിസ്ക് കണക്കാക്കുന്നത്.",
        "market_note": "ഡിമാൻഡ്, മത്സരം എന്നിവയുടെ പ്രോട്ടോടൈപ്പ് സൂചകങ്ങളെ അടിസ്ഥാനമാക്കിയാണ് മാർക്കറ്റ് റിസ്ക് കണക്കാക്കുന്നത്.",
        "cost_note": "ലഭ്യമായ മൂലധനവുമായി താരതമ്യം ചെയ്തുള്ള പ്രോജക്റ്റ് ചെലവ് പരിഗണിച്ചാണ് ചെലവ് റിസ്ക് കണക്കാക്കുന്നത്.",
        "operational_note": "ബിസിനസ് നടത്തിപ്പിന്റെ സങ്കീർണ്ണതയും ആവശ്യമായ പ്രവർത്തന നിയന്ത്രണവും പരിഗണിക്കുന്നു.",
        "self_funded_note": "പ്രോജക്റ്റ് ചെലവ് മുഴുവൻ വഹിക്കാൻ മതിയായ സ്വന്തം മൂലധനം ലഭ്യമാണ്. വായ്പാ ഭാരം കണക്കാക്കിയിട്ടില്ല.",
        "loan_note": "ഫണ്ടിംഗ് ഗ്യാപ് നികത്താൻ വായ്പ ആവശ്യമാണ്. തിരിച്ചടവ് സുരക്ഷ ശ്രദ്ധാപൂർവ്വം പരിശോധിക്കണം.",
        "unsafe_note": "പ്രതീക്ഷിക്കുന്ന EMI സുരക്ഷിതമായി അടയ്ക്കാൻ മാസത്തിലെ മിച്ചം മതിയാകുന്നില്ല.",
        "comfortable_note": "പ്രതീക്ഷിക്കുന്ന EMI-നെ അപേക്ഷിച്ച് മാസത്തിലെ മിച്ചത്തിൽ നല്ലൊരു സുരക്ഷാ ബഫർ ഉണ്ട്.",
        "manageable_note": "EMI അടയ്ക്കാൻ കഴിയുമെങ്കിലും സുരക്ഷാ ബഫർ പരിമിതമാണ്.",
        "back": "← തിരികെ",
        "continue": "തുടരുക →",
        "no_business": "ബിസിനസ് തിരഞ്ഞെടുത്തിട്ടില്ല. Opportunity Radar-ലേക്ക് തിരികെ പോകുക.",
        "prototype": "പ്രോട്ടോടൈപ്പ് വിലയിരുത്തൽ",
        "data_note": "റിസ്ക് സ്കോറുകൾ ലഭ്യമായ ഡെമോ ഡാറ്റയെ അടിസ്ഥാനമാക്കിയുള്ള പ്രോട്ടോടൈപ്പ് കണക്കുകളാണ്. ഇത് ബിസിനസ് വിജയത്തിന്റെ ഉറപ്പല്ല.",
        "recommendation_go_text": "നിലവിലെ അനുമാനങ്ങളിൽ ബിസിനസ് താരതമ്യേന അനുയോജ്യമാണെന്ന് തോന്നുന്നു. മുഴുവൻ തുകയും നിക്ഷേപിക്കുന്നതിന് മുമ്പ് പ്രാദേശിക ഡിമാൻഡും ചെലവുകളും പരിശോധിക്കുക.",
        "recommendation_review_text": "ബിസിനസ് സാധ്യമായേക്കാം, പക്ഷേ ചില റിസ്കുകൾ പരിശോധിക്കണം. വലിയ സാമ്പത്തിക ബാധ്യതയ്ക്ക് മുമ്പ് ചെറിയ പൈലറ്റ് ആരംഭിക്കുന്നത് പരിഗണിക്കുക.",
        "recommendation_dont_text": "നിലവിലെ അനുമാനങ്ങൾ പ്രകാരം വായ്പ തിരിച്ചടവ് സമ്മർദ്ദം കൂടുതലാകാം. പ്രോജക്റ്റ് വലുപ്പം കുറയ്ക്കുക, സ്വന്തം മൂലധനം വർധിപ്പിക്കുക, അല്ലെങ്കിൽ മറ്റൊരു ബിസിനസ് പരിഗണിക്കുക.",
        "demand_low": "ഡിമാൻഡ് സൂചകം താരതമ്യേന ശക്തമാണ്.",
        "demand_medium": "ഡിമാൻഡ് ഉണ്ട്, പക്ഷേ പ്രാദേശിക ഉപഭോക്താക്കളിലൂടെ പരിശോധിക്കുന്നത് പ്രധാനമാണ്.",
        "demand_high": "ഡിമാൻഡ് സൂചകം താരതമ്യേന ദുർബലമാണ്. നിക്ഷേപിക്കുന്നതിന് മുമ്പ് ഉപഭോക്താക്കളെ പരിശോധിക്കുക.",
        "competition_low": "മാർക്കറ്റ് അവസരവുമായി താരതമ്യം ചെയ്യുമ്പോൾ മത്സരം കൈകാര്യം ചെയ്യാവുന്നതാണ്.",
        "competition_medium": "മത്സര ബിസിനസുകൾ ഉണ്ട്. വ്യക്തമായ വ്യത്യസ്തത ആവശ്യമാണ്.",
        "competition_high": "മത്സരം ശക്തമാണ്. വ്യക്തമായ നേട്ടമില്ലാതെ മാർക്കറ്റിൽ പ്രവേശിക്കുന്നത് ബുദ്ധിമുട്ടാകാം.",
        "financial_low": "മാസത്തിലെ മിച്ചം നല്ല സുരക്ഷാ ബഫർ നൽകുന്നു.",
        "financial_medium": "മാസത്തിലെ മിച്ചം പോസിറ്റീവാണ്, പക്ഷേ സുരക്ഷാ മാർജിൻ നിരീക്ഷിക്കണം.",
        "financial_high": "സാമ്പത്തിക ബാധ്യതയുമായി താരതമ്യം ചെയ്യുമ്പോൾ മാസത്തിലെ മിച്ചം ദുർബലമാണ്.",
        "cost_low": "ലഭ്യമായ മൂലധനം പ്രോജക്റ്റ് ചെലവ് സുഖമായി വഹിക്കുന്നു.",
        "cost_medium": "ലഭ്യമായ മൂലധനത്തിന്റെ വലിയൊരു ഭാഗം പ്രോജക്റ്റ് ചെലവിനായി ഉപയോഗിക്കുന്നു.",
        "cost_high": "ലഭ്യമായ മൂലധനവുമായി താരതമ്യം ചെയ്യുമ്പോൾ പ്രോജക്റ്റ് ചെലവ് കൂടുതലാണ്. വായ്പ ആവശ്യമായി വരാം.",
        "operational_low": "ബിസിനസ് മോഡൽ താരതമ്യേന എളുപ്പത്തിൽ നടത്താനാകും.",
        "operational_medium": "ഓപ്പറേഷൻസ്, സപ്ലയർമാർ, ഉപഭോക്താക്കൾ എന്നിവയിൽ സ്ഥിരമായ ശ്രദ്ധ ആവശ്യമാണ്.",
        "operational_high": "കൂടുതൽ ഓപ്പറേഷണൽ കഴിവുകളും സപ്ലൈ മാനേജ്മെന്റും ആവശ്യമായി വരാം.",
        "warning_demand": "ആരംഭിക്കുന്നതിന് മുമ്പ് യഥാർത്ഥ ഉപഭോക്താക്കളിലൂടെ ഡിമാൻഡ് പരിശോധിക്കുക.",
        "warning_competition": "അടുത്തുള്ള മത്സരക്കാരെയും വിലയും ഉപഭോക്തൃ മുൻഗണനകളും പരിശോധിക്കുക.",
        "warning_cost": "ഉപകരണങ്ങൾ, ഇൻവെന്ററി, വാടക, working capital എന്നിവയുടെ പ്രാദേശിക ചെലവ് പരിശോധിക്കുക.",
        "warning_finance": "പ്രതീക്ഷിക്കുന്ന മിച്ചം എല്ലാ മാസവും ഒരുപോലെ തുടരുമെന്ന് കരുതരുത്.",
        "warning_loan": "വിൽപ്പന കുറഞ്ഞാലും സുരക്ഷിതമായ തിരിച്ചടവ് ബഫർ ഉണ്ടെങ്കിൽ മാത്രമേ വായ്പ എടുക്കാവൂ.",
        "warning_data": "ചില സൂചകങ്ങൾ പ്രോട്ടോടൈപ്പ് കണക്കുകളാണ്. പിന്നീട് പരിശോധിച്ച പ്രാദേശിക ഡാറ്റ ഉപയോഗിക്കണം."
    }
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_risk_label(level, language):
    if language == "ml":
        mapping = {
            "Low": T["ml"]["low"],
            "Medium": T["ml"]["medium"],
            "High": T["ml"]["high"],
            "Very High": T["ml"]["very_high"]
        }
    else:
        mapping = {
            "Low": T["en"]["low"],
            "Medium": T["en"]["medium"],
            "High": T["en"]["high"],
            "Very High": T["en"]["very_high"]
        }

    return mapping.get(level, level)


def get_risk_level_from_score(score):
    if score <= 30:
        return "Low"
    elif score <= 55:
        return "Medium"
    elif score <= 75:
        return "High"
    else:
        return "Very High"


def get_risk_score_from_demand(demand):
    demand = float(demand)

    if demand >= 75:
        return 20
    elif demand >= 60:
        return 40
    elif demand >= 45:
        return 65
    else:
        return 85


def get_risk_score_from_competition(competition):
    competition = float(competition)

    if competition <= 40:
        return 20
    elif competition <= 60:
        return 40
    elif competition <= 75:
        return 65
    else:
        return 85


def calculate_financial_risk(monthly_surplus, emi, loan_amount):
    """
    Uses the loan amount and EMI selected/calculated in Frame 5.
    """

    monthly_surplus = float(monthly_surplus or 0)
    emi = float(emi or 0)
    loan_amount = float(loan_amount or 0)

    # Self-funded
    if loan_amount <= 0 or emi <= 0:
        if monthly_surplus >= 20000:
            return 15
        elif monthly_surplus >= 10000:
            return 30
        elif monthly_surplus > 0:
            return 45
        else:
            return 85

    # Financed
    coverage = monthly_surplus / emi

    if coverage >= 1.5:
        return 20
    elif coverage >= 1.2:
        return 40
    elif coverage >= 1.0:
        return 60
    elif coverage >= 0.75:
        return 80
    else:
        return 95


def calculate_cost_risk(project_cost, available_capital):
    project_cost = float(project_cost or 0)
    available_capital = float(available_capital or 0)

    if project_cost <= 0:
        return 50

    if available_capital <= 0:
        return 95

    ratio = project_cost / available_capital

    if ratio <= 0.50:
        return 15
    elif ratio <= 0.75:
        return 25
    elif ratio <= 1.00:
        return 40
    elif ratio <= 1.50:
        return 65
    elif ratio <= 2.00:
        return 80
    else:
        return 95


def calculate_operational_risk(business_name):
    name = str(business_name).lower()

    if "tailor" in name:
        return 30

    if "bakery" in name:
        return 45

    if "dairy" in name:
        return 60

    return 45


def get_factor_message(factor, level, language):
    lang = "ml" if language == "ml" else "en"

    if factor == "demand":
        if level == "Low":
            return T[lang]["demand_low"]
        elif level == "Medium":
            return T[lang]["demand_medium"]
        else:
            return T[lang]["demand_high"]

    if factor == "competition":
        if level == "Low":
            return T[lang]["competition_low"]
        elif level == "Medium":
            return T[lang]["competition_medium"]
        else:
            return T[lang]["competition_high"]

    if factor == "financial":
        if level == "Low":
            return T[lang]["financial_low"]
        elif level == "Medium":
            return T[lang]["financial_medium"]
        else:
            return T[lang]["financial_high"]

    if factor == "cost":
        if level == "Low":
            return T[lang]["cost_low"]
        elif level == "Medium":
            return T[lang]["cost_medium"]
        else:
            return T[lang]["cost_high"]

    if factor == "operational":
        if level == "Low":
            return T[lang]["operational_low"]
        elif level == "Medium":
            return T[lang]["operational_medium"]
        else:
            return T[lang]["operational_high"]

    return ""


def get_recommendation(
    overall_score,
    financial_score,
    loan_amount,
    language
):
    lang = "ml" if language == "ml" else "en"

    # Financial safety has priority when borrowing.
    if loan_amount > 0 and financial_score >= 80:
        return (
            "DON'T BORROW",
            T[lang]["recommendation_dont_text"]
        )

    if overall_score <= 35:
        return (
            "GO",
            T[lang]["recommendation_go_text"]
        )

    if overall_score <= 60:
        return (
            "REVIEW",
            T[lang]["recommendation_review_text"]
        )

    return (
        "DON'T BORROW",
        T[lang]["recommendation_dont_text"]
    )


def get_risk_emoji(level):
    if level == "Low":
        return "🟢"
    elif level == "Medium":
        return "🟡"
    elif level == "High":
        return "🟠"
    else:
        return "🔴"


def get_recommendation_emoji(recommendation):
    if recommendation == "GO":
        return "🟢"
    elif recommendation == "REVIEW":
        return "🟡"
    else:
        return "🔴"


# ============================================================
# MAIN FRAME
# ============================================================

def render_frame6():

    # --------------------------------------------------------
    # LANGUAGE
    # --------------------------------------------------------

    language = st.session_state.get(
        "language",
        "en"
    )

    lang = "ml" if language == "ml" else "en"

    # --------------------------------------------------------
    # SELECTED BUSINESS
    # --------------------------------------------------------

    selected_business = st.session_state.get(
        "selected_business",
        ""
    )

    if not selected_business:

        st.warning(
            T[lang]["no_business"]
        )

        if st.button(
            T[lang]["back"]
        ):
            st.session_state.page = 3
            st.rerun()

        return

    # --------------------------------------------------------
    # BUSINESS DATA
    # --------------------------------------------------------

    try:

        from frames.frame4_business_detail import (
            BUSINESS_DATA,
            calculate_financials
        )

    except Exception:

        BUSINESS_DATA = {}
        calculate_financials = None

    business = BUSINESS_DATA.get(
        selected_business,
        {}
    )

    # --------------------------------------------------------
    # BUSINESS NAME
    # --------------------------------------------------------

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

    if not business_name:
        business_name = selected_business

    # --------------------------------------------------------
    # FINANCIAL VALUES
    # --------------------------------------------------------

    available_capital = float(
        st.session_state.get(
            "capital",
            0
        ) or 0
    )

    # Frame 5 is the source of truth.
    project_cost = float(
        st.session_state.get(
            "project_cost",
            0
        ) or 0
    )

    funding_gap = float(
        st.session_state.get(
            "funding_gap",
            0
        ) or 0
    )

    # IMPORTANT:
    # Read the exact loan amount selected in Frame 5.
    loan_amount = float(
        st.session_state.get(
            "loan_amount",
            0
        ) or 0
    )

    # IMPORTANT:
    # Read the exact EMI calculated in Frame 5.
    emi = float(
        st.session_state.get(
            "emi",
            0
        ) or 0
    )

    monthly_surplus = float(
        st.session_state.get(
            "monthly_surplus",
            0
        ) or 0
    )

    # --------------------------------------------------------
    # FALLBACK: CALCULATE FROM FRAME 4
    # --------------------------------------------------------

    if business and calculate_financials is not None:

        try:

            financials = calculate_financials(
                business
            )

            if project_cost <= 0:

                project_cost = float(
                    financials.get(
                        "startup_cost",
                        financials.get(
                            "project_cost",
                            0
                        )
                    ) or 0
                )

            if monthly_surplus <= 0:

                monthly_surplus = float(
                    financials.get(
                        "monthly_surplus",
                        financials.get(
                            "surplus",
                            0
                        )
                    ) or 0
                )

        except Exception:
            pass

    # --------------------------------------------------------
    # FUNDING FALLBACK
    # --------------------------------------------------------

    if funding_gap <= 0 and project_cost > 0:

        funding_gap = max(
            0,
            project_cost - available_capital
        )

    # IMPORTANT:
    # Do NOT overwrite a loan amount selected in Frame 5.
    #
    # Only use the funding gap if Frame 5 has not stored
    # a loan amount yet.
    if (
        "loan_amount" not in st.session_state
        and funding_gap > 0
    ):

        loan_amount = funding_gap

    # --------------------------------------------------------
    # MARKET VALUES
    # --------------------------------------------------------

    demand = float(
        business.get(
            "demand",
            60
        ) or 60
    )

    competition = float(
        business.get(
            "competition",
            60
        ) or 60
    )

    # --------------------------------------------------------
    # RISK SCORES
    # --------------------------------------------------------

    demand_risk_score = get_risk_score_from_demand(
        demand
    )

    competition_risk_score = get_risk_score_from_competition(
        competition
    )

    financial_risk_score = calculate_financial_risk(
        monthly_surplus,
        emi,
        loan_amount
    )

    cost_risk_score = calculate_cost_risk(
        project_cost,
        available_capital
    )

    operational_risk_score = calculate_operational_risk(
        selected_business
    )

    # --------------------------------------------------------
    # OVERALL RISK
    # --------------------------------------------------------

    overall_score = (
        demand_risk_score * 0.20
        + competition_risk_score * 0.20
        + financial_risk_score * 0.35
        + cost_risk_score * 0.15
        + operational_risk_score * 0.10
    )

    overall_score = round(
        overall_score
    )

    overall_level = get_risk_level_from_score(
        overall_score
    )

    # --------------------------------------------------------
    # FACTOR LEVELS
    # --------------------------------------------------------

    demand_level = get_risk_level_from_score(
        demand_risk_score
    )

    competition_level = get_risk_level_from_score(
        competition_risk_score
    )

    financial_level = get_risk_level_from_score(
        financial_risk_score
    )

    cost_level = get_risk_level_from_score(
        cost_risk_score
    )

    operational_level = get_risk_level_from_score(
        operational_risk_score
    )

    # --------------------------------------------------------
    # FINAL RECOMMENDATION
    # --------------------------------------------------------

    recommendation, recommendation_text = get_recommendation(
        overall_score,
        financial_risk_score,
        loan_amount,
        language
    )

    # --------------------------------------------------------
    # SAVE VALUES FOR NEXT SCREENS
    # --------------------------------------------------------

    st.session_state.overall_risk_score = overall_score
    st.session_state.overall_risk_level = overall_level

    st.session_state.demand_risk_score = demand_risk_score
    st.session_state.competition_risk_score = competition_risk_score
    st.session_state.financial_risk_score = financial_risk_score
    st.session_state.cost_risk_score = cost_risk_score
    st.session_state.operational_risk_score = operational_risk_score

    st.session_state.recommendation = recommendation

    # ========================================================
    # HEADER
    # ========================================================

    st.title(
        f"⚠️ {T[lang]['title']}"
    )

    st.caption(
        T[lang]["subtitle"]
    )

    st.markdown(
        f"### {T[lang]['selected_business']}: **{business_name}**"
    )

    # ========================================================
    # OVERALL RISK
    # ========================================================

    st.markdown(
        f"## {T[lang]['overall_risk']}"
    )

    risk_col1, risk_col2, risk_col3 = st.columns(
        [1, 1, 2]
    )

    with risk_col1:

        st.metric(
            label=T[lang]["overall_risk"],
            value=get_risk_label(
                overall_level,
                language
            )
        )

    with risk_col2:

        st.metric(
            label="Risk Score",
            value=f"{overall_score}/100"
        )

    with risk_col3:

        st.markdown(
            f"### {get_risk_emoji(overall_level)} "
            f"{get_risk_label(overall_level, language)}"
        )

        st.progress(
            min(
                overall_score / 100,
                1.0
            )
        )

    # ========================================================
    # RISK SUMMARY
    # ========================================================

    st.markdown(
        f"### {T[lang]['risk_summary']}"
    )

    if overall_level == "Low":

        st.success(
            T[lang]["recommendation_go_text"]
        )

    elif overall_level == "Medium":

        st.warning(
            T[lang]["recommendation_review_text"]
        )

    else:

        st.error(
            T[lang]["recommendation_dont_text"]
        )

    # ========================================================
    # RISK FACTORS
    # ========================================================

    st.markdown(
        f"## {T[lang]['risk_factors']}"
    )

    factors = [
        (
            T[lang]["demand_risk"],
            demand_risk_score,
            demand_level,
            "demand"
        ),
        (
            T[lang]["competition_risk"],
            competition_risk_score,
            competition_level,
            "competition"
        ),
        (
            T[lang]["financial_risk"],
            financial_risk_score,
            financial_level,
            "financial"
        ),
        (
            T[lang]["cost_risk"],
            cost_risk_score,
            cost_level,
            "cost"
        ),
        (
            T[lang]["operational_risk"],
            operational_risk_score,
            operational_level,
            "operational"
        )
    ]

    col1, col2 = st.columns(2)

    for index, (
        factor_name,
        score,
        level,
        factor_key
    ) in enumerate(factors):

        target_col = (
            col1
            if index % 2 == 0
            else col2
        )

        with target_col:

            with st.container(
                border=True
            ):

                st.markdown(
                    f"### {get_risk_emoji(level)} "
                    f"{factor_name}"
                )

                st.progress(
                    min(
                        score / 100,
                        1.0
                    )
                )

                metric_col1, metric_col2 = st.columns(2)

                with metric_col1:

                    st.metric(
                        "Risk Score",
                        f"{score}/100"
                    )

                with metric_col2:

                    st.metric(
                        "Level",
                        get_risk_label(
                            level,
                            language
                        )
                    )

                st.caption(
                    f"**{T[lang]['why']}**"
                )

                st.write(
                    get_factor_message(
                        factor_key,
                        level,
                        language
                    )
                )

    # ========================================================
    # FINANCIAL SAFETY
    # ========================================================

    st.markdown(
        f"## 💰 {T[lang]['financial_risk']}"
    )

    finance_col1, finance_col2, finance_col3 = st.columns(
        3
    )

    with finance_col1:

        st.metric(
            "Monthly Surplus",
            f"₹{monthly_surplus:,.0f}"
        )

    with finance_col2:

        st.metric(
            "Estimated EMI",
            f"₹{emi:,.0f}"
        )

    with finance_col3:

        if loan_amount > 0 and emi > 0:

            coverage = (
                monthly_surplus / emi
            )

            st.metric(
                "Surplus / EMI",
                f"{coverage:.2f}x"
            )

        else:

            st.metric(
                "Loan Burden",
                "None"
            )

    if loan_amount <= 0:

        st.success(
            T[lang]["self_funded_note"]
        )

    elif financial_risk_score >= 80:

        st.error(
            f"🔴 {T[lang]['unsafe_note']}"
        )

    elif financial_risk_score >= 50:

        st.warning(
            f"🟡 {T[lang]['manageable_note']}"
        )

    else:

        st.success(
            f"🟢 {T[lang]['comfortable_note']}"
        )

    # ========================================================
    # KEY WARNINGS
    # ========================================================

    st.markdown(
        f"## ⚠️ {T[lang]['key_warnings']}"
    )

    warnings = []

    if demand_level in [
        "Medium",
        "High",
        "Very High"
    ]:

        warnings.append(
            T[lang]["warning_demand"]
        )

    if competition_level in [
        "Medium",
        "High",
        "Very High"
    ]:

        warnings.append(
            T[lang]["warning_competition"]
        )

    if cost_level in [
        "Medium",
        "High",
        "Very High"
    ]:

        warnings.append(
            T[lang]["warning_cost"]
        )

    if financial_level in [
        "Medium",
        "High",
        "Very High"
    ]:

        warnings.append(
            T[lang]["warning_finance"]
        )

    if loan_amount > 0:

        warnings.append(
            T[lang]["warning_loan"]
        )

    # Always include prototype-data warning.
    warnings.append(
        T[lang]["warning_data"]
    )

    for warning in warnings:

        st.warning(
            f"• {warning}"
        )

    # ========================================================
    # FINAL RECOMMENDATION
    # ========================================================

    st.markdown(
        f"## {T[lang]['recommendation']}"
    )

    recommendation_emoji = get_recommendation_emoji(
        recommendation
    )

    if recommendation == "GO":

        st.success(
            f"{recommendation_emoji} "
            f"**{recommendation}**\n\n"
            f"{recommendation_text}"
        )

    elif recommendation == "REVIEW":

        st.warning(
            f"{recommendation_emoji} "
            f"**{recommendation}**\n\n"
            f"{recommendation_text}"
        )

    else:

        st.error(
            f"{recommendation_emoji} "
            f"**{recommendation} / {T[lang]['start_smaller']}**\n\n"
            f"{recommendation_text}"
        )

    # ========================================================
    # PROTOTYPE / DATA DISCLAIMER
    # ========================================================

    st.info(
        f"ℹ️ **{T[lang]['prototype']}** — "
        f"{T[lang]['data_note']}"
    )

    # ========================================================
    # NAVIGATION
    # ========================================================

    st.markdown("---")

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            T[lang]["back"],
            use_container_width=True
        ):

            st.session_state.page = 5
            st.rerun()

    with continue_col:

        if st.button(
            T[lang]["continue"],
            use_container_width=True
        ):

            st.session_state.page = 7
            st.rerun()
```
