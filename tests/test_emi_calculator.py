import pytest

def test_calculate_emi_standard_case():
    """
    Test standard EMI calculation with normal values
    """
    from emi_calculator import calculate_emi
    principal = 100000
    annual_interest_rate = 10
    loan_tenure_years = 1
    expected_emi = 8791.59  # Approximate value
    assert round(calculate_emi(principal, annual_interest_rate, loan_tenure_years), 2) == expected_emi

def test_zero_principal():
    """
    Test EMI calculation with zero principal amount
    """
    from emi_calculator import calculate_emi
    assert calculate_emi(0, 10, 1) == 0

def test_zero_interest():
    """
    Test EMI calculation with zero interest rate
    """
    from emi_calculator import calculate_emi
    assert round(calculate_emi(100000, 0, 1), 2) == 8333.33 