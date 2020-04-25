import databaseHelper as dbHelper


def initialization(info_on_file, message):
    if not dbHelper.isfile("user_information"):
        # Create empty user information file
        message["is_home"] = "0"
        message["app_info"] = "1"
        dbHelper.json_to_file(message, "user_information")
        info_on_file = False
    message: {} = dbHelper.file_to_json("user_information")

    if message["app_info"] == "-1" or list(message.keys()).__len__() < 3:
        info_on_file = False

    return info_on_file, message


def collect_temperature_preference(message):
    message["temperature"] = input("Please provide your preferred temperature of the room: ")
    while not message["temperature"].replace(".", "").isdigit():
        message["temperature"] = input(
            "Temperature has to be a float or integer, Please provide temperature value again: : ")

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
