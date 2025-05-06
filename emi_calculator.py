def calculate_emi(principal, annual_interest_rate, loan_tenure_years):
    """
    Calculate EMI for a loan
    
    Args:
        principal (float): Principal loan amount
        annual_interest_rate (float): Annual interest rate in percentage
        loan_tenure_years (float): Loan tenure in years
    
    Returns:
        float: Monthly EMI amount
    """
    # Convert annual interest rate to monthly
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Convert years to months
    loan_tenure_months = loan_tenure_years * 12
    
    # Basic EMI calculation (this will fail some tests)
    if principal == 0:
        return 0
    
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_months
    emi = emi / ((1 + monthly_interest_rate) ** loan_tenure_months - 1)
    
    return emi 