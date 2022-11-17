import csv

TITLE = ["Name", "Surname", "e-mail", "Phone_number"]
EXIT = True


def read_addr_book():
    """Read address_book.csv file and return list of lists with data and first row (titles)"""
    with open("address_book.csv", "r+", encoding="utf8", newline="") as file:
        csvreader = csv.reader(file, delimiter=";")
        next(csvreader)
        read_file_list = list(csvreader)
    return read_file_list


def write_addr_book(data_table):
    """Write into address_book.csv file"""
    with open("address_book.csv", "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(TITLE)
        data_table.sort(key=lambda x: x[0])
        for row in data_table:
            writer.writerow(row)


def brows_addr_book(data_table):
    """Show address book"""
    n = 15
    print(f"{TITLE[0]:<{n}}{TITLE[1]:<{n}}{TITLE[2]:<{n*2}}{TITLE[3]:<{n*2}}")
    for row in data_table:
        print(f"{row[0]:<{n}}{row[1]:<{n}}{row[2]:<{n*2}}{row[3]:<{n*2}}")
    print("")


def add_person(*pers):
    """Add new person to the address book"""
    person = []
    if pers:
        person = pers[0]
    else:
        person.append(input("Add Name - "))
        person.append(input("Add Surname - "))
        person.append(input("Add e-mail - "))
        person.append(input("Add Phone number - "))
    data_table = read_addr_book()
    data_table.append(person)
    write_addr_book(data_table)
    print(f"Done, you have {len(data_table)} people in your address book\n")


def modify_person():
    """Modify person in address book"""
    print("Search person")
    person_list = search_person()
    while len(person_list) != 1:
        print("Search too mach people, specify your search request")
        person_list = search_person()
    person = person_list[0]
    delete_person(person)
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
            modify_person()
    add_person(person)


def delete_person(*pers):
    """Delete person from address book"""
    person = []
    if pers:  # != ():
        person = pers[0]
        data_table = read_addr_book()
        data_table.remove(person)
        write_addr_book(data_table)
        print("The person has been removed")
    else:
        print("Search person for delete")
        person_list = search_person()
        while len(person_list) != 1:
            print("Search too mach people, specify your search request")
            person_list = search_person()
        person = person_list[0]
        delete_person(person)


def finder(col_number, search_request):
    """Find part of word in data_table"""
    data_table = read_addr_book()
    result = []
    for row in data_table:
        try:
            if search_request in row[col_number]:
                result.append(row)
        except:  # pylint: disable=bare-except
            print("Find nothing, try again")
            search_person()
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
        case _:
            print("Incorrect input, try again")
            search_person()
    try:
        if len(res) != 0:
            brows_addr_book(res)
    except:  # pylint: disable=bare-except
        print("--- Nothing found ---\n")
        search_person()
        res = []
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
