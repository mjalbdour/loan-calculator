
import argparse
import sys
from math import log, ceil


def calculate_number_of_monthly_payments(p, a, annual_interest_rate):
    i = convert_annual_to_nominal_interest(annual_interest_rate)
    dividend = a / (a - i * p)
    return ceil(log(dividend, 1 + i))


def calculate_annuity(p, n, annual_interest_rate):
    i = convert_annual_to_nominal_interest(annual_interest_rate)
    dividend = i * (1 + i) ** n
    divisor = (1 + i) ** n - 1
    return ceil(p * dividend / divisor)


def calculate_loan_principal(a, n, annual_interest_rate):
    i = convert_annual_to_nominal_interest(annual_interest_rate)
    dividend = i * (1 + i) ** n
    divisor = (1 + i) ** n - 1
    return ceil(a / (dividend / divisor))


def calculate_differentiated_payments(p, n, annual_interest_rate):
    i = convert_annual_to_nominal_interest(annual_interest_rate)
    diff_payments = [0] * n
    for m in range(1, n + 1):
        diff_payments[m - 1] = ceil((p / n) + i * (p - (p * (m - 1)) / n))
    return diff_payments


def calculate_overpayment(principal, future):
    return ceil(future - principal)


def convert_period_to_years_and_months(period_in_months):
    return period_in_months // 12, period_in_months % 12


def convert_annual_to_nominal_interest(annual_interest_rate):
    return (annual_interest_rate / 100) / 12


def print_number_of_monthly_payments(n):
    message = 'It will take '
    message_ending = ' to repay this loan!'
    if n[0] > 0:
        year_word = 'year'
        if n[1] > 1:
            year_word = 'years'
        message = message + str(n[0]) + ' ' + year_word
    if n[0] > 0 and n[1] > 1:
        message = message + ' and '
    if n[1] > 0:
        month_word = 'month'
        if n[1] > 1:
            month_word = 'months'
        message = message + str(n[1]) + ' ' + month_word

    message = message + message_ending
    print(message)


def print_annuity(a):
    print(f'Your monthly payment = {a}!')


def print_loan_principal(p):
    print(f'Your loan principal = {p}!')


def print_differentiated_payments(diff_payments):
    for m in range(1, len(diff_payments) + 1):
        print(f'Month {m}: payment is {diff_payments[m - 1]}')


def print_overpayment(op):
    print(f'Overpayment = {op}')


# Use argparse instead
parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=["diff", "annuity"])
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if len(sys.argv) < 5 or not args.interest:
    print('Incorrect parameters')
else:
    if args.type == 'diff':
        diffr_payments = calculate_differentiated_payments(float(args.principal), int(args.periods), float(args.interest))
        overpayment = calculate_overpayment(float(args.principal), sum(diffr_payments))
        print_differentiated_payments(diffr_payments)
        print_overpayment(overpayment)
    elif args.type == 'annuity':
        # Number of monthly payments
        if not args.periods:
            months = calculate_number_of_monthly_payments(float(args.principal), float(args.payment), float(args.interest))
            periods = convert_period_to_years_and_months(months)

            overpayment = calculate_overpayment(float(args.principal), float(args.payment) * months)

            print_number_of_monthly_payments(periods)
            print_overpayment(overpayment)

        # Annuity
        elif not args.payment:
            annuity = calculate_annuity(float(args.principal), int(args.periods), float(args.interest))
            overpayment = calculate_overpayment(float(args.principal), annuity * int(args.periods))

            print_annuity(annuity)
            print_overpayment(overpayment)

        # Principal
        elif not args.principal:
            pr = calculate_loan_principal(float(args.payment), int(args.periods), float(args.interest))
            overpayment = calculate_overpayment(pr, float(args.payment) * int(args.periods))

            print_loan_principal(pr)
            print_overpayment(overpayment)
