def electricity_bill(units):
    if units<=100:
        return units*10

    elif units <=200:
        return (100*10) + (units-100)*15

    elif units <=300:
        return (100*10)+(100*15)+(units-200)*20

    elif units >300:
        return (100*10)+(100*15)+(100*20)+(units - 300)*25


Units = int(input("Enter the number of units: "))
Bill = electricity_bill(Units)
print("Electricity bill is",Bill,"for the month")
