import streamlit as st
from emi_calculator import calculate_emi

st.title("EMI Calculator")
st.write("Calculate your Equated Monthly Installment (EMI)")

# Input fields
principal = st.number_input("Principal Loan Amount (₹)", min_value=0.0, value=100000.0, step=1000.0)
annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
loan_tenure_years = st.number_input("Loan Tenure (Years)", min_value=0.1, value=1.0, step=0.5)

# Calculate button
if st.button("Calculate EMI"):
    try:
        emi = calculate_emi(principal, annual_interest_rate, loan_tenure_years)
        st.success(f"Your Monthly EMI: ₹{emi:.2f}")
        
        # Additional information
        total_payment = emi * loan_tenure_years * 12
        total_interest = total_payment - principal
        
        # Display loan details
        st.write("### Loan Details")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Interest", f"₹{total_interest:.2f}")
        with col2:
            st.metric("Total Payment", f"₹{total_payment:.2f}")
        with col3:
            st.metric("Monthly EMI", f"₹{emi:.2f}")
            
    except ValueError as e:
        st.error(f"Error: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

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