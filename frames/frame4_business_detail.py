import streamlit as st


# ============================================================
# TRANSLATIONS
# ============================================================

TEXT = {
    "en": {
        "title": "Business Detail",
        "subtitle": (
            "Understand the selected business before moving "
            "to the financial plan."
        ),

        "selected_business": "Selected Business",
        "recommendation_score": "Recommendation Score",
        "why_recommended": "Why This Business Was Recommended",

        "skill_fit": "Your skills match this business.",
        "interest_fit": "Your business interest matches this opportunity.",
        "capital_fit": "Your available capital is suitable for this business.",
        "experience_fit": "Your experience supports this business.",
        "market_fit": "The business has potential demand in the selected market.",

        "local_market": "Local Market Context",
        "district": "District",
        "local_body": "Local Body",
        "ward": "Ward",

        "market_indicators": "Market Indicators",
        "demand": "Demand Potential",
        "competition": "Competition",
        "opportunity": "Opportunity Potential",

        "product_value": "Indicative Product / Service Value",
        "pricing_note": (
            "These are prototype estimates for demonstration purposes. "
            "Actual local prices should be verified before investment."
        ),

        "financial_snapshot": "Business Financial Snapshot",

        "startup_cost": "Estimated Startup Cost",
        "monthly_revenue": "Estimated Monthly Revenue",
        "monthly_expenses": "Estimated Monthly Expenses",
        "monthly_surplus": "Estimated Monthly Surplus",

        "cost_breakdown": "Estimated Startup Cost Breakdown",
        "equipment": "Equipment / Setup",
        "inventory": "Initial Inventory",
        "working_capital": "Working Capital",
        "registration": "Registration / Other",
        "total": "Total",

        "revenue_breakdown": "Estimated Monthly Revenue",
        "sales_quantity": "Estimated Monthly Sales",
        "average_price": "Average Selling Price",
        "revenue": "Estimated Revenue",

        "expense_breakdown": "Estimated Monthly Expenses",
        "raw_material": "Raw Materials",
        "rent": "Rent / Workspace",
        "utilities": "Utilities",
        "transport": "Transport",
        "other_expenses": "Other Expenses",

        "break_even": "Break-even Estimate",
        "break_even_note": (
            "Break-even indicates approximately how much monthly "
            "sales are needed to cover estimated operating costs."
        ),
        "break_even_quantity": "Approximate Break-even Sales",

        "risks": "Key Risks & Caveats",
        "risk_1": "Actual customer demand may differ from the prototype estimate.",
        "risk_2": "Local competitor pricing should be verified before launch.",
        "risk_3": "Raw material and operating costs may change over time.",
        "risk_4": "Business registration and local permissions may be required.",

        "data_confidence": "Data Confidence",
        "prototype": (
            "Prototype / demo estimates are being used for this screen. "
            "They are not verified local market statistics."
        ),

        "selected_note": "Selected from Opportunity Radar",

        "back": "← Back",
        "continue": "Continue to Financial Plan →",
    },

    "ml": {
        "title": "ബിസിനസ് വിശദാംശങ്ങൾ",
        "subtitle": (
            "തിരഞ്ഞെടുത്ത ബിസിനസിനെക്കുറിച്ച് മനസ്സിലാക്കിയ ശേഷം "
            "സാമ്പത്തിക പദ്ധതിയിലേക്ക് പോകാം."
        ),

        "selected_business": "തിരഞ്ഞെടുത്ത ബിസിനസ്",
        "recommendation_score": "ശുപാർശ സ്കോർ",
        "why_recommended": "ഈ ബിസിനസ് ശുപാർശ ചെയ്തതിന്റെ കാരണം",

        "skill_fit": "നിങ്ങളുടെ കഴിവുകൾ ഈ ബിസിനസുമായി പൊരുത്തപ്പെടുന്നു.",
        "interest_fit": "നിങ്ങളുടെ ബിസിനസ് താൽപര്യം ഈ അവസരവുമായി പൊരുത്തപ്പെടുന്നു.",
        "capital_fit": "നിങ്ങളുടെ ലഭ്യമായ മൂലധനം ഈ ബിസിനസിന് അനുയോജ്യമാണ്.",
        "experience_fit": "നിങ്ങളുടെ അനുഭവം ഈ ബിസിനസിനെ പിന്തുണയ്ക്കുന്നു.",
        "market_fit": "തിരഞ്ഞെടുത്ത വിപണിയിൽ ഈ ബിസിനസിന് ഡിമാൻഡ് സാധ്യതയുണ്ട്.",

        "local_market": "പ്രാദേശിക വിപണി വിവരങ്ങൾ",
        "district": "ജില്ല",
        "local_body": "തദ്ദേശ സ്ഥാപനം",
        "ward": "വാർഡ്",

        "market_indicators": "വിപണി സൂചകങ്ങൾ",
        "demand": "ഡിമാൻഡ് സാധ്യത",
        "competition": "മത്സരം",
        "opportunity": "അവസര സാധ്യത",

        "product_value": "സൂചക ഉൽപ്പന്ന / സേവന വില",
        "pricing_note": (
            "ഇവ ഡെമോ ആവശ്യത്തിനുള്ള പ്രോട്ടോടൈപ്പ് കണക്കുകളാണ്. "
            "നിക്ഷേപത്തിന് മുമ്പ് യഥാർത്ഥ പ്രാദേശിക വില പരിശോധിക്കണം."
        ),

        "financial_snapshot": "ബിസിനസ് സാമ്പത്തിക സംഗ്രഹം",

        "startup_cost": "കണക്കാക്കിയ ആരംഭ ചെലവ്",
        "monthly_revenue": "കണക്കാക്കിയ മാസ വരുമാനം",
        "monthly_expenses": "കണക്കാക്കിയ മാസ ചെലവ്",
        "monthly_surplus": "കണക്കാക്കിയ മാസ മിച്ചം",

        "cost_breakdown": "കണക്കാക്കിയ ആരംഭ ചെലവ് വിഭജനം",
        "equipment": "ഉപകരണങ്ങൾ / സജ്ജീകരണം",
        "inventory": "ആദ്യ സ്റ്റോക്ക്",
        "working_capital": "പ്രവർത്തന മൂലധനം",
        "registration": "രജിസ്ട്രേഷൻ / മറ്റ് ചെലവുകൾ",
        "total": "ആകെ",

        "revenue_breakdown": "കണക്കാക്കിയ മാസ വരുമാനം",
        "sales_quantity": "കണക്കാക്കിയ മാസ വിൽപ്പന",
        "average_price": "ശരാശരി വിൽപ്പന വില",
        "revenue": "കണക്കാക്കിയ വരുമാനം",

        "expense_breakdown": "കണക്കാക്കിയ മാസ ചെലവ്",
        "raw_material": "അസംസ്കൃത വസ്തുക്കൾ",
        "rent": "വാടക / ജോലി സ്ഥലം",
        "utilities": "വൈദ്യുതി / വെള്ളം / മറ്റ് യൂട്ടിലിറ്റികൾ",
        "transport": "ഗതാഗതം",
        "other_expenses": "മറ്റ് ചെലവുകൾ",

        "break_even": "ബ്രേക്ക്-ഈവൻ കണക്ക്",
        "break_even_note": (
            "കണക്കാക്കിയ പ്രവർത്തന ചെലവുകൾ നികത്താൻ ആവശ്യമായ "
            "ഏകദേശ മാസ വിൽപ്പനയാണ് ബ്രേക്ക്-ഈവൻ."
        ),
        "break_even_quantity": "ഏകദേശ ബ്രേക്ക്-ഈവൻ വിൽപ്പന",

        "risks": "പ്രധാന റിസ്കുകളും ശ്രദ്ധിക്കേണ്ട കാര്യങ്ങളും",
        "risk_1": "യഥാർത്ഥ ഉപഭോക്തൃ ഡിമാൻഡ് ഡെമോ കണക്കിൽ നിന്ന് വ്യത്യസ്തമായേക്കാം.",
        "risk_2": "ആരംഭിക്കുന്നതിന് മുമ്പ് പ്രാദേശിക മത്സരക്കാരുടെ വില പരിശോധിക്കണം.",
        "risk_3": "അസംസ്കൃത വസ്തുക്കളുടെയും പ്രവർത്തന ചെലവുകളുടെയും വില മാറാം.",
        "risk_4": "ബിസിനസ് രജിസ്ട്രേഷനും പ്രാദേശിക അനുമതികളും ആവശ്യമായേക്കാം.",

        "data_confidence": "ഡാറ്റാ വിശ്വാസ്യത",
        "prototype": (
            "ഈ സ്ക്രീനിൽ പ്രോട്ടോടൈപ്പ് / ഡെമോ കണക്കുകളാണ് ഉപയോഗിക്കുന്നത്. "
            "ഇവ പരിശോധിച്ച പ്രാദേശിക വിപണി കണക്കുകളല്ല."
        ),

        "selected_note": "Opportunity Radar-ൽ നിന്ന് തിരഞ്ഞെടുത്തത്",

        "back": "← പിന്നിലേക്ക്",
        "continue": "സാമ്പത്തിക പദ്ധതിയിലേക്ക് തുടരുക →",
    },
}


# ============================================================
# BUSINESS FINANCIAL DATA
# Prototype / demo estimates only
# ============================================================

BUSINESS_DATA = {

    "Bakery / Food": {
        "name_ml": "ബേക്കറി / ഭക്ഷ്യ ബിസിനസ്",

        "demand": 82,
        "competition": 62,
        "opportunity": 78,

        "price": 80,
        "price_unit": "average product/service unit",

        "startup": {
            "equipment": 70000,
            "inventory": 30000,
            "working_capital": 25000,
            "registration": 10000,
        },

        "monthly": {
            "sales_quantity": 900,
            "raw_material": 28000,
            "rent": 8000,
            "utilities": 5000,
            "transport": 4000,
            "other_expenses": 5000,
        },
    },

    "Tailoring": {
        "name_ml": "ടെയിലറിംഗ്",

        "demand": 76,
        "competition": 68,
        "opportunity": 82,

        "price": 500,
        "price_unit": "average order",

        "startup": {
            "equipment": 45000,
            "inventory": 12000,
            "working_capital": 15000,
            "registration": 5000,
        },

        "monthly": {
            "sales_quantity": 110,
            "raw_material": 18000,
            "rent": 5000,
            "utilities": 2500,
            "transport": 2000,
            "other_expenses": 3000,
        },
    },

    "Dairy": {
        "name_ml": "ക്ഷീര / ഡയറി ബിസിനസ്",

        "demand": 72,
        "competition": 58,
        "opportunity": 70,

        "price": 60,
        "price_unit": "average litre/product unit",

        "startup": {
            "equipment": 90000,
            "inventory": 30000,
            "working_capital": 50000,
            "registration": 10000,
        },

        "monthly": {
            "sales_quantity": 2500,
            "raw_material": 65000,
            "rent": 7000,
            "utilities": 5000,
            "transport": 8000,
            "other_expenses": 7000,
        },
    },
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_business_name(business_key, language):
    data = BUSINESS_DATA.get(business_key)

    if not data:
        return business_key

    if language == "ml":
        return data["name_ml"]

    return business_key


def calculate_financials(data):

    startup = data["startup"]
    monthly = data["monthly"]

    startup_total = (
        startup["equipment"]
        + startup["inventory"]
        + startup["working_capital"]
        + startup["registration"]
    )

    monthly_revenue = (
        monthly["sales_quantity"]
        * data["price"]
    )

    monthly_expenses = (
        monthly["raw_material"]
        + monthly["rent"]
        + monthly["utilities"]
        + monthly["transport"]
        + monthly["other_expenses"]
    )

    monthly_surplus = (
        monthly_revenue
        - monthly_expenses
    )

    # Approximate contribution after raw material cost
    contribution_per_unit = (
        data["price"]
        - (
            monthly["raw_material"]
            / monthly["sales_quantity"]
        )
    )

    fixed_costs = (
        monthly["rent"]
        + monthly["utilities"]
        + monthly["transport"]
        + monthly["other_expenses"]
    )

    if contribution_per_unit > 0:

        break_even_quantity = (
            fixed_costs
            / contribution_per_unit
        )

    else:

        break_even_quantity = 0

    return {
        "startup_total": round(startup_total),
        "monthly_revenue": round(monthly_revenue),
        "monthly_expenses": round(monthly_expenses),
        "monthly_surplus": round(monthly_surplus),
        "break_even_quantity": round(
            break_even_quantity
        ),
    }


# ============================================================
# MAIN FRAME
# ============================================================

def render_frame4():

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
    # GET SELECTED BUSINESS
    # --------------------------------------------------------

    selected_business = st.session_state.get(
        "selected_business",
        None
    )

    # --------------------------------------------------------
    # SAFETY CHECK
    # --------------------------------------------------------

    if not selected_business:

        st.warning(
            "Please select a business from Opportunity Radar."
            if language == "en"
            else
            "Opportunity Radar-ൽ നിന്ന് ഒരു ബിസിനസ് തിരഞ്ഞെടുക്കുക."
        )

        if st.button(
            t["back"],
            use_container_width=True,
            key="frame4_missing_back",
        ):

            st.session_state.page = 3
            st.rerun()

        return

    # --------------------------------------------------------
    # BUSINESS DATA CHECK
    # --------------------------------------------------------

    if selected_business not in BUSINESS_DATA:

        st.error(
            "Business data is not available for this prototype."
            if language == "en"
            else
            "ഈ പ്രോട്ടോടൈപ്പിൽ ഈ ബിസിനസിനുള്ള ഡാറ്റ ലഭ്യമല്ല."
        )

        if st.button(
            t["back"],
            use_container_width=True,
            key="frame4_data_back",
        ):

            st.session_state.page = 3
            st.rerun()

        return

    data = BUSINESS_DATA[
        selected_business
    ]

    # --------------------------------------------------------
    # CALCULATE FINANCIALS
    # --------------------------------------------------------

    financials = calculate_financials(
        data
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

    business_name = get_business_name(
        selected_business,
        language
    )

    st.success(
        f"✓ {t['selected_business']}: "
        f"**{business_name}**"
    )

    st.caption(
        t["selected_note"]
    )

    st.write("")

    # --------------------------------------------------------
    # RECOMMENDATION SCORE
    # --------------------------------------------------------

    selected_score = st.session_state.get(
        "selected_business_score",
        0
    )

    score_col1, score_col2 = st.columns(
        [1, 3]
    )

    with score_col1:

        st.metric(
            t["recommendation_score"],
            f"{selected_score}/100"
        )

    with score_col2:

        st.progress(
            selected_score / 100
        )

    st.write("")

    # --------------------------------------------------------
    # WHY RECOMMENDED
    # --------------------------------------------------------

    st.markdown(
        f"### {t['why_recommended']}"
    )

    reason_col1, reason_col2 = st.columns(2)

    with reason_col1:

        st.info(
            f"✓ {t['skill_fit']}"
        )

        st.info(
            f"✓ {t['capital_fit']}"
        )

        st.info(
            f"✓ {t['experience_fit']}"
        )

    with reason_col2:

        st.info(
            f"✓ {t['interest_fit']}"
        )

        st.info(
            f"✓ {t['market_fit']}"
        )

    st.write("")

    # --------------------------------------------------------
    # LOCAL MARKET
    # --------------------------------------------------------

    st.markdown(
        f"### {t['local_market']}"
    )

    location_col1, location_col2, location_col3 = st.columns(3)

    with location_col1:

        st.write(
            f"**{t['district']}**"
        )

        st.write(
            st.session_state.get(
                "district",
                "-"
            )
        )

    with location_col2:

        st.write(
            f"**{t['local_body']}**"
        )

        st.write(
            st.session_state.get(
                "local_body",
                "-"
            )
        )

    with location_col3:

        st.write(
            f"**{t['ward']}**"
        )

        st.write(
            st.session_state.get(
                "ward",
                "-"
            )
        )

    st.write("")

    # --------------------------------------------------------
    # MARKET INDICATORS
    # --------------------------------------------------------

    st.markdown(
        f"### {t['market_indicators']}"
    )

    market_col1, market_col2, market_col3 = st.columns(3)

    with market_col1:

        st.metric(
            t["demand"],
            f"{data['demand']}%"
        )

        st.progress(
            data["demand"] / 100
        )

    with market_col2:

        st.metric(
            t["competition"],
            f"{data['competition']}%"
        )

        st.progress(
            data["competition"] / 100
        )

    with market_col3:

        st.metric(
            t["opportunity"],
            f"{data['opportunity']}%"
        )

        st.progress(
            data["opportunity"] / 100
        )

    st.write("")

    # --------------------------------------------------------
    # PRODUCT / SERVICE VALUE
    # --------------------------------------------------------

    st.markdown(
        f"### {t['product_value']}"
    )

    st.metric(
        "₹",
        f"₹{data['price']:,.0f}"
    )

    st.caption(
        t["pricing_note"]
    )

    st.write("")

    # --------------------------------------------------------
    # FINANCIAL SNAPSHOT
    # --------------------------------------------------------

    st.markdown(
        f"### {t['financial_snapshot']}"
    )

    financial_col1, financial_col2 = st.columns(2)

    with financial_col1:

        st.metric(
            t["startup_cost"],
            f"₹{financials['startup_total']:,.0f}"
        )

        st.metric(
            t["monthly_revenue"],
            f"₹{financials['monthly_revenue']:,.0f}"
        )

    with financial_col2:

        st.metric(
            t["monthly_expenses"],
            f"₹{financials['monthly_expenses']:,.0f}"
        )

        surplus = financials["monthly_surplus"]

        st.metric(
            t["monthly_surplus"],
            f"₹{surplus:,.0f}"
        )

    st.write("")

    # --------------------------------------------------------
    # STARTUP COST BREAKDOWN
    # --------------------------------------------------------

    st.markdown(
        f"### {t['cost_breakdown']}"
    )

    startup = data["startup"]

    cost_col1, cost_col2 = st.columns(2)

    with cost_col1:

        st.write(
            f"**{t['equipment']}**"
        )

        st.write(
            f"₹{startup['equipment']:,.0f}"
        )

        st.write(
            f"**{t['inventory']}**"
        )

        st.write(
            f"₹{startup['inventory']:,.0f}"
        )

    with cost_col2:

        st.write(
            f"**{t['working_capital']}**"
        )

        st.write(
            f"₹{startup['working_capital']:,.0f}"
        )

        st.write(
            f"**{t['registration']}**"
        )

        st.write(
            f"₹{startup['registration']:,.0f}"
        )

    st.success(
        f"**{t['total']}: "
        f"₹{financials['startup_total']:,.0f}**"
    )

    st.write("")

    # --------------------------------------------------------
    # MONTHLY REVENUE
    # --------------------------------------------------------

    st.markdown(
        f"### {t['revenue_breakdown']}"
    )

    monthly = data["monthly"]

    revenue_col1, revenue_col2 = st.columns(2)

    with revenue_col1:

        st.write(
            f"**{t['sales_quantity']}**"
        )

        st.write(
            f"{monthly['sales_quantity']:,}"
        )

    with revenue_col2:

        st.write(
            f"**{t['average_price']}**"
        )

        st.write(
            f"₹{data['price']:,.0f}"
        )

    st.info(
        f"**{t['revenue']}: "
        f"₹{financials['monthly_revenue']:,.0f}**"
    )

    st.write("")

    # --------------------------------------------------------
    # MONTHLY EXPENSES
    # --------------------------------------------------------

    st.markdown(
        f"### {t['expense_breakdown']}"
    )

    expense_col1, expense_col2 = st.columns(2)

    with expense_col1:

        st.write(
            f"**{t['raw_material']}**"
        )

        st.write(
            f"₹{monthly['raw_material']:,.0f}"
        )

        st.write(
            f"**{t['rent']}**"
        )

        st.write(
            f"₹{monthly['rent']:,.0f}"
        )

        st.write(
            f"**{t['utilities']}**"
        )

        st.write(
            f"₹{monthly['utilities']:,.0f}"
        )

    with expense_col2:

        st.write(
            f"**{t['transport']}**"
        )

        st.write(
            f"₹{monthly['transport']:,.0f}"
        )

        st.write(
            f"**{t['other_expenses']}**"
        )

        st.write(
            f"₹{monthly['other_expenses']:,.0f}"
        )

    st.write("")

    # --------------------------------------------------------
    # BREAK EVEN
    # --------------------------------------------------------

    st.markdown(
        f"### {t['break_even']}"
    )

    st.metric(
        t["break_even_quantity"],
        f"{financials['break_even_quantity']:,}"
    )

    st.caption(
        t["break_even_note"]
    )

    st.write("")

    # --------------------------------------------------------
    # RISKS
    # --------------------------------------------------------

    st.markdown(
        f"### {t['risks']}"
    )

    st.warning(
        f"• {t['risk_1']}\n\n"
        f"• {t['risk_2']}\n\n"
        f"• {t['risk_3']}\n\n"
        f"• {t['risk_4']}"
    )

    st.write("")

    # --------------------------------------------------------
    # DATA CONFIDENCE
    # --------------------------------------------------------

    st.markdown(
        f"### {t['data_confidence']}"
    )

    st.warning(
        t["prototype"]
    )

    st.write("")

    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    back_col, continue_col = st.columns(2)

    with back_col:

        if st.button(
            t["back"],
            use_container_width=True,
            key="back_frame4",
        ):

            st.session_state.page = 3
            st.rerun()

    with continue_col:

        if st.button(
            t["continue"],
            type="primary",
            use_container_width=True,
            key="continue_frame4",
        ):

            st.session_state.page = 5
            st.rerun()
