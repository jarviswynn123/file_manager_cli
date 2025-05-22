import sys
import os
import datetime
import argparse
import getpass
import hashlib

user_name = getpass.getuser()

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
        "8. Verify log file\n" \
        "9. Erase log file\n" \
        "10. Exit\n").strip() \
        
        if user_input.strip() == "1":
            view_all_files()
            print("viewing all files")

        if user_input.strip() == "2":
            user_input_file = input("Input the name of the file that you want to create\n")
            create_new_file(user_input_file)
            print("creating new file")

        if user_input.strip() == "3":
            file_input = input("input the file you want to find\n")
            print("searching for file")
            search_files(file_input)

        if user_input.strip() == "4":
            file_name = input("Please enter the name of the file that you want to delete!\n")
            print("Deleting File")
            delete_file(file_name)

        if user_input.strip() == "5":
            file_name = input("Please enter the name of the file that you want to rename!\n")
            new_file_name = input("Please enter the what you want to rename the file\n")
            print("Renaming file")
            rename_file(file_name, new_file_name)

        if user_input.strip() == "6":
            pass

        if user_input.strip() == "7":
            pass

        if user_input.strip() == "8":
            file_name = input("Name of the Log you want to verify\n")
            print("Verifying Log File...")
            verify_logs(file_name)
            sys.exit(0)

        if user_input.strip() == "9":
            log_file = input("Type the log file that you would like to erase!\n")
            print("Erasing log file...")
            erase_log_file(log_file)
            sys.exit(0)


        if user_input.strip() == "10":
            print("Exiting...")
            add_log_file("activity.log", user_name, "Application Exited")
            sys.exit(0)




def view_all_files():
    directory = "/home/jarvismwynn/python/file_tool_cli"
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            print(file_path)
            add_log_file("activity.log", user_name, f"{file_path} FILE VIEWED")


def create_new_file(file):
    content = input(f"Enter the content of {file}\n")
    directory = "/home/jarvismwynn/python/file_tool_cli"

    file_path = os.path.join(directory, file)

    with open(file_path, "w") as new_file:
        new_file.write(content)

    add_log_file("activity.log", user_name, f"{new_file} FILE CREATED")


def rename_file(old_file, new_file):
    directory = "/home/jarvismwynn/python/file_tool_cli"
    old_path = os.path.join(directory, old_file)
    new_path = os.path.join(directory, new_file)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_file} -> {new_file}")
        add_log_file("activity.log", user_name, f"{old_file} - FILE RENAMED TO {new_file}")
    else:
        print("File not found")



def search_files(keyword):
    directory = "/home/jarvismwynn/python/file_tool_cli"
    found = False
    for file in os.listdir(directory):
        if keyword.lower() in file.lower():
            print(f"Found: {os.path.join(directory, file)}")
            add_log_file("activity.log", user_name, f"SEARCH HIT: {file}")
            found = True
    if not found:
        print("File not found")
        add_log_file("activity.log", user_name, f"FILE SEARCH: No match for {keyword}")

    

def delete_file(file_name):
    directory = "/home/jarvismwynn/python/file_tool_cli"
    path = os.path.join(directory, file_name)
    if os.path.exists(path):
        os.remove(path)
        print(f"{file_name} deleted")
    else:
        print("File not found")
    add_log_file("activity.log", user_name, f"{path} FILE DELETED")


def move_file(file_name, new_directory):
    pass

def copy_file(file_name, new_directory):
    pass

def rotate_log_file(file, max_lines):
    if not os.path.exists(file):
        return
    
    line_count = 0
    with open(file, "r") as fp:
        for line in fp:
            line_count += 1

    if line_count > max_lines:
        n = 1
        while True:
            rotated_name = file.replace(".log", f".{n}.log")
            if not os.path.exists(rotated_name):
                break
            n+=1 

        os.rename(file, rotated_name)

def add_log_file(file, message, user):
    rotate_log_file(file, max_lines = 500)
    directory = "/home/jarvismwynn/python/file_tool_cli"
    file_path = os.path.join(directory, file)

    now = datetime.datetime.now()
    datetime_string = now.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{datetime_string}] {user} {message}\n"

    if not os.path.exists(file_path):
        with open(file_path, "w") as fp:
            fp.write(log_line)

    else:
        with open(file_path, "a") as fp:
            fp.write(log_line)


    with open(file_path, "r") as file:
        log_content = file.read()

    hash = hashlib.sha256(log_content.encode("utf-8")).hexdigest()

    with open(file_path + ".sha256", "w") as file:
        file.write(hash)


def verify_logs(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()

    calculated_hash = hashlib.sha256(file_content.encode("utf-8")).hexdigest()

    with open(file_path + ".sha256", "r") as hash_file:
        stored_hash = hash_file.read().strip()

    if calculated_hash == stored_hash:
        print("Log is unmodified")

    else:
        print("Log hash been tampered with")

    add_log_file("activity.log", user_name, f"LOG VERIFICATION ATTEMPT")
    



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
    parser.add_argument("--verify", metavar="LOGFILE", help="Verify Log file")
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
    elif args.verify:
        log_path = os.path.join("/home/jarvismwynn/python/file_tool_cli", args.verify)
        verify_logs(log_path)
        return
    elif args.interactive:
        render_menu()
    else:
        parser.print_help()


    add_log_file("activity.log", "APPLICATION INITIATED", f" [User = {user_name}]")

init()