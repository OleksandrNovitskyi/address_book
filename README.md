Address Book Program
This is a simple command-line address book program written in Python. It allows you to manage a list of contacts by performing various actions such as
browsing, adding, modifying, deleting, and searching for contacts.

Features

The program provides the following features:
Browse: View the entire address book and display the contact information in a tabular format.
Add: Add a new person to the address book by providing their name, surname, email, and phone number.
Modify: Modify the information of an existing person in the address book by searching for them and updating their details.
Delete: Delete a person from the address book by searching for them and removing their entry.
Search: Search for a person in the address book by specifying a search criterion (name, surname, email, or phone number) and a search request. 
The program will display the matching contacts.

Getting Started
- Make sure you have Python installed on your system.
- Download the address_book.py file.
- Install the csv module if it's not already installed by running pip install csv in your command prompt or terminal.
- Run the program by executing the address_book.py file using Python.

Usage
Upon running the program, you will be presented with a menu of actions to choose from:

1 - Browse: Display the entire address book.
2 - Add: Add a new person to the address book.
3 - Modify: Modify the details of a person in the address book.
4 - Delete: Delete a person from the address book.
5 - Search: Search for a person in the address book.
0 - Exit: Exit the program.
Simply enter the corresponding number for the action you want to perform and follow the prompts to provide the required information.

Note: The program uses a CSV file named address_book.csv to store the contact information. Make sure the file is in the same directory as the main.py 
program file. If you don't get address_book.csv file - you can create it at program by adding new person.

The CSV file is encoded using UTF-8 and uses semicolons as delimiters.
Contact information is sorted alphabetically by the person's name.
When modifying a person's details, the program first searches for the person and then allows you to choose which information to modify.
Error handling for incorrect inputs is minimal in this program.
Feel free to modify and enhance the program according to your needs.
