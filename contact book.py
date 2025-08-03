contacts={}

def add_contact():
    name=input("enter name:")
    phone=int(input("enter phone number:"))
    if name in contacts:
        print("This is alrady exists.")
    else:
        contacts[name]=phone
        print("contact added successfully.")

def delet_contact():
    name=input("enter name:")
    if name in contacts:
        del contacts[name]
        print("conatct deleted successfully.")
    else:
        print("This contact dose not exist!")

def update_contact():
    name=input("enter the name:")
    for contact in contacts:
        if contact==name:
            phone=int(input("enter the new phone number:"))
            contacts[name]=phone
            print("contact updated successfully.")
            break
        else:
            print("this contact dose not exist!")

def search_contact():
    name=input("enter name:")
    for contact in contacts:
        if contact.lower()==name.lower():
            print("contact found.")
            print(contact,contacts[contact])
            break
        else:
            print("contact not found!")
def display_contact():
    if contacts=={}:
        print("there are no contacts.")
    else:
        print("contacts list:")
        for name,phone in contacts.items():
            print("name, phone")

while True:
    print("\n contact book menu:")
    print("1.add contact")
    print("2.delet contact")
    print("3.update contact")
    print("4.search contact")
    print("5.display contact")
    print("6.exit")

    choice=int(input("enter your choice(1-6):"))
    if choice==1:
        add_contact()
    elif choice==2:
        delet_contact()
    elif choice==3:
        update_contact()
    elif choice==4:
        search_contact()
    elif choice==5:
         display_contact()
    elif choice==6:
        print("exiting contact book\n good bye!")
        break
    else:
        print("invalid choice.\n please enter a number between 1to 6:")

