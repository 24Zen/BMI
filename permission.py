import math

a = float(input("Enter your weight(kg): "))
b = float(input("Enter your height(m): "))

result = a / (b ** 2)
yourbmi = a / result
#rounded_number = math.ceil(yourbmi)

print(f"Your BMI is: {yourbmi:.2f}")

if yourbmi < 18.5:
    print("Your weight is less than 18.5: %.3f" %yourbmi)
    #print("Your totalbest price for sale is :%.3f" %rounded_number )
    
elif 18.5 <= yourbmi < 25:
    print("Your weight is less than 25 so perfect boby : %.3f" %yourbmi)
    
elif 25 <= yourbmi < 30:
    print("Your weight is more than 30 chuby girl : %.3f" %yourbmi)

elif 30 <= yourbmi < 35:
    print("Your weight is more than 35, Ok you fatty : %.3f" %yourbmi)

elif 35 <= yourbmi < 40:
    print("Dangerous : %.3f" %yourbmi)

else:
    print("More than 40 go to hospital : %.3f" %yourbmi)
    
#print("Your cost is: %.3f" %result)


'''print("Your best price for sale is : %.3f" %yourbmi )
print("Your totalbest price for sale is :%.3f" %rounded_number )'''
        
        