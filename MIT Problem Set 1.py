# MIT Computer Science Course Problem Set 1
# PROBLEM SET 1 Paying the minimum:

"""Write a program to calculate the credit card balance after one
year if a person only pays the minimum monthly payment required
by the credit card company each month."""

# balance = float(input("Outstanding balance on the Card: "))
# annualInterest = float(input("Annual Interest Rate: "))
# minMonPayRate = float(input(" Minimum Monthly Payment Rate: "))
# principalPaid = 0
# totalPaid = 0
# for i in range(1,13):
#     minMonthlyPayment = minMonPayRate * balance
#     interestPaid = annualInterest / 12 * balance
#     print(f'Month: {i}')
#     print(f'Minimum monthly payment: ${round(minMonthlyPayment,2)}')
#     principalPaid = minMonthlyPayment - interestPaid
#     print(f'Principle paid: ${round(principalPaid,2)}')
#     balance = balance - principalPaid
#     print(f'Remaining balance: ${round(balance,2)}')
#     totalPaid += minMonthlyPayment
# print('RESULT')
# print(f'Total amount paid: ${round(totalPaid, 2)}')
# print(f'Remaining balance: ${round(balance, 2)}')


#PROBLEM 2 - Paying debt off in a year

'''Now write a program that calculates the minimum fixed 
monthly payment needed in order pay off a credit card balance 
within 12 months. We will not be dealing with a minimum monthly payment rate.'''

# outstandingBalance = float(input("Outstanding balance on the CCard: "))
# annualInterestRate = float(input("Annual interest rate: "))
# monthlyInterest = annualInterestRate/12
# monthlyPayment = 0
# updatedBalance = outstandingBalance
#
#
# while updatedBalance > 0:
#     updatedBalance = outstandingBalance
#     month = 0
#     monthlyPayment += 10
#     while month < 12 and updatedBalance > 0:
#         print('Month: ', month)
#         updatedBalance = updatedBalance * (1 + monthlyInterest) - monthlyPayment
#         month +=1
#     print('Monthly Payment: ', monthlyPayment)
# print(f'Balance: {updatedBalance}, after {month} months, with {monthlyPayment} Mpayments')

#Problem 3

'''Write a program that uses these bounds and bisection search 
to find the smallest monthly payment to the cent (no more multiples of $10)
such that we can pay off the debt within a year. Try it out with large inputs,
and notice how fast it is. Produce the output in the same format as you did 
in problem 2.'''

# outstanding_balance = float(input("Outstanding balance on the CCard: "))
# annual_interest_rate = float(input("Annual interest rate: "))
# monthly_interest = annual_interest_rate / 12
# # Initialize bisection search lower and upper bound
# lower_bound = outstanding_balance / 12
# upper_bound = (outstanding_balance * (1 + monthly_interest) ** 12) / 12
# monthly_payment = (lower_bound + upper_bound) / 2
#
# # check if the search space if small enough
# while abs(lower_bound - upper_bound) > 0.00045:
#     updated_balance = outstanding_balance
#     #print(f'Lower: {lowerBound}, High: {upperBound}')
#     #print('Monthly Payment: ', monthlyPayment)
#     month = 0
#     while month < 12 and updated_balance > 0:
#         #print('1st while Month: ', month)
#         #print('Updated balance: ', updatedBalance)
#         #print('Monthly Payment: ', monthlyPayment)
#         updated_balance = updated_balance * (1 + monthly_interest) - monthly_payment
#         month += 1
#     # Apply the bisection search
#     if updated_balance < 0:
#         upper_bound = monthly_payment
#     else:
#         lower_bound = monthly_payment
#     #print(f'Upper: {upperBound}, Lower: {lowerBound}')
#     monthly_payment = (lower_bound + upper_bound) / 2
# final_monthly_payment = round((monthly_payment + 0.0045), 2)
# print(f'Monthly payment to pay off debt in 1 year: {final_monthly_payment}')
# print(f'Number of months needed: {month}')
# print(f'Balance : {round((updated_balance - 0.0045), 2)}')
