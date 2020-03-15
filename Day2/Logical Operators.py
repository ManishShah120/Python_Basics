#Logical Operators(AND,OR,NOT)
'''
has_high_income=False
has_good_credit=True
if has_high_income or has_good_credit:
    print("Elligible for loan")
else:
    print("Not Elligible")
'''
has_good_credit=True
has_criminal_record=False
if has_good_credit and not has_criminal_record:
    print("Elligible for Loan")
else:
    print("Not elligible for Loan")