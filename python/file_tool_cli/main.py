import sys
import os
import datetime
import argparse

def render_menu():
    while True:
        user_input = input("Choose an option:\n" \
        "1. View all files\n" \
        "2. Create a new file\n" \
        "3. Find a file\n" \
        "4. Delete a file\n" \
        "5. Rename a file\n" \
        "6. Move a file\n" \
        "7. Copy a file\n" \
        "9. Erase log file\n" \
        "10. Exit\n").strip() \
        
        if user_input.strip() == "1":
            view_all_files()
            print("viewing all files")

        if user_input.strip() == "2":
            create_new_file()
            print("creating new file")

        if user_input.strip() == "3":
            file_input = input("input the file you want to find")
            file_input2 = input("input the path of the file you want to find")
            print("searching for file")
            search_files(file_input, file_input2)

        if user_input.strip() == "4":
            file_name = input("Please enter the name of the file that you want to delete!\n")
            print("Deleting File")
            delete_file(file_name)

        if user_input.strip() == "5":
            file_name = input("Please enter the name of the file that you want to rename!\n")
            new_file_name = input("Please enter the what you want to rename the file")
            print("Renaming file")
            rename_file(file_name, new_file_name)

        if user_input.strip() == "6":
            pass

        if user_input.strip() == "7":
            pass

        if user_input.strip() == "7":
            file_name = input("Please enter the name of the file that you want to delete!\n")
            print("Deleting File")
            delete_file(file_name)

        if user_input.strip() == "9":
            log_file = input("Type the log file that you would like to erase!\n")
            print("Erasing log file...")
            erase_log_file(log_file)
            sys.exit(0)


        if user_input.strip() == "10":
            print("Exiting...")
            add_log_file("activity.log", "Application Exited")
            sys.exit(0)




def view_all_files():
    directory = "/home/jarvismwynn/python/file_tool_cli"
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            print(file_path)
            add_log_file("activity.log", f"{file_path} FILE VIEWED")

def create_new_file():
    file_name_input = input("Enter the name of the file.\n Make sure to add the file extension\n")
    file_content_input = input(f"Enter the content of {file_name_input}\n")

    print(file_name_input)
    print(file_content_input)

    directory = "/home/jarvismwynn/python/file_tool_cli"
    file_path = os.path.join(directory, file_name_input)
    with open(file_path, "w") as new_file:
        new_file.write(file_content_input)
    add_log_file("activity.log", f"{new_file} FILE CREATED")

def rename_file(old_file, new_file):
    os.rename(old_file, new_file)
    add_log_file("activity.log", f"{old_file} - FILE RENAMED TO {new_file}")

def search_files(file_name, directory):
    for file in os.listdir(directory):
        if file == file_name:
            print(f"Found: {os.path.join(directory, file)}")
            return
    print("File not found")
    add_log_file("activity.log", f"FILE SEARCH INITIATED FOR {file}")

def delete_file(f):
    directory = "/home/jarvismwynn/python/file_tool_cli"
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if path == f:
            os.remove(file)
    add_log_file("activity.log", f"{path} FILE DELETED")


def move_file(file_name, new_directory):
    pass

def copy_file(file_name, new_directory):
    pass


def add_log_file(file, message):
    directory = "/home/jarvismwynn/python/file_tool_cli"
    file_path = os.path.join(directory, file)

    now = datetime.datetime.now()
    datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{datetime_string}] {message}\n"

    if not os.path.exists(file_path):
        with open(file_path, "w") as fp:
            fp.write(log_line)

    else:
        with open(file_path, "a") as fp:
            fp.write(log_line)

def erase_log_file(log_name):
    with open(log_name, "r+") as file:
        file.truncate(0)
    

        

def init():
    parser = argparse.ArgumentParser(description="CLI File Tool")

    parser.add_argument("--view", action="store_true", help="View all files in the directory")
    parser.add_argument("--create", metavar="FILENAME", help="Create a new file with that name")
    parser.add_argument("--delete", metavar="FILENAME", help="Delete a file by name")
    parser.add_argument("--rename", nargs=2, metavar=("OLD", "NEW"), help="Rename a file")
    parser.add_argument("--search", metavar="KEYWORD", help=("Search for files by keyword"))
    parser.add_argument("--interactive", action="store_true", help="Launch the interactive menu")

    args = parser.parse_args()

    if args.view:
        view_all_files()
    elif args.create:
        create_new_file(args.create)
    elif args.delete:
        delete_file(args.delete)
    elif args.rename:
        rename_file(args.rename[0], args.rename[1])
    elif args.search:
        search_files(args.search)
    elif args.interactive:
        render_menu()
    else:
        parser.print_help()

    add_log_file("activity.log", "APPLICATION INITIATED")
    # render_menu()

init()