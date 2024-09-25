# Owen Chickering
# Mail Sorter
# Log
# Bugs
# Features
# Sources    
def main():
    try:
        data = input("Enter your shipping info --> ")
        dimensions = data.split(",")
        l = float(dimensions[0])
        h = float(dimensions[1])
        w = float(dimensions[2])
        mfrom = int(dimensions[3])
        mto = int(dimensions[4])
        costs = getCost(h,l,w)
        if (costs == 1):
            print("Unmailable")
            main()
        zonechange = abs(getZone(mfrom) - getZone(mto))
        if (getZone(mfrom) == 7) or (getZone(mto) == 7):
            print("Your Zip Code is Incorrect")
            main()
        packageprice = costs[0]
        shippingprice = costs[1]
        shipcost = (shippingprice * zonechange)
        print(shipcost + packageprice)
    
    except ValueError:
        print("Your input is not in proper format")
        main()

def getCost(h,l,w):
    area = (h * 2) + (l * 2)+ (w * 2)
    if (l >= 3.5) and (l <= 4.25) and (h >= 3.5) and (h <= 6) and (w >= .007) and (w <= .016):
        return [.20,.03]
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
    if (zipcode >= 99999):
        return 7
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

main()


