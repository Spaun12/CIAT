#LiveSession 2 Week 4 Program 5-15 Mikes edit

CONTRIBUTION_RATE = 0.05

def main():
    # Get the gross pay and bonus from the user
    gross_pay = float(input('this is your retirment investment calculator. Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))

    # Prompt the user to input the contribution rate for bonuses
    while True:
        try:
            bonus_rate = float(input("Enter the contribution rate for bonuses (0-15): "))
            if bonus_rate > 15 or bonus_rate < 0:
                raise ValueError("Invalid value")
            break
        except ValueError as e:
            print("Invalid input. Please enter a number between 0 and 15.")
            continue
    
    #round the input to nearest 0.5
    bonus_rate = round(bonus_rate * 2) / 2
    bonus_rate = bonus_rate/100
    
    # check if the bonus is above a certain amount and increase the contribution rate
    threshold = float(input("Enter the threshold amount of bonus: "))
    bonus_rate_high = bonus_rate
    if bonus > threshold:
        bonus_rate_high = float(input("Enter the contribution rate for high bonuses (0-15): "))
        bonus_rate_high = round(bonus_rate_high * 2) / 2
        bonus_rate_high = bonus_rate_high/100
    
    # Show display the retirement contribution for the gross pay
    show_pay_contribution(gross_pay)

    # Show the retirement contribution for the bonus
    show_bonus_contribution(bonus, bonus_rate, bonus_rate_high, threshold)

# The calculate_pay_contribution function accepts the gross
# pay as an argument and returns the retirement
# contribution for that amount of pay.
def show_pay_contribution(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f'Contribution for gross pay: ${contrib:,.2f}.')

# The calculate_bonus_contribution function accepts the
# bonus amount and the bonus rate as arguments and returns the
# retirement contribution for that amount of pay.
def show_bonus_contribution(bonus, rate, high_rate, threshold):
    if bonus > threshold:
        contrib = bonus * high_rate
    else:
        contrib = bonus * rate
    print(f'Contribution for bonuses: ${contrib:,.2f}.')

if __name__ == "__main__":
    main()

