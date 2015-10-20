F = input("Enter the temperature in degrees Fahrenheit: ")
C = (F - 32)
C = C * 5/9
K = C + 273.15
print(u"{0}\u00b0F = {1}\u00b0C = {2}\u00b0K".format(F,C,K))
