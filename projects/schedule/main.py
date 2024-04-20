
class Contact:
    def __init__(self, name=None, type=None, value=None):
        self.name = name
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.name} | {self.type} | {self.value}"
    

class Schedule:
    def __init__(self) -> None:
        pass
            
    def addContact(self):
        
        print("\nPlease anwsers the questions bellow: \n")
        __name = str(input("Whats the name: "))
        __type = str(input("Whats the type: "))
        __value = str(input("Whats the value: "))

        contact = Contact(__name, __type, __value)
        print(contact.__str__())
        try:
            with open("arquivo.txt", "a") as file:
                file.write(contact.__str__() + "\n")
                print("Contact added with success.")
        except:
            print("Error to add a new contact, please try again. \n")

    def deleteContact(self):
        ...

    def ListContacts(self):
        try:
            with open("arquivo.txt", "r") as file:
                content = file.readlines()
                for idx, item in enumerate(content):
                    print(f"{idx + 1} | {item}")

        except:
            print("\nFile 'arquivo.txt' does not exist! If your first time here, try create a new contact first.\n")
            
if __name__ == "__main__":

    schedule = Schedule()


    while True:
        user = int(input("\nWhat would you like to do? \n 1-List all contacts \n 2-Create a new contact \n 3-Exit \n Option: "))
        print("\n")
        if user == 1:
            schedule.ListContacts()
            
        elif user == 2:
            schedule.addContact()
            continue
        else:
            break
