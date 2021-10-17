units = {"Mg":10**6, "kg":10**3, "hg":10**2, "dag":10, "g":10**0,"dg":10**-1,"cg":10**-2,"mg":10**-3,"µg":10**-6,"ng":10**-9,"lb":453.59237}

print("Available units:",list(units))
x = input("Value: ")
u = input("Unit: ")

g = float(x)*units[u]
for uni in list(units):
    print(g/units[uni],uni)


