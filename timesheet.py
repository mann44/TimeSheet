#Author: Manthan Gajjar
#Timesheet basic application written in Python

#Working Hours for a Week
#Run the program. Click an option A = Add :: S = Search :: D = Delete :: E = Edit :: R = Report :: Q = Quit
#To add time Type A, press enter, write In for Clock-in, and Out for Clock Out
#Search based on names, to see Total Hours worked
#Delete based on Date, only manager can detele records
#Edit data by selecting an Employee and a Date, Only manager can edit the record.
#Report of employee, only manager can see it

import datetime
import time
import fileinput
from operator import index

#Using Add to add data in file first, We have to add clock in time 

def Add():
    Time_emp = input("Enter 'IN' For Clockin or Enter 'Out' for Clockout: ")
    #Change it to upper to get rid of input error
    Time = Time_emp.upper()
    if Time == "OUT":
        Clock_out()
    elif Time == "IN":

        #Open the Timecard.txt file in append mode
        TimeCard_file = open('TimeCard.txt', 'a')

        # Add clock in time in file with current time.
        EmpName = input('Enter Your Name:')
        Emp_Name = EmpName.upper()
        now = datetime.datetime.now()
        print(file)
        Current  = now.strftime("%Y-%m-%d")
        Clock_in = now.strftime("%H:%M")

        #Append data to the file
        TimeCard_file.write(Emp_Name + " ")
        TimeCard_file.write(Current + " ")
        TimeCard_file.write(Clock_in)
        print("Your Current Date is:",Current)
        print("Your Clock in Time is :", Clock_in)
        TimeCard_file.write('\n')

        #Close the file
        TimeCard_file.close()
    
    #Check if user wants to add another record to the file
    func = input("Enter Q to quit or Press M for main menu:")
    if func == "Q" or func =="q":
        quit()
    elif func == "M" or func =="m":
        return main()
    else:
        print("Incorrect input, Please Try Again \n")

#First Ask for employee name so can add clock out time for same person.
def Clock_out():
    found = False
    val = 'x'
    #input the name what you want to search
    employee_name = input("Please Enter Your Name:")
    employee = employee_name.upper()
    #open the time card file and search name
    TimeCard_file = open("TimeCard.txt", 'r')
    TimeCard = TimeCard_file.readline()

    #read the file if you have entered any name
    while TimeCard != '':
        found = TimeCard.startswith(employee)
        if found:
            val = TimeCard
        TimeCard = TimeCard_file.readline()
    TimeCard_file.close()

    if val != '':
        now = datetime.datetime.now()
        #Add clouckout time in file with current time
        Current  = now.strftime("%Y-%m-%d")
        Clock_out = now.strftime("%H:%M")
        search = val
        print(search.rstrip('\n') + ' ' + Clock_out)
        print("You are Clocked out successfully")

        #open the file
        fn = "TimeCard.txt"
        f = open(fn)
        output = []
        #for loop i you find search record
        for line in f:
            if line.startswith(val):
                output.append(line.replace(line, line.rstrip('\n') + ' ' + Clock_out) + '\n')
            else:
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()

    #open the time card file and search name
    TimeCard_file = open('TimeCard.txt', 'r')

    TimeCard = TimeCard_file.readline()
    sum_h = 0
    sum_m = 0

    # read the file if you have entered any name
    while TimeCard != '':
        found =  TimeCard.startswith(employee)

        if found:
            start = TimeCard[-12:-7]
            end = TimeCard[-6:-1]
            #split the date
            clock_in = start.split(':')
            clock_out = end.split(':')

            #convert tiem from string to integer
            clock_out_int_h = int(clock_out[0])
            clock_out_int_m = int (clock_out[1])
            clock_in_int_h = int(clock_in[0])
            clock_in_int_m = int (clock_in[1])

            #calculate Working Hours
            if clock_out_int_m > clock_in_int_m:
                hours = (clock_out_int_h - clock_in_int_h)
                minutes = (clock_out_int_m - clock_in_int_m)
            else:
                hours = (clock_out_int_h - clock_in_int_h) - 1
                minutes = 60 - (clock_in_int_m - clock_out_int_m)
            sum_h += hours
            sum_m += minutes
        TimeCard = TimeCard_file.readline()

    #Collect Total Hours of the Employee
    if sum_m > 60:
        sum = (sum_m / 60)
        split_min = str(sum).split('.')
        int_part = int(split_min[0])
        decimal = int((sum - int_part) * 60)
        Total_hours = sum_h + int_part
        print("Weekly Working Hours is:", Total_hours, "Hours and", decimal, "Minutes", '\n')
    else:
        print("Weekly Working Hours is:", sum_h, "Hours and", sum_m,"Minutes", '\n')

    #added function to make decision if you want to work on this file or exit

    func = input("Enter Q to quit or Press M for main menu:")
    if func == "Q" or func =="q":
        quit()
    elif func == "M" or func =="m":
        return main()
    else:
        print("Incorrect input, Please Try Again \n")

#This function will display all working time for all employee
def TimeReport():
    #open time card
    TimeCard_file = open('TimeCard.txt','r')
    TimeCard = TimeCard_file.readline()
    #read the rest of the file
    while TimeCard != '':
        #Display the record
        print('Employee Hours:', TimeCard)

        #Read the next Description
        TimeCard = TimeCard_file.readline()
    #close the file
    TimeCard_file.close()

    #Added function to make decision if want to work or exit
    func = input("Enter Q to quit or Press M for main menu:")
    if func == "Q" or func =="q":
        quit()
    elif func == "M" or func =="m":
        return main()
    else:
        print("Incorrect input, Please Try Again \n")

def Edit():
    found =  False

    #input the name you want to search
    EmpName = input("Please Enter Employee Name:")
    employee = EmpName.upper()

    #open the time card file and search name
    TimeCard_file = open('TimeCard.txt','r')
    TimeCard = TimeCard_file.readline()


    #read the file if you have entered any name
    while TimeCard != '':
        found = TimeCard.startswith(employee)
        if found:
            print(TimeCard)

        TimeCard = TimeCard_file.readline()
    TimeCard_file.close()
    
    Date = input("Enter the Date you want to edit:")
    search = (employee + " " + Date)

    #Open the file
    fn = "TimeCard.txt"
    f = open(fn)
    output = []
    #for loop i you find search record
    for line in f:
        if not line.startswith(search):
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()

    #open the TimeCard.txt file in append mode
    TimeCard_file = open('TimeCard.txt', 'a')
    print("enter Clocl in and Clock out for",employee)

    Clock_in = input("Enter Clock In time:")
    Clock_out = input("Enter Clock Out time:")

    TimeCard_file.write(employee + " ")
    TimeCard_file.write(Date + " ")
    TimeCard_file.write(str(Clock_in) + " ")
    TimeCard_file.write(str(Clock_out) + " ")
    TimeCard_file.write('\n')

    #Close the file
    TimeCard_file.close()
    
    #Check if user wants to add another record to the file
    func = input("Enter Q to quit or Press M for main menu:")
    if func == "Q" or func =="q":
        quit()
    elif func == "M" or func =="m":
        return main()
    else:
        print("Incorrect input, Please Try Again \n")

#This function will search emplyee and his working hours
def Search():
    found = False

    EmpName  =  input("Please enter Employee Name:")
    search = EmpName.upper()

    #open the time card file and search name
    TimeCard_file = open('TimeCard.txt', 'r')

    TimeCard = TimeCard_file.readline()
    sum_h = 0
    sum_m = 0

    #read the file if you have entered any name
    while TimeCard != '':
        found = TimeCard.startswith(search)
        if found:
            #print(TimeCard)
            start = TimeCard[-12:-7]
            #print("start",start)
            end = TimeCard[-6:-1]
            print("end",end)
            #split the date
            clock_in = start.split(':')
            #print(clock_in)
            clock_out = end.split(':')
            #print(clock_out)

            #convert tiem from string to integer
            clock_out_int_h = int(clock_out[0])
            clock_out_int_m = int (clock_out[1])
            clock_in_int_h = int(clock_in[0])
            clock_in_int_m = int (clock_in[1])

            #calculate Working Hours
            if clock_out_int_m > clock_in_int_m:
                hours = (clock_out_int_h - clock_in_int_h)
                minutes = (clock_out_int_m - clock_in_int_m)
                #print("Total Hours Worked:", hours, 'Hours and', minutes,"Minutes", '\n' )
            else:
                hours = (clock_out_int_h - clock_in_int_h) - 1
                minutes = 60 - (clock_in_int_m - clock_out_int_m)
            sum_h += hours
            sum_m += minutes
            print("Total Hours Worked:", hours, 'Hours and', minutes,"Minutes", '\n' )
        TimeCard = TimeCard_file.readline()

    #Collect Total Hours of the Employee
    if sum_m > 60:
        sum = (sum_m / 60)
        split_min = str(sum).split('.')
        int_part = int(split_min[0])
        decimal = int((sum - int_part) * 60)
        Total_hours = sum_h + int_part
        print("Total Working Hours is:", Total_hours, "Hours and", decimal, "Minutes", '\n')
    else:
        print("Total Working Hours is:", sum_h, "Hours and", sum_m,"Minutes", '\n')

    #close the file
    TimeCard_file.close()
    #added function to make decision if you want to work on this file or exit

    func = input("Enter Q to quit or Press M for main menu:")
    if func == "Q" or func =="q":
        quit()
    elif func == "M" or func =="m":
        return main()
    else:
        print("Incorrect input, Please Try Again \n")

#this fucntion will remove unwanted data from report
def Delete():
    found = False


    #input the name you want to search
    EmpName = input("Please Enter Employee Name:")
    employee = EmpName.upper()

    #open the time card file and search name
    TimeCard_file = open('TimeCard.txt','r')
    TimeCard = TimeCard_file.readline()


    #read the file if you have entered any name
    while TimeCard != '':
        found = TimeCard.startswith(employee)
        if found:
            print(TimeCard)

        TimeCard = TimeCard_file.readline()
    TimeCard_file.close()
    TimeCard = filter(lambda x: not x.isspace(), TimeCard)
    #Find the blank space and delete it
    Date = input("Enter the date you want to delete:")
    search = (employee + '' + Date)

    #open the file
    fn = 'TimeCard.txt'
    f = open(fn)
    output = []
    #for loop i you find search record
    for line in f:
        if not line.startswith(search):
            output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.write("".join(TimeCard))
    f.close()

    print("You successfully deleted " + search + "'s Record")
    func = input("Enter Q to quit or Press M for main menu:")
    if func == "Q" or func =="q":
        quit()
    elif func == "M" or func =="m":
        return main()
    else:
        print("Incorrect input, Please Try Again \n")

#Add date in time Card
def main():
    #Select the option what you like to do in you time card
    print("What would you like to do in Time Card System?")
    print("A = Add :: S = Search :: D = Delete :: E = Edit :: R = Report :: Q = Quit")
    func = input("Please select a function from the list above:")

    #Use while loop to enter in time card as selected option
    while func == '' or func != 'A'  or func != 'a' or func != 'S' or func != 's' or func != 'D' or func != 'd' or func != 'E' or func != 'e' or func != 'R' or func != 'r':
        if func == 'A' or func == 'a':
            Add()
        elif func == 'S' or func == 's':
            Search()
        
        # only manager can use Report, Delte and Edit Optipns
        elif func == 'D' or func == 'd':
            print('Are you Manager?:')
            Mrg_emp = input("Y=Yes, Anything Else = No:")
            Mgr= Mrg_emp.upper()
            if (Mgr == 'YES' or Mgr == 'Y'):
                Delete()
            else:
                print('\n')
                main()
        elif func == 'E' or func == 'e':
            print('Are you Manager?:')
            Mrg_emp = input("Y=Yes, Anything Else = No:")
            Mgr= Mrg_emp.upper()
            if (Mgr == 'YES' or Mgr == 'Y'):
                Edit()
            else:
                print('\n')
                main()
        elif func == 'R' or func == 'r':
            print('Are you Manager?:')
            Mrg_emp = input("Y=Yes, Anything Else = No:")
            Mgr= Mrg_emp.upper()
            if (Mgr == 'YES' or Mgr == 'Y'):
                TimeReport()
            else:
                print('\n')
                main()
        elif func == "Q" or func == "q":
            quit()
        #if you press any random key it will bring you here
        else:
            print("Incorrect input please try again \n")
            func = input("enter A for Add, S for Search, D for Delete, E for Edit, R for Report:")

main()


