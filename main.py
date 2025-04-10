
def calculate_receipt_fee(receipt_needed,receipts):
    fee = (receipt_needed - receipts) * 0.22
    return fee

def check_receipt_fee(income,receipts):
    if income <= 10000:
        receipt_needed = income * 0.1
    elif 10000 < income <= 30000:
        receipt_needed = income * 0.2
    else:
        receipt_needed = income * 0.3
    if receipt_needed > receipts:
        return calculate_receipt_fee(receipt_needed, receipts)
    else:
        return 0


def calculate_tax_income(income,tax_per_1,tax_per_2,tax_per_3,tax_per_4,tax_per_5):
    tax_9 = 10000 * tax_per_1
    tax_22 = 10000 * tax_per_2
    tax_28 = 10000 * tax_per_3
    tax_36 = 10000 * tax_per_4
    if income <= 10000: #9%
        sum_tax = income * tax_per_1
    elif 10000 < income <= 20000: #22%
        income -= 10000
        tax_22 = income * tax_per_2
        sum_tax = tax_9 + tax_22
    elif 20000 < income <= 30000: #28%
        income -= 20000
        tax_28 = income * tax_per_3
        sum_tax = tax_9 + tax_22 + tax_28
    elif 30000 < income <= 40000: #36%
        income -= 30000
        tax_36 = income * tax_per_4
        sum_tax = tax_9 + tax_22 + tax_28 + tax_36
    else: #income > 40000 #44%
        income -= 40000
        tax_44 = income * tax_per_5
        sum_tax = tax_9 + tax_22 + tax_28 + tax_36 + tax_44
    return sum_tax

def solidarity_tax_calc(income,tax_per_1,tax_per_2,tax_per_3,tax_per_4,tax_per_5,tax_per_6):
    tax_1 = 8000 * tax_per_1
    tax_2 = 10000 * tax_per_2
    tax_3 = 10000 * tax_per_3
    tax_4 = 25000 * tax_per_4
    tax_5 = 155000 * tax_per_5

    if income <= 12000:  #no tax
        sum_s_tax = 0
    elif 12000 < income <= 20000:  # 2.2%
        sum_s_tax = income * tax_per_1
    elif 20000 < income <= 30000:  # 5%
        income -= 20000 #the first 20k
        tax_2 = income * tax_per_2
        sum_s_tax =tax_1 + tax_2
    elif 30000 < income <= 40000:  # 6.5%
        income -= 30000
        tax_3 = income * tax_per_4
        sum_s_tax = tax_1 + tax_2 + tax_3
    elif 40000 < income <= 65000: #7.5%
        income -= 40000
        tax_4 = income * tax_per_4
        sum_s_tax = tax_1 + tax_2 + tax_3 + tax_4
    elif 65000 < income <= 225000: #9%
        income -= 65000
        tax_5 = income * tax_per_5
        sum_s_tax = tax_1 + tax_2 + tax_3 + tax_4 + tax_5
    else:  # income > 220000 #10%
        income -= 220000
        tax_6 = income * tax_per_6
        sum_s_tax = tax_1 + tax_2 + tax_3 + tax_4 + tax_5 + tax_6
    return sum_s_tax

# annual_income = float(input("Εισάγετε το ετήσιο εισόδημα: "))
# receipt = float(input("Εισάγετε το ποσό ηλεκτρονικών αποδείξεων: "))

annual_income = 25000 #for testing
receipt = 3000 #for testing


tax_income = calculate_tax_income(annual_income,0.09,0.22,0.28,0.36,0.44)
receipt_fee = check_receipt_fee(annual_income,receipt)
solidarity_tax = solidarity_tax_calc(annual_income,0.022,0.05,0.065,0.075,0.09,0.1)


sum = tax_income + receipt_fee + solidarity_tax


print(f"Φόρος εισοδήματος: {tax_income}")
print(f"Εισφορά αλληλεγγύης: {solidarity_tax}")
print(f"Πρόστιμο αποδείξεων: {receipt_fee}")
print(f"Συνολικός φόρος: {sum}")
