import json
import csv

print("Сhoose the action you want to perform! \n\n"
        "Display the languages in which employees work, enter '1' \n"
        "To display employee data, press '2' \n"
        "To find out the average height of employees, enter '3' \n\n"
        )


#Create a json file and fill it with data
def write(data, jsonfile):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(jsonfile, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=5)

m_data = [
        {
            "name": "John Smith",
            "birthday": "02.10.1990",
            "height": 175,
            "weight": 76.5,
            "car": 'true',
            "languages": "Delphi"
        },
        {
            "name": "Alexey Alexeev",
            "birthday": "05.06.1986",
            "height": 197,
            "weight": 101.2,
            "car": 'false',
            "languages": ["Pascal", "Delphi"]
        },
        {
            "name": "Maria Ivanova",
            "birthday": "28.08.1998",
            "height": 165,
            "weight": 56.1,
            "car": 'true',
            "languages": ["C#", "C++", "C"]
        }
]


# The function of changing the json file to csv
def jsontocsv():
    with open('jsonfile.json') as json_file:
        jsondata = json.load(json_file)

    data_file = open('jsonoutput.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(data_file)

    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())

    data_file.close()


# The function of adding to a csv file
def new_user_csv():
    data = {"Miroslav Shagun": "name", "23.12.1993": "birthday", "188": "height",
            "86": "weight", "false": "car", "Python": "languages"}

    with open("jsonoutput.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


# Function for adding new parameters to a json file
def new_user_json():
    new_user = {"name": "Miroslav Shagun",
                "birthday": "23.12.1993",
                "height": 188,
                "weight": 86,
                "car": "false",
                "languages": "Python"}

    with open("jsonfile.json", "r") as f:
        data = json.load(f)
        m_data.append(new_user)
        with open("jsonfile.json", "w", encoding='utf-8') as outfile:
            json.dump(m_data, outfile, ensure_ascii=False, indent=4)


# Data search function by name
def search_by_name(name):
    name_m = input("Enter name: ")
    with open("jsonfile.json", "r") as f:
        for i in json.load(f):
            for key, val in i.items():
                if key == "name" and val == name_m:
                    print(i.items())


# Language filter function
def language_filter(languages):
    languages_enter = input("Enter languages: ")
    with open("jsonfile.json", "r") as f:
        for i in json.load(f):
            for k, v in i.items():
                if k == "languages" and languages_enter in v:
                    print(i.items())


# Search function for average height of employees
def enter_height(height):
    enter_data = input("Enter birthday: ")
    with open("jsonfile.json", "r") as f:
        data = json.load(f)

    counter = 0
    sumheight = 0

    for i in data:
        if i["birthday"][-4:] < enter_data:
            sumheight += i[height]
            counter = counter + 1

    average = sumheight/counter
    print(f"Average growth of employees = {average}")

# the main function of the program
def program():
    user_selection = input("What do you want to choose?: ")

    while True:
        if user_selection == "1":
            language_filter("languages")
            break
        elif user_selection == "2":
            search_by_name("name")
            break
        elif user_selection == "3":
            enter_height("height")
            break
        else:
            print("Incorrect input !!!")
            break

    action = input("Do you want to do something else? (Y/N): ")

    if action == "Y".lower():
        program()
    if action == "N".lower():
        print("The work of the program is completed!")
        StopIteration


write(m_data, "jsonfile.json")
jsontocsv()
new_user_json()
new_user_csv()
program()

