
#Read All the data from User 
def main():
    details={'firmName':[],'customer':[],'hours':[],'material':[],'labor':None,'jobFee':None,'discount':None,'finalAmount':None}
    print("Enter the Details of 3 Contractor")
    for i in range(3):
        details['firmName'].append(input("Name of the Construction Firm "))
        details['customer'].append(input("Name of the Customer "))
        details['hours'].append(int(input("Number of labor hours for the job ")))
        details['material'].append(int(input("Amount of materials ")))
    #call function for calculte the bill and store it in details dict 
    details['labor']=calTotalLabor(details['hours'])
    details['jobFee']=calJobFee(details['labor'],details['material'])
    details['discount']=calDiscount(details['jobFee'])
    details['finalAmount']=calFinalAmount(details['jobFee'],details['discount'])
    #print the bill 
    displayBillDetails(details)
    
#function fro calculation of bill
def calTotalLabor(hours):
    labor=[]
    for i in hours:
        labor.append(i*50)
    return labor

def calJobFee(labor,meterial):
    jobFee=[]
    for i in range(3):
        jobFee.append(labor[i]+meterial[i])
    return jobFee
def calDiscount(jobFee):
    discount=[]
    for i in jobFee:
        if i<5000:
            discount.append(0)
        elif i>=5000 and i<=10000:
            discount.append(i*0.05)
        elif i>=10000 and i<=20000:
            discount.append(i*0.1)
        else :
            discount.append(i*0.2)
    return discount
def calFinalAmount(jobFee,discount):
    finalAmount=[]
    for i in range(3):
        finalAmount.append(jobFee[i]-discount[i])
    return finalAmount
def displayBillDetails(details):
    for i in range(3):
        print(details['firmName'][i])
        print("Customer : ",details['customer'][i])
        print("\tNumber of Hours = ",details['hours'][i])
        print("\tLabor = ",details['labor'][i])
        print("\tMaterials = ",details['material'][i])
        print("\tJob Fee = ",details['jobFee'][i])
        print("\tDiscount = ",details['discount'][i])
        print("\tFinal Amount Due = ",details['finalAmount'][i])

#call main for start the billing ...        
main()
