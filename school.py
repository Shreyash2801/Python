#Project 1: Basic school administration tool
import csv
def write_into_csv(info_list):
    with open('student info.csv', 'a', newlines='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow( ["Name", "Age", "Contact Number", "E-Mail ID"])
        writer.writerow(info_list)
if_name_== '_main_':
condition = True

while(condition):
   student_info=input("Enter student information in the following format (Name Age Contact Number E-mail ID): ")
   print("Entered information:"+ student_info)

   #split
   student_info_list = student_info.split(' ')
   print("Entered split up information is:" + str(istudent_info_list))

   print("\nThe entered information is -\nName: {}\nAge: {}\nContact number: {}\nE-Mail ID: {}".format()
   write_into_csv(student_info_list)

   condition_check = input("Enter (yes/no) if you want to enter information for another students ")
   if condition_check == "yes":
     condition = True
   elif condition_check == "no":
     condition = False