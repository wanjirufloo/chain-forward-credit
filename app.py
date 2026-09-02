import streamlit as st
import joblib
import pandas as pd


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

model = joblib.load("logistic_model.pkl")


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Forward Fintech Credit Risk",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# DASHBOARD HEADER
# =========================================================

st.markdown(
    """
    <div style="
        background-color:#12355B;
        padding:20px;
        border-radius:10px;
        margin-bottom:20px;
    ">
        <h1 style="color:white; margin:0;">
            Forward Fintech
        </h1>
        <p style="color:white; margin:5px 0 0 0;">
            Chain Forward Credit Risk Dashboard
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.title("Forward Fintech")
st.sidebar.write("Chain Forward Risk Dashboard")

page = st.sidebar.radio(
    "Navigate to",
    [
        "Overview",
        "Portfolio Risk",
        "Default Prediction",
        "Financial Scenarios",
        "Pricing"
    ]
)


# =========================================================
# OVERVIEW
# =========================================================

if page == "Overview":

    st.title("Chain Forward")

    st.subheader(
        "Credit Risk & Financial Viability Assessment"
    )

    st.write(
        "A risk analytics dashboard for evaluating MSME credit risk, "
        "portfolio profitability, and lending decisions."
    )

    st.header("Executive Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Active Borrowers",
            "20,000"
        )

    with col2:
        st.metric(
            "Monthly Interest Income",
            "$160,000"
        )

    with col3:
        st.metric(
            "Base Default Rate",
            "6.0%"
        )

    with col4:
        st.metric(
            "Break-even Default Rate",
            "0.5%"
        )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Monthly Expected Credit Loss",
            "$360,000"
        )

    with col2:
        st.metric(
            "Monthly Profit",
            "-$330,000"
        )

    with col3:
        st.metric(
            "3-Year ROI",
            "-264%"
        )

    st.warning(
        "Under the illustrative assumptions used in this analysis, "
        "Chain Forward is not financially viable at the projected "
        "6% default rate."
    )


# =========================================================
# PORTFOLIO RISK
# =========================================================

elif page == "Portfolio Risk":

    st.title("Portfolio Risk")

    st.header("Customer Risk Segmentation")

    st.write(
        "Customers were segmented using K-Means clustering based on "
        "transaction, repayment, business, and concentration characteristics."
    )

    segment_data = {
        "Risk Segment": [
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ],
        "Customers": [
            1471,
            6128,
            2401
        ],
        "Default Rate": [
            4.21,
            5.22,
            8.45
        ]
    }

    segment_df = pd.DataFrame(segment_data)

    st.dataframe(
        segment_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Default Rate by Risk Segment")

    st.bar_chart(
        segment_df.set_index(
            "Risk Segment"
        )["Default Rate"]
    )

    st.subheader("Segment Risk Profiles")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### Low Risk")

        st.write(
            "Default rate: **4.21%**"
        )

        st.write(
            "Typically characterized by longer business histories, "
            "stronger revenue and mobile money activity, and fewer "
            "previous defaults."
        )

    with col2:

        st.markdown("### Medium Risk")

        st.write(
            "Default rate: **5.22%**"
        )

        st.write(
            "The largest segment, representing moderate overall "
            "credit risk in the simulated portfolio."
        )

    with col3:

        st.markdown("### High Risk")

        st.write(
            "Default rate: **8.45%**"
        )

        st.write(
            "Characterized primarily by more previous defaults and "
            "shorter business histories."
        )

    st.info(
        "Risk segments are descriptive portfolio groups created using "
        "K-Means. Cluster numbers themselves do not represent risk levels."
    )

    st.divider()

    st.header("Early Warning Indicators")

    warning_data = pd.DataFrame({
        "Indicator": [
            "Loan-to-Revenue Ratio",
            "Days Overdue",
            "Previous Defaults",
            "Transaction Volatility",
            "Repayment History",
            "Cash Flow Growth",
            "Supplier Default Exposure",
            "Buyer Concentration"
        ],
        "Risk Direction": [
            "Higher = Higher Risk",
            "Higher = Higher Risk",
            "Higher = Higher Risk",
            "Higher = Higher Risk",
            "Higher = Lower Risk",
            "Higher = Lower Risk",
            "Higher = Higher Risk",
            "Higher = Higher Risk"
        ]
    })

    st.dataframe(
        warning_data,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "The strongest model indicators were loan-to-revenue ratio, "
        "days overdue, previous defaults, and transaction volatility."
    )


# =========================================================
# DEFAULT PREDICTION
# =========================================================

elif page == "Default Prediction":

    st.title("Default Risk Prediction")

    st.write(
        "Enter borrower characteristics to estimate the probability "
        "of loan default."
    )

    st.info(
        "The model was trained using the simulated portfolio data "
        "developed for this assessment."
    )

    # -----------------------------------------------------
    # BORROWER INFORMATION
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.number_input(
            "Age",
            min_value=25,
            max_value=55,
            value=35
        )

        roles = st.selectbox(
            "Value Chain Role",
            [
                "Buyer",
                "Supplier",
                "Distributor",
                "Retailer"
            ]
        )

        country = st.selectbox(
            "Country",
            [
                "Kenya",
                "Uganda",
                "Nigeria",
                "Ghana"
            ]
        )

        business_sector = st.selectbox(
            "Business Sector",
            [
                "Agriculture",
                "Retail",
                "Manufacturing",
                "Services"
            ]
        )

        business_age_years = st.number_input(
            "Business Age (years)",
            min_value=0.5,
            max_value=30.0,
            value=5.0
        )

    with col2:

        loan_amount_usd = st.number_input(
            "Loan Amount (USD)",
            min_value=1.0,
            value=500.0
        )

        loan_duration_days = st.number_input(
            "Loan Duration (days)",
            min_value=7,
            max_value=90,
            value=30
        )

        monthly_revenue_usd = st.number_input(
            "Monthly Revenue (USD)",
            min_value=1.0,
            value=1500.0
        )

        transaction_volatility = st.slider(
            "Transaction Volatility",
            0.0,
            1.0,
            0.5
        )

        repayment_history = st.slider(
            "Repayment History",
            0.5,
            1.0,
            0.8
        )

    with col3:

        days_overdue = st.number_input(
            "Days Overdue",
            min_value=0.0,
            max_value=90.0,
            value=0.0
        )

        monthly_cash_flow_growth = st.slider(
            "Monthly Cash Flow Growth",
            -0.5,
            0.5,
            0.05
        )

        mobile_money_volume = st.number_input(
            "Mobile Money Volume (USD)",
            min_value=0.0,
            value=1000.0
        )

        loan_frequency = st.number_input(
            "Loan Frequency",
            min_value=1,
            max_value=12,
            value=3
        )

        previous_loans = st.number_input(
            "Previous Loans",
            min_value=0,
            max_value=10,
            value=2
        )

        previous_defaults = st.number_input(
            "Previous Defaults",
            min_value=0,
            max_value=5,
            value=0
        )

        supplier_default_flag = st.selectbox(
            "Supplier Default Flag",
            [0, 1]
        )

        buyer_concentration = st.slider(
            "Buyer Concentration",
            0.1,
            1.0,
            0.5
        )

    # -----------------------------------------------------
    # DERIVED FEATURE
    # -----------------------------------------------------

    loan_to_revenue = (
        loan_amount_usd /
        monthly_revenue_usd
    )

    # -----------------------------------------------------
    # MODEL INPUT
    # -----------------------------------------------------

    input_data = pd.DataFrame({
        "age": [age],
        "roles": [roles],
        "country": [country],
        "business_age_years": [business_age_years],
        "business_sector": [business_sector],
        "loan_amount_usd": [loan_amount_usd],
        "loan_duration_days": [loan_duration_days],
        "monthly_revenue_usd": [monthly_revenue_usd],
        "transaction_volatility": [transaction_volatility],
        "repayment_history": [repayment_history],
        "days_overdue": [days_overdue],
        "monthly_cash_flow_growth": [
            monthly_cash_flow_growth
        ],
        "mobile_money_volume": [
            mobile_money_volume
        ],
        "loan_frequency": [loan_frequency],
        "previous_loans": [previous_loans],
        "previous_defaults": [previous_defaults],
        "supplier_default_flag": [
            supplier_default_flag
        ],
        "buyer_concentration": [
            buyer_concentration
        ],
        "loan_to_revenue": [
            loan_to_revenue
        ]
    })

    st.divider()

    if st.button(
        "Predict Default Risk",
        type="primary"
    ):

        probability = model.predict_proba(
            input_data
        )[0, 1]

        st.subheader("Prediction Result")

        st.metric(
            "Predicted Default Probability",
            f"{probability:.1%}"
        )

        if probability >= 0.87:

            st.error(
                "HIGH RISK — Flag borrower for further credit review."
            )

        else:

            st.success(
                "LOWER RISK — Borrower is below the review threshold."
            )

        st.caption(
            "Review threshold: 0.87, selected during model evaluation "
            "using F1-score."
        )


# =========================================================
# FINANCIAL SCENARIOS
# =========================================================

elif page == "Financial Scenarios":

    st.title("Financial Scenario Analysis")

    st.write(
        "This section compares expected profitability under "
        "different default-rate scenarios."
    )

    # -----------------------------------------------------
    # SCENARIO ANALYSIS
    # -----------------------------------------------------

    scenario_df = pd.DataFrame({
        "Scenario": [
            "Optimistic",
            "Base Case",
            "Pessimistic"
        ],
        "Default Rate": [
            0.04,
            0.06,
            0.08
        ],
        "Expected Credit Loss": [
            240000,
            360000,
            480000
        ],
        "Monthly Profit": [
            -210000,
            -330000,
            -450000
        ]
    })

    scenario_df["3-Year Operating Profit"] = (
        scenario_df["Monthly Profit"] * 36
    )

    scenario_df["Net Outcome After Investment"] = (
        scenario_df["3-Year Operating Profit"] - 4500000
    )

    st.dataframe(
        scenario_df.style.format({
            "Default Rate": "{:.1%}",
            "Expected Credit Loss": "${:,.0f}",
            "Monthly Profit": "${:,.0f}",
            "3-Year Operating Profit": "${:,.0f}",
            "Net Outcome After Investment": "${:,.0f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Monthly Profit")

    st.bar_chart(
        scenario_df.set_index(
            "Scenario"
        )["Monthly Profit"]
    )

    st.warning(
        "All three scenarios result in negative monthly profit "
        "under the illustrative assumptions."
    )

    st.subheader("Break-even Default Rate")

    st.metric(
        "Break-even Default Rate",
        "0.5%"
    )

    st.write(
        "The product reaches monthly break-even when the default rate "
        "is approximately 0.5%. The projected 6% default rate is therefore "
        "well above the break-even level."
    )


# =========================================================
# RISK-BASED PRICING
# =========================================================

elif page == "Pricing":

    st.title("Risk-Based Pricing")

    st.write(
        "Pricing recommendations based on expected credit losses, "
        "funding costs, operating costs, and target margin."
    )

    # -----------------------------------------------------
    # PRICING DATA
    # -----------------------------------------------------

    pricing_df = pd.DataFrame({
        "Risk Segment": [
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ],
        "Default Rate": [
            0.0421,
            0.0522,
            0.0845
        ],
        "Recommended Monthly Income": [
            23.93,
            27.71,
            39.83
        ]
    })

    st.dataframe(
        pricing_df.style.format({
            "Default Rate": "{:.1%}",
            "Recommended Monthly Income": "${:,.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Recommended Pricing")

    st.bar_chart(
        pricing_df.set_index(
            "Risk Segment"
        )["Recommended Monthly Income"]
    )

    st.info(
        "Higher-risk borrowers require higher expected income to "
        "compensate for greater expected credit losses. These figures "
        "are illustrative monthly income requirements, not quoted "
        "interest rates."
    )