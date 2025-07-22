def check_loan_eligibility():
    print("=== Loan Eligibility Checker ===")
    
    age = int(input("Enter your age: "))
    income = float(input("Enter your monthly income (in ₹): "))
    credit_score = int(input("Enter your credit score (300 - 900): "))
    employment = input("Are you employed? (yes/no): ").lower()
    
    # Eligibility conditions
    if age >= 21 and income >= 25000 and credit_score >= 650 and employment == "yes":
        print("✅ You are eligible for a loan.")
    else:
        print("❌ Sorry, you are not eligible for a loan.")
    
# Run the function
check_loan_eligibility()
