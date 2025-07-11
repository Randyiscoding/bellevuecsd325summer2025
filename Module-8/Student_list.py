# --------------------------------------------------------
# Name: Randy Easton
# Date: 7/9/2025
# Assignment: Module 8.2 Assignment: JSON Practice
# --------------------------------------------------------
# Purpose:
# Load student data from a JSON file and print it using a class.
# --------------------------------------------------------
import json


def main():

    # Step 1: Load and print original student list
    filename = "student.json"
    student_manager = StudentInfo(filename)
    print("Original Student List:")
    student_manager.viewcurrentstudentlist()

    # Step 2: Add new student (your info)
    print("Adding new student...")
    student_manager.create_new_student("Randy", "Easton", 99999, "reaston@fictionalmail.com")

    # Step 3: Save changes (without prompt)
    student_manager.save(safesave=False)  # Set to True if you want confirmation

    # Step 4: Show updated student list
    print("Updated Student List:")
    student_manager.viewcurrentstudentlist()


class StudentInfo():
    def __init__(self, file):
        """
        Initializes the StudentInfo object with the path to the student JSON file
        Must be full path, Must be JSON file. format for each student should be:
        {
            "F_Name": FirstName,
            "L_Name": LastName,
            "Student_ID": XXXXX (Numerical Characters only)
            "Email": email
        }
        """
        self.file = file

    def viewcurrentstudentlist(self):
        """
        Loads and prints the list of students in Last, First : ID, Email format.
        Reads from the JSON file and prints each entry line by line.
        """
        with open(self.file, 'r') as student_data:
            student_list = json.load(student_data)
            for student in student_list:
                print(f"{student['L_Name']}, {student['F_Name']}: ID = {student['Student_ID']} Email = {student['Email']}")
            print("\n")

    def create_new_student(self, fname, lname, stuID, email):
        """
        creates new student dictionary, must be executed before save or error will occur
        function could cause unintended duplication
        """
        self.new_student = {
            "F_Name": fname,
            "L_Name": lname,
            "Student_ID": int(stuID),
            "Email": email
        }
    def save(self, safesave=True):
        """
        Saves the new student to the JSON file. If 'safesave' is True,
        prompts the user for confirmation before saving.
        """
        if safesave:
            while True:
                print("Are you sure the following student information is accurate? \n Would you like to save? \n ")
                print(self.new_student)
                save = input("Y/N?: ").strip().upper()
                if save == 'Y':
                    break
                elif save == 'N':
                    print("Changes not saved")
                    return None
                else:
                    print("Invalid input try again")

        # Loads The JSON, appends and, saves
        with open(self.file, 'r') as student_data:
            student_list = json.load(student_data)
            student_list.append(self.new_student)

        with open(self.file, 'w') as student_data:
            json.dump(student_list, student_data, indent=4)

        print("\n Student List has been updated \n")
        return None

    def removestudentfromlist(self, stuID):
        with open(self.file, 'r') as student_data:
            student_list = json.load(student_data)
        newlist = [student for student in student_list
                   if student["Student_ID"] != stuID]
        if len(newlist) == len(student_list):
            return "Student Not found"
        else:
            with open(self.file, 'w') as student_data:
                json.dump(newlist, student_data, indent=4)
            for student in student_list:
                if student["Student_ID"] == stuID:
                    print(f"\n {student['F_Name']} {student['L_Name']} has been removed from the list \n")
            return None



# Program starts here
if __name__ == "__main__":
    main()
