import databaseHelper as dbHelper

database_fileName = "door_locker_info"


def initialization():
    if not dbHelper.isfile(database_fileName):
        # Create empty user list information file
        dbHelper.json_to_file([], database_fileName)


def prompt_with_user_list(users_list: []):
    if users_list.__len__() < 1:
        print("")
        print("No users found to be able to modify presence.")
        print("")
        return

    index = -1

    print("")
    print("List of users present in the house")
    for user in users_list:
        index += 1
        print("{} : UserName = {}, User_inside = {}".format(index, user["user_name"], user["is_home"]))

    print("")
    user_index = input("Please select a number to invert the presence of the user")

    while not user_index.isdigit() or (int(user_index) < 0 or int(user_index) > index):
        user_index = input("Please select the number to invert the presence of the user: ")

    return int(user_index)


def user_choice():
    print("")
    return input("""What would you like to do?
    0: Modify list of users inside the house
    1: View list of users in the house
    """)


def display_current_information(message):
    print("")
    print("")
    print("Your existing information ", message)
    print("")
    print("")


if __name__ == "__main__":
    m = []
    a = {
        "is_home": "0",
        "temperature": "36",
        "user_name": "salman"
    }

    m.append(a)
    m.append(a)
    m.append(a)

    import json

    s = json.dumps(m)
    ss = json.loads(s)

    # print(ss)

    i = prompt_with_user_list(ss)

    print(ss[i])
