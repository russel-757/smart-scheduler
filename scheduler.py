exams = []


def add_exam():
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter assigned room: ")
    exams.append({"name": name, "date": date, "time": time, "room": room})
    print("✔ Exam added successfully.\n")


def view_exams():
    if not exams:
        print(" No exams scheduled.\n")
    else:
        print("\n--- All Exams ---")
        for i, exam in enumerate(exams):
            print(f"{i + 1}. {exam['name']} | {exam['date']} | {exam['time']} | Room: {exam['room']}")
        print()


def edit_exam():
    view_exams()
    try:
        index = int(input("Enter exam number to edit: ")) - 1
        if 0 <= index < len(exams):
            exams[index]["name"] = input("New exam name: ")
            exams[index]["date"] = input("New exam date (YYYY-MM-DD): ")
            exams[index]["time"] = input("New exam time (HH:MM): ")
            exams[index]["room"] = input("New assigned room: ")
            print("✔ Exam updated successfully.\n")
        else:
            print(" Invalid exam number.\n")
    except:
        print(" Invalid input.\n")


def delete_exam():
    view_exams()
    try:
        index = int(input("Enter exam number to delete: ")) - 1
        if 0 <= index < len(exams):
            removed = exams.pop(index)
            print(f"✔ Exam '{removed['name']}' deleted.\n")
        else:
            print(" Invalid exam number.\n")
    except:
        print(" Invalid input.\n")


def menu():
    while True:
        print("==== Smart Scheduler ====")
        print("1. Add New Exam")
        print("2. View All Exams")
        print("3. Edit an Exam")
        print("4. Delete an Exam")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print(" Invalid option. Try again.\n")


menu()