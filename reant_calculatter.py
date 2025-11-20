rent = int(input("enter your hostel/flat rent =  "))
food = int (input("Enter the ammount  of foof order = "))
electicity_spend  = int(input("Enter the total of electricity spand = "))
chareg_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the number of persion living in room/flt = "))
total_bill = electicity_spend*chareg_per_unit

output =  (food+rent+total_bill)//person
print("Each perion will pay = ", output)