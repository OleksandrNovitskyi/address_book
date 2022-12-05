import csv

TITLE = ["Name", "Surname", "e-mail", "Phone_number"]
EXIT = True


class Person:
    """Represent person on address book"""

    def __init__(self, name="", surname="", email="", phone_num=""):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_num = phone_num

    def __str__(self):
        n = 15
        return f"{self.name:<{n}}{self.surname:<{n}}{self.email:<{2*n}}{self.phone_num:<{2*n}}"

    def __iter__(self):
        return iter([self.name, self.surname, self.email, self.phone_num])


class AddressBook:
    """Represent list of people

    Attributes:
      people: list of Person objects.
    """

    def __init__(self):
        self.people = []
        self.load_addr_book()

    def load_addr_book(self):
        """Read address_book.csv file as instance of AddressBook"""
        with open("address_book.csv", "r+", encoding="utf8", newline="") as file:
            csvreader = csv.reader(file, delimiter=";")
            next(csvreader)
            read_file_list = list(csvreader)
            for row in read_file_list:
                self.people.append(Person(*row))

    def save_addr_book(self):
        """Write into address_book.csv file"""
        with open("address_book.csv", "w", encoding="utf8", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(TITLE)
            for row in self.people:
                writer.writerow(row)

    def add_person(self, *pers):
        """Add new person to the address book"""
        if pers:
            person = pers[0]
        else:
            name = input("Add Name - ")
            surname = input("Add Surname - ")
            email = input("Add e-mail - ")
            phone_num = input("Add Phone number - ")
            person = Person(name, surname, email, phone_num)
        self.people.append(person)
        print(f"Done, you have {len(self.people)} people in your address book\n")

    def modify_person(self):
        """Modify person in address book"""
        print("Search person")
        person_list = self.search_person()
        person = person_list[0]
        self.delete_person(person)
        print("Need modify:")
        modif = input("1 - Name; 2 - Surname; 3 - e-mail; 4 - Phone number\n")
        match modif:
            case "1":
                person.name = input("New name:\n")
            case "2":
                person.surname = input("New surname:\n")
            case "3":
                person.email = input("New e-mail:\n")
            case "4":
                person.phone_num = input("New phone number:\n")
            case _:
                print("Incorrect input, try again")
                self.modify_person()
        self.add_person(person)

    def delete_person(self, *pers):
        """Delete person from address book"""
        person = []
        if pers:
            person = pers[0]
            self.people.remove(person)
            print("The person has been removed")
        else:
            print("Search person for delete")
            person_list = self.search_person()
            person = person_list[0]
            self.delete_person(person)

    def search_person(self):
        """Search person in address book"""
        print("Search by:")
        argument = input("1 - Name; 2 - Surname; 3 - e-mail; 4 - Phone number\n")
        result = []
        search_request = input("Search request: ")
        match argument:
            case "1":
                for row in self.people:
                    if search_request in row.name:
                        result.append(row)
            case "2":
                for row in self.people:
                    if search_request in row.surname:
                        result.append(row)
            case "3":
                for row in self.people:
                    if search_request in row.email:
                        result.append(row)
            case "4":
                for row in self.people:
                    if search_request in row.phone_num:
                        result.append(row)
            case _:
                print("Incorrect input, try again")
                self.search_person()
        if len(result) != 0:
            print(row)
        else:
            print("Find nothing, try again")
        return result

    def browse_addr_book(self):
        """Browse Address book to screen"""
        n = 15
        print(f"{TITLE[0]:<{n}}{TITLE[1]:<{n}}{TITLE[2]:<{2*n}}{TITLE[3]:<{2*n}}")
        print(*self.people, sep="\n")


addr_book = AddressBook()


def stop_program():
    """Stop program execution"""
    global EXIT
    EXIT = False
    addr_book.save_addr_book()


def do_action():
    """Choose action to do some thing"""
    print("Type action:")
    argument = input(
        "1 - Browse; 2 - Add; 3 - Modify; 4 - Delete; 5 - Search; 0 - Exit \n"
    )
    dispatcher = {
        "1": addr_book.browse_addr_book,
        "2": addr_book.add_person,
        "3": addr_book.modify_person,
        "4": addr_book.delete_person,
        "5": addr_book.search_person,
        "0": stop_program,
    }
    try:
        dispatcher[argument]()
    except KeyError:
        print("Wrong command")


if __name__ == "__main__":
    while EXIT:
        do_action()
