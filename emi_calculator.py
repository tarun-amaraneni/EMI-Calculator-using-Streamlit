def calculate_emi(principal, annual_interest_rate, loan_tenure_years):
    """
    Basic EMI calculator implementation
    """
    # Convert annual interest rate to monthly
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Convert years to months
    loan_tenure_months = loan_tenure_years * 12
    
    # Basic EMI calculation (without validation)
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_months
    emi = emi / ((1 + monthly_interest_rate) ** loan_tenure_months - 1)
    
    return emi 