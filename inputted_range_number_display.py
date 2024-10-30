#declare each range as an empty array
var1_10 = []
var11_20 = []
var21_30 = []
var31_40 = []
var41_50 = []

#build a loop and ask the user to input variables ranging from 1 to 50
while True:
    value = int(input("Please input numbers from 1 to 50: "))
    
    #add conditions to each range
        #append each range to add every new input from the user
    if value >= 1 and value <= 10:
        var1_10.append(value)

    elif value >= 11 and value <= 20:
        var11_20.append(value)
    
    elif value >= 21 and value <= 30:
        var21_30.append(value)

    elif value >= 31 and value <= 40:
        var31_40.append(value)

    elif value >= 41 and value <= 50:
        var41_50.append(value)
        
        #print the inputted numbers/variables in each array
    else:
        print("The values you have entered in the range from 1 to 10 are:", var1_10)
        print("The values you have entered in the range from 11 to 20 are:", var11_20)
        print("The values you have entered in the range from 21 to 30 are:", var21_30)
        print("The values you have entered in the range from 21 to 30 are:", var31_40)
        print("The values you have entered in the range from 21 to 30 are:", var41_50)
        break