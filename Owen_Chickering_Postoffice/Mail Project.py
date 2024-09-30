# Owen Chickering
# Mail Sorter
# Bugs: NA
# Features: NA
# Sources: Teacher assistance

def main(): #Defines the main function
    try: #Tries the code for any errors
        data = input("Enter your shipping info --> ")
        dimensions = data.split(",") #Splits the user input into five parts
        l = float(dimensions[0]) #Designates a name to each value of Data
        h = float(dimensions[1])
        w = float(dimensions[2])
        mfrom = int(dimensions[3])
        mto = int(dimensions[4])
        costs = getCost(h,l,w) #Calls getCost function with the data from Height,Length,Width
        if (costs == 1):#If the geCost function returns one then
            print("Unmailable") 
            main() #Calls main function to create loop
        zonechange = abs(getZone(mfrom) - getZone(mto))
        if (getZone(mfrom) == 7) or (getZone(mto) == 7): #If funciton returns a 7, then the zip is out of the defined range
            print("Your Zip Code is Incorrect") #Informs the user their zip code is wrong
            main() #Calls main function to create loop
        packageprice = costs[0]
        shippingprice = costs[1]
        shipcost = (shippingprice * zonechange) #Calculates the shipping cost
        print(shipcost + packageprice) #Prints the final value of the package
    
    except ValueError: #If there is a value error, it intercepts it and loops the main funciton
        print("Your input is not in proper format") #Tells the user to correct their format 
        main() #Calls main function to create loop

def getCost(h,l,w): #takes in height,length,width and returns package pricing
    '''
    Calculates the shipping cost and package price using the package dimensions

    Returns:
        List: Value of the package, and cost to ship, in that order
    '''
    area = (h * 2) + (l * 2)+ (w * 2) #Calculates area
    if (l >= 3.5) and (l <= 4.25) and (h >= 3.5) and (h <= 6) and (w >= .007) and (w <= .016): #Defines the value of a set package type
        return [.20,.03] #Returns price of shipping and price of package
    elif (l > 4.25) and (l < 6) and (h > 6) and (h < 11.5) and (w >= .007) and (w <= .015):
        return [.37,.03]
    elif (l >= 3.5) and (l <= 6.125) and (h >= 5) and (h <= 11.5) and (w > .016) and (w < .25):
        return [.37,.04]
    elif (l > 6.125) and (l < 24) and (h >= 11) and (h <= 18) and (w >= .25) and (w <= .5):
        return [.60,.05]
    elif (area <= 84):
        return [3.95,.25]
    elif (area > 84) and (area <= 130):
        return [3.95,.35]
    else:
        return 1 
             
def getZone(zipcode):
    '''
    Recieves zipcode user input and designates a distance grouping

    Returns:
        Int: Distance between two zipcodes 1-7
        
    '''
    if (zipcode >= 99999): #Defines a zipcode range affiliated with a value
        return 7 #returns a value affiliated with a zipcode
    elif (zipcode >= 85000) and (zipcode <= 99999):
        return 6
    elif (zipcode >= 63000) and (zipcode <= 84999):
        return 5
    elif (zipcode >= 36000) and (zipcode <= 62999):
        return 4
    elif (zipcode >= 20000) and (zipcode <= 35999):
        return 3
    elif (zipcode >= 7000) and (zipcode <= 19999):
        return 2
    else:
        return 1 

main() #Main function jump starts the code


