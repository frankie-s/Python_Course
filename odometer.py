print("Welcome to Odometerometer!")
o_start = float(input("Enter the initial odometer reading: "))
o_fin = float(input("Enter the final odometer reading: ")) 
gal = float(input("Enter the number of gallons used: ") )
cost = float(input("Enter the cost per gallon: "))

miles = o_fin - o_start
mpg = miles / gal
cost_mi = cost * gal / miles

print("Total miles: {0:.2f}".format(miles))
print("mpg: {0:.2f}".format(mpg))
print("cost per mile: ${0:.2f}".format(cost_mi))
