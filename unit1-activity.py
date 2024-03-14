# Clinton Chieng
# March 5, 2024
# Yearly Income Calculator

def calculate_yearly_income(hourly_rate, hours_worked_per_week, weeks_worked_per_year):

    # Calculate the yearly income based on hourly rate, hours worked per week, and weeks worked per year.

    weekly_income = hourly_rate * hours_worked_per_week
    yearly_income = weekly_income * weeks_worked_per_year
    return yearly_income

def main():
    print("Welcome to the Yearly Income Calculator!")

    # Ask data from client
    hourly_rate = float(input("Enter your hourly rate: $"))
    hours_worked_per_week = float(input("Enter the number of hours you work per week: "))
    weeks_worked_per_year = float(input("Enter the number of weeks you work per year: "))

    # Calculate income
    yearly_income = calculate_yearly_income(hourly_rate, hours_worked_per_week, weeks_worked_per_year)

    # give out income
    print(f"Your yearly income is: ${yearly_income}")

    # respond to client about yearly income.
    if yearly_income < 30000:
        print("You might want to consider finding additional sources of income.")
    elif yearly_income >= 35000 and yearly_income < 70000:
        print("You're doing well, but there's room for improvement.")
    else:
        print("Congratulations! You're earning a comfortable income.")

if __name__ == "__main__":
    main()
