def find_customer(customer):
    with open("CustomerList.txt", "r") as r:
            customer_list = r.readlines()
            for item in customer_list:
                record = item.split(",")
                if customer == record[0]:
                    return record
    return "none"

def returning():
    my_customer = get_customer()
    customer_record = find_customer(my_customer)
    if customer_record == "none":
        print ("That number was not found. Try again.")
        returning()
    else:
        for item in customer_record:
            print item

def guest():
    if entry == 3:
        print ("Welcome! We hope to see you often!")

def new():
    if entry == 2:
        print ("New Customer")


def get_customer():
    customer = raw_input("Please enter your customer number:  \n")
    return customer


entry = 0
if entry >=0:
    print (">*< >*< >*< >*< >*< >*< >*<")
    print (" Please choose an option:\n")
    print ("1. Returning Customer")
    print ("2. New Customer")
    print ("3. Guest")
    print (">*< >*< >*< >*< >*< >*< >*<")
    entry = int(raw_input("Enter option:     "))
    if entry < 1 or entry > 3:
        entry = int(raw_input("Please enter Customer option 1, 2 or 3:     "))
    elif entry == 1:
        returning()
    elif entry == 2:
        new()
    elif entry == 3:
        guest()

