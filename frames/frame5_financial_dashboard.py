```python
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
            "മൊറട്ടോറിയം, ലോൺ അംഗീ
```
