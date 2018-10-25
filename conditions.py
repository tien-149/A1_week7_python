print("Rules that govern state of water")

current_temp = False

while current_temp is False:
    current_temp = input("Enter a temperature: \n")
    print(current_temp)

    if(int(current_temp) < 0) or (int(current_temp) == 0):
        print("Water is a solid. icy")
        current_temp = False

    elif (int(current_temp) < 100):
        print("Water is a liquid.profit!")
        current_temp = False

    elif (int(current_temp) < 100) or (int(current_temp) == 100):
        print("Water is a vapor, cuz it hot")
        current_temp = False
    

