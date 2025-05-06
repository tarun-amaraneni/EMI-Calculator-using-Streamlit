# EMI Calculator using Streamlit

A web application to calculate Equated Monthly Installment (EMI) using Python Streamlit. This project follows Test-Driven Development (TDD) principles and includes comprehensive unit tests.

## Features

- Calculate EMI based on:
  - Principal loan amount
  - Annual interest rate
  - Loan tenure in years
- Handle edge cases:
  - Zero interest rate
  - Zero principal amount
  - Input validation for negative values
- Display additional loan information:
  - Total interest payable
  - Total payment amount
  - Monthly EMI amount
- Interactive web interface using Streamlit
- Error handling and user feedback
- Input validation with min/max bounds

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tarun-amaraneni/EMI-Calculator-using-Streamlit.git
cd EMI-Calculator-using-Streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Enter your loan details:
   - Principal amount (must be non-negative)
   - Annual interest rate (between 0% and 100%)
   - Loan tenure (minimum 0.1 years)
   
4. Click "Calculate EMI" to see the results

## Development

This project follows Test-Driven Development (TDD) principles. To run the tests:

```bash
python -m pytest tests/ -v
```

## Project Structure

```
EMI-Calculator-using-Streamlit/
├── app.py                 # Streamlit web interface
├── emi_calculator.py      # Core EMI calculation logic
├── tests/
│   └── test_emi_calculator.py  # Unit tests
└── requirements.txt       # Project dependencies
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 