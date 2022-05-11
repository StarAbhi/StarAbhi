import os
#Function to read the input text file.This function takes the file name.
def readMenuTextFile(fileName):
    fileDataDict = {}
    #The path where the python program is executed from
    progFilepath = os.path.dirname(os.path.abspath(__file__))
    #Set the working directory to the place from where the python program is present
    os.chdir(progFilepath)                
    try:
        menuFile = open(fileName, "r")        
        #Read the contents of the file using the read() and split based on new lines using splitlines()
        menuItems = menuFile.read().splitlines()        
        
        #Return the file data.The return data is a Dict.
        for item in menuItems:
            #Split by $ to get the item name and price
            itemDetails = item.split('$')
            if (len(itemDetails) == 2):                
                itemName = itemDetails[0]
                #Remove the eading and trailing spaces from the item name
                itemName = itemName.strip()
                itemPrice = itemDetails[1]
                itemPrice = round(float(itemPrice), 2)
                #Add item to the fileDataDict dict
                if itemName not in fileDataDict:
                    fileDataDict[itemName] = itemPrice
        #Close the menu.txt file
        menuFile.close()
        #Return the fileDataDict
        return fileDataDict
                    
    #Exception handling if file is not found
    except FileNotFoundError:        
        print("FILE NOT FOUND ERROR")
        print("Input file {} not found in the path {}: ".format(fileName, progFilepath))        
        print("Kindly ensure the input file {} is in the same location where the Python program is running".format(fileName))        
        print("Exiting the program - Execution Terminated !!!")
        return {}
    #Exception handling if file opening error in input file
    except:
        print("FILE OPEN ERROR")
        print("Unable to open the file: {} in path {}".format(fileName, progFilepath))        
        print("Kindly ensure the input file is in the same location where the Python program is running and try again")
        print("Exiting the program - Execution Terminated !!!")
        return {}

def addItems(menuDict):
    #Get the item name to be added from the user
    itemName = input("Enter the Item Name to be added: ")    
    validPrice = False
    #Loop until a valid number is entered for price
    while (validPrice == False):
        try:
            #Get the price from the user
            itemPrice = input("Enter the item price: ")
            itemPrice = float(itemPrice)
            validPrice = True
        except ValueError:
            print("Enter a numeric value for item price")
            validPrice = False            
    #If item already present print the message, else add the item
    if itemName in menuDict.keys():
        print("Item '{}' already present in the Menu".format(itemName))
    else:
        menuDict[itemName] = itemPrice
        print("Item {} added successfullly!".format(itemName))
    #Return the updated menuDict back
    return menuDict

def deleteItems(menuDict):
    #Get the item name to be deleted
    itemName = input("Enter the Item Name to be deleted: ")
    #Print error message if item not found for deleting, else delete item
    if itemName not in menuDict:
        print("Item '{}' not found in the menu to delete".format(itemName))
    else:
        #Use pop() function to delete the item
        menuDict.pop(itemName)
        print("Item {} deleted successfullly!".format(itemName))
    #Return the updated menuDict back
    return menuDict

def updateItems(menuDict):
    #Get item name from user to update
    itemName = input("Enter the Item Name to be updated: ")    
    validPrice = False
    #Loop until a valid amount is entered for item price
    while (validPrice == False):
        try:
            #Get item price from the user
            itemPrice = input("Enter the new price: ")
            itemPrice = float(itemPrice)
            validPrice = True
        except ValueError:
            print("Enter a numeric value for item price")
            validPrice = False                
    #If item not in menu print error meaage, else update the price
    if itemName not in menuDict.keys():
        print("Item '{}' not present in the Menu to update".format(itemName))
    else:
        menuDict[itemName] = itemPrice   
        print("Item {} updated successfullly!".format(itemName))
    #Return the updated menuDict back
    return menuDict
            
#printMenu() functions formats the items menu.txt file and calls appropriate functions to do the processing
def printMenu(menuDict):
    #Print the header line
    print("{:<35}{}".format("Item Name", "Price"))
    #Loop the Dict and print the detail lines
    for item, price in menuDict.items():
        price = round(float(price), 2)        
        print("{:<35}${:.2f}".format(item, price))    
    #Preset the user with the menu options until user chooses to exit
    validChoice = False
    while (validChoice == False):        
        print("1. Add item")
        print("2. Delete item")
        print("3. Update price")
        print("4. Exit")
        userChoice = input("Enter Choice: ")
        #Error message if invalid option is choosen
        if userChoice not in ['1', '2', '3', '4']:
            print("Invalid Choice entered")
            validChoice = False
        else:
            #In case Option 1 is selected call addItems() do the processing the redisplay the menu
            if (userChoice == '1'):
                #Call addItems()
                menuDict = addItems(menuDict)    
                #Redisplay Menu after adding items
                printMenu(menuDict)
            #In case Option 2 is selected call deleteItems() do the processing the redisplay the menu
            elif (userChoice == '2'):
                #Call deleteItems()
                menuDict = deleteItems(menuDict)                
                #Redisplay Menu after deleting items
                printMenu(menuDict)
            #In case Option 3 is selected call updateItems() do the processing the redisplay the menu
            elif (userChoice == '3'):  
                #Call updateItems()
                updateItems(menuDict)
                #Redisplay Menu after updating items
                printMenu(menuDict)
            validChoice = True
    return menuDict

#The function takes the updated Menu Dict after the user has updated the Menu
#Write items whose price > 20 to the specialOccassionMenu.txt file
def writeSpecialOccasionMenu(updatedMenuDict, ofileName):
    #Intialize the specialOccassionMenu Dict
    specialOccassionMenuDict = {}
    #Variable to hold the total price of special items
    totalPrice = 0
    #Variable to hold the count of special items
    specialMenuItemCount = 0
    
    #Loop the updatedMenuDict and generate the specialOccassionMenuDict
    for item, price in updatedMenuDict.items():
        price = float(price)
        #Check if price is gt 20.
        if (price > 20):
            #Add price to total
            totalPrice += price
            #Add 1 to specialMenuItemCount
            specialMenuItemCount += 1
            #Add item to specialOccassionMenuDict
            if item not in specialOccassionMenuDict:
                price = round(float(price), 2)
                specialOccassionMenuDict[item] = price
    
    #Open the specialOccassionMenu.txt file in write mode
    ofile = open(ofileName, "w")    
    #Generate the headerLine
    headerLine = "{:<35}{}".format("Item Name", "Price\n")
    #Write header line to specialOccassionMenu.txt file
    ofile.write(headerLine)
    
    #Loop the newly created specialOccassionMenuDict to write items to the specialOccassionMenu.txt file
    for item, price in specialOccassionMenuDict.items():
        price = round(float(price), 2)        
        #Write item details to the out file.
        detailLine = "{:<35}${:.2f}\n".format(item, price)
        ofile.write(detailLine)
    
    #To handle zero division error in case there are no items with price gt 20
    if specialMenuItemCount > 0:
        #Calculate the average price of the special menu items
        avgPricePerItem = totalPrice / specialMenuItemCount
    elif specialMenuItemCount == 0:
        avgPricePerItem = 0    
    #Round the special menu item
    avgPricePerItem = round(avgPricePerItem, 2)
    #Generate the summary line and write to file
    summaryLine = "The average price per item for special occassion menu is: ${:.2f}".format(avgPricePerItem)
    ofile.write(summaryLine)
    #Close the file
    ofile.close()

#Function get the updated Dict after the user has added, deleted, updated the item details and  writes back to the menu file
def writeUpdatedMenuFile(updatedMenuDict, ofileName):
    #Open the file in write mode
    ofile = open(ofileName, "w")
    #Generate the header line
    headerLine = "{}{}".format("Item Name", "Price\n")
    #Write the header Line to the menu.txt file
    ofile.write(headerLine)
    
    #Loop the items in the Dict and write the item details to the menu.txt file
    for item, price in updatedMenuDict.items():
        price = round(float(price), 2)        
        detailLine = "{}${}\n".format(item, price)
        ofile.write(detailLine)    
    #Close the file
    ofile.close()

#Call the main() function for main processing
def main():
    menuFileName = "menu.txt"
    #Call the readMenuTextFile to read the menu.txt file for further processing 
    menuDict = readMenuTextFile(menuFileName)
    #Call the printMenu() function which prints the menu and carries out the options selected by the user
    updatedMenuDict = printMenu(menuDict)
    #Call the writeSpecialOccasionMenu() to write the the specialOccassionMenu.txt file
    writeSpecialOccasionMenu(updatedMenuDict, "specialOccassionMenu.txt")
    #Call the writeUpdatedMenuFile() to write the the updated menu details back to the menu.txt file
    writeUpdatedMenuFile(updatedMenuDict, menuFileName)
    

#This is the standard way to call the main() function/module in python.
if __name__ == '__main__':
  main()