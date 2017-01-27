monthInterestRate = annualInterestRate / 12.0
actualBalance = balance
actualPayment = 0
monthidx = 1
totalPayment = 0

while monthidx <= 12:
    actualPayment = monthlyPaymentRate * actualBalance
    totalPayment += actualPayment
    actualBalance -= actualPayment
    actualBalance += monthInterestRate * actualBalance
    monthidx += 1
print('Remaining balance: ' + str(round(actualBalance, 2))) 