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
        self.load()

    def load(self):
        """Read address_book.csv file as instance of AddressBook"""
        with open("address_book.csv", "r+", encoding="utf8", newline="") as file:
            csvreader = csv.reader(file, delimiter=";")
            next(csvreader)
            read_file_list = list(csvreader)
            for row in read_file_list:
                self.people.append(Person(*row))

    def save(self):
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

        try:
            for row in self.people:
                dispatcher2 = {
                    "1": row.name,
                    "2": row.surname,
                    "3": row.email,
                    "4": row.phone_num,
                }
                if search_request in dispatcher2[argument]:
                    result.append(row)
                    print(row)
        except KeyError:
            pass
        if len(result) == 0:
            print("Find nothing, try again")
        return result

    def browse_addr_book(self):
        """Browse Address book to screen"""
        n = 15
        print(f"{TITLE[0]:<{n}}{TITLE[1]:<{n}}{TITLE[2]:<{2*n}}{TITLE[3]:<{2*n}}")
        print(*self.people, sep="\n")

    def run(self):
        """Start using address book"""
        print("Type action:")
        argument = input(
            "1 - Browse; 2 - Add; 3 - Modify; 4 - Delete; 5 - Search; 0 - Exit \n"
        )
        dispatcher = {
            "1": self.browse_addr_book,
            "2": self.add_person,
            "3": self.modify_person,
            "4": self.delete_person,
            "5": self.search_person,
            "0": self.stop_program,
        }
        try:
            dispatcher[argument]()
        except KeyError:
            pass

    def stop_program(self):
        """Stop program execution"""
        global EXIT
        EXIT = False
        self.save()


if __name__ == "__main__":
    addr_book = AddressBook()
    while EXIT:
        addr_book.run()
