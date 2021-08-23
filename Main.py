from Super_user import Super_user
from Member import Member

print("*"*55)
print("-"*11+"Welcome to the GYM Membership App"+"-"*11)
print("*"*55)

while True:
    choice = int(input("Press 1 to Log-in as a SUPER-USER \nPress 2 to Log-in as a Member \nPress 3 to Close the App \n--"))
    if choice == 1:
        print("******WELCOME SUPER-USER******\n\nPlease choose from the menu.")
        
        while (True):

            choose_option =int(input("Press 1 for Create Member \nPress 2 for View Member "
                                  "\nPress 3 for Delete Member \nPress 4 for Update Member "
                                  "\nPress 5 for Create Regimen \nPress 6 for View Regimen "
                                  "\nPress 7 for Delete Regimen \nPress 8 for Update Regimen \n"
                                  "Press 0 for Exit from Super-User Section\n--"))
            
            if choose_option == 1:
                Name = str(input("Enter Member Name -"))
                Age = str(input("Enter Member Age -"))
                Gender = str(input("Enter Member Gender -"))
                Mobile_no = str(input("Enter Member Mobile_no. -"))
                Email = str(input("Enter Member Email -"))
                BMI = str(input("Enter Member BMI(Body Mass Index)-"))
                if BMI < '18.5':
                    regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Rest", "Thu": "Back", "Fri": "Triceps", "Sat": "Rest", "Sun": "Rest"}
                elif BMI < '25':
                    regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio/Abs", "Thu": "Back", "Fri": "Triceps", "Sat": "Legs", "Sun": "Rest"}
                elif BMI < '30':
                    regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Abs/Cardio", "Thu": "Back", "Fri": "Triceps", "Sat": "Legs", "Sun": "Cardio"}
                elif BMI >='30':
                    regimens_details = {"Mon": "Chest", "Tue": "Biceps", "Wed": "Cardio", "Thu": "Back", "Fri": "Triceps", "Sat": "Cardio", "Sun": "Cardio"}
                Duration = str(input("Enter Membership Duration in Months- 1,3,6 or 12 -"))
                member=Member(Name,Age,Gender,Mobile_no,Email,BMI,Duration)
                Super_user.regimen[Mobile_no]=regimens_details
                Super_user.addMember(member)

            elif choose_option == 2:
                check_phn = input("Enter Mobile no- of to View member details \n--")
                print("Name\tAge\tGender\tMobile_no.\tE-mail\tBMI\tDuration")
                for cusId in Super_user.members.keys():
                    if cusId==check_phn:
                        member=Super_user.members[cusId]
                        Name=member.getName()
                        Age=member.getAge()
                        Gender=member.getGender()
                        Mobile_no=member.getMobile_no()
                        Email=member.getEmail()
                        BMI=member.getBMI()
                        Duartion=member.getDuration()
                        print(Name+"\t"+Age+"\t"+Gender+"\t"+Mobile_no+"\t\t"+Email+"\t"+BMI+"\t"+Duration)
                print("\n")

            elif choose_option == 3:
                check_phn = input("Enter Mobile Number of Member you want to delete-\n--")
                try:
                    for cusId in Super_user.members.keys():
                        if cusId==check_phn:
                            print("Member Deleted Successfully") 
                    Super_user.members.pop(check_phn)
                except:
                    print("Mobile no. does not exist. Please enter correct Mobile no.")

            elif choose_option == 4:
                check = input("Enter Mobile Number to Update Member Details-\n--")
                exr = int(input("Press 0 If you want to Extend \nPress 1 If you want to Revoke:-\n--"))
                if exr == 0:
                    for cusId in Super_user.members.keys():
                        member=Super_user.members[cusId]
                        if cusId==check:
                            dur=member.getDuration()
                            s = int(dur)+int(input("Enter how many months you wnat to it to be extended for:-"))
                            res=str(s)
                            member.setDuration(res)
                elif exr == 1:
                    for cusId in Super_user.members.keys():
                        member=Super_user.members[cusId]
                        if cusId==check:
                            member.setDuration('0')
                            print("Membership revoked")

                            
            elif choose_option == 5:
                phn=input("Enter the Mobile no. of member you want to create regimen of:")
                for i in Super_user.regimen:
                    if i==phn:
                        for j in Super_user.regimen[i]:
                            Super_user.regimen[i][j]=input(j+":")

                            
            elif choose_option == 6:
                check_phn = input("Enter Mobile Number to view Regimen of a Member-\n--")
                for i in Super_user.regimen:
                        if i==check_phn:
                            for key,val in Super_user.regimen[i].items():
                                print(key,":",val)

                
            elif choose_option == 7:
                check_phn = input("Enter Mobile Number of a Member to Delete Regimen-\n--")
                for i in Super_user.regimen:
                        if i==check_phn:
                            print("Workout Regimen deleted of a Member")
                Super_user.regimen.pop(check_phn)
                print("\n")

            elif choose_option == 8:
                check_phn = input("Enter Mobile Number of a Member who's Workout Regimen you want to update:-\n--")
                for i in Super_user.regimen:
                        if i==check_phn:
                            d=input("Enter the day which you want to update:")
                            for j in Super_user.regimen[i]:
                                if j==d:
                                    Super_user.regimen[i][j]=input("Enter the Workout:-")
                                    print("Workout Updated Successfully!!")
                print("\n")
                
            elif choose_option == 0:
                print("---!!Exit from Super-User section!!---")
                print("-----------!!!Thankyou!!!-------------")
                break

            else:
                print("Invalid Input!!!\n Please enter a valid option")


    elif choice == 2:
        print("*******WELCOME MEMBER*******\nPlease enter your choice:\n")
        while (True):
            choose_option = int(input("Press 1 for My Regimen \n Press 2 for My Profile \n Press 3 to Exit from Member Section. "))
                                  
            if choose_option == 1:
                p=input("Enter you Mobile Number")
                print("---Your Regimen Based on Your BMI---")
                for i in Super_user.regimen:
                    if i==p:
                        for key,val in Super_user.regimen[i].items():
                            print(key,":",val)
                print("\n")
                
            elif choose_option == 2:
                p=input("Enter you Mobile Number")
                try:
                    for cusId in Super_user.members.keys():
                        if cusId==p:
                            member=Super_user.members[cusId]
                            Name=member.getName()
                            Age=member.getAge()
                            Gender=member.getGender()
                            Mobile_no=member.getMobile_no()
                            Email=member.getEmail()
                            BMI=member.getBMI()
                            Duartion=member.getDuartion()
                            print("*******YOUR PROFILE*******")
                            print("Name:",Name," \n Age:",Age," \n Gender:",Gender," \n Mobile no:",Mobile_no," \n E-mail:",Email,
                              " \n BMI:",BMI," \n Duration:",Duration,"\n")
                except:
                    print("No Member with this Mobile Number exist.")

            elif choose_option == 3:
                print("---!!Exit from Member section!!---")
                print("----------!!!Thankyou!!!----------")
                break
                
            else:
                print("Invalid Input!!!\n Please enter a valid option")
                
    elif choice == 3:
                print("--------!!!Exit!!!--------")
                print("------!!!Thankyou!!!------")
                break
    else:
        print("Invalid Input!!!\n Please enter a valid number")
