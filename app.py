import streamlit as st
from emi_calculator import calculate_emi

st.title("EMI Calculator")
st.write("Calculate your Equated Monthly Installment (EMI)")

# Input fields
principal = st.number_input("Principal Loan Amount (₹)", value=100000.0, step=1000.0)
annual_interest_rate = st.number_input("Annual Interest Rate (%)", value=10.0, step=0.1)
loan_tenure_years = st.number_input("Loan Tenure (Years)", value=1.0, step=0.5)

# Calculate button
if st.button("Calculate EMI"):
    emi = calculate_emi(principal, annual_interest_rate, loan_tenure_years)
    st.success(f"Your Monthly EMI: ₹{emi:.2f}")

# Add some information about EMI calculation
st.write("### How is EMI calculated?")
st.write("""
The EMI is calculated using the formula:
```
EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
```
where:
- P = Principal loan amount
- r = Monthly interest rate (Annual rate ÷ 12 ÷ 100)
- n = Total number of months (Years × 12)
""") 