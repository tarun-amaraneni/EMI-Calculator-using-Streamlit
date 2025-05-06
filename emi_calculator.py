def calculate_emi(principal, annual_interest_rate, loan_tenure_years):
    """
    Calculate EMI for a loan
    
    Args:
        principal (float): Principal loan amount
        annual_interest_rate (float): Annual interest rate in percentage
        loan_tenure_years (float): Loan tenure in years
    
    Returns:
        float: Monthly EMI amount
        
    Raises:
        ValueError: If any input parameters are invalid
    """
    # Input validation
    if principal < 0:
        raise ValueError("Principal amount cannot be negative")
    if annual_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if loan_tenure_years <= 0:
        raise ValueError("Loan tenure must be greater than zero")
    
    if principal == 0:
        return 0
        
    # Convert years to months
    loan_tenure_months = loan_tenure_years * 12
    
    # Handle zero interest rate case
    if annual_interest_rate == 0:
        return principal / loan_tenure_months
        
    # Convert annual interest rate to monthly
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # EMI calculation
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_months
    emi = emi / ((1 + monthly_interest_rate) ** loan_tenure_months - 1)
    
    return emi 