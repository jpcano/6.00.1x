monthInterestRate = annualInterestRate / 12.0
actualBalance = balance
monthlyPaymentLower = balance / 12.0
monthlyPaymentUpper = (balance * ((1 + monthInterestRate) ** 12)) / 12.0
monthlyPaymentTemp = 0
monthlyPayment = round((monthlyPaymentLower + monthlyPaymentUpper) / 2.0, 2)

while True:
   
    for monthidx in range(12):
        actualBalance -= monthlyPayment
        actualBalance += monthInterestRate * actualBalance
    
    if actualBalance > 0:
        monthlyPaymentLower = monthlyPayment
    elif actualBalance < 0:
        monthlyPaymentUpper = monthlyPayment
    else:
        break

    monthlyPaymentTemp = round((monthlyPaymentLower + monthlyPaymentUpper) / 2.0, 2)

    if monthlyPaymentTemp == monthlyPayment:
        break
    
    actualBalance = balance
    monthlyPayment = monthlyPaymentTemp
        
print('Lowest Payment: ' + str(monthlyPayment))