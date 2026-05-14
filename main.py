
import values as values
"""
Requirements:
    -Save detail of total mortgage once. 
    -Save total investments once
    -Enter mortgage payment + interest rate. Calculate interest and principal
    -Enter leftover savings. Divide it by two. Subtract one part by the principal. Leftover goes towards mortgage. Rest towards investments.
    -Show if you pay of mortgage at this rate, when does it hit 0? Save the actual contribution you did and make it affect the total mortgage
    -Show if you invest at this rate, your investments in 5, 10, 15, 20 and 30 yrs.

"""

"""
streamlit to be able to enter all those values and then connect it to here (the backend)
then receive the answers and display it to the user
"""

#### WRITE TESTCASES AS WELL

def monthlyInterestCharged(totalMortgage: float, interestRate: float):

    monthlyInterest = (interestRate/100 * totalMortgage)/12

    return monthlyInterest


def monthlyPrincipalSaved(monthlyRepayment: float, monthlyInterest: float):
    return monthlyRepayment - monthlyInterest


# Savings towards stocks

def savingsTowardsStocks(savings: float, monthlyPrincipal: float):
    savingsPlusPrincipal = savings + monthlyPrincipal
    return savingsPlusPrincipal/2

"""
savings towards mortgage = total savings - savings towards stocks = 700 (or same as principal ??)
"""
# Savings towards mortgage
def savingsTowardsMortgage(savings: float, savingsTowardsStocks: float):
    return savings - savingsTowardsStocks



monthlyInterest = monthlyInterestCharged(values.mortgageLeft, values.interestRate)
print(f"Monthly Interest: {monthlyInterest}")

monthlyPrincipal = monthlyPrincipalSaved(values.monthlyRepayment, monthlyInterest)
print(f"Monthly Principal: {monthlyPrincipal}")

monthlyStocksSavings = savingsTowardsStocks(values.savings, monthlyPrincipal)
print(f"This is how much you need to put into stocks this month: {monthlyStocksSavings}")


monthlyExtraMortgageContribution = savingsTowardsMortgage(values.savings, monthlyStocksSavings)
print(f"This is how much extra you need to put into the mortgage this month:{monthlyExtraMortgageContribution}")