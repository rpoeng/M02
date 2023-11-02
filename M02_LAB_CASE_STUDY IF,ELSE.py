#Robert K Poeng
#Dean's List Verification
#This Program will allow faculty members to check if a student makes it onto the Dean's List or the Honor
#Allows user to enter student's GPA

# Initialize an empty list to store student records
student_records = []

while True:
    # Ask for the student's last name, 'ZZZ' to quit
    last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ")
    
    if last_name == 'ZZZ':
        break  # Exit the loop if 'ZZZ' is entered
    
    # Prompts user for the student's first name
    first_name = input("Enter the student's first name: ")
    
    # Prompts user for students GPA
    gpa = float(input("Enter the student's GPA: "))
    
    # Check if the student's GPA is 3.5 or greater for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    # Check if the student's GPA is 3.25 or greater for Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    
    # Keeps Track of the information inputted for one student so it can be printed out.
    student_record = {
        'first_name': first_name,
        'last_name': last_name,
        'gpa': gpa
    }
    
   