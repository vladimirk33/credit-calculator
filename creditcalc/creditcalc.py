# write your code here
import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="choose the mode: annuity or diff")
parser.add_argument("--principal", help="takes credit principal", type=int)
parser.add_argument("--periods", help="takes periods (months)", type=int)
parser.add_argument("--interest", help="takes rate interest", type=float)
parser.add_argument("--payment", help="takes monthly payment", type=int)
args = parser.parse_args()
if args.type == "diff":
    if args.principal and args.periods and args.interest:
        credit_principal = args.principal
        months = args.periods
        credit_interest = args.interest
        response = "diff"
    else:
        print("Incorrect parameters")
        sys.exit()
elif args.type == "annuity":
    if args.principal and args.periods and args.interest:
        credit_principal = args.principal
        months = args.periods
        credit_interest = args.interest
        response = "annuity"
    elif args.payment and args.periods and args.interest:
        annuity_payment = args.payment
        months = args.periods
        credit_interest = args.interest
        response = "principal"
    elif args.principal and args.payment and args.interest:
        credit_principal = args.principal
        monthly_payment = args.payment
        credit_interest = args.interest
        response = "repay"
    else:
        print("Incorrect parameters")
        sys.exit()
else:
    print("Incorrect parameters")
    sys.exit()


if response == "repay":
    i = credit_interest / 12 / 100
    months = math.ceil(
        math.log((monthly_payment / (monthly_payment - i * credit_principal)),
                 1 + i))
    overpayment = monthly_payment * months - credit_principal
    years = months // 12
    mod_months = months % 12
    if months / 12 < 1:
        if months == 1:
            print(f"You need {months} month to repay this credit!")
        else:
            print(f"You need {months} months to repay this credit!")
    elif years >= 1 and not mod_months:
        if years == 1:
            print(f"You need {years} year to repay this credit!")
        else:
            print(f"You need {years} years to repay this credit!")
    else:
        if years == 1 and months == 1:
            print(
                f"You need {years} year and {mod_months} month to repay this credit!")
        elif years == 1:
            print(
                f"You need {years} year and {mod_months} months to repay this credit!")
        elif months == 1:
            print(
                f"You need {years} years and {mod_months} month to repay this credit!")
        else:
            print(
                f"You need {years} years and {mod_months} months to repay this credit!")
    print(f"Overpayment = {overpayment:.0f}")
elif response == "annuity":
    i = credit_interest / 12 / 100
    annuity_payment = math.ceil(credit_principal * ((i * ((1 + i) ** months))
                                          / (((1 + i) ** months) - 1)))
    overpayment = annuity_payment * months - credit_principal
    print(f"Your annuity payment = {annuity_payment}!")
    print(f"Overpayment = {overpayment:.0f}")
elif response == "principal":
    i = credit_interest / 12 / 100
    credit_principal = annuity_payment / ((i * (1 + i) ** months)
                                          / ((1 + i) ** months - 1))
    overpayment = annuity_payment * months - credit_principal
    print(f"Your credit principal = {math.floor(credit_principal)}!")
    print(f"Overpayment = {math.ceil(overpayment)}")
elif response == "diff":
    i = credit_interest / 12 / 100
    credit_sum = 0
    for k in range(1, months + 1):
        D = (credit_principal / months
             + i * (credit_principal
                    - (credit_principal * (k - 1) / months)))
        print(f"Month {k}: paid out {math.ceil(D)}")
        credit_sum += math.ceil(D)
    overpayment = credit_sum - credit_principal
    print(f"\nOverpayment = {overpayment:.0f}")