from student import Student
from teacher import Teacher
from hod import HOD
from department import Department


flag = True
inner_flag = True
students = []
teachers = []
hods = []
departments = ['Computer']

while flag:
    print('\n ******************** Welcome to the University Notification System. ******************************** \n')

    print('Kindly Make a choice. \n 1. Student\n 2. Teacher\n 3. HOD\n 4. Department\n 5. Notification\n 6. Exit')
    choice = input()
    choice = int(choice) if choice.isdigit() else choice
    print('*******************************')
    print('*******************************')
    print('*******************************')
    if choice == 1:
        inner_flag = True
        while inner_flag:
            print('*******************************')
            print('Student')
            print('*******************************')
            option = input('\n Please Choose \n 1. Add Student\n 2. Remove Student \n Any Other Key for Main Menu\n')
            option = int(option) if option.isdigit() else option
            if option == 1:
                print('\n*******************************')
                print('*******************************')
                print('Add Student')
                print('*******************************')
                print('*******************************')
                fname = input('Please Enter First Name\n')
                lname = input('Please Enter Last Name\n')
                email = input('Please Enter Email ID\n')
                sub_flag = True
                while sub_flag:
                    depart = input('Please Enter the Department Name\n').capitalize()
                    if depart in departments:
                        students.append(Student(fname, lname, email, depart))
                        sub_flag = False
                    else:
                        print('There is no Department with this Name {}.'.format(depart))
                        print('Select 1. for changing the department Name 2. Going to Main Menu To Add New Department')
                        inner_option = input()
                        inner_option = int(inner_option) if inner_option.isdigit() else inner_option
                        if inner_option != 1:
                            sub_flag = False
                            inner_flag = False
                            break
            elif option == 2:
                print('\n*******************************')
                print('*******************************')
                print('Remove Student')
                print('*******************************')
                print('*******************************')
                print('All Students')
                for counter, student in enumerate(students):
                    print('{}. \t {}'.format(counter, student))
                print('---------------------------------')
                inner_option = input('Enter the Index Number to Delete. \n')
                inner_option = int(inner_option) if inner_option.isdigit() else inner_option
                if inner_option < len(students):
                    students.pop(inner_option)
            else:
                inner_flag = False
    elif choice == 2:
        inner_flag = True
        while inner_flag:
            print('*******************************')
            print('Teacher')
            print('*******************************')
            option = input('\n Please Choose \n 1. Add Teacher\n 2. Remove Teacher \n Any Other Key for Main Menu\n')
            option = int(option) if option.isdigit() else option
            if option == 1:
                print('\n*******************************')
                print('*******************************')
                print('Add Teacher')
                print('*******************************')
                print('*******************************')
            elif option == 2:
                print('\n*******************************')
                print('*******************************')
                print('Remove Teacher')
                print('*******************************')
                print('*******************************')
            else:
                inner_flag = False
    elif choice == 3:
        inner_flag = True
        while inner_flag:
            print('*******************************')
            print('HOD')
            print('*******************************')
            option = input('\n Please Choose \n 1. Add HOD\n 2. Remove HOD \n Any Other Key for Main Menu\n')
            option = int(option) if option.isdigit() else option
            if option == 1:
                print('\n*******************************')
                print('*******************************')
                print('Add HOD')
                print('*******************************')
                print('*******************************')
            elif option == 2:
                print('\n*******************************')
                print('*******************************')
                print('Remove HOD')
                print('*******************************')
                print('*******************************')
            else:
                inner_flag = False
    elif choice == 4:
        inner_flag = True
        while inner_flag:
            print('*******************************')
            print('Department')
            print('*******************************')
            option = input('\n Please Choose \n 1. Add Department\n 2. Remove Department \n Any Other Key for Main Menu\n')
            option = int(option) if option.isdigit() else option
            if option == 1:
                print('\n*******************************')
                print('*******************************')
                print('Add Department')
                print('*******************************')
                print('*******************************')
            elif option == 2:
                print('\n*******************************')
                print('*******************************')
                print('Remove Department')
                print('*******************************')
                print('*******************************')
            else:
                inner_flag = False
    elif choice == 5:
        inner_flag = True
        while inner_flag:
            print('*******************************')
            print('Student')
            print('*******************************')
            option = input('\n Please Choose \n 1. Add Student\n 2. Remove Student \n Any Other Key for Main Menu\n')
            option = int(option) if option.isdigit() else option
            if option == 1:
                print('\n*******************************')
                print('*******************************')
                print('Add Student')
                print('*******************************')
                print('*******************************')
            elif option == 2:
                print('\n*******************************')
                print('*******************************')
                print('Remove Student')
                print('*******************************')
                print('*******************************')
            else:
                inner_flag = False
    elif choice == 6:
        flag = False
        break
    else:
        print('You have enter the wrong choice, please enter corresponding numbers.')

