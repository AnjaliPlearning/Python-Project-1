import sys

#Check password 
class Password:
    def __init__(self):
        self.password = ''
        self.attempts_left = 3
        
# This function determines whether a given password meets certain criteria for strength, 
# such as minimum length, uppercase letters, numbers, and special characters.

    def checkpassword(self, password):
        if len(password) < 10:
            print("Password should have at least 10 characters.")
            return False
        elif not any(i.isupper() for i in password):
            print("Password should have at least one uppercase letter.")
            return False
        elif not (2 <= sum(i.isdigit() for i in password) <= 3):
            print("Password should have at least two or three numbers.")
            return False
        elif not any(i in ['$', '@', '#', '%', '&', '!', '*', '^', '~', '+', '-'] for i in password):
            print("Password should have at least one special character from the following: $@#%&!*^~+-")
            return False
        return True

# This function check for ask for password input maximum number of login attempts and 
# exits the process if the attempts is exceeded.

    def login(self):
        while self.attempts_left > 0:
            password = input('''Please enter a password that satisfies the following criteria:
                     • Should not be less than 10 characters.
                     • Should contain at least one upper case letter.
                     • Should contain two or three numbers.
                     • Should contain one special character.
                     Password:''')
            if self.checkpassword(password):
                self.password = password
                print("Login successful!")
                return True
            else:
                self.attempts_left -= 1
                print(f"{self.attempts_left} attempts left.")
        print("Max attempts exceeded. Exiting process.")
        sys.exit(1)

        
# This function prompts the user to input the number of students and their names, 
# with input validation and a maximum of three attempts.

def numberofstuds():
    attempts_no_of_studs =  1
    counter_for_stud_names = 1
    global name_list, input_no_of_studs
    name_list = []
    while attempts_no_of_studs <= 3:
        input_no_of_studs = int(input('Enter the number of students. The student count should be between 1 to 50: '))
        if 1 <= input_no_of_studs <= 50:
                for i in range(1, input_no_of_studs+1):
                    while True:
                        enter_names = str(input('Enter the name of Student {}: '.format(i)))
                        if enter_names.isalpha() or ' ' in enter_names:
                            name_list.append(enter_names)
                            break
                        else:
                            print("Please enter only alphabetical characters as name.")
                return name_list
                break
        else:
            print("Enter a correct number (i.e., between 1-50).")
            attempts_no_of_studs += 1
    print("Max attempts exceeded. Exiting process.")
    sys.exit(1)


# This function takes in a list of names, prompts the user to enter marks for each student in six subjects, 
# calculates their GPA, determines their school of acceptance based on the GPA, 
# and returns a list of schools and their corresponding count.    
    
def entermarks(name_list):
    global school
    global count_engg, count_buss, count_law, count_na
    count_engg, count_buss, count_law, count_na, j = 0, 0, 0, 0, 0
    all_marks = []
    for i in range(0,len(name_list)):
        all_marks.append([])
        print("Enter Marks for", name_list[i])
        while j < 100:
            math = float(input('Input mark in MATH (1 - 100): '))
            if math<=100 and math>=1:
                    all_marks[i].append(math)
                    j+=1
                    break
            else:
                print("Please enter between 0 and 100")

        while j < 100:
            science = float(input('Input mark in Science (1 - 100): '))
            if science<=100 and science>=1:
                all_marks[i].append(science)
                j+=1
                break
            else:
                print("Please enter between 0 and 100")
                
        while j < 100:
            language = float(input('Input mark in language (1 - 100): '))
            if language<=100 and language>=1:
                all_marks[i].append(language)
                j+=1
                break
            else:
                print("Please enter between 0 and 100")
                
        while j < 100:
            drama = float(input('Input mark in drama (1 - 100): '))
            if drama<=100 and drama>=1:
                all_marks[i].append(drama)
                j+=1
                break
            else:
                print("Please enter between 0 and 100")
                
        while j < 100:
            music = float(input('Input mark in music (1 - 100): '))
            if music<=100 and music>=1:
                all_marks[i].append(music)
                j+=1
                break
            else:
                print("Please enter between 0 and 100")
                
        while j < 100:
            biology = float(input('Input mark in biology (1 - 100): '))
            if biology<=100 and biology>=1:
                all_marks[i].append(biology)
                print(all_marks)
                j+=1
                break
            else:
                print("Please enter between 0 and 100")
                
        gpa=getGPA(math, science, language, drama, music, biology)
      
        
        gpa_list.append(gpa)
        rounded_list = []
        for value in gpa_list:
            rounded_list.append(round(value, 2))
            
        print("Calculated GPA is ",rounded_list)
        if gpa >= 90 and gpa <= 100:
            school = "School of Engineering"
            count_engg += 1 
            school_list.append(school)
        elif gpa >= 80 and gpa < 90:
            school = "School of Business"
            count_buss += 1
            school_list.append(school)
        elif gpa >= 70 and gpa < 80:
            school = "Law School"
            count_law += 1
            school_list.append(school)
        else:
            school = "Not accepted"
            count_na += 1
            school_list.append(school)
        print(school_list)
    return  school_list, count_engg, count_buss, count_law, count_na
    return gpa_list


# This function computes the GPA based on the marks assigned to each subject.

def getGPA(math, science, language, drama, music, biology):
    total_points = math * 4 + science * 5 + language * 4 + drama *3 + music*2 + biology* 4
    total_credits = sum([4, 5, 4, 3, 2, 4])
    gpa = total_points/total_credits
    return gpa


def main():
    global school_list, gpa_list  
    gpa_list = []
    school_list=[]
    print("Welcome in Humber College")
    p = Password()
    p.login()
    numberofstuds()
    entermarks(name_list)

# This code block generates a report with student names and school names.

    print('************************REPORT 1*****************************')
    
    for i in range(input_no_of_studs):
        print('Student Name:',name_list[i],',','School Name:',school_list[i])
    
# This code block displays the number of students accepted to each school as well as 
# the number of students who were denied admission.

    print('************************REPORT 2*****************************')
    
    print('SCHOOL_OF_ENGINEERING:', count_engg)
    print('SCHOOL_OF_BUSINESS:', count_buss)
    print('LAW_SCHOOL:', count_law)
    print('NOT ACCEPTED:', count_na)

# This code displays the total number of accepted and rejected students

    print('************************REPORT 3*****************************')
    
    print('Total number of Accepted Students = ', count_engg+count_buss+count_law)
    print('Total number of Non-Accepted students = ', count_na)
    
# This code generates a report of schools, their students with top 2 GPAs and their average GPAs. 

    print('************************REPORT 4*****************************')
    
    print('Report of schools, their students with top 2 GPAs and their average GPAs ')
    joined_list = []
    for i in range(len(school_list)):
        if school_list[i] is not None and name_list[i] is not None and gpa_list[i] is not None:
            joined_list.append((school_list[i], name_list[i], round(gpa_list[i],2)))

    new_list = [sublist for sublist in joined_list if 'Not accepted' not in sublist]

    name = [sublist[1] for sublist in new_list]
    keys = [sublist[0] for sublist in new_list]
    values = [sublist[2] for sublist in new_list]

    new_list = [(name[i], keys[i], values[i]) for i in range(len(keys))]

    unique_values = list(set([item[1] for item in new_list]))

    separated_lists = [[item for item in new_list if item[1] == value] for value in unique_values]


    def get_second_max(lst):
        max1, max2 = None, None
        for item in lst:
            if max1 is None or item[2] > max1[2]:
                max2 = max1
                max1 = item
            elif max2 is None or item[2] > max2[2]:
                max2 = item
        result = []
        if max1 is not None:
            result.append(max1)
        if max2 is not None:
            result.append(max2)
        return result

    def get_school_average(lst):
        total_gpa = 0
        num_students = len(lst)
        for item in lst:
            total_gpa += item[2]
        return round(total_gpa / num_students, 2)  

    print('+-----------------------+------------------------+-------------------+-----------------+')
    print('| School                | Name                   | Top 2 GPAs        |  Average GPA    |')
    print('+-----------------------+------------------------+-------------------+-----------------+')

    for lst in separated_lists:
        results = get_second_max(lst)
        if len(results) > 0:
            max1, max2 = results[0], results[-1]
            print('| {:<21} | {:<22} | {:<17} | {:<16}|'.format(max1[1], max1[0], max1[2], get_school_average(lst)))
            if len(results) > 1:
                print('| {:<21} | {:<22} | {:<17} |'.format(max2[1], max2[0], max2[2]))
        print('+-----------------------+------------------------+-------------------+-----------------+')

    total_gpa = 0
    total_count = 0

    for item in new_list:
        total_gpa += item[2]
        total_count += 1

main()
