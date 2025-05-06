# EMI Calculator using Streamlit

A web-based EMI (Equated Monthly Installment) calculator built with Python and Streamlit.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.9 or later
- pip3 (Python package installer)

### Installing pip3

If you don't have pip3 installed, follow these steps:

1. For macOS:
   ```bash
   # Install pip3 using curl
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python3 get-pip.py
   ```

2. For Linux:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   ```

3. For Windows:
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"
   - pip3 will be installed automatically with Python

### Installing Streamlit

After installing pip3, install Streamlit using:

```bash
# Install Streamlit
python3 -m pip install --user streamlit

# If you get a "command not found" error after installation, add this to your PATH:
# For macOS/Linux, add to ~/.zshrc or ~/.bashrc:
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
# Then reload your shell:
source ~/.zshrc  # or source ~/.bashrc
```

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd emi-calculator
   ```

2. Install dependencies:
   ```bash
   python3 -m pip install --user -r requirements.txt
   ```

3. Run the application:
   ```bash
   python3 -m streamlit run app.py
   ```

## Features (Planned)
- EMI calculation with principal, interest rate, and tenure
- Interactive web interface using Streamlit
- Input validation and error handling
- Detailed payment schedule

## Project Status
🚧 Under Development

This project is currently under development following Test-Driven Development (TDD) methodology.

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

## Development

This project follows Test-Driven Development (TDD) principles. To run the tests:

```bash
python3 -m pytest tests/ -v
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

