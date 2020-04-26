import databaseHelper as dbHelper

database_fileName = "thermostat_user_info"


def initialization():
    if not dbHelper.isfile(database_fileName):
        # Create empty user list information file
        dbHelper.json_to_file([], database_fileName)


def display_current_information():
    print("")
    print("")
    print("Your existing information ")
    print("")
    print("")
