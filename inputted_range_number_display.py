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
    if value >= 1 and value <= 10:
        var1_10.append(value)
        #append each range to add every new input from the user
        #print the inputted numbers/variables in each array
        #break
    else:
        print("The values you have entered are:", var1_10)