
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
    toStocks = savingsPlusPrincipal/2

    if toStocks > savings:
        return savings
    else:
        return toStocks

"""
savings towards mortgage = total savings - savings towards stocks = 700 (or same as principal ??)
"""
# Savings towards mortgage
def savingsTowardsMortgage(savings: float, savingsTowardsStocks: float):
    return savings - savingsTowardsStocks



def stockPortfolio(startingPortfolioValue, potentialYearlyContribution, marketInterestRate, yearsMeasuring):
    portfolioValues = [0] * yearsMeasuring
    interestRate = (100 + marketInterestRate)/100
    for i in range(yearsMeasuring): # Iterate 30 times or whatever years you wanna measure
        portfolioValues[i] = (startingPortfolioValue + potentialYearlyContribution) * interestRate
        startingPortfolioValue = portfolioValues[i]
    return portfolioValues




print(stockPortfolio(values.startingPortfolio, values.potentialYearly, values.marketInterest, values.years))