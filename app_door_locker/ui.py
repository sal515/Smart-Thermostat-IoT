import databaseHelper as dbHelper
import json


def initialization():
    if not dbHelper.isfile("user_information"):
        # Create empty user list information file
        dbHelper.json_to_file([], "user_information")


def prompt_with_user_list(users_list: []):
    if users_list.__len__() < 1:
        print("")
        print("No users found to be able to modify presence.")
        print("")
        return

    index = -1
    print("List of users present in the house")
    for user in users_list:
        index += 1
        print("{} : UserName = {}, User_inside = {}".format(index, user["user_name"], user["is_home"]))

    user_index = input("Please select a number to invert the presence of the user")

    while not user_index.isdigit() or (int(user_index) < 0 or int(user_index) > index):
        user_index = input("Please select the number to invert the presence of the user: ")

    return int(user_index)


def user_choice():
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


# # =================================== App Variables ========================
# info_on_file = True
# choices = 3
# message: {} = {}
#
# # =================================== App logic ========================

# # Initialization of the client application
# initialization()
#
#
#
#
#
# while True:
#
#     if not info_on_file:
#         print("Program setup.")
#         print("")
#
#         collect_user_name(message)
#         collect_temperature_preference(message)
#
#         dbHelper.json_to_file(message, "user_information")
#         info_on_file = True
#         # print(message)
#
#     choice = user_choice()
#     while not choice.isdigit() and not (int(choice) < choices):
#         print("Invalid input, please try again")
#         choice = user_choice()
#
#     if choice == "0":
#         collect_temperature_preference(message)
#         dbHelper.json_to_file(message, "user_information")
#
#     elif choice == "1":
#         message = {}
#         dbHelper.json_to_file(message, "user_information")
#         info_on_file = False
#
#     elif choice == "2":
#         display_current_information(message)


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
