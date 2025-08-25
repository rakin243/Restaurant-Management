menu = {

'Pizza':100,
'Burger':60,
'Cofee':120,
'Pasta':150,
'Nudels':180
	
	
}


print("Wellcome our python Restuarent")

print("Pizza:100BDT\nBurger:60BDT\nCofee:120BDT\nPasta:150BDT\nNudels:180BDT")



money_total = 0


oder_1 = input("Enter the name of food you want to oder:")

if oder_1 in menu:
	money_total += menu[oder_1]
	print(f"your food {oder_1} has been added to your oder")
	
else :
	print("This food is not available in menu")
	
	
Food_2 = input("Do you want to add another item to your oder ?  {Yes / No} : ")

if Food_2 == "Yes" :
	oder_2 = input("Enter the Second Food name you want to oder:")
	if oder_2 in menu :
		money_total += menu[oder_2]
	
	else :
		print("This food is not available in menu")
		
		
print(f"The total amount of oder to pay is{money_total}")


print("Thank you sir\nCome our Restuarent again")
	