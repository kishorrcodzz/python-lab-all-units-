print("CONTACT BOOK")
contacts = []
n = int(input("Enter the number of contacts: "))
for i in range(n):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contact = {
        "Name": name,
        "Phone": phone
    }
    contacts.append(contact)

print("\nCONTACT DETAILS")

for contact in contacts:
    print("Name:", contact["Name"])
    print("Phone:", contact["Phone"])
    print("-------------------")