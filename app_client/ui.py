import databaseHelper as dbHelper


def initialization(info_on_file, message):
    if not dbHelper.isfile("user_information"):
        # Create empty user information file
        dbHelper.json_to_file({}, "user_information")
        info_on_file = False
    message: {} = dbHelper.file_to_json("user_information")
    message["is_home"] = "0"
    message["app_info"] = "1"
    # print(list(message.keys()).__len__())
    if list(message.keys()).__len__() < 3:
        info_on_file = False

    return info_on_file, message


def collect_temperature_preference(message):
    message["temperature"] = input("Please provide your preferred temperature of the room: ")
    while not message["temperature"].replace(".", "").isdigit():
        message["temperature"] = input(
            "Temperature has to be a float or integer, Please provide temperature value again: : ")

    # message["is_home"] = input("Are you currently at home: (yes/no)")
    # while message["is_home"].lower() != "yes" and message["is_home"].lower() != "no":
    #     message["is_home"] = input(
    #         "Presence indication has be a string of either yes or not, please provide your answer again: ")

    return message


def collect_user_name(message):
    message["user_name"] = input("Please provide your name: ")
    while not message["user_name"].isalnum():
        message["user_name"] = input("Name has to be alphaNumeric, Please provide name again: ")
    return message


def user_choice():
    return input("""What would you like to do?
    0: Modify existing information
    1: Remove your existing information
    2: View your existing information

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
