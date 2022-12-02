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
        n = 10
        return (
            f"{self.name:<{n}}{self.surname:<{n}}{self.email:<{n}}{self.phone_num:<{n}}"
        )


class AddressBook:
    """Represent list of people

    Attributes:
      people: list of Person objects.
    """

    def __init__(self):
        self.people = []

    def __str__(self):
        """Returns a table representation of the address book."""
        n = 10
        res = [f"{TITLE[0]:<{n}}{TITLE[1]:<{n}}{TITLE[2]:<{n}}{TITLE[3]:<{n}}"]
        for person in self.people:
            res.append(str(person))
        return "\n".join(res)

    def read_addr_book(self):
        """Read address_book.csv file and return list of lists with data and first row (titles)"""
        with open("address_book.csv", "r+", encoding="utf8", newline="") as file:
            csvreader = csv.reader(file, delimiter=";")
            next(csvreader)
            read_file_list = list(csvreader)
            for row in read_file_list:
                self.people.append(Person(*row))
        return read_file_list

    def add_person(self, *pers):
        """Add new person to the address book"""
        person = []
        if pers:
            person = pers[0]
        else:
            person.append(input("Add Name - "))
            person.append(input("Add Surname - "))
            person.append(input("Add e-mail - "))
            person.append(input("Add Phone number - "))
        data_table = self.read_addr_book()
        data_table.append(person)
        write_addr_book(data_table)
        print(f"Done, you have {len(data_table)} people in your address book\n")

    def modify_person(self):
        """Modify person in address book"""
        print("Search person")
        person_list = self.search_person()
        while len(person_list) != 1:
            print("Search too mach people, specify your search request")
            person_list = search_person()
        person = person_list[0]
        self.delete_person(person)
        print("Need modify:")
        modif = input("1 - Name; 2 - Surname; 3 - e-mail; 4 - Phone number\n")
        match modif:
            case "1":
                person[0] = input("New name:\n")
            case "2":
                person[1] = input("New surname:\n")
            case "3":
                person[2] = input("New e-mail:\n")
            case "4":
                person[3] = input("New phone number:\n")
            case _:
                print("Incorrect input, try again")
                self.modify_person()
        self.add_person(person)

    def delete_person(self, *pers):
        """Delete person from address book"""
        person = []
        if pers:
            person = pers[0]
            data_table = self.read_addr_book()
            data_table.remove(person)
            write_addr_book(data_table)
            print("The person has been removed")
        else:
            print("Search person for delete")
            person_list = self.search_person()
            while len(person_list) != 1:
                print("Search too mach people, specify your search request")
                person_list = self.search_person()
            person = person_list[0]
            self.delete_person(person)

    def finder(self, col_number, search_request):
        """Find part of word in data_table"""
        data_table = self.read_addr_book()
        result = []
        for row in data_table:
            try:
                if search_request == row[col_number]:
                    result.append(row)
            except:
                print("Find nothing, try again")
                self.search_person()
        return result

    def search_person(self):
        """Search person in address book"""
        print("Search by:")
        argument = input("1 - Name; 2 - Surname; 3 - e-mail; 4 - Phone number\n")

        match argument:
            case "1":
                search_request = input("Search request: ")
                res = self.finder(0, search_request)
            case "2":
                search_request = input("Search request: ")
                res = self.finder(1, search_request)
            case "3":
                search_request = input("Search request: ")
                res = self.finder(2, search_request)
            case "4":
                search_request = input("Search request: ")
                res = self.finder(3, search_request)
            case _:
                print("Incorrect input, try again")
                self.search_person()
        try:
            if len(res) != 0:
                print(addr_book)
        except:
            print("--- Nothing found ---\n")
            self.search_person()
            res = []
        return res


def write_addr_book(data_table):
    """Write into address_book.csv file"""
    with open("address_book.csv", "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(TITLE)
        data_table.sort(key=lambda x: x[0])
        for row in data_table:
            writer.writerow(row)


addr_book = AddressBook()


def do_action():
    """Choose action to do some thing"""
    global EXIT
    print("Type action:")
    argument = input(
        "1 - Browse; 2 - Add; 3 - Modify; 4 - Delete; 5 - Search; 0 - Exit \n"
    )
    match argument:
        case "1":
            addr_book.read_addr_book()
            print(addr_book)
        case "2":
            addr_book.add_person()
        case "3":
            addr_book.modify_person()
        case "4":
            addr_book.delete_person()
        case "5":
            addr_book.search_person()
        case "0":
            EXIT = False
        case _:
            print("Incorrect input")


if __name__ == "__main__":
    while EXIT:
        do_action()
