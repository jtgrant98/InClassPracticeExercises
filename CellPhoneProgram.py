import CellPhoneClass

def main():
    #Get the phone data
    man = input("Who is the manufacturer of your phone?")
    mod = input("What is the model of your phone?")
    retail = float(input("What is the price of your phone?"))

#create instance
    phone = CellPhoneClass.CellPhone(man,mod,retail)


    #display the data 
    print('Here is the data you entered')
    print('Manufacturer:', phone.get_manufacturer())
    print('Model number:', phone.get_model())
    print('Retail price: $', format(phone.get_retail_price()))
main()