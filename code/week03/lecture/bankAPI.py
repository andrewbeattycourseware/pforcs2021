# messing about with dictionaries
# Author: Andrew Beatty
sampleRequest={ 
    "Data": { 
        "tags": ['debit', 'checking'], 
        "InstructedAmount": { 
            "Amount": 100, 
            "Currency": "GBP" 
        }, 
        "DebtorAccount": { 
            "Identification": "30130900103004", 
            "Name": "DName" 
        }, 
        "CreditorAccount": { 
            "Identification": "30180500016825", 
            "Name": "CName" 
        },  
        "Risk": "Risk" 
    } 
}
#print(sampleRequest['Data']['InstructedAmount']['Amount'])

for key in sampleRequest['Data']:
    print (key + " is of type "+ str(type(sampleRequest['Data'][key])))

