import streamlit as st

st.set_page_config(
    page_title="GramVyapar AI",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 GramVyapar AI")
st.subheader("Know Before You Borrow")

st.write(
    "AI-powered business advisory for rural micro-entrepreneurs."
)

st.divider()

st.header("Tell us about your business")

location = st.text_input(
    "Village / Local Area",
    placeholder="Enter your village"
)

capital = st.number_input(
    "Available Own Capital (₹)",
    min_value=0,
    value=100000,
    step=5000
)

business = st.selectbox(
    "Business Category",
    [
        "Dairy",
        "Bakery",
        "Tailoring",
        "Grocery",
        "Poultry",
        "Food Processing"
    ]
)

if st.button("🔍 Analyze Business", type="primary"):

    st.success("Analysis started!")

    st.write("### Your Inputs")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Location", location or "Not provided")

    with col2:
        st.metric("Own Capital", f"₹{capital:,.0f}")

    with col3:
        st.metric("Business", business)

    st.info(
        "Market intelligence and financial analysis will appear here."
    )
