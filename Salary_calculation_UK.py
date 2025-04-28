def calculate_uk_salary(salary):
    # UK Income Tax Bands for 2024-2025
    personal_allowance = 12570  # No tax on income up to this amount
    basic_rate_limit = 50270    # 20% tax rate up to this amount
    higher_rate_limit = 125140  # 40% tax rate up to this amount

    # National Insurance Thresholds for Class 1
    ni_lower_limit = 12570
    ni_upper_limit = 50270

    # Tax calculations
    if salary <= personal_allowance:
        income_tax = 0
    elif salary <= basic_rate_limit:
        income_tax = (salary - personal_allowance) * 0.20
    elif salary <= higher_rate_limit:
        income_tax = (basic_rate_limit - personal_allowance) * 0.20 + (salary - basic_rate_limit) * 0.40
    else:
        income_tax = (basic_rate_limit - personal_allowance) * 0.20 + (higher_rate_limit - basic_rate_limit) * 0.40 + (salary - higher_rate_limit) * 0.45

    # National Insurance (NI) calculations
    if salary <= ni_lower_limit:
        ni_contribution = 0
    elif salary <= ni_upper_limit:
        ni_contribution = (salary - ni_lower_limit) * 0.12
    else:
        ni_contribution = (ni_upper_limit - ni_lower_limit) * 0.12 + (salary - ni_upper_limit) * 0.02

    # Annual and monthly breakdown
    annual_tax = income_tax
    monthly_tax = income_tax / 12
    annual_ni = ni_contribution
    monthly_ni = ni_contribution / 12
    in_hand_salary = salary - annual_tax - annual_ni

    # Display results10001
    print(f"\nGross Annual Salary: £{salary:.2f}")
    print(f"Annual Income Tax: £{annual_tax:.2f} | Monthly: £{monthly_tax:.2f}")
    print(f"Annual National Insurance: £{annual_ni:.2f} | Monthly: £{monthly_ni:.2f}")
    print(f"Annual In-hand Salary: £{in_hand_salary:.2f} | Monthly: £{in_hand_salary / 12:.2f}")


if __name__ == "__main__":
    try:
        salary = float(input("Enter your annual gross salary in GBP: £"))
        calculate_uk_salary(salary)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
