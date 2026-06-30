bill = int(input("Enter the bill amount: "))

bill = float(bill)

ppl = int(input("Enter the number of people: "))

ppl = int(ppl)

tip = int(input("Enter the tip percentage: "))
tip = float(tip)

tip_amount = (tip / 100) * bill

total_bill = bill + tip_amount

bill_per_person = total_bill / ppl

print(f" bill_per_person :{bill_per_person:.2f}" )