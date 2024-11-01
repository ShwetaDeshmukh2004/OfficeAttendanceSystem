from datetime import datetime

office_info = []

def entry(name):
    for info in office_info:
        if info["name"] == name and info["status"] == "entered":
            print(f"{name} is already in the office and cannot enter again without exiting.")
            return
    entry_time = datetime.now()
    office_info.append({"name": name, "entry_time": entry_time, "status": "entered"})
    print(f"{name} entered the office at {entry_time}")

def exit(name):
    exit_time = datetime.now()
    for info in office_info:
        if info["name"] == name and info["status"] == "entered":
            info["exit_time"] = exit_time
            info["status"] = "exited"
            print(f"{name} left the office at {exit_time}")
            return
    print(f"{name} is not currently in the office.")

def count_people_in_office():
    current_count = sum(1 for info in office_info if info["status"] == "entered")
    print(f"People currently in the office: {current_count}")
    return current_count

while True:
    print("\nOptions:")
    print("1. Enter the office")
    print("2. Exit the office")
    print("3. Show current count of people in the office")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter the name of the person entering: ")
        entry(name)
    elif choice == "2":
        name = input("Enter the name of the person exiting: ")
        exit(name)
    elif choice == "3":
        count_people_in_office()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose again.")
