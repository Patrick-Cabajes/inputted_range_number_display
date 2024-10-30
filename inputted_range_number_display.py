#declare each range as an empty array
var1_10 = []
var11_20 = []
var21_30 = []
var31_40 = []
var41_50 = []

#build a loop and ask the user to input variables ranging from 1 to 50
while True:
    try:
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
        
        #print how many numbers/variables are inputted in each range
        else:
            print("Invalid Input")
            break
        
    except:
        print("Please input numbers only")
        break

print(f"You have inputted {len(var1_10)} number(s) in the range of 1 to 10.")
print(f"You have inputted {len(var11_20)} number(s) in the range of 11 to 20.")
print(f"You have inputted {len(var21_30)} number(s) in the range of 21 to 30.")
print(f"You have inputted {len(var31_40)} number(s) in the range of 31 to 40.")
print(f"You have inputted {len(var41_50)} number(s) in the range of 41 to 50.")