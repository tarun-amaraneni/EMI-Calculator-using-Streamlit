import pytest
from emi_calculator import calculate_emi

def test_calculate_emi_standard_case():
    """
    Test standard EMI calculation with normal values
    """
    principal = 100000
    annual_interest_rate = 10
    loan_tenure_years = 1
    expected_emi = 8791.59  # Approximate value
    assert round(calculate_emi(principal, annual_interest_rate, loan_tenure_years), 2) == expected_emi

def test_zero_principal():
    """
    Test EMI calculation with zero principal amount
    """
    assert calculate_emi(0, 10, 1) == 0

def test_zero_interest():
    """
    Test EMI calculation with zero interest rate
    """
    assert round(calculate_emi(100000, 0, 1), 2) == 8333.33

def test_negative_principal():
    """
    Test EMI calculation with negative principal amount
    """
    with pytest.raises(ValueError, match="Principal amount cannot be negative"):
        calculate_emi(-100000, 10, 1)

def test_negative_interest():
    """
    Test EMI calculation with negative interest rate
    """
    with pytest.raises(ValueError, match="Interest rate cannot be negative"):
        calculate_emi(100000, -10, 1)

def test_zero_tenure():
    """
    Test EMI calculation with zero loan tenure
    """
    with pytest.raises(ValueError, match="Loan tenure must be greater than zero"):
        calculate_emi(100000, 10, 0) 