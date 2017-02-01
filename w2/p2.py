monthInterestRate = annualInterestRate / 12.0
actualBalance = balance
monthlyPayment = 10

while True:
    for monthidx in range(12):
        actualBalance -= monthlyPayment
        actualBalance += monthInterestRate * actualBalance
    if actualBalance > 0:
        monthlyPayment += 10
        actualBalance = balance
    else:
        break
print('Lowest Payment: ' + str(monthlyPayment))
