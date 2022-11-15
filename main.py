import csv

TITLE = ["Name", "Surname", "e-mail", "Phone_number"]
EXIT = True


# class Person:
#     """Represent person on address book"""

#     def __init__(self, name="", surname="", email="", phone_num=""):
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.phone_num = phone_num

#     def __str__(self):
#         return [self.name, self.surname, self.email, self.phone_num]


# class AddressBook:
#     """Represent list of people

#     Attributes:
#       people: list of Person objects.
#     """

#     def __init__(self):
#         self.people = []

#     def add_person(self, person):
#         """Adds a person to the address book.

#         person: Person
#         """
#         self.people.append(person)


def read_addr_book():
    """Read address_book.csv file and return list of lists with data and first row (titles)"""
    with open("address_book.csv", "r+", encoding="utf8", newline="") as file:
        csvreader = csv.reader(file, delimiter=";")
        next(csvreader)
        # for row in csvreader:
        #     print("%-12s%-12s%-24s%-24s" % (row[0], row[1], row[2], row[3]))
        # for elem in row:
        #     print(*elem)
        read_file_list = list(csvreader)
    return read_file_list


def write_addr_book(data_table):
    """Write into address_book.csv file"""
    with open("address_book.csv", "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(TITLE)
        for row in data_table:
            writer.writerow(row)


def brows_addr_book(data_table):
    """Show address book"""
    # print("%-12s%-12s%-24s%-24s" % (TITLE[0], TITLE[1], TITLE[2], TITLE[3]))
    n = 10
    print(f"{TITLE[0]:<{n}}{TITLE[1]:<{n}}{TITLE[2]:<{n}}{TITLE[3]:<{n}}")
    for row in data_table:
        print(f"{row[0]:<{n}}{row[1]:<{n}}{row[2]:<{n}}{row[3]:<{n}}")
    print("")


def add_person():
    """Add new person to the address book"""
    name = input("Add Name")
    surname = input("Add Surname")
    email = input("Add e-mail")
    phone_num = input("Add Phone number")
    data_table = read_addr_book()
    data_table.append([name, surname, email, phone_num])
    write_addr_book(data_table)
    print(f"Done, you have {len(data_table)} people in your address book\n")


def modify_person():
    """Modify person in address book"""
    print("Search person")
    person = search_person()


def delete_person():
    """Delete person from address book"""
    pass


def finder(col_number, search_request):
    """Find part of word in data_table"""
    data_table = read_addr_book()
    result = []
    for row in data_table:
        if search_request in row[col_number]:
            result.append(row)
    return result


def search_person():
    """Search person in address book"""
    print("Search by:")
    argument = input("1 - Name; 2 - Surname; 3 - e-mail; 4 - Phone number\n")
    search_request = input("Search request: ")

    match argument:
        case "1":
            res = finder(0, search_request)
        case "2":
            res = finder(1, search_request)
        case "3":
            res = finder(2, search_request)
        case "4":
            res = finder(3, search_request)
    if len(res) != 0:
        brows_addr_book(res)
    else:
        print("--- Nothing found ---\n")
    return res


def do_action():
    """Choose action to do some thing"""
    global EXIT
    print("Type action:")
    argument = input(
        "1 - Browse; 2 - Add; 3 - Modify; 4 - Delete; 5 - Search; 0 - Exit \n"
    )
    match argument:
        case "1":
            brows_addr_book(read_addr_book())
        case "2":
            add_person()
        case "3":
            modify_person()
        case "4":
            delete_person()
        case "5":
            search_person()
        case "0":
            EXIT = False
        case _:
            print("Incorrect input")


if __name__ == "__main__":
    while EXIT:
        do_action()
